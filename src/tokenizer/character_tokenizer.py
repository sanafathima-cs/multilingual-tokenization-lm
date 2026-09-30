from pathlib import Path

# Dataset paths
train_dir = Path("/srv/data/lt2326-h26/a1/train")
valid_dir = Path("/srv/data/lt2326-h26/a1/valid")
languages = ["en", "tr", "zh"]


# Build character vocabulary from training data
chars = set()

for lang in languages:
    path = train_dir / f"{lang}.txt"
    text = path.read_text(encoding="utf-8")

    for line in text.splitlines():
        chars.update(line)

# Sort characters for deterministic IDs
sorted_chars = sorted(chars)

# Character-to-ID and ID-to-character mappings
stoi = {"<UNK>": 0}
itos = {0: "<UNK>"}

for i, char in enumerate(sorted_chars, start=1):
    stoi[char] = i
    itos[i] = char

print("Vocabulary size:", len(stoi))
print("First 20 entries:", list(stoi.items())[:20])


# Convert text to token IDs
def encode(text):
    encoded_ids = []

    for char in text:
        encoded_ids.append(stoi.get(char, 0))

    return encoded_ids


# Convert token IDs back to text
def decode(ids):
    decoded_chars = []

    for token_id in ids:
        decoded_chars.append(itos.get(token_id, "<UNK>"))

    return "".join(decoded_chars)


# Test encoding and decoding
test_texts = [
    "Hello",
    "Merhaba",
    "你好"
]

for text in test_texts:
    encoded = encode(text)
    decoded = decode(encoded)

    print("\n========== Encode / Decode Test ==========")
    print("Original text:", text)
    print("Encoded:", encoded)
    print("Decoded:", decoded)


# Count tokens and sentences in a file
def total_tokens_in_file(path):
    total_tokens = 0
    num_sentences = 0

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    for line in lines:
        encoded = encode(line)
        total_tokens += len(encoded)
        num_sentences += 1

    return total_tokens, num_sentences


# Validation statistics
for lang in languages:
    path = valid_dir / f"{lang}.txt"

    total_tokens, num_sentences = total_tokens_in_file(path)

    average_tokens = total_tokens / num_sentences

    # Character tokenizer has one Unicode character per token
    average_characters_per_token = 1.0

    print(f"\n========== {lang.upper()} validation data ==========")
    print("Total tokens:", total_tokens)
    print("Sentences:", num_sentences)
    print("Average tokens per sentence:", average_tokens)
    print(
        "Average Unicode characters per token:",
        average_characters_per_token
    )


# Find validation characters not seen during training
print("\n====== Unseen validation characters ======")

for lang in languages:
    train_path = train_dir / f"{lang}.txt"
    valid_path = valid_dir / f"{lang}.txt"

    train_text = train_path.read_text(encoding="utf-8")
    valid_text = valid_path.read_text(encoding="utf-8")

    train_chars = set(train_text)
    valid_chars = set(valid_text)

    unseen_chars = valid_chars - train_chars

    print(f"\n{lang.upper()}")
    print("Number of unseen validation characters:", len(unseen_chars))
    print("Unseen characters:", sorted(unseen_chars))