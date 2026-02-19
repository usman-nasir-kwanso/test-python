"""Tokenize text using tiktoken."""

import tiktoken


def main():
    """Encode and print tokens for a sample text."""
    enc = tiktoken.encoding_for_model("gpt-4o")

    text = "Hello, world! This is a test of the tokenization system."
    tokens = enc.encode(text)
    print(tokens)

    # Decode tokens back into text
    decoded_text = enc.decode(tokens)
    print(decoded_text)


if __name__ == "__main__":
    main()
