def has_duplicates(word):
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            if word[i] == word[j]:
                return True
    return False

words = ["hello", "world", "python", "apple"]
results = []
for w in words:
    results.append(has_duplicates(w))

print(results)  # [True, False, False, True]