word1 = input()
word2 = input()

merged_string = ""
# Determine the length of the longer word
max_len = max(len(word1), len(word2))

for i in range(max_len):
    # Append character from word1 if index is within bounds
    if i < len(word1):
        merged_string += word1[i]
    # Append character from word2 if index is within bounds
    if i < len(word2):
        merged_string += word2[i]

print(merged_string)
# Output: abpapnlae
