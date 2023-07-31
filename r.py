import sys
import json
from gradio_client import Client

def process_file(filename):
    client = Client("https://xinyu1205-recognize-anything.hf.space/")
    result = client.predict(
        filename,
        "",
        fn_index=3
    )
    return {"filename": filename, "data": result}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a filename as the first argument.")
        sys.exit(1)

    filename = sys.argv[1]
    data = process_file(filename)
    print(json.dumps(data), end=",")