# Weekly coding challenges

| Week | Challenge | Implementation | Tests |
| --- | --- | --- | --- |
| W2 | 單檔版本快照追蹤器 | [git_snapshot.py](w2/git_snapshot.py) | [test_git_snapshot.py](w2/test_git_snapshot.py) |
| W3 | 有容量限制的雙帳戶轉帳 | [transfer.py](w3/transfer.py) | [test_transfer.py](w3/test_transfer.py) |
| W4 | 多型停車帳單計費 | [parking_fees.cpp](w4/parking_fees.cpp) | [verify_challenges.py](verify_challenges.py) |
| W5 | 多型任務排程 | [task_scheduler.cpp](../../W5/task_scheduler.cpp) | [verify_scheduler.py](../../W5/verify_scheduler.py) |
| W6 | 無人載具任務消息狀態機 | [mission_state.cpp](w6/mission_state.cpp) | [verify_challenges.py](verify_challenges.py) |
| W7 | 安全候選的多行為加權決策器 | [weighted_decision.cpp](w7/weighted_decision.cpp) | [verify_weighted_decision.py](w7/verify_weighted_decision.py) |
| W9 | 有容量限制的批次裝載器 | [cargocpp.cpp](w9/cargocpp.cpp) | [verify_cargo.py](w9/verify_cargo.py) |
| W10 | 帶倒退編輯的括號驗證器 | [edited_brackets.py](w10/edited_brackets.py) | [verify_brackets.py](w10/verify_brackets.py) |

完整題目、三組範例、解法、複雜度與反思在上層的 w2.md～w7.md。

新增 W9、W10 的完整題目見上層 [w9.md](../w9.md)、[w10.md](../w10.md)。2026-11-10 實測分別為 **221／221** 與 **3,070／3,070** 項通過；證據見 [W9 結果](w9/verification.json)、[W10 結果](w10/verification.json)。W9 需 pybind11、g++ 與 Python 開發標頭，測試會在臨時目錄編譯並匯入真實擴充模組；W10 僅需 Python 3。各週重跑方式見其學習單。這兩週未使用既有 W2～W7 的 sanitizer 設定。

## Reproduce the results

需要 Python 3、pytest、Git、g++；C++ 以 C++11 編譯。以下在 Linux／WSL 執行：

```bash
cd 112511054/AI_tutor/challenges
python3 -m venv /tmp/aoop-challenges-venv
/tmp/aoop-challenges-venv/bin/python -m pip install -r requirements.txt
/tmp/aoop-challenges-venv/bin/python verify_challenges.py
cd ../../W5
python3 verify_scheduler.py
```

verify_challenges.py 在臨時目錄編譯執行檔，結束後自動清理；Git 比較測試也只使用臨時 repo。C++ 測試啟用 AddressSanitizer、UndefinedBehaviorSanitizer 與洩漏偵測；W5 原測試啟用 AddressSanitizer 與洩漏偵測。

2026-10-14 結果：W2 為 11 項 pytest 加 3 組命令列案例、W3 為 15 項 pytest 加 3 組命令列案例、W4 為 30 組、W5 為 7 組、W6 為 36 組；共 105 項通過。

- W2～W4、W6 的逐項輸出：[verification.json](verification.json)。
- W5 本次重新驗證：[verification-2026-10-14.txt](../../W5/verification-2026-10-14.txt)。

verification.json 會在重新執行成功時更新。程式挑戰中的簡化狀態模型不能代替真實 Git 的全部功能或實際 MOOS 航行測試。

## W7

2026-10-20：W7 加權決策器 114／114 組通過；結果見 [w7/verification.json](w7/verification.json)。

```bash
cd 112511054/AI_tutor/challenges/w7
python3 verify_weighted_decision.py
```

本週測試工具獨立執行，不需要 pytest。既有 W2～W6 的 105 項結果保留為原測試日期的紀錄。
