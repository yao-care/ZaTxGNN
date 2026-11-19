# TxGNN 國際化 SOP - 從初始化包建立地區藥品老藥新用預測系統

## 目標

將此初始化包轉換為您國家的藥品老藥新用預測系統。

**使用方式**：
1. 解壓縮 TxGNN_init.zip
2. 閱讀本文件，按照階段化流程執行
3. 將 `.template` 檔案改名並填入當地資訊
4. 執行預測流程

---

## 一、元件分類總覽

### 1.1 通用元件（直接使用，約 60-70%）

| 類別 | 檔案 | 說明 |
|------|------|------|
| **TxGNN 知識圖譜** | `data/node.csv`, `data/kg.csv` | 知識圖譜基礎資料（需下載） |
| **詞彙表提取** | `scripts/prepare_external_data.py` | 從 TxGNN 提取 DrugBank/疾病詞彙 |
| **藥名正規化** | `src/txgnn/mapping/normalizer.py` | 通用藥名標準化 |
| **DrugBank 映射** | `src/txgnn/mapping/drugbank_mapper.py` | 成分 → DrugBank ID |
| **KG 預測** | `src/txgnn/predict/repurposing.py` | 知識圖譜方法 |
| **DL 預測** | `src/txgnn/predict/txgnn_model.py` | 深度學習方法 |
| **通用收集器** | `collectors/clinicaltrials.py`, `pubmed.py`, `drugbank.py`, `ictrp.py` | 全球資料來源 |
| **收集器基類** | `src/txgnn/collectors/base.py` | 收集器介面 |

### 1.2 需在地化元件（約 30-40%）

| 類別 | 模板檔案 | 需修改內容 |
|------|----------|------------|
| **專案設定** | `pyproject.toml.template` | 專案名稱 |
| **欄位映射** | `config/fields.yaml.template` | 藥監局資料欄位對應 |
| **資料載入** | `src/txgnn/data/loader.py.template` | 載入邏輯 |
| **疾病映射** | `src/txgnn/mapping/disease_mapper.py.template` | DISEASE_DICT（當地語言→英文） |
| **資料處理** | `scripts/process_fda_data.py.template` | ZIP/JSON 解析 |
| **預測腳本** | `scripts/run_kg_prediction.py.template` | 微調欄位名稱 |
| **FHIR 生成** | `scripts/generate_fhir_resources.py.template` | URL 和管轄區域 |
| **新聞同義詞** | `data/news/synonyms.json.template` | 疾病/藥物同義詞 |
| **網站設定** | `docs/_config.yml.template` | 標題、URL |
| **SMART App** | `docs/smart/launch.html.template` | Client ID |
| **CI/CD** | `.github/workflows/pages.yml.template` | 部署設定 |

---

## 二、階段化實施流程

### Phase 0：專案初始化

**目標**：設定專案基礎

#### 步驟：

1. **重新命名專案**
   ```bash
   # 建議命名：{Country}TxGNN
   # 例：JpTxGNN, KrTxGNN, ThTxGNN
   mv TxGNN_init {Country}TxGNN
   cd {Country}TxGNN
   ```

2. **設定 pyproject.toml**
   ```bash
   mv pyproject.toml.template pyproject.toml
   # 編輯 pyproject.toml，修改 name 和 description
   ```

3. **下載 TxGNN 資料**
   ```bash
   mkdir -p data
   curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
   curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"
   ```

4. **安裝依賴**
   ```bash
   uv sync
   ```

**品質檢查點**：
- [ ] 專案已重新命名
- [ ] `pyproject.toml` 已修改
- [ ] `uv sync` 執行成功
- [ ] TxGNN 資料下載完成（node.csv ~15MB, kg.csv ~500MB）

---

### Phase 1：FDA 資料整合

**目標**：整合當地藥監局資料

#### 1.1 調查資料來源

常見藥監局資料來源：

| 國家 | 藥監局 | 資料來源 |
|------|--------|----------|
| 日本 | PMDA | https://www.pmda.go.jp/ |
| 韓國 | MFDS | https://nedrug.mfds.go.kr/ |
| 泰國 | Thai FDA | https://www.fda.moph.go.th/ |

**產出**：記錄資料來源 URL、格式、欄位說明

