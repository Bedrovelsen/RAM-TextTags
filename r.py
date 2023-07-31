import sys
from gradio_client import Client

if len(sys.argv) < 2:
    print("Please provide a filename as the first argument.")
    sys.exit(1)

filename = sys.argv[1]  # Get the filename from the command line arguments

client = Client("https://xinyu1205-recognize-anything.hf.space/")

result = client.predict(
    filename,  # Use the filename from the command line arguments
    "",  # str in 'User Specified Tags (Optional, separated by comma)' Textbox component
    fn_index=3
)
print("{\"filename\": \"%s\", \"data\": \"%s\"}," % (filename, result))