# Lab02：Git 與 GitHub 版本控制入門

本實驗練習 Git 的基本操作，了解檔案修改如何從工作目錄進入暫存區、形成 commit，再同步到 GitHub。課程的主要交付檔案為 `intro.md`，不是 Python 或 C++ 程式。

## 學習目標

- 分辨工作目錄、暫存區、本機儲存庫與遠端儲存庫。
- 使用 `git status`、`git diff` 檢查檔案變更。
- 透過 `git add` 與 `git commit` 建立版本。
- 理解 `push`、`pull`、Fork、Clone 與 Pull Request 的用途。

## 檔案結構

```text
lab02/
├── README.md
├── intro.md                 # 個人介紹範本，待自行填寫
├── .gitattributes           # 確保 shell 腳本使用 LF 換行
└── code/
    └── local_git_demo.sh     # 新增的本機 Git 示範，無網路操作
```


## Git 的四個位置

| 位置 | 保存的內容 | 相關指令 |
|---|---|---|
| Working Directory | 目前正在編輯的檔案 | `git status`、`git diff` |
| Staging Area | 準備納入下一次 commit 的變更 | `git add`、`git diff --cached` |
| Local Repository | 已提交的版本與歷史 | `git commit`、`git log` |
| Remote Repository | GitHub 等平台上的儲存庫 | `git push`、`git pull` |

```text
修改檔案 → git add → 暫存區 → git commit → 本機版本歷史
                                             │
                                          git push
                                             ↓
                                        遠端儲存庫
```

`git add` 會暫存當下的檔案內容；若之後又修改檔案，需要再次 `add` 才會把新修改放入同一次 commit。`git commit` 建立本機版本，不會自動將檔案上傳到 GitHub。

## 教材任務

依教材第 10～12 頁，原課堂任務包含：

1. 使用 WSL 終端機準備 Git，設定提交者名稱與 email。
2. 設定 SSH 金鑰並驗證 GitHub 認證。
3. 建立名為 `github-practice-<學號>` 的 GitHub repository。
4. 建立 `intro.md`，至少包含姓名、學號與 GitHub 帳號。
5. 建立至少一個 commit，以 SSH URL 設定 remote 並 push。
6. 繳交 repository 連結，確認 GitHub 上可看到 `intro.md`。

這些是教材要求；原始 repo 連結、commit 與認證截圖未保留，因此本紀錄未將它們列為已驗收成果。教材另介紹組員協作與 PR，與個人的首次 push 任務分開理解。

## 本機練習方式

環境需求：Bash 與 Git，例如 WSL 或 Git Bash。這是執行需求，並非當年的環境紀錄。

在 `lab02` 資料夾執行：

```bash
git --version
bash code/local_git_demo.sh
```

腳本會在系統暫存目錄建立獨立的練習 repo，複製 `intro.md` 範本，並完成以下步驟：

1. 建立 `main` 分支，查看未追蹤檔案。
2. 暫存 `intro.md`，查看即將提交的內容。
3. 建立第一個 commit。
4. 新增一段練習筆記，查看尚未暫存的差異。
5. 建立第二個 commit，顯示版本歷史與最後狀態。

成功結束時，應看到兩筆 commit，最後 `git status --short` 不輸出任何檔案。腳本會印出練習 repo 的位置；這些是本次示範產生的新紀錄。

腳本使用 `Lab02 Demo` 和 `lab02@example.invalid` 作為示範提交身分，僅對個別 commit 指令生效，不會修改全域 Git 設定。它不設定遠端、不讀取金鑰，也不執行 SSH、push 或 pull。


## 常用指令筆記

以下指令應在要檢查的 repo 中逐一執行。

```bash
git status                       # 檢查工作目錄與暫存區
git diff                         # 查看尚未暫存的修改
git add intro.md                 # 暫存指定檔案
git diff --cached                # 檢查即將提交的內容
git commit -m "add intro.md"      # 建立本機版本，需先設定提交身分
git log --oneline --graph         # 查看版本歷史
```

| 概念／指令 | 用途與注意事項 |
|---|---|
| `git push` | 將本機 commit 傳到遠端；commit 成功不代表 push 已完成。 |
| `git pull` | 取得遠端更新並整合到目前分支；未完成修改可能影響整合。 |
| `git stash -u` | 暫存已追蹤檔案的修改及未追蹤檔案，不含忽略檔案。 |
| `git stash pop` | 將暫存修改套回；可能產生衝突，需先檢查結果。 |
| Fork | 在 GitHub 建立自己帳號下的專案副本。 |
| Clone | 將既有儲存庫及其版本歷史複製到本機。 |
| Pull Request | 提議把一個分支的變更合併到另一個分支或專案，供維護者審查。 |

教材以 SSH 示範遠端工作流程。本資料夾保留其概念說明，未執行遠端操作。

## 重點整理

- 提交前先看 `status`、`diff` 與 `diff --cached`，確認提交範圍。
- 空資料夾不會被 Git 單獨追蹤；建立小組資料夾時，還需要加入實際檔案。
- commit 訊息應描述變更，例如 `add intro.md`。
- 工作區有未完成修改時，應先處理或暫存，再整合其他版本。

