# 04 · 用 AltStore 簽名＋自動續期

> AltStore 係最出名嘅「自動續期」側載方案——7 日簽名由佢幫你續，你唔使成日理。

## 呢篇學到

1. AltStore 原理（點樣自動續期）
2. 安裝步驟（電腦 + 手機兩邊）
3. 設定自動續期
4. 限制同排錯

---

## Part 0：AltStore 點解可以「自動續期」？

**原理**：AltStore 用你 iPhone 上嘅 **「郵件（Mail）插件」**同電腦溝通，透過 Apple 嘅「無線開發安裝」機制幫你續簽。

簡單講：

```
AltStore (iPhone) ←——郵件插件——→ AltServer (電腦)
                                           │
                                     你嘅 Apple ID
                                           │
                                       每 7 日自動重新簽名
```

**你要做嘅**：iPhone 同電腦保持「同一個 Wi-Fi」＋AltStore 有開。佢就會自動續。

---

## Part 1：安裝步驟

### Step 1 — 電腦裝 AltServer

- 官方網站：https://altstore.io
- 下載對應 OS（Windows / macOS）
- 安裝後，狀態欄會見到「菱形」icon

### Step 2 — 電腦裝 iTunes（Windows 限定）

Windows 需要 iTunes（含 iCloud）先認到 iPhone：
- 去 Apple 官網裝 iTunes（唔好用 Microsoft Store 版，易有問題）
- 裝完重啟電腦

### Step 3 — 手機裝 AltStore

```text
1. iPhone 用 USB 連電腦
2. 電腦狀態欄右鍵 AltServer icon
   → 「Install AltStore」→ 揀你部 iPhone
3. 輸入你嘅 Apple ID（免費即可）
4. 等佢裝（會出「信任憑證」提示）
5. iPhone → 設定 → 一般 → VPN 與裝置管理 → 信任
6. 完成！主畫面有 AltStore app
```

### Step 4 — 加入你嘅 IPA

```text
1. 用 Safari 開某個開源 IPA 嘅下載頁
2. 下載 .ipa（Safari 下載）
3. 開啟 AltStore app
4. 「My Apps」右上角 + 號
5. 揀你下載嘅 .ipa
6. 入你嘅 Apple ID → 完成簽名安裝
```

> 或者用電腦 AltServer：將 .ipa 拖入 AltServer icon 都得。

---

## Part 2：設定自動續期

AltStore 預設會喺 app **到期前自動續簽**，但要滿足：

| 條件 | 說明 |
|------|------|
| 同一 Wi-Fi | iPhone 同電腦要喺同一網絡 |
| AltServer 有開 | 電腦唔可以完全熄機 |
| AltStore 有開 | 手機上 AltStore 唔可以刪走 |
| 背景重新整理 | iPhone 設定 → 一般 → 背景 App 重新整理 → 開 |

> 💡 實際經驗：間中開吓 AltStore app 可以確保佢有續簽。唔好隔太耐唔開。

---

## Part 3：AltStore 限制

| 限制 | 說明 |
|------|------|
| 需要電腦 | 自動續期要電腦 AltServer 在線（同 Wi-Fi） |
| 7 日機制唔變 | 本質仲係 Apple ID 免費簽名，AltStore 幫你自動做 |
| 最多 3 個 app | 免費 Apple ID 限制（AltStore 計一個 app） |
| 部分地區 | Apple ID 地區可能要啱先順 |

---

## Part 4：常見問題

### ❌ AltStore 開唔到（無法驗證 App）

```text
→ iPhone → 設定 → 一般 → VPN 與裝置管理 → 信任
```

### ❌ 裝唔到（Failed to install AltStore）

```text
1. 確認 iTunes/Apple Devices 認到 iPhone
2. 換 USB 線／重插
3. 重啟 AltServer 再試
```

### ❌ 冇自動續期？

```text
1. 確認 iPhone 同電腦同一 Wi-Fi
2. 確認 AltServer 有開
3. 手動開一次 AltStore app（觸發續期檢查）
```

---

## 總結

- AltStore = 免費 Apple ID 簽名＋自動續期
- 安裝要電腦（AltServer）＋iPhone（AltStore）＋信任憑證
- 保持同一 Wi-Fi，佢就會自動續 7 日
- 適合「長期用幾個開源 app」嘅人

**下一篇**：05 用 TrollStore 安裝（支援設備限定，唔使續期）。