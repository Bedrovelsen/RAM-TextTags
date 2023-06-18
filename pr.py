import json

with open('test.json') as file:
    data = json.load(file)

new_data = []
for item in data:
    tags, caption = eval(item['data'])
    new_item = {
        'filename': item['filename'],
        'data': {
            'tags': [tag.strip() for tag in tags.split('|')],
            'caption': caption.strip()
        }
    }
    new_data.append(new_item)

with open('output.json', 'w') as file:
    json.dump(new_data, file, indent=2)