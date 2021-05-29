import json
from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


def main():
    data = json.load(open('data/poems.json', 'r'))
    tandc = [p for p in data if p['book_slug'] == 'tulips-and-chimneys']
    poem_lookup = dict((p['slug'], p['text']) for p in tandc)
    toc = json.load(open('data/toc.json', 'r'))
    poem_list = []
    for section in toc:
        poem_list.append(dict(name=section['name'].upper()))
        for chapter in section['children']:
            if chapter.get('children', False):
                poem_list.append(dict(name=chapter['name']))
                for poem in chapter['children']:
                    poem['text'] = poem_lookup[poem['slug']]
                    poem_list.append(poem)
            else:
                chapter['text'] = poem_lookup[chapter['slug']]
                poem_list.append(chapter)

    json.dump(poem_list, open("data/book.json", "w"), indent=2)

    template = env.get_template('book.txt')
    output = template.render(obj_list=poem_list)
    with open("output/tulips-and-chimneys.txt", "w") as f:
        f.write(open("templates/title.txt", "r").read())
        f.write(output)


if __name__ == '__main__':
    main()
