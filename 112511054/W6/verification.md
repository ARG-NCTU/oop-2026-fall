# 實際驗證紀錄

日期：2026-10-12（Asia/Taipei）。環境：Ubuntu 26.04.1 LTS、WSL 2、WSLg。

## 安裝與編譯

依課堂簡報安裝開發工具、FLTK、OpenGL、圖像函式庫及 xterm，下載官方 `v24.8.1`，執行 `./build.sh` 成功（exit code 0）。完整編譯日誌保留於 WSL 的 `/home/nick0/moos-ivp-build.log`。

版本 commit：`477be7e91bf220185d55e5a2a9dba16dbde32c3f`。

已確認 `MOOSDB`、`pHelmIvP`、`pAntler`、`pMarineViewer` 都位於 `/home/nick0/moos-ivp/bin`。

## 任務整合測試

執行 `pAntler alpha.moos --MOOSTimeWarp=10`，以十倍模擬時間加速測試；一般啟動腳本仍使用一倍時間。`pMarineViewer` 程序成功啟動。本次用 `uPokeDB` 發布與按鈕相同的消息測試速度切換，沒有手動點擊 GUI 按鈕。

下列時間是日誌中的模擬任務秒數：

| 驗證項目 | 日誌證據 | 結果 |
| --- | --- | --- |
| 藍色船身 | `NODE_REPORT_LOCAL` 含 `COLOR=dodger_blue` | 通過 |
| 閉合正方形 | `VIEW_SEGLIST` 含 `pts={60,-40:60,-160:180,-160:180,-40:60,-40}` | 通過 |
| 慢速更新 | 181.41130 秒收到 `WPT_UPDATE=speed=1.0`；185.50105 秒 `DESIRED_SPEED=1.00000` | 通過 |
| 快速更新 | 287.73681 秒收到 `WPT_UPDATE=speed=4.0`；291.22885 秒 `DESIRED_SPEED=4.00000` | 通過 |
| 完成巡航 | 393.44626 秒 `behavior-name=waypt_survey,completed` | 通過 |
| 完成返航 | 422.14472 秒 `behavior-name=waypt_return,completed` | 通過 |
| 任務完成 | 422.14493 秒 `MISSION=complete` | 通過 |
| 行為異常 | 日誌沒有 `BHV_ERROR` 或 `BHV_WARNING` 記錄 | 通過 |

精簡原始證據見 `verification-evidence.json`；完整 `.alog` 保留於本機 `MOOSLog_12_10_2026_____19_30_03`，由 `.gitignore` 排除。測試中出現 Fontconfig 初始化提醒、預設日誌路徑提醒，以及十倍時間模式下外部查詢／發布工具的消息延遲提醒；未阻止巡航或返航完成。

轉向參數的效果說明根據此版本原始碼整理；尚未實際執行不同 PID／轉向率的比較實驗。
