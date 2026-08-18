# 🔧 系統工具類收納庫

> 開源系統工具 — 檔案管理、系統監控、網絡診斷。

## 呢篇學到

1. 檔案管理工具
2. 系統監控／診斷工具
3. 網絡工具

---

## 推薦清單

| 工具 | 用途 | 來源 | 備註 |
|------|------|------|------|
| **Filza** | 檔案管理器（越獄） | 越獄商店 | 需越獄 |
| **Santander** | 檔案管理器 | GitHub | 開源，可側載 |
| **iTorrent** | BT 下載 | GitHub「XITRIX/iTorrent」 | 開源 |
| **Termius** | SSH / 終端 | App Store | 免費版夠用 |
| **Ping / Network Tools** | 網絡診斷 | GitHub | 開源 |
| **System Status** | 系統監控 | GitHub | 開源 |
| **Battery Health** | 電池健康 | GitHub | 開源 |

---

## 重點推介

### Santander（檔案管理器）

```text
開源檔案管理器：可以睇 system 檔案（讀寫權限內）
來源：GitHub「willieSantos/Santander」or 搜尋「santander ipa」
安裝：GitHub Release 下載 IPA → 側載
注意：唔會比你改系統（非越獄冇權限）
```

### iTorrent（BT 下載）

```text
開源 BitTorrent 客戶端
來源：GitHub「XITRIX/iTorrent」
安裝：GitHub Release 有現成 IPA → 側載
```

### Network 工具

```text
開源網絡診斷 app：
- Ping / Traceroute / Port Scanner
來源：GitHub 搜尋「iOS network scanner open source」
```

---

## 系統工具嘅「限制」

| 工具類型 | 非越獄 | 越獄 |
|----------|--------|------|
| 檔案管理器 | 只睇到自己 app 沙盒／部分共享 | 可以睇全系統 |
| 系統監控 | 有限資訊 | 完整 |
| 改系統 | ❌ 唔得 | ✅ |

> 💡 唔好以為側載就等於「控制部機」。iOS 沙盒限制依然存在，**冇越獄就冇全系統權限**。想深入了解系統權限，可以去睇我哋另一個倉庫 ios-reversing-guide。

---

## 安全提醒

- ✅ 只裝開源 GitHub 項目
- ⚠️ 網絡工具（如掃描器）只可以用喺自己網絡／自己設備
- ❌ 唔好用「系統優化神器」類嚟路不明 app

---

## 總結

- 開源檔案管理器：Santander
- 開源下載：iTorrent
- 系統工具受沙盒限制，想全系統要先了解越獄

返回：[收納庫目錄](../README.md) · [200 個開源 IPA 大全](../catalog.md)