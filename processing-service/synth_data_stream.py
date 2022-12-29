import random
import requests
import json
import time
import argparse


# ENDPOINT = 'https://pubsub-proxy-hyp-67qykeacca-ew.a.run.app/json'

def main(endpoint):
    draw = round(random.uniform(0, 1), 2)

    if 0 <= draw < 1 / 3:
        # get view payload
        view_item_f = open('../datalayer/view_item.json')
        view_item_payload = json.load(view_item_f)

        # send view
        r = requests.post(endpoint, json=view_item_payload)

    elif 1 / 3 <= draw < 2 / 3:
        # get add to cart payload
        add_to_cart_f = open('../datalayer/add_to_cart.json')
        add_to_cart_payload = json.load(add_to_cart_f)

        # send add to cart
        r = requests.post(endpoint, json=add_to_cart_payload)

    else:
        # decide between anomaly or no anomaly
        if draw < 0.99:
            # get payload
            purchase_f = open('../datalayer/purchase.json')
            purchase_payload = json.load(purchase_f)

            # send request
            r = requests.post(endpoint, json=purchase_payload)
        else:
            # get payload
            purchase_anomaly_f = open('../datalayer/purchase_anomaly.json')
            purchase_anomaly_payload = json.load(purchase_anomaly_f)

            # send request
            r = requests.post(endpoint, json=purchase_anomaly_payload)

    # print(r.text)
    print(f'{time.time()} -- {r.status_code}')


if __name__ == "__main__":
    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", help="Target Endpoint")

    args = parser.parse_args()

    endpoint = args.endpoint

    while True:
        main(endpoint)
        time.sleep(2)
