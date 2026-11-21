# 筆名常見問題與修復（FAQ）

簽名安裝 IPA 時最常遇到的問題，同點樣逐個排除。

## Q1：簽名完成後安裝失敗，顯示「無法安裝此應用」

### 可能原因

| 原因 | 檢查方法 |
|------|----------|
| Apple ID 未信任開發者 | 設定 → 通用 → VPN 與裝置管理，信任該 Apple ID |
| 憑證過期（免費 Apple ID 只有 7 天） | 重新簽名，或用 AltStore 自動續期 |
| 描述文件（Provisioning Profile）不匹配 | 用對應的 Apple ID 與 Bundle ID 簽名 |

### 修復

```bash
# AltStore 自動續期範例
altstore --install your-app.ipa
# 然後在 iPhone 上：設定 → 通用 → 裝置管理 → 信任
```

---

## Q2：App 打開即閃退（崩潰）

### 常見原因

1. **Entitlements 不足** — 缺少 `com.apple.developer.associated-domains`、`aps-environment` 等
2. **架構不匹配** — IPA 裡沒有對應 iPhone 的 CPU 架構（arm64）
3. **砸殼不完整** — FairPlay 加密殼沒清乾淨

### 診斷命令

```bash
# 查看 IPA 裡的架構
lipo -archs Payload/YourApp.app/YourApp

# 查看 entitlements
codesign -d --entitlements - Payload/YourApp.app

# 查看崩潰日誌（連接 Mac 後）
xcrun devicelog | grep -i your-app
```

### 修復建議

- 用 `codesign --entitlements Entitlements.plist` 補上缺失權限
- 確認用 `ios-deploy` 或 `xcodebuild` 重新編譯為 arm64

---

## Q3：簽名後 7 天到期， App 打不開

### 原因

免費 Apple ID 簽名的憑證只有 **7 天有效期**。

### 解決方案

| 方法 | 有效期 | 優點 | 缺點 |
|------|--------|------|------|
| 重新簽名 | 7 天 | 免費 | 每週要重來 |
| AltStore | 7 天（自動續期） | 自動 | 需電腦常開 |
| 開發者帳號 ($99/年) | 1 年 | 穩定 | 需付費 |
| TrollStore | 永久 | 無到期 | 只限特定 iOS 版本 |

---

## Q4：`codesign` 報錯「代碼簽名失效」

### 原因

IPA 內部已有其他開發者的簽名，直接簽名會衝突。

### 修復

```bash
# 先移除原有簽名（砸殼）
rm -rf Payload/YourApp.app/_CodeSignature
rm -rf Payload/YourApp.app/CodeResources

# 然後重新簽名
codesign -s "iPhone Developer: Your Apple ID" \
  --entitlements Entitlements.plist \
  Payload/YourApp.app
```

---

## Q5：Sideloadly 提示「Apple ID 驗證失敗」

### 原因

雙重驗證（2FA）開啟後，不能直接用主密碼。

### 修復

1. 到 [appleid.apple.com](https://appleid.apple.com) → 安全性 → App 專用密碼
2. 產生一個專用密碼
3. 在 Sideloadly 裡用「Apple ID + 專用密碼」登入

---

## Q6：TrollStore 安裝後 App 沒有圖標

### 原因

TrollStore 安裝的 IPA 必須包含正確的 `Bundle Identifier` 與圖標資源。

### 修復

- 確認 `Info.plist` 裡的 `CFBundleIdentifier` 與簽名時用的一致
- 確認 `Assets.car` 裡有 App 圖標
- 重新打包 IPA 後再用 TrollStore Sideloadly 安裝

---

## 快速檢查清單

在安裝前逐項確認：

- [ ] Apple ID 已在 iPhone 設定裡「信任」
- [ ] 憑證未過期（免費帳號 7 天）
- [ ] `codesign -dvvvv` 沒有報錯
- [ ] 架構包含 `arm64`
- [ ] `Bundle ID` 與憑證對應
- [ ] 2FA 用 App 專用密碼（Sideloadly）
