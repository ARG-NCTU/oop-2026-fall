# 📝 Learning Reflection & Concept Check

**Topic:** Tuples, Lists, Aliasing, Mutability, and Cloning (MIT 6.0001 Lecture 5)  
**Date:** 2026-09-07  

---

### ① Check My Understanding

* **Questions completed:** 5 / 5
* **Answers revised after AI hints:** 2 / 5  
  *(Q2: 巢狀串列淺拷貝的副作用；Q5: 函式傳參時的原地修改 vs 重新賦值)*

---

### ② My Misconception

**Before: I thought…**  
只要透過切片語法（如 `B = A[:]`）將串列拷貝一份，新舊兩個串列就已經完全獨立，對 `B` 內部進行任何修改都絕不可能影響到 `A`。同時直覺認為只要把串列傳入函式，在函式內對該變數做任何操作都會直接影響外部原資料。

⸻

**Now: I understand…**  
切片 `A[:]` 只是「淺拷貝（Shallow Copy）」，只複製了最外層的容器；如果串列中包含指標或巢狀串列等可變物件，內層依然指向同一份記憶體位址（Aliasing），修改內層可變元素仍會對原串列產生副作用（Side Effects）。  
此外在函式中，只有原地修改（In-place Mutation，如 `data.append()`）會改動原物件；若使用運算子重新賦值（Re-binding，如 `data = data + [1]`），會建立新物件並切斷原本的參照連結，不會改動外部原物件。

---

### ③ Challenge the AI

**One AI-generated question I challenged:**  
Question 5（探討函式參數傳遞串列時，`data.append(1)` 與 `data = data + [1]` 對外部原串列影響的題目）

⸻

**Why?**

* [ ] Ambiguous
* [x] Oversimplified
* [ ] Technically questionable
* [ ] Too easy
* [x] Other: 不夠貼近實際開發應用情境（Less connected to real-world application contexts）

**Brief explanation:**  
題目使用的是較為抽象的變數與語法對比（如 `data.append(1)` 對比 `data = data + [1]`），感覺偏向紙上談兵。如果能包裝成實際專案開發的情境（例如：電商購物車追加商品、使用者帳號角色權限更新等真實商業邏輯），會更能體會實務上踩雷時的具體症狀與除錯關鍵。

---

### ④ One-Minute Reflection

**One thing I am still unsure about:**  
在實際專案開發中傳遞資料時，究竟該如何系統性地權衡「安全性（避免非預期副作用）」與「執行效率（減少記憶體拷貝開銷）」？有些操作會原地修改原物件、有些則會回傳新物件，面對複雜的大型系統時，該如何設計與規範才最不容易搞混或引發 Bug？

⸻

**Key Takeaways & Conclusions from Today's Discussion:**
* **安全優先（純函式思維）**：一般商業邏輯與中小規模資料，優先採用「不改動原物件、回傳全新物件」（例如 List Comprehension `[s + 5 for s in scores]`），從根本上消除副作用（No Side Effects），程式最穩定且易測試。
* **大資料的原地修改規範**：處理海量數據若為節省記憶體與時間而必須原地修改（In-place Mutation），應嚴格遵循 Python 慣例：函式一律回傳 `None`，且函式名稱加上明確動詞或 `_inplace` 後綴提醒呼叫者。
* **介面防禦性設計**：傳遞關鍵唯讀資料（如使用者權限、座標）時，主動轉為 `tuple` 傳出，利用其不可變性（Immutability）強制防止外部函式誤改內部狀態。
* **拷貝時機與粒度**：純數值或字串串列使用淺拷貝（`[:]`）即可兼顧效能與安全；若結構內部含有巢狀串列或字典等指標參照，則須使用 `copy.deepcopy()` 才能完全切斷 Aliasing 關聯。

⸻
