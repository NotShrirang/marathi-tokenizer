# 🖋️ Marathi Tokenizer: A BPE-Based Tokenizer for Marathi Language

![GitHub stars](https://img.shields.io/github/stars/NotShrirang/marathi-tokenizer?style=social)
![GitHub forks](https://img.shields.io/github/forks/NotShrirang/marathi-tokenizer?style=social)
![GitHub commits](https://img.shields.io/github/commit-activity/t/NotShrirang/marathi-tokenizer)
![GitHub issues](https://img.shields.io/github/issues/NotShrirang/marathi-tokenizer)
![GitHub pull requests](https://img.shields.io/github/issues-pr/NotShrirang/marathi-tokenizer)
![GitHub](https://img.shields.io/github/license/NotShrirang/marathi-tokenizer)
![GitHub last commit](https://img.shields.io/github/last-commit/NotShrirang/marathi-tokenizer)
![GitHub repo size](https://img.shields.io/github/repo-size/NotShrirang/marathi-tokenizer)

---

Marathi Tokenizer is an open-source project for tokenizing Marathi text using Byte Pair Encoding (BPE). Based on Hugging Face's `tokenizers` library, it is optimized to handle the linguistic nuances of the Marathi language. This tokenizer is ideal for tasks such as language modeling, machine translation, and other natural language processing (NLP) applications.

---

## ✨ Features

- 🧠 **BPE Encoding**: Leverages Byte Pair Encoding to tokenize Marathi text into subword units efficiently.
- 📚 **Multi-Dataset Support**: Trained on a diverse set of Marathi datasets, including news articles, conversational text, and more.
- 🔍 **Custom Vocabulary**: Supports configurable vocabulary size and frequency thresholds for token inclusion.
- 📦 **Hugging Face Integration**: Fully compatible with Hugging Face's `PreTrainedTokenizerFast` for seamless NLP pipeline integration.
- ⚡ **Efficient Training**: Optimized for fast and scalable training using Hugging Face datasets.
- 🌐 **Unicode Support**: Handles complex Marathi characters and ligatures seamlessly.

---

## 🏗️ Architecture Overview

1. **Dataset Preparation**:
   - Combines multiple datasets from Hugging Face, including:
     - Marathi news articles
     - Conversational text
     - Instructional datasets
   - Preprocesses datasets to standardize text and remove irrelevant columns.

2. **BPE Tokenizer Training**:
   - Trains a Byte Pair Encoding tokenizer with configurable parameters, such as vocabulary size and minimum token frequency.
   - Tokenizer is saved in Hugging Face's `PreTrainedTokenizerFast` format for compatibility.

3. **Tokenization Workflow**:
   - Custom rules ensure optimal tokenization for Marathi language structure.
   - Provides robust encoding and decoding capabilities.

4. **Output**:
   - Tokenized text as subword units.
   - Saved tokenizer files for integration into NLP pipelines.

---

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NotShrirang/marathi-tokenizer.git
   cd marathi-tokenizer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📖 Usage

1. **Training the Tokenizer**:

   Use the provided script `tokenizer.py` to train the BPE tokenizer on predefined datasets:

   ```bash
   python tokenizer.py
   ```

   The tokenizer will be saved in the `marathi_bpe_tokenizer` directory.

2. **Using the Tokenizer**:

   Example usage with the trained tokenizer:
  
  (It is a gated repository, so for using this model, you will have to get an access token from HuggingFace.)
   ```python
   from tokenizers import Tokenizer
  
   hfToken = "<HUGGINGFACE_TOKEN>"
  
   tokenizer: Tokenizer = Tokenizer.from_pretrained("NotShrirang/marathi-tokenizer", token=hfToken)
   
   text = "मराठी भाषा ही भारतातील एक प्रमुख भाषा आहे."

   encoded = tokenizer.encode(text)

   print("Encoded token IDs:", encoded)
   print("Decoded text:", tokenizer.decode(encoded))
   ```

3. **Sample Encoding**:

   A sample usage script `sample.py` is included for testing the tokenizer:

   ```bash
   python sample.py
   ```

---

## 🗺️ Roadmap

- [x] Support for BPE-based tokenization.
- [x] Integration with Hugging Face datasets and tokenizer.
- [ ] Extend support for SentencePiece tokenization.
- [ ] Add tokenization benchmarks and evaluation scripts.

---

## ⚙️ Configuration

- **Vocabulary Size**: Default is set to `32768`, adjustable via script parameters.
- **Minimum Frequency**: Default is `2`, configurable for token inclusion.
- **Datasets**: Combines multiple Marathi datasets for comprehensive coverage.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for feature requests, bug fixes, or improvements.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/)
- [Byte Pair Encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding)
- [Marathi Language Resources](https://www.marathi-language.org/)
