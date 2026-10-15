# AOOP Lec3 學習單

**Topic:** String Manipulation, Guess-and-Check, Approximation, Bisection Search  
**Date:** 2026-10-15

---

## ① Check My Understanding

Questions completed: **5 / 5**  
Answers revised after AI hints: **2 / 5**

---

## ② My Misconception

### Before: I thought…
- Guess-and-Check 不一定能完成任務，因為可能不存在正確答案。
- 我傾向將 Bisection Search 理解成「每次砍掉一半」的方法。

### Now: I understand…
- Guess-and-Check 的重點是有限且可驗證的搜尋空間。即使沒有解，也能在檢查完所有可能後正確回報無解。
- Bisection Search 的核心不在於一定砍掉一半，而在於持續縮小可能解範圍，並保留真正答案所在的區間。
- String 是 immutable，所謂修改字串內容，本質上通常是建立新字串後再進行 rebind。
- Approximation 要保證停止，除了持續逼近答案外，還需要明確的容忍誤差（tolerance）或停止條件。

---

## ③ Challenge the AI

### One AI-generated question I challenged:
第 2 題（Guess-and-Check）

### Why?
☑ Ambiguous  
☐ Oversimplified  
☐ Technically questionable  
☐ Too easy  
☐ Other: __________

### Brief explanation:
題目中的「成功完成任務」容易被理解成「找到正確答案」，而非「正確結束搜尋程序」。

若問題本身無解，Guess-and-Check 無法找到答案，但仍然可以搜尋完所有候選解並正確回報無解。因此題目用詞應更精確地描述為：

> 在有限搜尋空間中完成搜尋，並回報找到答案或不存在答案。

---

## ④ One-Minute Reflection

### One thing I am still unsure about:
Bisection Search 是否只是眾多搜尋方法中的基礎版本？除了二分搜尋之外，是否存在更高階、更快速或更具一般性的搜尋與最佳化方法，以及它們適用的條件為何？

---

## 個人重點整理

1. Immutable 不代表不能改變變數名稱綁定的內容，而是不能直接修改原物件。
2. Guess-and-Check 的關鍵是有限搜尋空間與可驗證性。
3. Bisection Search 需要答案具有順序性且能判斷應保留哪一側區間。
4. Approximation 的有限性來自停止條件，而非單純持續逼近答案。
5. 分辨必要條件（necessary condition）與充分條件（sufficient condition）比背誦定義更重要。
