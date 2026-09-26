def mirror_equal(s, index=0, count=0):
    # Base case: 已經處理完整個字串
    if index == len(s):
        return count == 0

    # 遇到 'a'，count + 1
    if s[index] == 'a':
        return mirror_equal(s, index + 1, count + 1)

    # 遇到 'b'，count - 1
    if s[index] == 'b':
        return mirror_equal(s, index + 1, count - 1)

    # 其他字元忽略
    return mirror_equal(s, index + 1, count)


print(mirror_equal("abab"))        # True
print(mirror_equal("aaabb"))       # False
print(mirror_equal("ccddeeff"))    # True
print(mirror_equal("a!b?ab123"))   # True