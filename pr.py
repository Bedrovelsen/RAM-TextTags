import json
import sys

def reformat_data(item):
    tags, caption = item['data']
    new_item = {
        'filename': item['filename'],
        'data': {
            'tags': [tag.strip() for tag in tags.split('|')],
            'caption': caption.strip()
        }
    }
    return new_item

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a filename as the first argument.")
        sys.exit(1)

    inputpath = sys.argv[1]

    with open(inputpath) as file:
        data = json.load(file)

    new_data = [reformat_data(item) for item in data]

    with open('output.json', 'w') as file:
        json.dump(new_data, file, indent=2)
