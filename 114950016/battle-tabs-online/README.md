# Battle Tabs Online

真正的雙人連線房間版。

## 功能
- 玩家 1 建立房間
- 系統產生 4 碼房間代碼
- 玩家 2 輸入 4 碼加入
- 雙方各自只看到自己的畫面
- 各自部署 4 艘船
- 即時輪流攻擊
- Radar：3×3 掃描，中心格顯示敵艦格數
- Shield：偏移下一次命中
- Missile：十字 5 格攻擊
- 技能冷卻
- 擊沉與勝負判定

## Windows 執行
雙擊：
run_server.bat

看到伺服器啟動後，瀏覽器開：
http://127.0.0.1:8000

## 同一個 Wi-Fi 的兩台電腦連線
伺服器那台 Windows 開 cmd，輸入：
ipconfig

找到 IPv4 Address，例如：
192.168.1.25

另一台電腦瀏覽器開：
http://192.168.1.25:8000

注意：
Windows 防火牆第一次可能會詢問是否允許 Python/uvicorn 網路存取，要允許「私人網路」。

## 真正跨網路分享給朋友
如果朋友不在同一個 Wi-Fi，還需要部署到雲端，例如 Render、Railway 或 Fly.io。
這份程式已經是 FastAPI + WebSocket 架構，可以直接拿去部署。
