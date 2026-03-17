sentence = input()

arr = [str(x) for x in sentence.split()]

last_word = arr[-1]

print(f"the last word was \"{last_word}\" with the length {len(last_word)}")
