# MOOS-IvP 延伸 Lab：行為權重與拔河

準備日期：2026-10-19；學號：112511054。教材簡報仍標示「2026 AOOP W6」，此處以本工作區的 `W7` 資料夾保存本次延伸內容。

教材：[MOOS-IvP intro.2](https://docs.google.com/presentation/d/1oZKZzyBvslyOxXwQshp9kFUxYXDEvnFTxUkRwxygNyA/edit)；[老師提供的資料夾](https://drive.google.com/drive/folders/1Pt-iVzwTIAfxCvV1v8lyDeWjTA-R9XzO)。

## 已準備的環境

原始 `Lab06.zip` 已下載保留，解壓後的任務位於 WSL：

```text
/home/nick0/moos-ivp/ivp/missions/exp1_tugofwar
```

已依後續要求，直接將此任務的 Case 3 加入 `keep_moving` 速度行為；保留東／北權重 30／100，新增速度行為權重 200、目標速度 2 m/s。Case 1、2、4 不受此條件區塊影響。原版保存在 `Lab06.zip`，WSL 中另有 `meta_tug.original.bhv` 備份。沿用上週已安裝的 MOOS-IvP v24.8.1，shell 腳本已設定執行權限。

目前直接執行 `./launch.sh --case=3 --warp=5` 就會使用會動的版本；下方原始 Case 3 停船描述是修改前的實測。修改檔案也保存於本資料夾的 `exp1_tugofwar/meta_tug.bhv`，已重新載入當時正在執行的 Case 3，並確認船有移動，證據見 `case3-live-verification.json`。

ZIP SHA-256：`2533b02ddabd967bd528581a59d70a5c2fe65e533c23329ca88ec7b48ddec76f`。

## 上課啟動

在 **WSL Ubuntu 終端**執行：

```bash
export PATH="$HOME/moos-ivp/bin:$PATH"
cd ~/moos-ivp/ivp/missions/exp1_tugofwar
./launch.sh --case=1 --warp=5
```

在地圖視窗按 **DEPLOY** 開始，按 **STOP** 停止自主行為。切換情境前，在終端的 uMAC 輸入 `q` 結束本次任務，再以 `--case=2`、`3` 或 `4` 重開。一次只啟動一個任務，因為這些範例都使用 port 9000。

也可以在 Windows PowerShell 執行：

```powershell
& 'C:\Users\nick0\Desktop\AOOP\112511054\W7\start-lab.ps1' -Case 1 -Warp 5
```

`--case=k` 中的 `k` 要換成 1～4，不是直接輸入字母 k。

## 簡報預習重點

每個 MOOSApp 各自執行，透過 MOOSDB 發布／訂閱變數。pHelmIvP 每個週期整合行為產生的效用函數，決定一組航向與速度。本例的決策空間是 360 個航向 × 41 個速度，共 14,760 個組合。

`go_east` 使用 `BHV_Waypoint` 前往 `(3000,0)`，同時考慮航向與速度；`go_north` 使用 `BHV_ConstantHeading` 偏好北方航向，沒有直接指定航速。`pwt` 是各行為效用函數的加權係數，權重大不代表會完全覆蓋其他行為。

簡報的分數表提供直觀示意。本機 v24.8.1 的 ROC 實作還有速度與繞路代價，並將解析函數近似為分段 IvP 函數，所以不能只拿簡報在固定 2 m/s 下的幾個航向分數，當成完整模擬的精確預測。船初始位置是 `(0,-300)`，因此目標初始方位約 84.3°，也不是恰好 90°。

## DEMO 問題參考解答

這些解答由 AI 協助整理；實際觀測數字見 `verification.md` 與 `verification-results.json`，不是同學自行觀察的聲稱。

### 1. 每個 Case 觀察到什麼？

| Case | 東／北權重 | 觀察方向 |
| --- | --- | --- |
| 1 | 100／100 | 兩行為折衷，選擇向東北航行；等權重不代表一定是 45° |
| 2 | 100／30 | 東向行為影響較強，航向更接近目標方位 |
| 3 | 30／100 | 期望航向為北，但期望速度為 0，船停在起點 |
| 4 | 100／0 | 北向行為不貢獻加權效用，主要朝東側航點航行 |

### 2. 將兩個 PWT 等比縮放，是否影響結果？

如果將所有參與加總的行為權重乘上同一個正數 `c`，總效用 `F(x)` 變成 `c × F(x)`，最佳解的集合不變。因此本題的 100／100 改成 200／200，理論上不影響最佳決策。實際函數近似、平手解或數值誤差可能造成微小差異。若另外加入第三個行為卻未一併縮放它的權重，就不再是整體等比縮放；乘以 0 或負數也不適用這個結論。

### 3. Case 3 的船為什麼不動？

Helm 仍在 DRIVE 狀態，已收到 DEPLOY，也沒有行為錯誤。它選到的是 `DESIRED_SPEED=0`。北向行為只限制航向，不會自己要求向前航行；較弱的東向航點行為，面對北向航向與其速度／繞路代價後，讓「朝北、速度 0」成為這份設定下的最佳解。控制器因此輸出停船結果。

這不是兩股推力互相抵銷；兩個行為提供的是分數函數。`go_east` 裡的 `speed=2.0` 也不是強制船速，Helm 仍在 0～4 m/s 的空間中共同求解。

### 4. 不降低任何原有 PWT，如何讓 Case 3 動起來？

保留 `go_east=30`、`go_north=100`，新增具有自己權重的速度偏好：

```text
Behavior = BHV_ConstantSpeed
{
  name = keep_moving
  pwt = 200
  condition = DEPLOY = true
  duration = no-time-limit
  speed = 2.0
  peakwidth = 0
  basewidth = 0.4
  summitdelta = 100
}
```

這個行為對接近 2 m/s 的解給予高效用，使零速度不再是最佳解。`duration = no-time-limit` 避免速度行為立即到期。200 是本次驗證採用的新增行為權重，不是唯一或最小可行值。它只鼓勵航速；航向仍交由原有的東向與北向行為折衷。

解法保存於本資料夾的 `exp1_tugofwar_solution`，也已另行安裝至 WSL 的 `~/moos-ivp/ivp/missions/exp1_tugofwar_solution`；只有 Case 3 會額外加入此行為。啟動方式：

```bash
cd ~/moos-ivp/ivp/missions/exp1_tugofwar_solution
./launch.sh --case=3 --warp=5
```

或從 PowerShell 執行：

```powershell
& 'C:\Users\nick0\Desktop\AOOP\112511054\W7\start-lab.ps1' -Case 3 -Solution
```

## 重現驗證

結束其他 MOOS 任務後執行：

```powershell
wsl -d Ubuntu -- python3 /mnt/c/Users/nick0/Desktop/AOOP/112511054/W7/verify_cases.py
```

腳本會在暫存資料夾依序測試四個原始 Case、Case 1 權重加倍、Case 3 新增速度行為，記錄結果並關閉自己啟動的程序。測試不開 GUI，以日誌驗證決策與船速；上課仍可用上方指令開啟地圖觀察。