#### 1.2 建立欄位映射設定

```bash
mv config/fields.yaml.template config/fields.yaml
# 編輯 fields.yaml，填入欄位對應
```

**fields.yaml 範例（日本 PMDA）**：
```yaml
country_code: JP
language: ja
regulatory_agency: PMDA

field_mapping:
  license_id: "承認番号"
  brand_name_local: "販売名"
  brand_name_en: "一般名"
  ingredients: "有効成分"
  indication: "効能・効果"
  dosage_form: "剤形"
  status: "承認状況"

withdrawn_statuses:
  - "取消"
  - "回収"
```

#### 1.3 實作資料載入器

```bash
mv src/txgnn/data/loader.py.template src/txgnn/data/loader.py
# 編輯 loader.py，實作載入邏輯
```

#### 1.4 實作資料處理腳本

```bash
mv scripts/process_fda_data.py.template scripts/process_fda_data.py
# 編輯並執行
uv run python scripts/process_fda_data.py
```

**品質檢查點**：
- [ ] `config/fields.yaml` 建立完成
- [ ] `loader.py` 能正確載入資料
- [ ] `process_fda_data.py` 執行成功
- [ ] `data/raw/{country}_fda_drugs.json` 產生

---

### Phase 2：疾病映射

**目標**：建立當地語言 → 英文疾病對照

#### 2.1 建立 DISEASE_DICT

```bash
mv src/txgnn/mapping/disease_mapper.py.template src/txgnn/mapping/disease_mapper.py
# 編輯 disease_mapper.py，填入 DISEASE_DICT
```

**目標數量**：150-200 個疾病詞條

**分類建議**：

| 分類 | 建議數量 |
|------|----------|
| 心血管系統 | 15-20 |
| 呼吸系統 | 10-15 |
| 消化系統 | 15-20 |
| 神經系統 | 10-15 |
| 精神疾病 | 8-12 |
| 內分泌系統 | 10-15 |
| 肌肉骨骼 | 10-15 |
| 皮膚疾病 | 10-15 |
| 泌尿系統 | 8-12 |
| 眼科 | 5-8 |
| 耳鼻喉 | 5-8 |
| 感染症 | 10-15 |
| 過敏 | 5-8 |
| 婦科 | 8-12 |
| 腫瘤/癌症 | 10-15 |
| 一般症狀 | 15-20 |

#### 2.2 建立新聞同義詞

```bash
mv data/news/synonyms.json.template data/news/synonyms.json
# 編輯 synonyms.json，填入當地語言同義詞
```

**品質檢查點**：
- [ ] DISEASE_DICT 有 150+ 詞條
- [ ] 涵蓋所有主要疾病分類
- [ ] `synonyms.json` 建立完成

---

### Phase 3：KG 預測流程

**目標**：執行知識圖譜預測

#### 執行步驟：

```bash
# 1. 準備詞彙表
uv run python scripts/prepare_external_data.py

# 2. 設定預測腳本
mv scripts/run_kg_prediction.py.template scripts/run_kg_prediction.py
# 編輯並執行

# 3. 執行預測
uv run python scripts/run_kg_prediction.py
```

#### 預期產出：

| 檔案 | 預期內容 |
|------|----------|
| `data/external/drugbank_vocab.csv` | ~7,958 個藥物 |
| `data/external/disease_vocab.csv` | ~17,081 個疾病 |
| `data/external/drug_disease_relations.csv` | ~80,127 個關係 |
| `data/processed/repurposing_candidates.csv` | 視藥品數量而定 |

**品質檢查點**：
- [ ] 詞彙表正確產生
- [ ] `repurposing_candidates.csv` 產生
- [ ] DrugBank 映射率 > 30%
- [ ] 疾病映射率 > 20%

---

### Phase 4：網站與 FHIR

**目標**：部署文件網站與 FHIR API

#### 4.1 Jekyll 設定

```bash
mv docs/_config.yml.template docs/_config.yml
# 編輯 _config.yml，修改標題、URL、語言
```

#### 4.2 FHIR 資源設定

```bash
mv scripts/generate_fhir_resources.py.template scripts/generate_fhir_resources.py
# 編輯 BASE_URL 和 JURISDICTION
uv run python scripts/generate_fhir_resources.py
```

