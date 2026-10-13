def average_scores(texts):
    count = 0
    new_texts = []
    for i in texts:
        try:
            score = int(i)
        except ValueError:
            count += 1
        else:
            if score < 0 or score > 100:
                count += 1
            else:
                new_texts.append(score)
    if len(new_texts) == 0:
        raise ValueError("沒有有效的成績")
    else:
        average = sum(new_texts) / len(new_texts)
        return (average, count)

if __name__ == "__main__":
    print(average_scores(["80", "abc", "90"]))
    print(average_scores(["100", "-5", "70", "x"]))

    try:
        average_scores(["abc", ""])
    except ValueError as e:
        print("錯誤：", e)
