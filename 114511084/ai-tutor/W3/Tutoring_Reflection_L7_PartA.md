<!-- AI prompt
I just learned Testing, Debugging, Exceptions, and Assertions in today's lecture.

Act as my AI Tutor.

1. Generate 5 True/False questions, one question at a time, to test my conceptual understanding of today's topic.
2. Focus on concepts and reasoning, not memorization or Python syntax.
3. After I answer, do not immediately tell me the correct answer.
4. If my answer or reasoning is incorrect, give me a hint, counterexample, or follow-up question.
5. Let me revise my answer before explaining the concept.
6. Adjust the difficulty based on my responses.
7. After five questions, ask me to identify one question that may be ambiguous, misleading, too easy, or technically questionable.
8. Finish by asking me what misconception I corrected and what I am still unsure about.
-->

# 📝 Learning Reflection & Concept Check — Part A

**Topic:** Testing, Debugging, Exceptions, Assertions (MIT 6.0001 Lecture 7)  
**Date:** 2026-10-05  

---

### ① Check My Understanding

* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 1 / 5  

| # | 題目 | 我的回答 | 結果 |
| :--- | :--- | :--- | :--- |
| Q1 | 程式通過所有測試，就代表沒有 bug。 | False，測試只能證明有 bug，不能證明沒有 bug。 | ✅ |
| Q2 | `assert` 和 `raise` 都會讓程式停下，所以檢查使用者輸入時兩者可以互相替代。 | False，`assert` 可能被 `-O` 關掉，檢查輸入要用 `raise`。 | ✅ |
| Q3 | 函式 `f` 的單元測試失敗，bug 一定在 `f` 裡面。 | False，測試本身也可能寫錯。 | ✅ |
| Q4 | 設計良好的函式應該 catch 所有 exception，讓呼叫端永遠不必處理錯誤。 | False，吞掉錯誤會讓呼叫端不知道出錯，應該把錯誤「往下推」。→ 經提示後修正為「往上傳給呼叫端，能處理的才 catch」。 | ✅（修正後） |
| Q5 | 用 exception 控制「正常流程」一定是不好的設計。 | False，Python 常用 `try/except KeyError` 查 dict。 | ✅ |

**AI 補充的重點：**
* **Q2**：除了 `-O` 會關掉 `assert`，兩者的**用途**本來就不同。`assert` 檢查「程式寫對的話絕不可能發生」的內部不變量，觸發時代表是程式設計師的錯；`raise` 處理可預期的錯誤狀況，例如使用者輸入錯誤或檔案不存在。
* **Q3**：測試失敗但 `f` 沒錯的其他情況還包括：相依的函式有 bug、對規格的理解不一致、環境或全域狀態殘留、浮點數用 `==` 比較。**症狀出現的位置不一定是原因所在的位置。**
* **Q4**：所謂「能處理」，是指這一層能做出有意義的反應，例如重試、改用 fallback 預設值、補上這一層才知道的資訊後轉成更高層次的 exception（如 `FileNotFoundError` → `ConfigError`），或在最外層統一記錄 log。
* **Q5**：Python 有 EAFP（先做，出錯再處理）與 LBYL（先檢查再做）兩種風格，EAFP 被視為 Pythonic，也能避免「檢查完到實際使用之間狀態被改掉」的 race condition；`for` 迴圈本身也是靠 `StopIteration` 結束的。但仍不應濫用，例如在效能熱點頻繁觸發，或把 exception 當 `goto` 用。

---

### ② My Misconception

**Before: I thought…**  
錯誤發生時，應該把錯誤訊息「往下推」。我對 exception 在呼叫鏈中傳遞的方向沒有清楚的概念。

⸻

**Now: I understand…**  
Exception 會沿著 call stack **往上**傳給呼叫端，例如 `open_file()` → `load_config()` → `main()`，直到某一層 catch 它為止；如果都沒人處理，程式就會終止並印出 traceback。函式只應該 catch 自己**能有意義地處理**的 exception，其餘的就讓它往上傳。

另外也要區分兩件事：
* **Exception 傳遞**：往上傳給呼叫端。
* **除錯時看 traceback**：從錯誤被拋出的位置**往回追原因**。traceback 最後一行是錯誤被拋出的地方，但真正的原因可能在更早的呼叫端，例如傳進了錯誤的參數。

---

### ③ Challenge the AI

**One AI-generated question I challenged:**  
Question 1（「程式通過所有測試，就代表沒有 bug」）

⸻

**Why?**

