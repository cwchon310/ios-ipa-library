# 03 · 用 Sideloadly 簽名安裝（Windows/Mac）

> Sideloadly 係最熱門嘅免費側載工具，Windows 同 macOS 都支援，功能多。

## 呢篇學到

1. Sideloadly 進階功能（Apple ID 儲存、Bundle ID 修改）
2. 進階設定逐項解
3. 常見錯誤同解決方法

> 基礎安裝步驟見 02 篇。呢篇專講 Sideloadly 嘅進階技巧同排錯。

---

## Part 1：Sideloadly 界面逐欄解

開啟 Sideloadly 後你會見到：

| 欄位 | 用途 | 提示 |
|------|------|------|
| **iOS device** | 揀目標 iPhone/iPad | 要用 USB 連接 |
| **IPA** | 揀 IPA 檔 | 支持 .ipa 同 .deb（越獄用） |
| **Apple ID** | 你嘅 Apple ID | 免費即可 |
| **Apple ID password** | 密碼 | ⚠️ 只自己用 |
| **Start** | 開始簽名安裝 | 會跑一陣 |

---

## Part 2：進階功能

### 2.1 儲存 Apple ID（Save credentials）

Sideloadly 可以記住你嘅 Apple ID 憑證，下次唔使再入。但：

> ⚠️ 密碼會儲存喺你部電腦。如果部機唔係得你自己用，建議唔好記。

### 2.2 修改 Bundle ID

免費 Apple ID 同時最多 3 個 app。如果裝第 4 個會失敗，可以：

```text
1. 刪走部機一個舊 app
2. 或者用「Bundle ID」欄改成唔同嘅 ID
   （例如 com.yourname.appname2）
```

> 每個 app 嘅 Bundle ID 要唔同，先計入「3 個 app」限額。

### 2.3 其他選項

| 選項 | 作用 |
|------|------|
| Remove previous app | 裝前先刪舊版（防衝突） |
| Install to a specific UDID | 指定設備（多部機時用） |
| Enable debug | 出詳細 log（排錯用） |
| Export ipa | 唔安裝，只輸出已簽名 IPA |

---

## Part 3：常見錯誤同解決

### ❌ Error: Device not found

```text
原因：iPhone 冇被電腦認到
解決：
1. 換一條數據線（最好原裝或 MFI）
2. 確認 iPhone 螢幕有「信任此電腦」並揀信任
3. Mac 上確認 Apple Devices／iTunes 見到部機
4. 重啟 Sideloadly
```

### ❌ Error: Failed to get a profile

```text
原因：Apple 簽名流程失敗，常見係網絡／Apple ID 問題
解決：
1. 確認電腦有上網
2. 確認 Apple ID 正確（密碼／雙重認證）
3. 等幾分鐘再試（Apple 伺服器有時慢）
```

### ❌ Error: Please sign in with your Apple ID

```text
原因：Apple ID 驗證失敗
解決：
1. 確認帳號有開「App Store 登入」
2. 如果開咗雙重認證，可能要喺 iPhone 上核准
3. 試吓用返 iPhone 上登入 App Store 嗰個 Apple ID
```

### ❌ App shows "Untrusted Developer"

```text
原因：未喺 iPhone 信任憑證
解決：
iPhone → 設定 → 一般 → VPN 與裝置管理
→ 揀你嘅 Apple ID → 信任
```

### ❌ App expired (無法驗證 App)

```text
原因：7 日有效期到期
解決：重新用 Sideloadly 簽名安裝一次（或 AltStore 自動續）
```

---

## Part 4：安全提醒

| ✅ 好做法 | ❌ 唔好 |
|-----------|---------|
| 官方網站下載 Sideloadly | 第三方「破解版 Sideloadly」 |
| 開雙重認證 | 將 Apple ID 密碼俾「在線簽名網站」 |
| 自己部機簽自己嘅 app | 幫陌生人簽名（會被盜用） |

---

## 總結

- Sideloadly 係免費又穩定嘅側載工具
- 進階功能：儲存憑證、改 Bundle ID、export IPA
- 常見錯誤 80% 係「信任憑證」或「7 日到期」
- 安全永遠第一：用官方工具、唔好交密碼俾人

**下一篇**：04 用 AltStore 簽名＋自動續期（長期使用更省心）。