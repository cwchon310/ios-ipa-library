# 09 · 用 LiveContainer 一次過跑無限咁多 app

> LiveContainer 係近期最熱嘅側載神器：**一個容器 app，入面可以裝無限咁多個 IPA，唔受限 3 個 app 限制。**

## 呢篇學到

1. LiveContainer 係咩／點解咁正
2. 安裝 LiveContainer 本體
3. 喺容器入面裝 app
4. 配合 SideStore 做到「免電腦」側載
5. 限制同注意事項

---

## Part 0：LiveContainer 係咩？

**LiveContainer** 係一個開源 app（GitHub：`LiveContainer/LiveContainer`），概念好聰明：

> 佢係一個「容器」——你只係側載 **一個** LiveContainer app，然後喺佢 **入面** 運行任意多個其他 app。其他 app 唔使逐個簽名安裝，所以唔受 Apple「3 個 app」限制。

```
之前：     app A + app B + app C  →  3 個簽名位置（爆滿）
LiveContainer：  LiveContainer（1 個簽名位置）
                     ├── app A（容器內，唔使簽）
                     ├── app B（容器內，唔使簽）
                     ├── app C（容器內，唔使簽）
                     └── 無限個 app……
```

**點解做到？** LiveContainer 用「動態載入」技術喺沙盒內啟動其他 app 嘅主執行檔，佢哋唔係正式「安裝」，所以唔計 3 app 限額。

---

## Part 1：安裝 LiveContainer 本體

### 下載

- GitHub Releases：https://github.com/LiveContainer/LiveContainer/releases
- 下載最新 `LiveContainer.ipa`（或跟 Release 說明）

### 簽名安裝（同普通 IPA 一樣）

```text
方式一：AltStore/SideStore（04 篇）
  → 攞 .ipa → 加入 AltStore → 輸入 Apple ID → 完成

方式二：Sideloadly（03 篇）
  → 揀 .ipa → Apple ID → Start → iPhone 信任憑證

方式三：TrollStore（05 篇）
  → 部機支援 TrollStore 嘅話，直接裝入 TrollStore 最快
```

> 💡 **最推薦組合：LiveContainer + SideStore**——SideStore 負責簽名（7 日自動續），LiveContainer 負責無限裝 app。

---

## Part 2：喺 LiveContainer 入面裝 app

裝好 LiveContainer 之後：

```text
1. 開啟 LiveContainer
2. 撳右上「+」加 app
3. 揀你嘅 .ipa 檔（可以 AirDrop / Safari 下載）
4. 佢會喺容器入面啟動

完成！想裝幾多個都得。
```

### 將容器 app 加到主畫面（可選）

```text
1. 喺 LiveContainer 內長按某個 app
2. 揀「Add to Home Screen」
3. 跟住部機彈「Profile Downloaded」→ 去設定裝咗個描述檔
4. 主畫面就會出現嗰個 app 嘅獨立圖示，直接開
```

---

## Part 3：LiveContainer + SideStore 免電腦方案

**最新玩法**：iPhone 完全唔使電腦，直接喺手機完成簽名＋無限裝 app。

```text
1. 用 iloader（catalog #93）喺電腦整好「pairing file」
2. 裝 SideStore（catalog #88）
3. 喺手機用 SideStore 自動續簽（7 日）
4. 裝 LiveContainer
5. 之後所有 app 都入 LiveContainer 裝

結果：唔使電腦、唔使越獄、無限 app、7 日自動續期
```

> 詳細免電腦教學：參考 SideStore 官方文檔 https://docs.sidestore.io

---

## Part 4：LiveContainer 限制

| ⚠️ 事項 | 說明 |
|---------|------|
| 唔係所有 app 都行到 | 有 JIT 需要嘅 app、部分系統功能 app 可能開唔到 |
| 每個 app 用沙盒 | 容器內 app 同正式安裝有少少分別（如某些推送） |
| 主要 app 要續期 | LiveContainer 本體 7 日要續（AltStore/SideStore 自動做） |
| 支援版本 | 跟官方 Release 支援範圍 |

---

## Part 5：點解啱你？

| 你嘅情況 | LiveContainer 幫到你咩 |
|----------|----------------------|
| 想裝好多開源 app | 突破 3 個限制，無限裝 |
| 想試 app 又唔想「污染」主畫面 | 全部收喺容器入面 |
| 想免電腦側載 | 配合 SideStore 免電腦 |
| 開發者測試 | 一次過跑多個版本 |

---

## 總結

- LiveContainer = 一個容器，裝無限個 IPA
- 本體用 AltStore/SideStore/Sideloadly/TrollStore 簽名安裝
- 入面裝 app 唔使再簽名、唔計 3 app 限制
- 進階：LiveContainer + SideStore = 免電腦無限側載

**下一篇**：08 FAQ（整個簽名系列總結）。