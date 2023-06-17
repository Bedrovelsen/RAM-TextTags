from gradio_client import Client

client = Client("https://xinyu1205-recognize-anything-tag2text.hf.space/")
result = client.predict(
    "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'parameter_5' Image component
    "",
				fn_index=3
)

print(result)