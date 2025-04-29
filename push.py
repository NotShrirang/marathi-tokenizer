from tokenizers import Tokenizer
from transformers import PreTrainedTokenizerFast

tokenizer: Tokenizer = Tokenizer.from_file("./marathi_bpe_tokenizer/marathi_bpe_tokenizer.json")

hfToken = "<HF_TOKEN>"

hf_tokenizer = PreTrainedTokenizerFast(tokenizer_object=tokenizer)
hf_tokenizer.push_to_hub(
    repo_id="NotShrirang/marathi-tokenizer",
    token=hfToken
)

