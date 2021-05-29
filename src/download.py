import json
import requests


def main():
    # Get poems
    r = requests.get("https://cummings.ee/downloads/poems.json")
    j = r.json()
    json.dump(j, open('data/poems.json', 'w'), indent=2)
    # Get TOC
    r = requests.get("https://raw.githubusercontent.com/ee-cummings-archive/cummings.ee/master/_data/toc/tulips-and-chimneys.json")
    j = r.json()
    json.dump(j, open('data/toc.json', 'w'), indent=2)


if __name__ == '__main__':
    main()
