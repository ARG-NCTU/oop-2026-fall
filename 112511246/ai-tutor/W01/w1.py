# W1 Part B: Pass List（及格名單）
#
# 寫一個函式 pass_list(scores, limit)：
#   1. 找出所有大於或等於 limit 的分數
#   2. 由小到大排序，放進一個新的 list
#   3. 計算不及格（被排除）的分數有幾個
#   4. 用 tuple 回傳 (及格名單, 不及格人數)
# 規定：函式執行完後，原本的 scores 必須完全不變（內容與順序都不能變）。
#
# 範例：
#   pass_list([70, 45, 90, 60], 60) -> ([60, 70, 90], 1)
#   pass_list([50, 80, 50], 60)     -> ([80], 2)
#   pass_list([], 60)               -> ([], 0)


def pass_list(scores, limit):
    passed = []
    count = 0

    for i in scores:
        if i >= limit:
            passed.append(i)
        else:
            count += 1

    passed.sort()
    return (passed, count)


if __name__ == "__main__":
    scores = [70, 45, 90, 60]
    print(pass_list(scores, 60))
    print(scores)

    print(pass_list([50, 80, 50], 60))
    print(pass_list([], 60))
