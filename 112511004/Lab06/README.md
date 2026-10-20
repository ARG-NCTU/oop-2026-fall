# Lab06：MOOS-IvP 行為權重與航速控制實驗

本實驗使用 MOOS-IvP 模擬單艘無人船，觀察「往東邊航點前進」與「船頭朝北」兩個行為如何透過權重共同決定航向與航速，並測試如何在保留原有權重的情況下，讓停止的船重新前進。

## 實驗目標

1. 比較四組行為權重下的航行結果。
2. 測試兩個 PWT 等比縮放是否影響決策。
3. 分析 Case 3 停止的原因。
4. 新增具有獨立 PWT 的航速行為，驗證能否讓 Case 3 前進。

## 實驗原理

`pHelmIvP` 會綜合各行為提供的效用函數，選擇加權總分最高的「航向＋航速」組合。

```text
加權總分 = PWT_EAST × 往東行為評分
         + PWT_NORTH × 朝北行為評分
```

- `BHV_Waypoint`：前往航點 `(3000, 0)`，使用 `ipf_type = roc`。
- `BHV_ConstantHeading`：期望航向為 `0°`，即正北。
- `pwt`：行為在總分中的權重，表示其相對影響程度。

本實驗的決策空間包含航向 `0～359°`、航速 `0～4 m/s`。航速 `0` 也是合法的候選決策。航向 `0°` 與 `360°` 都代表正北，`90°` 代表正東。

## 執行環境與檔案

實驗環境為 WSL Ubuntu 24.04，使用 MOOS-IvP，模擬介面為 pMarineViewer v24.8.1，並透過 VS Code 編輯設定檔。

將本 README 與實驗檔案放在同一個資料夾，結構如下：

```text
exp1_tugofwar/
├── README.md
├── launch.sh          # 依 Case 產生設定並啟動模擬
├── clean.sh           # 清理產生的紀錄與設定檔
├── meta_tug.moos      # 模擬器、Helm、控制器及介面設定
└── meta_tug.bhv       # 行為與各 Case 的 PWT 設定
```

啟動後會產生 `targ_tug.moos`、`targ_tug.bhv` 與帶有時間戳記的 `LOG_TUG_CASE*` 資料夾。應編輯 `meta_*` 原始設定檔；`targ_*` 每次啟動時會重新產生。

## 執行方式

先確認已安裝 MOOS-IvP，且相關執行檔可由終端機找到：

```bash
command -v MOOSDB pAntler nsplug pHelmIvP pMarineViewer
```

進入實驗資料夾並執行：

```bash
cd ~/exp1_tugofwar
chmod u+x launch.sh clean.sh
./launch.sh --case=1 --warp=5
```

模擬視窗開啟後，按 **DEPLOY** 啟動行為。每次結束目前模擬後，再將 `--case=1` 改為 `--case=2`、`--case=3` 或 `--case=4`，分別進行測試。

`--warp=5` 表示模擬時間約以現實時間的五倍運行，不會直接把船速設定乘以五。若要以一般時間速度觀察，可使用 `--warp=1`。

在左側 App 清單選取 `pHelmIvP`，可以查看啟動的行為、各行為的 PWT，以及 Helm 選出的 `course`、`speed`。畫面下方的 `Hdg`、`Spd` 則是船的實際航向與速度。

## 四個 Case 的觀察結果

下表記錄新增航速行為之前的實驗結果。

| Case | PWT_EAST | PWT_NORTH | 觀察結果 |
|---|---:|---:|---|
| 1 | 100 | 100 | 船向東北方向持續前進，起步轉彎後，軌跡大致呈直線。 |
| 2 | 100 | 30 | 船朝東偏北前進，相較 Case 1 更偏向東方。 |
| 3 | 30 | 100 | 兩個行為皆啟動，但 Helm 選擇航向 0°、航速 0，船停在起點。 |
| 4 | 100 | 0 | 船先從起始朝南的方向轉彎，再朝東邊航點前進。 |

Case 1 顯示兩個行為可以產生折衷的決策；Case 2 增加往東行為的相對影響；Case 4 則將朝北行為的加權貢獻設為零。

