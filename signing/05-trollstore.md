# 05 · 用 TrollStore 安裝（支援設備限定）

> TrollStore 係 iOS 側載嘅「神器」——安裝嘅 app 永久有效、唔使簽名、唔使 Apple ID。但只支援特定 iOS 版本。

## 呢篇學到

1. TrollStore 係咩／點解咁正
2. 你部機支唔支援
3. 安裝方法
4. 使用技巧同限制

---

## Part 0：TrollStore 係咩？

**TrollStore** 係一個利用 iOS 漏洞嘅工具，可以喺唔簽名嘅情況下安裝「永久有效」嘅 app。核心賣點：

| 特性 | 說明 |
|------|------|
| 永久有效 | 唔使 7 日續簽，唔會過期 |
| 唔使 Apple ID | 完全唔使登入 |
| 唔使電腦 | 裝好 TrollStore 後，喺手機直接裝 IPA |
| 系統 app 都可以 | 部分情況可以替換系統 app |

> ⚠️ 技術上係用「CoreTrust」漏洞簽名繞過，只係 Apple 未完全封鎖嘅特定版本先得。唔同於越獄，唔會改系統檔案。

---

## Part 1：你部機支唔支援？

**關鍵**：TrollStore 只支援特定 iOS 版本。唔支援就唔好強裝（會裝唔到／有風險）。

| iOS 版本 | 支援情況 |
|----------|----------|
| iOS 14.0 – 16.6.1（部分） | ✅ 支援（睇安裝器） |
| iOS 17.0（部分設備） | ✅ 部分支援 |
| iOS 17.0.1+ | ❌ 暫時唔支援 |
| 最新 iOS | ❌ 等更新 |

> **重要**：支援範圍會隨時間變。安裝前一定要去官方 Git 睇最新支援清單：
> - 官方：https://github.com/opa334/TrollStore
> - 睇 README 有「Supported versions」表

---

## Part 2：點裝 TrollStore？

TrollStore 嘅安裝方法會因版本唔同，常見途徑：

### 方法 A：用 TrollInstaller（越獄／半越獄環境）

```text
1. 確認你部機有越獄環境（如 Dopamine 等）
2. 安裝 TrollInstaller（越獄商店有）
3. 開啟 → Install TrollStore
```

### 方法 B：直接網頁安裝（特定版本先有）

```text
1. 用 Safari 開對應嘅 TrollStore 安裝網頁
2. 下載並安裝
```

### 方法 C：用電腦工具（如 TrollHelper）

```text
1. 下載對應你 iOS 版本嘅 TrollHelper
2. 用 Sideloadly（03 篇）簽名裝入去
3. 開啟 TrollHelper → Install TrollStore
```

> ⚠️ 每個 iOS 版本嘅安裝器都唔同，**一定要睇官方 README**，唔好亂揾「一鍵安裝」嚟路不明工具。

---

## Part 3：用 TrollStore 裝 IPA

TrollStore 裝好之後，裝 app 好簡單：

```text
方法 1（手機直接裝）：
1. 用 Safari 下載 .ipa
2. 開啟 TrollStore
3. 「App 資料庫」→ 右上 + → 揀 .ipa → Install

方法 2（AirDrop）：
1. 用電腦 AirDrop .ipa 過去 iPhone
2. 揀「在 TrollStore 開啟」→ Install
```

完成！個 app 直接喺主畫面，永久有效，唔使續。

---

## Part 4：TrollStore 常見操作

| 操作 | 做法 |
|------|------|
| 卸載 app | TrollStore 內長按 → Delete |
| 裝 .ipa | + 號揀檔 |
| 替換系統 app | 進階功能（會破壞原 app，小心） |
| 更新 TrollStore | 官方出更新，GitHub 下載新 .ipa 裝入去 |

---

## Part 5：限制同風險

| ⚠️ 事項 | 說明 |
|---------|------|
| 版本限定 | 唔支援嘅 iOS 裝唔到 |
| 漏洞被封 | Apple 更新 iOS 後可能失效（唔好升錯版） |
| 唔係越獄 | 唔可以改系統／裝 tweak（除非配合其他） |
| 有風險 | 用嚟路不明嘅 TrollStore 安裝器 = 危險 |

> 💡 如果你部機支援 TrollStore，佢係「最舒服」嘅側載方式。如果唔支援，返去用 AltStore（04 篇）。

---

## 總結

- TrollStore = 永久簽名繞過，安裝嘅 app 唔使續期
- 只支援特定 iOS 版本，**先睇官方支援表**
- 安裝器因版本而異，一定要跟官方步驟
- 裝好後，喺手機直接裝 IPA，超方便

**下一篇**：06 用開發者帳號（$99/年）簽名，無效期、大量安裝。