def count_words(words):
    counts = {}

    def helper(index):
        if index == len(words):
            return

        word = words[index]

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

        helper(index + 1)

    helper(0)

    return counts