# 02 · Apple ID 免費簽名（7 日有效期）

> 唔使俾錢、最快起步：用你嘅免費 Apple ID 簽名安裝開源 IPA。

## 呢篇學到

1. 免費簽名嘅限制（7 日、3 個 app）
2. 完整步驟（準備 → 簽名 → 安裝）
3. 點樣解決「7 日到期」
4. 注意事項

---

## Part 0：免費 Apple ID 簽名嘅限制

| 項目 | 限制 |
|------|------|
| 有效期 | **7 日**（到期要重新簽名） |
| 同時安裝 | 最多 **3 個 app** |
| 每個 app | 要用唔同 Bundle ID |
| 條件 | 一個有效 Apple ID（免費） |

**意思**：你可以免費試裝開源 app，但每 7 日要「續簽」一次。想自動續→用 AltStore（04 篇）。

---

## Part 1：事前準備

```
✅ 一個 Apple ID（建議開雙重認證）
✅ 一部 iPhone/iPad（要用返呢個 Apple ID 登入 App Store）
✅ 一部電腦（Windows 或 Mac）
✅ 簽名工具（Sideloadly 或 AltStore）
✅ 一個開源 IPA（收納庫 categories/ 有推薦）
```

**揀工具**：
- **Windows**：Sideloadly（03 篇）
- **Mac**：Sideloadly 或 AltStore（04 篇）

呢篇用 Sideloadly 做例子（Windows/Mac 都支援）。

---

## Part 2：完整步驟（Sideloadly）

### Step 1 — 下載 Sideloadly

- 官方網站：https://sideloadly.io
- 下載對應你 OS 嘅版本（Windows / macOS）

### Step 2 — 準備 IPA

- 攞一個開源 IPA（例如收納庫 categories/ 推薦）
- 放喺電腦一個易揾嘅位置

### Step 3 — 連接 iPhone

```text
1. 用 USB 線將 iPhone 連到電腦
2. iPhone 上會彈「信任此電腦？」→ 揀「信任」
3. 確認 iTunes/Apple Devices 認到部機
```

### Step 4 — 開啟 Sideloadly 簽名

```text
1. 開啟 Sideloadly
2. 左邊揀你部 iPhone
3. 「IPA」欄揀你嘅 IPA 檔
4. 輸入你嘅 Apple ID 同密碼
   （⚠️ 只輸入你自己嘅；Sideloadly 係開源工具，唔會儲存）
5. 揀「Start」
```

### Step 5 — 處理彈出嘅提示

```text
- 第一次會有「Apple ID 未受信任」提示 → 照繼續
- 可能要求你喺 iPhone 上輸入 Apple ID 密碼
  （呢個係 Apple 嘅驗證，唔係工具要）
- 完成後會話你「Successfully installed」
```

### Step 6 — iPhone 上信任憑證

**呢步好重要！** 裝完要「信任」先開到：

```text
iPhone → 設定 → 一般 → VPN 與裝置管理
→ 揀你嘅 Apple ID → 「信任」佢
```

完成後，返去主畫面就可以開 app！

---

## Part 3：7 日到期點算？

**免費簽名得 7 日。** 到期後 app 會開唔到（「無法驗證 App」）。解決方法：

| 方法 | 做法 | 適合 |
|------|------|------|
| 手動續簽 | 每次到期用 Sideloadly 重新裝一次 | 間中用 |
| AltStore 自動續 | 部機開 AltStore，自動幫你續 | 長期用（04 篇） |

> 💡 免費簽名本質係「開發者測試」，Apple 設計上就係要你 7 日續一次。想一勞永逸→TrollStore（05）或開發者帳號（06）。

---

## Part 4：注意事項

| ⚠️ 事項 | 說明 |
|---------|------|
| Apple ID 安全 | 只用開源/知名工具；輸入密碼前確認係你自己部機 |
| 雙重認證 | 強烈建議開，防被盜 |
| 唔好亂攞 IPA | 只裝開源／免費／你有權限嘅 |
| 7 日要續 | 唔續就開唔到 |
| 3 個 app 上限 | 想裝多啲→清走冇用嘅再裝 |

---

## 總結

```
下載 Sideloadly → 連接 iPhone → 揀 IPA → 輸入 Apple ID → Start
→ iPhone 信任憑證 → 開 app
每 7 日：重複一次（或改用 AltStore 自動續）
```

**下一篇**：03 用 Sideloadly 深入實戰（更多選項同排錯）。