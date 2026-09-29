from pathlib import Path

train_dir = Path("/srv/data/lt2326-h26/a1/train")
languages = ["en", "tr", "zh"]

#collect all unique characters from the training data
chars = set()
for lang in languages:
    path = train_dir / f"{lang}.txt"

    text = path.read_text(encoding = "utf-8")
    lines = text.splitlines()

    for line in lines:
        chars.update(set(line))

#sort characters so that IDs are determinitic
sorted_chars = sorted(chars)

#character to ID and ID to character mappings
stoi = {}
itos = {}

#Reserve ID 0 for unknown characters
stoi["<UNK>"] = 0
itos[0] = "<UNK>"

#Assign IDs to characters
for i, char in enumerate(sorted_chars, start=1):
    stoi[char] = i
    itos[i] = char

print("Vocabulary size:", len(stoi))
print("First 20 entries:", list(stoi.items())[:20])