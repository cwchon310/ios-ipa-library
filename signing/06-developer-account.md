# 06 · 用開發者帳號（$99/年）簽名，無效期

> 如果你想「一勞永逸」＋大量安裝＋正式開發，Apple Developer Program（$99/年）係正路。

## 呢篇學到

1. 開發者帳號 vs 免費 Apple ID 分別
2. 申請流程
3. 用 Xcode 簽名安裝（無效期）
4. 優點／缺點

---

## Part 0：開發者帳號 vs 免費 Apple ID

| 項目 | 免費 Apple ID | Developer Program ($99/年) |
|------|--------------|---------------------------|
| 費用 | $0 | $99/年 |
| 簽名有效期 | 7 日 | **1 年** |
| 同時安裝上限 | 3 個 | **100 部設備／大量 app** |
| 訪問開發工具 | 有限 | 完整（Xcode 全功能） |
| 適合 | 試玩 | 長期用／開發者／公司 |

> 💡 對側載嚟講，最大分別就係：**唔使 7 日續簽**，同埋可以裝好多個。

---

## Part 1：申請開發者帳號

```text
1. 去 https://developer.apple.com
2. 用 Apple ID 登入
3. 揀「Enroll」（登記）
4. 個人開發者：$99/年
   （公司／機構：$299/年，要 D-U-N-S 編號）
5. 填資料 → 付款 → 等批准（通常好快）
```

> ⚠️ 需要信用卡／有效付款方式，同埋你嘅 Apple ID 地區要支援。部分國家/地區未開放個人開發者計劃。

---

## Part 2：用 Xcode 簽名安裝（最正統）

有開發者帳號後，最簡單嘅安裝方式係經 Xcode（macOS）：

```text
1. 開啟 Xcode（App Store 免費下載）
2. 用你嘅開發者 Apple ID 登入（Xcode → Settings → Accounts）
3. 開一個空 project（或者 import 你想裝嘅項目）
4. Signing 揀你嘅 Team（開發者帳號）
5. 連 iPhone → 按 Run

完成！app 直接裝上手機，簽名有效期 1 年。
```

**但注意**：經 Xcode 簽名，你裝嘅係「開發版」app，要你部機喺「已註冊設備」清單。自己部機好簡單，自動註冊。

---

## Part 3：對「側載現成 IPA」嘅實際做法

如果你想側載**現成 IPA**（收納庫嘅開源 app），開發者帳號方法：

### 方法 A：用 App Signer 重新簽名

```text
1. 下載 App Signer（開源工具）
2. 揀你嘅 IPA + 揀你嘅開發者憑證
3. 輸出已簽名 IPA
4. 再用 Sideloadly（03 篇）裝入去
```

> App Signer 官網：GitHub 搜尋「AppSigner」Mac 版。

### 方法 B：用 Xcode 直接裝

```text
1. Xcode → Window → Devices and Simulators
2. 將已簽名 .ipa 拖入去
3. 安裝
```

---

## Part 4：開發者帳號嘅好處同成本

### 好處

- ✅ 簽名有效期 1 年（唔使成日續）
- ✅ 唔受「3 個 app」限制
- ✅ 可以用正式開發工具（TestFlight、CloudKit 等）
- ✅ 開發 app 必備

### 成本／考慮

| 成本 | 說明 |
|------|------|
| $99/年 | 對淨係側載嚟講算貴 |
| 註冊限制 | 部分地區唔支援個人開發者 |
| 信用卡 | 付款需要 |

> 💡 如果你只係想裝幾個開源 app 玩下，免費 Apple ID + AltStore 已經夠。開發者帳號係「當你真係認真做 iOS 開發／大量側載」先值得。

---

## 總結

| 你嘅情況 | 建議 |
|----------|------|
| 試玩幾個開源 app | 免費 Apple ID + AltStore（唔使俾錢） |
| 長期用 3 個以內 | AltStore 自動續期就夠 |
| 大量側載／開發 | Developer Program + Xcode |
| 公司內部分發 | Enterprise Program（$299/年） |

**下一篇**：07 簽名工具大全對比＋注意事項。