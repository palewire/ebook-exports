import json
import requests


def main():
    r = requests.get("https://cummings.ee/downloads/poems.json")
    j = r.json()
    json.dump(j, open('data/poems.json', 'w'))


if __name__ == '__main__':
    main()