#### 4.3 SMART App 設定

```bash
mv docs/smart/launch.html.template docs/smart/launch.html
# 編輯 CLIENT_ID
```

#### 4.4 本地測試

```bash
cd docs
bundle install
bundle exec jekyll serve
# 訪問 http://localhost:4000
```

**品質檢查點**：
- [ ] Jekyll 本地建置成功
- [ ] `/fhir/metadata` 可存取
- [ ] FHIR 資源正確產生

---

### Phase 5：證據收集

**目標**：設定證據收集器

#### 5.1 建立當地 FDA 收集器

建立 `src/txgnn/collectors/{country}fda.py`：

```python
from .base import BaseCollector, CollectorResult

class {Country}FDACollector(BaseCollector):
    source_name = "{country}fda"

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        # 實作搜尋邏輯
        pass
```

#### 5.2 區域臨床試驗註冊

ICTRP 涵蓋的區域註冊：
- 日本：JPRN (UMIN-CTR, JapicCTI)
- 韓國：CRIS
- 泰國：TCTR

**品質檢查點**：
- [ ] 當地 FDA 收集器建立
- [ ] ClinicalTrials.gov 收集器正常
- [ ] PubMed 收集器正常

---

### Phase 6：新聞監測

**目標**：設定健康新聞監測

#### 6.1 設定關鍵字模式

建立 `scripts/generate_news_keywords.py`，參考 TwTxGNN 版本。

#### 6.2 新增當地新聞來源

建立 `scripts/fetchers/{country}_news.py`

**品質檢查點**：
- [ ] `keywords.json` 產生
- [ ] 新聞爬蟲正常運作

---

### Phase 7：驗證與部署

**目標**：端對端驗證並部署

#### 7.1 設定 GitHub Actions

```bash
mv .github/workflows/pages.yml.template .github/workflows/pages.yml
# 編輯部署設定
```

#### 7.2 完整流程測試

```bash
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/generate_fhir_resources.py
```

#### 7.3 品質指標

| 指標 | 台灣參考值 | 目標 |
|------|-----------|------|
| FDA 藥品總數 | 71,552 | 記錄 |
| 有效藥品比例 | 33% | > 20% |
| DrugBank 映射率 | 73.87% | > 50% |
| 疾病映射率 | 44.85% | > 30% |
| 預測候選數 | 142,328 | 記錄 |

**品質檢查點**：
- [ ] 端對端流程通過
- [ ] GitHub Pages 部署成功
- [ ] SMART App 可從 SMART Launcher 啟動

---

## 三、關鍵檔案詳解

### 3.1 `config/fields.yaml`

欄位映射設定檔，定義藥監局資料欄位與標準欄位的對應關係。

### 3.2 `src/txgnn/data/loader.py`

資料載入器，根據 `fields.yaml` 載入並過濾藥品資料。

### 3.3 `src/txgnn/mapping/disease_mapper.py`

疾病映射模組，包含 `DISEASE_DICT`（當地語言→英文對照表）。

### 3.4 `scripts/process_fda_data.py`

資料處理腳本，將原始資料轉換為標準 JSON 格式。

---

## 四、GitHub Actions 設定

### 需設定的 Workflow：

| Workflow | 功能 | 需修改 |
|----------|------|--------|
| `pages.yml` | Jekyll 部署 | URL |
| `link-check.yml` | 連結檢查 | 無 |
| `check-new-evidence.yml` | 證據檢查 | 無 |

### 需設定的 Secrets：

| Secret | 用途 |
|--------|------|
| `GITHUB_TOKEN` | 自動提供 |
| `NCBI_API_KEY` | PubMed API（可選，提高速率限制） |

---

## 五、驗證清單

### 總體完成檢查

- [ ] Phase 0：專案初始化完成
- [ ] Phase 1：FDA 資料整合完成
- [ ] Phase 2：疾病映射完成
- [ ] Phase 3：KG 預測完成
- [ ] Phase 4：網站與 FHIR 完成
- [ ] Phase 5：證據收集完成
- [ ] Phase 6：新聞監測完成
- [ ] Phase 7：驗證與部署完成

### YMYL 檢查（醫療內容必檢）

