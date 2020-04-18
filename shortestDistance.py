def shortestDistance(words, word1, word2):
    i1 = 0
    minDistance = len(words)
    currentWord = None
    for i, w in enumerate(words):
        print(i, w)
        if w not in (word1, word2): continue
        if currentWord and w != currentWord:
            minDistance = abs(min(minDistance, i - i1))
        currentWord, i1 = w, i
        print(minDistance)
    print(minDistance)
    return minDistance


print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))
