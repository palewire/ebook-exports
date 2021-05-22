import json


def main():
    data = json.load(open('data/poems.json'))
    tandc = [p for p in data if p['book_slug'] == 'tulips-and-chimneys']
    print(f"Creating a text file with {len(tandc)} poems in Tulips and Chimneys")


if __name__ == '__main__':
    main()
