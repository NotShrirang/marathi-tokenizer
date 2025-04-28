import datasets
from transformers import PreTrainedTokenizerFast
from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers, processors
import os

def train_bpe_tokenizer(dataset, vocab_size=32768, min_frequency=2, output_dir="marathi_tokenizer"):
    """
    Train a BPE tokenizer on a Marathi dataset from Hugging Face.

    Args:
        dataset_name: Name of the Hugging Face dataset
        vocab_size: Maximum vocabulary size
        min_frequency: Minimum frequency for a token to be included in the vocabulary
        output_dir: Directory to save the tokenizer
    """

    os.makedirs(output_dir, exist_ok=True)

    def get_training_corpus():
        for i in range(0, len(dataset["train"])):
            text_field = "text" if "text" in dataset["train"][i] else list(dataset["train"][i].keys())[0]
            yield dataset["train"][i][text_field]

    tokenizer = Tokenizer(models.BPE(unk_token="[UNK]"))

    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)

    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size,
        min_frequency=min_frequency,
        special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"]
    )

    print(f"Training BPE tokenizer with vocab size {vocab_size}")
    tokenizer.train_from_iterator(get_training_corpus(), trainer)

    tokenizer.post_processor = processors.ByteLevel(trim_offsets=False)

    tokenizer.decoder = decoders.ByteLevel()

    tokenizer_path = os.path.join(output_dir, "marathi_bpe_tokenizer.json")
    tokenizer.save(tokenizer_path)
    print(f"Tokenizer saved to {tokenizer_path}")
    
    hf_tokenizer = PreTrainedTokenizerFast(tokenizer_file=tokenizer_path)
    hf_tokenizer.save_pretrained(output_dir)
    print(f"HuggingFace tokenizer saved to {output_dir}")
    
    return tokenizer, hf_tokenizer

if __name__ == "__main__":
    ds = datasets.load_dataset("samarthSonawane/marathi_news_articles")

    tokenizer, hf_tokenizer = train_bpe_tokenizer(
        dataset=ds,
        vocab_size=32768,
        min_frequency=2,
        output_dir="marathi_bpe_tokenizer"
    )

    test_text = "मराठी भाषा ही भारतातील एक प्रमुख भाषा आहे."
    encoded = hf_tokenizer.encode(test_text)
    
    print("\nTest encoding:")
    print(f"Original text: {test_text}")
    print(f"Encoded token IDs: {encoded[:10]}... (truncated)")
    print(f"Decoded text: {hf_tokenizer.decode(encoded)}")

    vocab_size = len(hf_tokenizer.get_vocab())
    print(f"\nVocabulary size: {vocab_size}")
    print("Sample of vocabulary:")
    sample_tokens = list(hf_tokenizer.get_vocab().items())[:10]
    for token, id in sample_tokens:
        print(f"{token}: {id}")
