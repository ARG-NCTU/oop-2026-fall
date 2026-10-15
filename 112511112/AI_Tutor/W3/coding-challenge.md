OCW Lec3 Coding Challenge Reflection
Name: 朱昱瑋 Date: 2026-10-15 Topic: Approximation & Bisection Search

1. Today’s Challenge
Core concept from today’s OCW lecture:

Bisection Search、Approximation、維護搜尋區間（low/high）與誤差容忍範圍（epsilon）。

AI-generated coding challenge title:

Minimum Square Side Length

2. My Initial Approach — Before AI Help
Before asking AI for hints, briefly describe how you planned to solve the problem.

My approach:

使用 Approximation。

從 side = 0 開始，每次增加一個很小的增量（epsilon × 0.01），持續計算 side²。

當 area ≥ target_area 時停止。

我認為只要步長夠小，就能逐漸逼近答案。

3. AI Tutor Help
Did you ask the AI Tutor for help?

☐ No — I solved it independently

☑ Yes — I received one or more hints

The most useful hint/question from AI was:

「你的程式是否真的保證：

abs(side² - target_area) < epsilon？」

以及：

「當 target_area = 0.25 時，

high = target_area 是否一定包含答案？」

It helped me realize that:

我的第一版雖然能逼近答案，但沒有真正檢查誤差是否小於 epsilon。
Approximation 可以工作，但效率很差。
Bisection Search 應該利用大小關係來縮小搜尋區間。
target_area < 1 時，答案可能大於 target_area，因此 high = target_area 不一定正確。
4. My Revision
Did you change your approach or code after interacting with AI?

☐ No

☑ Yes

What did you change, and why?

原本：

使用 Approximation。
每次 side += epsilon × 0.01。
沒有使用搜尋區間。
修改後：

改用 Bisection Search。

引入 low 與 high。

每次取區間中點 side。

根據 side² 是否大於 target_area 決定保留左半或右半區間。

加入：

if target_area < 1: high = 1.0

確保答案一定落在搜尋區間內。

另外將第一次計算中點移到迴圈之前，使演算法完全符合二分搜尋流程。

5. Verification
My final program:

☑ Passed the provided examples

☑ Passed additional edge cases

☐ Still has unresolved problems

One edge case I tested:

Input:

target_area = 0.25

epsilon = 0.001

Expected output:

0.5

Actual output:

約 0.5（誤差小於 epsilon）

6. One-Minute Reflection
What idea from the OCW lecture did you transfer to this new problem?

原本課堂是在利用 Bisection Search 求 cube root。

這次則是利用相同概念求 square root（由面積反推邊長）。

雖然問題不同，但都使用：

維護包含答案的搜尋區間
每次排除一半不可能答案
利用誤差條件判斷何時停止
One thing I understand better now:

Bisection Search 真正重要的不是「每次砍一半」，

而是：

答案始終保留在搜尋區間內。
搜尋區間持續縮小。
最終收斂到允許誤差範圍內。
One thing I am still unsure about:

除了 Bisection Search 之外，

還有哪些搜尋或最佳化方法（例如 Newton's Method、Gradient Descent、Interpolation Search）？

它們各自適合什麼類型的問題？
