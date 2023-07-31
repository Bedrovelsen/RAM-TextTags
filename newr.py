from gradio_client import Client

client = Client("https://xinyu1205-recognize-anything.hf.space/")
result = client.predict(
				"https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'parameter_17' Image component
				"Howdy!",	# str  in 'User Specified Tags (Optional, separated by comma)' Textbox component
				fn_index=3
)
print(result)
