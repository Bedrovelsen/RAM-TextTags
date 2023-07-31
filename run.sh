#! /bin/bash

echo "[" > output.json

for file in "$1"/*; do
  python r.py "$file" | grep -v Loaded >> output.json
done

# Remove the trailing comma
sed -i '$ s/.$//' output.json

echo "]" >> output.json

python pr.py output.json
