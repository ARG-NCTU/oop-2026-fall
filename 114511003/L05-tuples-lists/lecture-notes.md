# Lecture 5: Tuples, lists, aliasing, mutability, and cloning

## Tuple

Tuple 是一種有順序的資料結構，可以放入多個元素。Tuple 中的元素可以是不同型別，例如整數、字串或布林值。

1. Tuple 通常使用小括號建立：

   ```python
   student = ("Amy", 20, True)

   print(student)
   ```

2. Tuple 的索引從 `0` 開始，也可以使用切片：

   ```python
   student = ("Amy", 20, True)

   print(student[0])    # Amy
   print(student[0:2])  # ("Amy", 20)
   ```

3. Tuple 是 `immutable`，意思是建立後不能直接修改其中的元素：

   ```python
   values = (1, 2, 3)

   values[0] = 10
   # TypeError
   ```

4. Tuple 可以使用 `+` 連接，並產生一個新的 Tuple：

   ```python
   first = (1, 2)
   second = (3, 4)

   result = first + second

   print(result)  # (1, 2, 3, 4)
   ```

5. Tuple 可以用來同時指定多個變數：

   ```python
   x, y = (10, 20)

   print(x)  # 10
   print(y)  # 20
   ```

6. 函式可以使用 Tuple 回傳多個值：

   ```python
   def quotient_and_remainder(x, y):
       quotient = x // y
       remainder = x % y
       return quotient, remainder


   quotient, remainder = quotient_and_remainder(10, 3)

   print(quotient)   # 3
   print(remainder)  # 1
   ```

7. 只有一個元素的 Tuple 必須加上逗號：

   ```python
   one_item = (5,)

   print(type(one_item))  # <class 'tuple'>
   ```

## List

List 是一種有順序的資料結構，可以使用索引存取元素。List 通常使用中括號建立。

1. List 可以包含多個元素：

   ```python
   numbers = [2, 4, 6, 8]

   print(numbers[0])  # 2
   print(len(numbers))  # 4
   ```

2. List 中的元素通常是相同型別，但也可以包含不同型別：

   ```python
   values = [2, "hello", True, [1, 2]]
   ```

3. List 是 `mutable`，意思是建立後可以修改元素：

   ```python
   numbers = [1, 2, 3]

   numbers[0] = 10

   print(numbers)  # [10, 2, 3]
   ```

4. List 的索引從 `0` 開始。如果使用不存在的索引，會發生 `IndexError`：

   ```python
   numbers = [10, 20, 30]

   print(numbers[0])  # 10

   # print(numbers[3])  # IndexError
   ```

## Iterating over a list

可以使用 `for` 迴圈逐一處理 List 中的元素。

1. 使用索引走訪 List：

   ```python
   numbers = [1, 2, 3]
   total = 0

   for index in range(len(numbers)):
       total += numbers[index]

   print(total)  # 6
   ```

2. 直接走訪 List 中的元素通常比較簡單：

   ```python
   numbers = [1, 2, 3]
   total = 0

   for number in numbers:
       total += number

   print(total)  # 6
   ```

3. `range(len(numbers))` 的索引範圍是 `0` 到 `len(numbers) - 1`。

## Adding elements to a list

1. `append()` 會將一個元素加入 List 的尾端，並修改原本的 List：

   ```python
   numbers = [1, 2, 3]

   result = numbers.append(4)

   print(numbers)  # [1, 2, 3, 4]
   print(result)   # None
   ```

2. `+` 可以連接兩個 List，並產生一個新的 List：

   ```python
   first = [1, 2]
   second = [3, 4]

   result = first + second

   print(first)   # [1, 2]
   print(second)  # [3, 4]
   print(result)  # [1, 2, 3, 4]
   ```

3. `extend()` 會把另一個 List 的元素加入原本的 List：

   ```python
   numbers = [1, 2, 3]

   numbers.extend([4, 5])

   print(numbers)  # [1, 2, 3, 4, 5]
   ```

`+` 會建立新的 List，而 `extend()` 會修改原本的 List。

## Removing elements from a list

1. `del` 可以刪除指定索引的元素：

   ```python
   numbers = [10, 20, 30]

   del numbers[1]

   print(numbers)  # [10, 30]
   ```

2. `pop()` 會刪除並回傳 List 最後一個元素：

   ```python
   numbers = [1, 2, 3]

   removed = numbers.pop()

   print(removed)  # 3
   print(numbers)  # [1, 2]
   ```

3. `remove()` 會尋找指定的元素，並刪除第一次出現的元素：

   ```python
   numbers = [1, 2, 3, 2]

   numbers.remove(2)

   print(numbers)  # [1, 3, 2]
   ```

