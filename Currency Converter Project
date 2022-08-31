import json
import requests

their_currency = input().lower()
r = requests.get(f"http://www.floatrates.com/daily/{their_currency}.json")
r1 = json.loads(r.text)
cache = {}
if their_currency != "usd":
    cache.update({"usd": r1["usd"]["rate"]})
if their_currency != "eur":
    cache.update({"eur": r1["eur"]["rate"]})

while True:
    exchange_to = input()
    if exchange_to == "":
        break
    amount = int(input())
    print("Checking the cache...")
    if exchange_to in cache:
        print("Oh! It is in the cache!")
        total = round(amount * cache[exchange_to], 2)
        print(f"You received {total} {exchange_to.upper()}")
    else:
        print("Sorry, but it is not in the cache!")
        cache.update({exchange_to: r1[exchange_to]["rate"]})
        total = round(amount * cache[exchange_to], 2)
        print(f"You received {total} {exchange_to.upper()}")
