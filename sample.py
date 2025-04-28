from tokenizers import Tokenizer

hfToken = "<HF_TOKEN>"

tokenizer: Tokenizer = Tokenizer.from_pretrained("NotShrirang/marathi-tokenizer", token=hfToken)

text = "नमस्कार, तुम्ही कसे आहात? मी ठीक आहे. तुम्ही ठीक आहात का? "
encoded = tokenizer.encode(text)
print(f"Encoded text: {encoded}")
print(f"Decoded text: {tokenizer.decode(encoded.ids)}")
