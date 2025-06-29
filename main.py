print("hello world, this is a sample Python script.")
# Importing a function from torchtext
from torchtext.data.utils import get_tokenizer
# Using the get_tokenizer function to tokenize a sample text
#  The tokenizer is set to "basic_english" which is a simple tokenizer that splits text into words.
tokenizer = get_tokenizer("basic_english")
# get_tokenizer (which is a function ) returns a callable function (here named tokenizer)
# This tokenizer function can be used to tokenize text
tokenizer("This is a sample text for tokenization.")

def yield_tokens(data_iter):
    for text in data_iter:
        yield tokenizer(text)