* [ ] Ambiguous
* [ ] Oversimplified
* [ ] Technically questionable
* [x] Too easy
* [ ] Other: 

**Brief explanation:**  
這題幾乎就是 Dijkstra 名言「Testing shows the presence, not the absence of bugs」的改寫，只要記得這句話就能答對，測不出是否真的理解背後的原因，違反了「重推理、不考記憶」的原則。

AI 建議的改寫版本：「如果測試涵蓋了所有程式路徑（100% path coverage），就能保證沒有 bug。」這樣就必須自己想出反例，例如**漏掉的功能**（規格要求的行為根本沒寫，所以也沒有對應的路徑），或是**同一條路徑在不同輸入值下行為不同**（例如邊界值、overflow）。

AI 也指出，Q5 同樣值得挑剔：「用 exception 控制正常流程」的定義本身就很模糊，`try/except KeyError` 查 dict 到底算正常流程還是錯誤處理，不同人可能有不同解讀。

---

### ④ One-Minute Reflection

**One thing I am still unsure about:**  
怎麼從 traceback 判斷 bug 的真正位置，我還不太熟。

⸻

**Follow-up Practice: Reading a Traceback**

```python
 1  def average(scores):
 2      return sum(scores) / len(scores)
 3
 4  def class_report(students):
 5      results = {}
 6      for name, scores in students.items():
 7          results[name] = average(scores)
 8      return results
 9
10  def load_students(raw):
11      students = {}
12      for line in raw:
13          name, *scores = line.split(",")
14          students[name] = [int(s) for s in scores if s.strip()]
15      return students
16
17  data = ["Amy,90,85", "Bob,", "Cat,70,80"]
18  print(class_report(load_students(data)))
```

```
Traceback (most recent call last):
  File "report.py", line 18, in <module>
    print(class_report(load_students(data)))
  File "report.py", line 7, in class_report
    results[name] = average(scores)
  File "report.py", line 2, in average
    return sum(scores) / len(scores)
ZeroDivisionError: division by zero
```

| 問題 | 我的回答 |
| :--- | :--- |
| 錯誤在哪一行被拋出？`scores` 是什麼？是哪個學生造成的？ | 第 2 行，`scores` 是空 list `[]`，由 Bob 造成。（`"Bob,"` 經 `split(",")` 變成 `["Bob", ""]`，空字串在第 14 行被濾掉。） |
| 空 list 是 `load_students` 產生的，為什麼 traceback 裡沒有它？ | 因為 `load_students` 已經執行完並回傳了，traceback 只顯示錯誤發生當下的呼叫堆疊。 |
| 要在 `load_students`（A）、`class_report`（B）還是 `average`（C）修？用 `raise` 還是 `assert`？ | 選 A，用 `raise`，因為資料本身就可能缺成績。 |

修正範例（在資料進入系統的邊界就把關）：

```python
def load_students(raw):
    students = {}
    for line in raw:
        name, *scores = line.split(",")
        scores = [int(s) for s in scores if s.strip()]
        if not scores:
            raise ValueError(f"student {name!r} has no scores: {line!r}")
        students[name] = scores
    return students
```

⸻

**Key Takeaways & Conclusions from Today's Discussion:**
* **讀 traceback 的順序**：先看最後一行的錯誤類型與訊息（發生了什麼事）→ 往上讀呼叫鏈（越下面越接近錯誤被拋出的位置）→ 問自己：拋出錯誤的那一行真的寫錯了嗎？還是它收到了不該收到的資料？
* **Traceback 的限制**：traceback 只顯示「錯誤發生當下，誰在呼叫誰」，不會顯示「壞資料從哪裡來」。已經 return 的函式不會出現在裡面，**製造壞資料的兇手常常不在現場**，必須順著資料往回追。
* **`raise` 與 `assert` 的分工**：在資料邊界（A）用 `raise` 擋外部資料；在 `average`（C）可以加上 `assert scores, "average() requires non-empty list"`，因為只要 A 有做好，空 list 理論上不可能傳到這裡，真的傳進來就代表是程式設計師的錯。
* **修 bug 要回頭看需求**：如果 Bob 只是缺考、報表仍然要產出，直接 `raise` 反而會讓整份報表出不來，這時跳過 Bob 或標記為 `"N/A"` 可能更合適。技術選擇要依規格決定。
* **下一步練習方向**：更深的呼叫鏈，以及 exception 被 catch 後重新 raise 的情況（traceback 中會出現 `During handling of the above exception...`）。

⸻
