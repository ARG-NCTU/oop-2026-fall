# Week 8 — AI Tutor Learning Record (Part A)

- 學號：112511246
- Topic：Lecture 12 — 搜尋與排序（Searching and Sorting）
- 教材：MIT OCW 6.0001 Fall 2016, Lecture 12，題目依課堂內容出題
- 完成方式：直接整理五題概念題與解答，未採逐題提示後修正的流程。
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## Part A: True or False

### ① Check My Understanding

- Questions completed: 5 / 5
- Answers revised after AI hints: 不適用；未採逐題提示後修正的流程。

### 題目與解答

#### 第 1 題：先排序再搜尋

**題目：** 二分搜尋比線性搜尋快，所以遇到沒有排序的 list，先排序再用二分搜尋，一定比直接線性搜尋快。

**答案：錯。**

先排序再二分搜尋的成本是 O(n log n) + O(log n)，光是排序就比線性搜尋的 O(n) 大，所以只搜尋一次時，直接線性搜尋比較快。課堂用攤銷成本（amortized cost）說明：如果要搜尋 k 次，線性搜尋是 k × n，先排序則是 n log n + k × log n；排序的成本只付一次，分攤到之後每一次搜尋，當 k 夠大（大約超過 log n 次）時，先排序才划算。

#### 第 2 題：bubble sort 何時停止

**題目：** bubble sort 只要某一輪從頭到尾都沒有發生交換，就可以確定 list 已經排好，可以停止。

**答案：對。**

bubble sort 每一輪從左到右比較相鄰的兩個數，順序錯了就交換。如果某一輪完全沒有交換，代表每一對相鄰的數都已經是「左邊 ≤ 右邊」，整個 list 就是排好的。課堂的程式用變數 `swap` 記錄這一輪有沒有交換，`while swap:` 在沒有交換時就結束迴圈。也因為有這個提早停止，bubble sort 在 list 本來就排好時只要跑一輪，是 O(n)；最壞情況仍是 O(n²)。

#### 第 3 題：selection sort 遇到已排好的 list

**題目：** 如果 list 本來就已經排好，selection sort 的比較次數會降到 O(n)。

**答案：錯。**

selection sort 每一次都要走過「還沒排好的部分」，才能確定其中最小的是誰，不管 list 本來的順序如何，這一步都省不掉：第一次看 n 個、第二次看 n − 1 個……加起來約 n²/2 次比較，永遠是 O(n²)。即使 list 已經排好、一次交換都沒發生，比較的次數也不會減少。這點跟 bubble sort 不同，bubble sort 有「整輪沒交換就停」的機制，selection sort 沒有。

#### 第 4 題：合併兩個已排序的 list

**題目：** 合併兩個已經排好、長度加起來是 n 的 list，需要 O(n log n) 的時間。

**答案：錯。**

合併時只需要比較兩個 list 目前最前面的元素，把比較小的那個放進結果，再往後移一格。因為兩邊都已排好，最前面的元素就是各自剩下的最小值，所以每一步都能確定下一個最小值。每個元素只會被拿走一次，一邊拿完之後另一邊剩下的直接接上，總共 O(n)。O(n log n) 是整個 merge sort 的複雜度：log n 層，每層合併 O(n)。

#### 第 5 題：merge sort 的切片複製

**題目：** merge sort 用 `L[:middle]` 和 `L[middle:]` 切片複製 list，所以會像 Lecture 11 的 `bisect_search1` 一樣，被複製的成本拖慢，複雜度等級變差。

**答案：錯。**

`bisect_search1` 原本每一層只做 O(1) 的比較，加上 O(n) 的複製後，複製就成了主要成本，等級從 O(log n) 變成 O(n)。merge sort 則不同：每一層的合併本來就要處理全部 n 個元素，是 O(n)；每一層切片複製的總量也是 n，同樣是 O(n)。兩者加起來每層仍是 O(n)，共 log n 層，整體還是 O(n log n)，等級沒有改變，只是常數變大。

### ② My Misconception

- **Before（常見誤解）：** 以為二分搜尋比較快，所以資料沒排好時先排序一定划算；也以為所有 O(n²) 的排序法遇到已排好的 list 都會變快，以及只要有切片複製就一定會讓複雜度變差。
- **Now（觀念整理）：** 先排序是否划算取決於要搜尋幾次，排序成本要分攤到多次搜尋才值得。bubble sort 有提早停止的機制，最好情況是 O(n)，selection sort 則永遠是 O(n²)。切片複製會不會改變等級，要看它跟每層原本的工作量比起來是否更大：二分搜尋每層只做 O(1)，複製就變成主要成本；merge sort 每層本來就是 O(n)，複製不改變等級。

### ③ Challenge the AI

- **Question examined：** 第 1 題，先排序再二分搜尋是否一定比較快。
- **Why：** Too easy。
- **Brief explanation：** 題目用了「一定」這個絕對的字眼，即使不懂攤銷成本，看到「一定」也很容易猜出答案是錯。這題真正想測的是「搜尋幾次之後，先排序才划算」，改成具體的情境會更有鑑別度，例如「對一個 100 萬筆、沒排序的 list 搜尋 1000 次，先排序再二分搜尋比較快，對或錯？」，這樣就必須實際比較 k × n 和 n log n + k × log n 才能回答。

### ④ One-Minute Reflection

- **One thing I am still unsure about：** merge sort 在合併時會建立新的 list，切片時也會複製，需要額外的記憶體；bubble sort 和 selection sort 則是直接在原本的 list 裡交換，不需要額外空間。實際寫程式時，如果記憶體有限，要怎麼在速度和記憶體之間取捨，我還不確定。
- **Further question（延伸思考）：** Python 內建的 `sort()` 是以 merge sort 為基礎改良的，它對於已經「幾乎排好」的 list 會不會比較快？如果會，它是怎麼利用原本已有的順序的？