如果指定的元素不在 List 中，`remove()` 會產生 `ValueError`。

## Converting between lists and strings

1. `list()` 可以把字串轉換成由字元組成的 List：

   ```python
   text = "hello"

   characters = list(text)

   print(characters)  # ['h', 'e', 'l', 'l', 'o']
   ```

2. `split()` 可以根據指定的分隔符號切割字串：

   ```python
   text = "I love Python"

   words = text.split()

   print(words)  # ['I', 'love', 'Python']
   ```

3. `join()` 可以把 List 中的字串連接成一個字串：

   ```python
   letters = ["a", "b", "c"]

   result = "-".join(letters)

   print(result)  # a-b-c
   ```

## Sorting a list

1. `sorted()` 不會修改原本的 List，而是回傳一個新的排序結果：

   ```python
   numbers = [9, 6, 0, 3]

   sorted_numbers = sorted(numbers)

   print(numbers)        # [9, 6, 0, 3]
   print(sorted_numbers)  # [0, 3, 6, 9]
   ```

2. `sort()` 會直接修改原本的 List：

   ```python
   numbers = [9, 6, 0, 3]

   result = numbers.sort()

   print(numbers)  # [0, 3, 6, 9]
   print(result)   # None
   ```

3. `reverse()` 會將原本的 List 反轉：

   ```python
   numbers = [1, 2, 3, 4]

   numbers.reverse()

   print(numbers)  # [4, 3, 2, 1]
   ```

## Aliasing

Aliasing 是指兩個變數指向同一個物件。修改其中一個變數指向的 List，另一個變數也會受到影響。

```python
original = [1, 2, 3]
alias = original

alias.append(4)

print(original)  # [1, 2, 3, 4]
print(alias)     # [1, 2, 3, 4]
print(original is alias)  # True
```

`original` 和 `alias` 不是兩個不同的 List，而是指向記憶體中的同一個 List。

## Cloning a list

Cloning 是建立一個新的 List，並複製原本 List 中的元素。

```python
original = [1, 2, 3]
clone = original[:]

clone.append(4)

print(original)  # [1, 2, 3]
print(clone)     # [1, 2, 3, 4]
print(original is clone)  # False
```

使用 `original[:]` 可以建立一個新的 List，因此修改 `clone` 不會直接修改 `original`。

## Nested lists and shallow cloning

如果 List 裡面還有其他 List，使用切片只會複製最外層的 List。

```python
original = [[1, 2], [3, 4]]
clone = original[:]

clone[0].append(99)

print(original)  # [[1, 2, 99], [3, 4]]
print(clone)     # [[1, 2, 99], [3, 4]]
```

這是因為 `original[0]` 和 `clone[0]` 仍然指向同一個內層 List。

## Mutation during iteration

在走訪 List 時直接修改 List 可能造成問題，因為元素刪除後，其他元素的索引會改變。

```python
def remove_duplicates(values, targets):
    for value in values:
        if value in targets:
            values.remove(value)

    return values
```

例如：

```python
values = [1, 2, 3, 4]
targets = [1, 2]

print(remove_duplicates(values, targets))
```

這個函式可能無法刪除所有符合條件的元素，因為 List 在迴圈執行期間被修改了。

一種比較安全的方法是走訪 List 的複製品：

```python
def remove_duplicates(values, targets):
    values_copy = values[:]

    for value in values_copy:
        if value in targets:
            values.remove(value)

    return values
```

## Common mistakes

- 把 Tuple 和 List 的括號混淆。
- 忘記 Tuple 是 immutable。
- 誤以為 `a = b` 會建立新的 List。
- 把 `sort()` 的回傳值存進變數。
- 在迭代 List 時直接刪除元素。
- 以為 shallow clone 會複製所有 nested lists。

## Complexity

- 讀取 List 中指定索引的元素通常是 `O(1)`。
- `append()` 平均是 `O(1)`。
- 使用 `x in L` 搜尋 List 通常是 `O(n)`。
- 使用 `L[:]` 複製長度為 `n` 的 List 是 `O(n)`。
- `sorted(L)` 通常需要 `O(n log n)` 時間。
- 複製 List 需要 `O(n)` 的額外空間。

## Personal reflection

### What I understand now

Write what I understand after studying this lecture.

### What confused me

Write one concept that was difficult to understand.

### One example that helped me

Write the example that helped me understand aliasing, mutation, or cloning.

## Closed-AI check

Without looking at notes or using AI, answer this question:

Why do `original` and `alias` change together in the following code?

```python
original = [1, 2, 3]
alias = original

alias.append(4)
```
  