- [ ] 免責聲明：「僅供研究參考，不構成醫療建議」
- [ ] 預測結果標註：「需經臨床驗證」
- [ ] 資料來源標註完整

---

## 六、附錄：區域特殊考量

### 日本 (PMDA)
- 資料格式：可能有 Shift-JIS 編碼
- 藥名：漢字/平假名/片假名混用
- 臨床試驗：JPRN (UMIN-CTR, JapicCTI, JMACCT)

### 韓國 (MFDS)
- 資料格式：UTF-8
- 藥名：韓文 + 英文音譯
- 臨床試驗：CRIS

### 泰國 (Thai FDA)
- 資料格式：UTF-8
- 藥名：泰文 + 英文
- 臨床試驗：TCTR

### 常見挑戰

1. **成分名稱變異**：同一藥物可能有不同鹽類形式
2. **品牌名映射**：當地品牌名需對應到國際名稱
3. **適應症文字解析**：不同語言的標點符號慣例不同
4. **日期格式**：各地區日期格式不同
5. **狀態碼**：有效/註銷的術語不同

---

## 常用命令

```bash
# 安裝依賴
uv sync

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 本地測試網站
cd docs && bundle exec jekyll serve

# 執行測試
uv run pytest tests/ -v
```

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節；
做法同 UsTxGNN，見 UsTxGNN/CLAUDE.md 同名一節）。規則與程式都在本 repo；頁面文字用英文，依據是SAHPRA 註冊（medapps 匯出；MPR 價格登錄補的有效註冊加註「status not confirmed by SAHPRA」）。本站的在地設定集中在 `src/zatxgnn/regulatory/site.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/zatxgnn/regulatory/page_format.py`（規則在 site.py 的 HEADER_RULE） | 頁首＝Quick Overview「Evidence Level」格的**第一個**等級（主預測）。2026-11-12 實測 354 頁有總覽等級，全部符合；整格取最高會有 5 頁不同 |
| 撤回預測 | `src/zatxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `scripts/sync_license_pages.py`、`snapshots/za_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/zatxgnn/regulatory/licenses.py` | 程式產生的表前後有 `<!-- licenses:begin/end -->` 標記；快照存程式表列、總數、本藥號碼、事實層；gate 依快照驗程式區塊、號碼歸屬、狀態列與張數列 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依成分重建刪句後（`scripts/license_rebuild_run.py` 有的話會自動跑）或依 git 前後版本，把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；證據包沒有適應症文字的頁不比對，程式照實回報 |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首＝本站規則算出的等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、license_rebuild_run.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（排程與重建會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 依成分重建後直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 395 筆紀錄（304 頁；其中 0 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁時，會重套紀錄（有程式許可證表的站也保留舊頁的程式區塊），notes 裡的舊錯句會被紀錄再更正一次。
2026-11-12 正文張數對事實層再掃一次：calcipotriol（只有 2 個產品）、fenofibrate（唯一註冊可能是複方）、citalopram（4 個產品）、pseudoephedrine（19 張）、donepezil_hydrochloride（目前零註冊）跟 SAHPRA 事實層相反，以 `za-lic-20261112-*` 刪掉矛盾子句。

## 新資料查不到的註冊號（2026-11-17）

2026-11-17 每週排程：證據包 12,918 張註冊號，SAHPRA medapps 匯出（21,435 筆）只涵蓋 93.4%，「新資料查不到」847 張（摘要只列前 300；本站 COVER_MIN 較寬，沒開 issue）。
用戶要求確認實際狀態，逐號比對 Release data-20261116-101839 裡 GitHub Actions 下載的匯出（data/raw/sahpra_status.json；medapps 在 6006 埠，雲端代理不支援，雲端 session 無法重新下載）：
- 847 張裡 844 張是只在 MPR 價格登錄有、頁面本來就標「status not confirmed by SAHPRA」的號碼，3 張是 SAHPRA 以前匯出的六碼寫法（590209 等）。
- 56 張其實是 SAHPRA 匯出上的註冊、只差號碼寫法（`scripts/rebuild_licenses_by_ingredient.py` 新增 R7、R8，每週更新與依成分重建共用；只在原有 R1–R6 對不到時才試，
  只認品牌字整字出現在 SAHPRA 產品名、SAHPRA 只有一個號碼的數字段相同）：
  R7 字首字母漏打或打錯 53 張（例 38/2.2/0565＝A38/2.2/0565 PHARMA-Q MIDAZOLAM、A48/1.2/0910＝48/1.2/0910 ILLOVEX XR、Z/3.1/0153＝W/3.1/153 NAPFLAM、
  REG NO. G/5.7/80＝G/5.7/80 ASIC）；R8 六碼連寫 3 張（590209＝59/8.2/0209 PIXULANT 5、590463＝59/21.1/0463 BLASILIN、590984＝59/2.9/0984 SEDMEDEX RTU 100 ml）。
  其中 49 張 Registered（狀態不變，拿掉「not confirmed」、號碼改 SAHPRA 寫法）、7 張 SAHPRA 是 Canceled，頁面原本寫成有效：VOMIZ INJECTION A39/5.10/0581、
  ESTALIS SEQUI PLUS 50/140、50/250（A40/21.8.2/0112、0113）、ILOSONE 250 P（B/20.1.1/168）、COXEP 100／200 mg（47/3.1/0690、0691）、MEGAPYN TABLETS（X/2.8/240）。
  同一個證據包本來就有 SAHPRA 號碼的，merge_records 合併（60 筆）。`scripts/license_adapter.py` 的 record_id 改成對所有 SAHPRA 匯出沒有的號碼套寫法統一（原本只對 status_unconfirmed）。
- ESTALIS SEQUI PLUS 50/140 在 MPR 成分欄錯植 paracetamol、pseudoephedrine，對回 SAHPRA（成分 estradiol＋norethisterone）後從 acetaminophen、paracetamol、
  pseudoephedrine（含 _hcl、_hydrochloride）5 個證據包移到 excluded_records（重建時「SAHPRA 成分全文不含本藥」會自動剔除）。
- 其餘 791 張當時判斷不了，維持原狀態（Valid, status not confirmed by SAHPRA）；同日人工查證結果見下一節（「匯出依註冊日期篩選漏收」的假設後來證明不成立）。
- 頁面：34 頁概覽狀態列／張數列與許可證表由排程程式同步（張數多半因合併與 Estalis 剔除而減少）；正文沒有跟新事實矛盾的句子，沒有新查核紀錄。
  celecoxib、pseudoephedrine 的 11-05 查核框寫「as of 2026-11-05」的張數，是當時的數字，不改。

## 只在 MPR 有的 791 張查證（2026-11-17）

用戶要求自己查證上節 791 列（788 個號碼，人工查核清單 txgnn/.claude/manual_license_lookup_20261117/）。來源：
- SAHPRA medapps 首頁的伺服器端產品表（POST https://medapps.sahpra.org.za:6006/Home/getData，`.github/workflows/medapps-lookup.yml` 取得，2026-11-17）全部 21,439 筆
  （Registered 14,386、Canceled 5,162、Old Medicine 1,817、Registrered 74），跟每週排程用的匯出是同一批；全部列都有 reg_date，所以「匯出依註冊日期篩選漏收」不成立。
  Canceled 列的到期日幾乎都在 2020 年以後：medapps 只收新系統時期（約 2020 年起）的撤銷，更早撤銷的註冊整筆不在。
- 衛生部 MPR（Database of Medicine Prices）現行一期 2026-10-01（https://www.health.gov.za/nhi-pee/ 上的 Database_Of_Medicine_Prices_1_October_2026.xlsx，
  13,734 個產品列、10,731 個註冊號；另比對 2026-04-30 那期）。本站 MPR 紀錄原本取自 medicineprices.org.za API（data/raw/mpr_medicines.json 2026-03、
  mpr_by_ingredient 快取 2026-11-05），788 個號碼全部仍在 2026-10-01 那期（號碼與 NAPPI 都對得上）。MPR 有 Status 欄（Discontinued 1,228 列等）。
結果：
- (c) SAHPRA 有同一品項、只差號碼寫法 7 張（全部 Registered）：`scripts/rebuild_licenses_by_ingredient.py` 加 R9（藥理分類段點號位置：43/7.13/0939＝43/7.1.3/0939 MIXANVAL 10/5、
  51/20.1.1/0109＝51/20.11/0109 FUROCSEM 500、55/7.1.3/0356＝55/7.13/0356 ENPRESIL 20、56/10.2.2/0911＝56/10.22/0911 MONTEFLO 4 mg）與 R10（SAHPRA 自己寫六碼：
  56/7.1.3/0003＝560003 DIPTATRIS、55/7.1.3/0670＝550670 TESDYN 80/5、55/18.5/0863＝550863 NITROFURANTOIN 100 PHARMC）；條件同 R7、R8（品牌字整字出現、SAHPRA 只有一個號碼相符）。
  同證據包本來就有 SAHPRA 號碼的合併（19 筆）。
- (a) SAHPRA 沒有、現行 MPR 該號每一列都是 Discontinued 270 張（例 Zerit 5 張、Serenace 4 張、Aurorix／Clorix、Requip 0.5–5.0、Berotec、Monopril、Inhibace Y/7.1.3/65、
  Cilest／Tricilest、Tredaptive、Besobrial、Phosphosorb 660、Estracombi TTS）：兩個官方來源都不列為現行，判為非有效。SAHPRA 與 MPR 都完全不列的號碼 0 張。
  `scripts/license_adapter.py`：fetch() 另下載 nhi-pee 頁上日期最新的一期 MPR（少於 MPR_MIN＝8,000 個號碼或下載失敗不判定）；preprocess 對 SAHPRA（含寫法統一）沒有、
  MPR 不列或全部 Discontinued 的號碼標 `license_status: cancelled`＋`mpr_not_current`（第一次發現日）＋`mpr_status`＋`mpr_edition`，status 改
  「Not on SAHPRA register; discontinued in MPR (Database of Medicine Prices, <日期>)」（原值存 `status_before_mpr_not_current`），拿掉 status_unconfirmed；
  MPR 又列為現行或 SAHPRA 查得到就還原。`confirmed_absent()` 讓排程把這些列成「主管機關現行清單確認已不列」。許可證表狀態格寫「Not on SAHPRA register; discontinued in MPR」
  （`scripts/sync_license_pages.py` 的 MPR_LAB），不寫 SAHPRA 撤銷；sync_tables 對有這種紀錄的藥一律重排。全部非有效的頁狀態列＝母目錄 check_drug_page.py 的
  SCOPE_CANCELLED["ZaTxGNN"]「Not marketed (no current registration: N of N cancelled by SAHPRA, or not on the SAHPRA register and discontinued in or absent from the current
  Medicine Price Registry)」（本站 tools/txgnn 同步同一份；母目錄 gen_local_home 首頁表的字樣跟著改）。本機試跑讀已下載的 SAHPRA 匯出：環境變數 ZA_SAHPRA_RAW。
  依成分重建（rebuild_licenses_by_ingredient.py）會把這些號碼重設成 status_unconfirmed，下一次每週排程的 preprocess 會再標回（第一次發現日會變成那天）。
- (b) SAHPRA 沒有、現行 MPR 仍列（沒有 Discontinued）511 張，維持 Valid（status not confirmed by SAHPRA）：MPR 是價格登錄、不是註冊登錄，2026-10-01 那期仍列 2010 年就撤市的
  sibutramine（Reductil 10／15 33/11.3/0025–0026、Ectiva 10／15 0027–0028、Leantil 41/11.3/0180、0153、Ciplatrim 10／15 0312–0313，價格照年度 SEP 調整、生效日 2026-10-01）
  與 dextropropoxyphene（Doloxene、Distalgesic），不能當成仍註冊的證據；但 SAHPRA 只收約 2020 年起的撤銷，「不在 SAHPRA」也不能推定撤銷。sibutramine 8 張照這條規則維持 not confirmed
  （2010-10 政府新聞稿說 Abbott 與 MCC 協商後撤下 Reductil／Ectiva、MCC 要對學名藥採取行動；雲端連不到 sanews.gov.za，沒有取得 MCC／SAHPRA 撤銷註冊的官方文件）。
- 頁面：140 頁概覽狀態列／張數列與許可證表由程式同步（8 頁變成全部非有效：acamprosate、acamprosate_calcium、calcium、calcium_acetate、conjugated_estrogens、ginseng、niacin、norgestimate；
  另 buclizine、metoprolol 原本就全部 SAHPRA 註銷，狀態列跟著換成 SCOPE_CANCELLED 寫法）；正文矛盾 1 句：norgestimate「Both registrations are valid」以 `za-lic-20261106-norgestimate-1` 同 id 重發更正（前版存 history）。

## 官方撤市的人工確認表（2026-11-18）

用戶 2026-11-18 決定：上節 (b) 裡 MPR 仍列、SAHPRA 不列的 sibutramine 與 dextropropoxyphene 產品「加人工確認表、寫成已撤市」。只收找得到官方撤市依據、能對到號碼的：
- sibutramine 4 張：Reductil 10／15（33/11.3/0025、0026）、Ectiva 10／15 mg（33/11.3/0027、0028）。依據 SAnews（GCIS）2010-10-13「Ectiva, Reductil off SA shelves」
  （https://www.sanews.gov.za/south-africa/ectiva-reductil-sa-shelves：Abbott 與 MCC 協商後同意撤出南非市場）；Abbott 公告（bizcommunity 轉載）。
- dextropropoxyphene 4 張：Distalgesic E/2.8/0090、Doloxene Plain B0586 (ACT 101)、Doloxene Co-65 B0584 (ACT 101)、Lentogesic B1334(ACT 101/1965) OM*（證據包在 acetaminophen、paracetamol、
  acetylsalicylic_acid、caffeine、caffeine_anhydrous、dextropropoxyphene）。依據 MCC 2011-05-03 媒體聲明（gov.za「Withdrawal of dextropropoxyphene containing medicines from the South African market」：
  MCC 2011-04-14～15 決議所有含 DPP 藥品撤出南非市場，點名 Distalgesic、Doloxene、Doloxene CO-65、Doxyfene、Lentogesic、Synap Forte，3 個月過渡期）。
- 沒收：Ciplatrim 10／15（41/11.3/0312–0313）、Leantil 10／15 mg（41/11.3/0180、0153）——MCC 2010 只說對學名藥會「take appropriate action」，媒體（news24／Health24 2012–2013，雲端連不到）
  提到 Ciplatrim 暫停上市，但沒找到 MCC／SAHPRA 官方文件，維持 Valid（not confirmed）。SAHPRA 註冊表仍列 Registered 的 Doxyfene E/2.9/97、Synap Forte J/2.8/252 與 Old Medicine 的
  Lentogesic B1334、Zomax B0882 跟 MCC 2011 決議有出入，照 SAHPRA 不改，dextropropoxyphene 頁以 `za-lic-20261118-dextropropoxyphene-1`（annotate）加註 MCC 決議。
- `scripts/license_adapter.py` 的 ZA_WITHDRAWN（每筆附依據網址、日期、摘要）：preprocess 對表內、SAHPRA 匯出（含寫法統一）查不到的號碼標 `license_status: cancelled`＋`za_withdrawn`（第一次標記日）
  ＋`za_withdrawn_basis`，status 改「Withdrawn from the South African market (<年>; MCC, <依據網址>); not on SAHPRA register」（原值存 `status_before_za_withdrawn`），拿掉 status_unconfirmed；
  表不依賴下載，依成分重建重設成 status_unconfirmed 後下一次 preprocess 會再標回；移出表或 SAHPRA 查得到就還原。`confirmed_absent()` 回真。許可證表狀態格寫
  「Withdrawn from the South African market (<年>); not on SAHPRA register」（`scripts/sync_license_pages.py` 的 WD_LAB），不寫 SAHPRA 撤銷；sync_tables 對有 za_withdrawn 的藥一律重排。
- 頁面：5 頁概覽狀態列／張數列與 2 頁許可證表由排程同步（sibutramine 8 張中有效 8→4、dextropropoxyphene 12 張中有效 8→4；acetaminophen、acetylsalicylic_acid、caffeine 各少 1～2 張）；
  正文沒有說這些產品有效或在售的句子，沒有 correct 紀錄。沒有頁變成全部非有效。

- 2026-11-19：MPR 把 Leantil Capsules 15 Mg（41/11.3/0153，sibutramine；SAHPRA 匯出與產品總表都沒有這個號碼）的成分欄錯寫成 sibutramine＋paracetamol 400 mg＋codeine phosphate 8 mg，
  被收進 acetaminophen、paracetamol、codeine、codeine_hcl、codeine_phosphate 5 個證據包。同品牌 Leantil 10 Mg（41/11.3/0180）的 MPR 成分只有 sibutramine、藥理分類 11.3 與其他 sibutramine 產品相同，
  判為錯植：`scripts/rebuild_licenses_by_ingredient.py` 的 MISMATCH 加 ("41/11.3/0153", "*sibutramine")（SAHPRA 沒有這號，「成分全文不含本藥」自動判定用不上），5 個證據包的這一列移到 excluded_records（附理由）；
  sibutramine 證據包照舊收。acetaminophen（564→563）、codeine（272→271）2 頁狀態列／張數列與許可證表由排程同步，正文沒有矛盾句。
- 2026-11-19（同日，用戶決定照 Leantil 做法）：另兩筆 MPR 成分欄錯植列進 MISMATCH——Alli（43/11.3/0192，orlistat 60 mg 減重膠囊，MPR S2；成分欄另列 salmeterol、tetanus toxoid、pertussis toxoid、polio 等吸入劑與疫苗成分）
  原被收進 salmeterol 證據包，移到 excluded_records（("43/11.3/0192", "*orlistat")；本站沒有 orlistat 證據包，所以哪裡都不收），salmeterol 頁狀態列／張數列與許可證表由排程同步（44→43 張，有效 38 不變）；
  Ciplatrim 15（41/11.3/0313，sibutramine 15 mg；同品牌 Ciplatrim 10 41/11.3/0312 的 MPR 成分只有 sibutramine，成分欄另列 Isophane Insulin 70%）沒有被收進任何 insulin 類證據包，只加 ("41/11.3/0313", "*sibutramine") 防止以後重建收進，
  sibutramine 證據包照舊收。兩個號碼 SAHPRA 匯出與產品總表都沒有。重建 dry-run 確認 Alli 從 salmeterol 剔除、Ciplatrim 15 留在 sibutramine、insulin 類證據包不變；正文沒有矛盾句。

## 同一 DrugBank ID 的重複公開頁改轉址（2026-11-19）

用戶 2026-11-19 決定（照 ARTxGNN 同日做法）：公開藥物頁同一 DrugBank ID（front matter drugbank_id，沒有的用證據包與 dbXXXXX 轉址頁推斷）、預測相同的，留一頁、另一頁改轉址（layout: id_redirect、permalink 不變、sitemap: false、search_exclude、nav_exclude）。
4 組，各組預測、等級、SAHPRA 註冊號完全相同；保留順序：查核紀錄數→字數：d-biotin→biotin、arginine_hydrochloride→arginine、dl-threonine→threonine、cupric_chloride→cupric_chloride_dihydrate（db09131 轉址頁改成直接指保留頁）。
被轉址頁的查核紀錄（d-biotin 1 筆、arginine_hydrochloride 2 筆，全是 resolved_by_regeneration）留在 drug_reviews.json 當歷史（apply_drug_reviews 跳過轉址頁）。
公開藥物頁 399→395；FHIR：cupric_chloride 的 DB09131 由 sync_fhir_levels 當重複刪；d-biotin、arginine_hydrochloride、dl-threonine 以頁名命名的 MK 跟保留頁的 DB00121／DB00125／DB00156（經 dbXXXXX 轉址頁對到）重複、預測相同，連同 CUD 手動刪掉（MK 399→395、CUD 1852→1845）；衍生檔、hreflang 照重產。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 343 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Detailed mechanism of action data is not available in the data compiled for this report.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `za-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：「According to the … section of the US FDA-approved prescribing information for <藥>: "…" ([DailyMed: …](…), label version …; accessed …)」。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 2026-11-19 結果：269 頁寫入紀錄（美國仿單 244、ChEMBL 25），74 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Approved use: Not recorded in the local data」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：SAHPRA 註冊（含 MPR 補的）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：acetic_acid「Approved use: Not recorded in the local data」→「In South Africa: 26 SAHPRA registrations (18 valid)」；2026-11-19 改了 234 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site ZaTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。
