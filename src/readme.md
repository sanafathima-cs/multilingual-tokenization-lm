For this project, I used the multilingual language-modeling dataset provided for the assignment, containing English (en), Turkish (tr), and Chinese (zh) data divided into training, validation, and test sets. Each line represents one sentence. I loaded the data as UTF-8 text and used splitlines() to separate the sentences. The character vocabulary was created only from the training data, while validation was used for preliminary analysis and the test set will be used for final evaluation.

I explored sentence lengths, example sentences, character frequencies, whitespace, digits, and shared or language-specific characters. I then implemented a character-level tokenizer by collecting unique characters with a set. The vocabulary contains 9,443 tokens, including <UNK>. I created stoi and itos mappings and implemented encode() and decode(). Tests with English (Hello), Turkish (Merhaba), and Chinese (你好) successfully decoded back to the original text.

On validation data, the character tokenizer produced:
for English 368269 tokens and Avg tokens/sentence are 81.116 and the Avg unicode character per token are 1.0.
for Turkish 368383 tokens, Avg tokens/sentence are 98.629 and the Avg unicode characters/token are 1.0.
For Chinese 368266 tokens, Avg tokens/sentence 38.545 and the Avg unicode characters/tokens are 1.0.  The vlaue of 1.0 character per token is expected because a character tokenizer represents each Unicode character as one token.

The value 1.0 Unicode characters/token is expected because each character is represented as one token. I also found 61 unseen validation characters in English, 26 in Turkish, and 222 in Chinese, showing the usefulness of the <UNK> token. The languages have similar amounts of validation characters but different numbers of sentences because their average sentence lengths differ. 

The character tokenizer provides a baseline for the next step, where i will compare it with BPE tokenizers and see how the different tokenization methods affect token counts and language-model performance.