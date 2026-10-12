# MOOS-IvP 船舶航行模擬實驗

使用 MOOS-IvP 的 `s1_alpha` 範例，練習修改船隻顏色、航行路徑、速度按鈕及轉向反應。

## 實驗環境

- Windows + WSL Ubuntu 24.04
- MOOS-IvP 24.8.1
- Visual Studio Code

## 主要檔案

| 檔案 | 用途 |
| --- | --- |
| `alpha.moos` | 設定啟動程式、船舶模擬參數、顯示介面與操作按鈕 |
| `alpha.bhv` | 設定巡航、返航行為與航點 |

本實驗在 `s1_alpha_hw` 副本中修改，保留原始 `s1_alpha` 範例。

## 執行方式

執行前需先安裝並編譯 MOOS-IvP，且將其 `bin` 資料夾加入 PATH。

在 Ubuntu 終端機切換至實驗資料夾：

```bash
cd ~/moos-ivp/ivp/missions/s1_alpha_hw
pAntler alpha.moos
```

若資料夾放在其他位置，請調整 `cd` 路徑。

視窗開啟後，按 **DEPLOY** 啟動自動航行。停止模擬時，回到執行 `pAntler` 的終端機按 **Ctrl+C**。

修改設定後需儲存並重新啟動模擬。

## 實驗修改

### 1. 修改船隻顏色

在 `alpha.moos` 的 `pNodeReporter` 區塊加入：

```text
platform_color = red
```

`pNodeReporter` 將顏色加入船舶狀態報告，讓 `pMarineViewer` 顯示紅色船隻。

### 2. 將航線改為正方形

在 `alpha.bhv` 的 `waypt_survey` 區塊設定：

```text
polygon = 60,-40:60,-160:180,-160:180,-40:60,-40
```

每組數字代表 `(X,Y)` 座標，單位為公尺，冒號用來分隔航點。

| 順序 | 座標 | 位置 |
| --- | --- | --- |
| 1 | `(60,-40)` | 左上角 |
| 2 | `(60,-160)` | 左下角 |
| 3 | `(180,-160)` | 右下角 |
| 4 | `(180,-40)` | 右上角 |
| 5 | `(60,-40)` | 回到起點 |

航線為邊長 120 公尺的正方形。最後重複起點，讓航線閉合。

航點定義的是目標路徑；船舶實際轉彎時仍可能產生弧形軌跡。

### 3. 新增速度按鈕

在 `alpha.moos` 的 `pMarineViewer` 區塊加入：

```text
button_five = MUCHSLO # WPT_UPDATE=speed=1.0
button_six  = MUCHFST # WPT_UPDATE=speed=4.0
```

| 按鈕 | 目標速度 |
| --- | --- |
| MUCHSLO | 1.0 m/s |
| MUCHFST | 4.0 m/s |

按鈕透過 `WPT_UPDATE` 發布速度設定。`alpha.bhv` 中的巡航行為透過以下設定接收更新：

```text
updates = WPT_UPDATE
```

實際速度會隨控制器與模擬動態逐漸改變，可從畫面下方的 `Spd` 觀察。

### 4. 調整轉向反應

在 `alpha.moos` 的 `uSimMarineV22` 區塊，將：

```text
turn_rate = 95
```

改為：

```text
turn_rate = 50
```

在相同速度與舵角條件下，降低 `turn_rate` 會使轉向較慢，提高則使轉向較快。此數值不能直接解讀為船隻每秒固定轉動的角度。

比較效果時，應保持相同速度，觀察同一個航線轉角。實際轉彎也受控制器及其他模擬參數影響。

## 系統運作邏輯

各程式透過 MOOSDB 交換資料：

1. `pMarineViewer` 在按下 DEPLOY 後發布啟航設定。
2. `pHelmIvP` 根據航點與行為條件產生目標航向和速度。
3. `pMarinePIDV22` 將目標轉換成舵角與推力。
4. `uSimMarineV22` 模擬船舶移動。
5. `pNodeReporter` 回報船舶位置、速度及顏色。
6. `pMarineViewer` 顯示船舶狀態、航線與軌跡。

## 驗證結果

- 已確認船隻顯示為紅色。
- 已確認目標航線為封閉正方形。
- 已確認兩個新增按鈕可調整速度至接近 1.0 與 4.0 m/s。
- 已調整轉向參數。

## 範例來源

本實驗修改自 MOOS-IvP 24.8.1 的 `ivp/missions/s1_alpha` 範例，並非從零開發完整模擬系統。原始程式與素材的授權請參閱 MOOS-IvP 專案所附文件。
