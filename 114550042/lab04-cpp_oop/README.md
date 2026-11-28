# C++ 上機驗收

只需要改 `student.cpp`，其他檔案都不要動。

## 步驟
1. 檢查環境（看到 `ENV OK` 才往下）

       make doctor

   如果缺工具：

       sudo apt update && sudo apt install -y build-essential git

2. 打開專案，一節一節進行：先讀 `GUIDE.md` 的觀念說明，再完成 `student.cpp` 對應的 TODO（每個約 1~3 行）

       code .

   在 VS Code 裡對 `GUIDE.md` 按 `Ctrl+Shift+V` 可以看排版後的版本。

3. 驗收

       make check

   畫面最後出現 `ALL PASS (4/4)`，就叫助教過來看終端機。

## 規則

- 可以用 AI 寫，但助教會隨機指一行，請你用一句話說明「為什麼這樣寫」。說不出來就不算完成。
- FAIL 時，畫面會告訴你原因和該回頭看 GUIDE.md 的哪一節。
- 編譯失敗時，從「第一個」error 開始看。