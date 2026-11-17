# Lab05：MOOS-IvP s1_alpha 船舶航行模擬

使用 MOOS-IvP 內建的 `s1_alpha` 範例，練習修改船隻外觀、操作按鈕與航行路徑。

## 環境

- macOS（Apple M2），MOOS-IvP 從原始碼編譯
- Visual Studio Code

## 修改內容

| 檔案 | 修改 | 說明 |
|---|---|---|
| `alpha.moos` | `platform_color = yellow` → `pink` | 地圖上的船改成粉紅色 |
| `alpha.moos` | 新增 `button_five = MUCHSLO # WPT_UPDATE=speed=1.0` | 按下後航速改為 1.0 m/s |
| `alpha.moos` | 新增 `button_six = MUCHFST # WPT_UPDATE=speed=4.0` | 按下後航速改為 4.0 m/s |
| `alpha.bhv` | 航點多邊形從五邊形改為長方形 `60,-40:60,-140:160,-140:160,-40` | 船改成繞長方形航行 |

### 按鈕的運作方式

`pMarineViewer` 的按鈕格式是 `button_N = 顯示文字 # 變數=值`。按下按鈕時，會發布 `WPT_UPDATE=speed=1.0`，`BHV_Waypoint` 收到後就把航速更新成新的值，不需要重新啟動任務。

## 執行方式

```bash
cd ~/moos-ivp/ivp/missions/s1_alpha
pAntler alpha.moos
```

地圖出現後按 **DEPLOY** 讓船出發，按 **MUCHSLO / MUCHFST** 可以切換航速，按 **RETURN** 讓船返航。結束時在終端機按 `Ctrl + C`。

## 結果

- 船以粉紅色顯示，並依照長方形的四個航點繞行。
- 按下 MUCHSLO、MUCHFST 後，船速分別變為 1.0、4.0 m/s。
