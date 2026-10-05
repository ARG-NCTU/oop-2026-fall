Topic: Pytest Implementation and Unit Testing (lab03-pytest)  Date: 2026-09-21

① Check My Understanding
Questions completed: 5 / 5
Answers revised after AI hints: 1 / 5

② My Misconception
Before: I thought…
我一開始以為只要寫出函式功能即可，測試部分隨便寫幾行 print 檢查輸出符合就好，不需要特別寫獨立的測試框架。
Now: I understand…
透過 Pytest 可以系統化地自動執行多組測資，並且利用 pytest.raises 來嚴謹地驗證例外狀況（如分數範圍錯誤或空列表）是否正確被拋出。

③ Challenge the AI
One AI-generated question I challenged:
關於 average() 傳入空列表時是否一定要拋出 ValueError 的測試題。
Why?
☑ Too easy
Brief explanation:
因為這個邊際條件在作業要求中非常明確，AI 出的判斷題選項一眼就能看出正確答案，缺乏挑戰性。

④ One-Minute Reflection
One thing I am still unsure about:
- 如何在大型專案中更有效率地面對複雜的依賴項進行 pytest 的 Mock 測試。

Part B: Coding Challenge (lab03-pytest - Grade & Average Implementation)
- Core concept from today's OCW lecture: Python Unit Testing, Exception Handling (ValueError), and Pytest Framework Assertions.
- AI-generated coding challenge title: Grade Calculation and Average Score Validator with Exception Handling.

My Initial Approach – Before AI Help
- My approach: 撰寫 letter_grade() 透過 if-elif 判斷成績級距，並在分數小於 0 或大於 100 時用 raise ValueError；average() 則先檢查列表是否為空，若空則拋出錯誤，否則回傳平均值。

AI Tutor Help
- Did you ask the AI Tutor for help? [x] Yes – I received one or more hints
- The most useful hint/question from AI was: 引導我使用 pytest.raises(ValueError) 來完整測試例外狀況是否被正確觸發。
- It helped me realized that: 測試不只要驗證「對的答案」，更要嚴格確保「錯的輸入」會引發預期的例外報錯。

My Revision
- Did you change your approach or code after interacting with AI? [x] Yes
- What did you change, and why?: 補充了針對極端邊際條件（如分數壓在 60、70、80、90 分的級距邊界，以及傳入 -1 與 101）的測試案例，讓測試覆蓋率更完整。

Verification
- My final program:
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
- One edge case I tested:
  - Input: letter_grade(101)
  - Expected output: ValueError("Score must be between 0 and 100")
  - Actual output: ValueError successfully raised and passed via pytest

One-Minute Reflection
- What idea from the OCW lecture did you transfer to this new problem? 將課堂學到的單元測試結構與 Git 結合 WSL 的版控流程應用在作業繳交中。
- One thing I understand better now: 更加熟悉了 Pytest 的執行邏輯以及 Git 在面對遠端重置時利用 --rebase 安全更新的方法。
- One thing I am still unsure about: 實際開發大型軟體時，測試檔案與原始碼的最佳資料夾結構配置細節。
