pip install transformers datasets
pip install torch

summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
summarizer("An apple a day, keeps the doctor away", min_length=5, max_length=20)
