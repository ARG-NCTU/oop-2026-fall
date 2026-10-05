Topic: C++ Core Concepts: Reference, Encapsulation, Virtual Functions, and Dynamic Memory (Lab04)  Date: 2026-10-05

① Check My Understanding

Questions completed: 5 / 5

Answers revised after AI hints: 1 / 5

② My Misconception

Before: I thought…
我一開始以為在 C++ 中動態配置的陣列直接呼叫 delete p; 就能完整釋放記憶體，並不需要特別區分純變數與陣列的釋放語法。

Now: I understand…
動態配置陣列時必須使用 delete[] p; 來成對釋放，否則只會解構第一個元素造成未定義行為與記憶體洩漏，且容易被 AddressSanitizer 偵測出錯誤。

③ Challenge the AI

One AI-generated question I challenged:
關於 clamp_value(double &v, double lo, double hi) 傳參考參數是否可以在不回傳值的情況下直接修改外部呼叫者變數的真偽題。

Why?

☐ Ambiguous
☑ Too easy
☐ Technically questionable
☐ Oversimplified
☐ Other: __________

Brief explanation:
傳參考作為呼叫者變數別名的概念非常基礎，題目缺乏針對邊界條件（如 v == lo 或 lo > hi）的更深層判斷與挑戰性。

④ One-Minute Reflection

One thing I am still unsure about:
在多重繼承與多型複雜應用下，vtable（虛擬函式表）底層指標在記憶體中的具體配置與呼叫開銷細節。

---

Part B: Coding Challenge (Lab04 - C++ Object-Oriented Fundamentals & Memory Management)

* Core concept from today's OCW lecture: Reference Passing, Class Encapsulation with Initialization Lists, Virtual Function Polymorphism with override, and Heap Dynamic Memory Allocation (new[] / delete[]).
* AI-generated coding challenge title: Object-Oriented Task Manager with Memory Management and Polymorphic Application Base.

My Initial Approach – Before AI Help
* My approach: 撰寫 clamp_value 使用 if-else 依序將數值夾在範圍內；Battery 建構子使用初始化清單並於 setLevel 檢查 0 至 100 邊界；MyApp 繼承 BaseApp 並覆寫虛擬函式；make_buffer 配置記憶體後以迴圈依序賦值，最後在 free_buffer 使用 delete[]。

AI Tutor Help
* Did you ask the AI Tutor for help?
  - [ ] No – I solved it independently
  - [x] Yes – I received one or more hints
* The most useful hint/question from AI was: 提醒我覆寫父類別虛擬函式時務必加上 override 關鍵字，以避免簽署不一致並滿足編譯器 -Werror=suggest-override 的嚴格檢查。
* It helped me realize that: 善用編譯器的強制檢查機制能在編譯期直接揪出虛擬函式名稱、參數或 const 修飾符不符合的隱含錯誤。

My Revision
* Did you change your approach or code after interacting with AI?
  - [ ] No
  - [x] Yes
* What did you change, and why?: 在 student.cpp 的 MyApp 成員函式後全面補上 const override 與 override 修飾詞，並確保 free_buffer 採用 delete[] 配對釋放陣列記憶體。

Verification
* My final program:
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
  - [ ] Still has unresolved problems
* One edge case I tested:
  - Input: b.setLevel(120) 與 b.setLevel(-1)
  - Expected output: 回傳 false 且維持原本 m_level 數值不被篡改
  - Actual output: 正確回傳 false 且 getLevel() 維持原值，通過 test_battery() 檢查

One-Minute Reflection
* What idea from the OCW lecture did you transfer to this new problem? 將講義介紹的物件封裝概念應用於防止非預期數值寫入私有成員，以及運用指標搭配純虛擬基底類別實現介面分離。
* One thing I understand better now: 清楚掌握了建構子初始化清單的執行時機，以及 AddressSanitizer 偵測記憶體洩漏與懸置指標的工作原理。
* One thing I am still unsure about: 解構子被宣告為虛擬函式時，透過基底類別指標進行記憶體釋放的完整鏈式調用細節。
