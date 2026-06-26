# API Data Collection & Analysis  
### *UC Berkeley Adavanced Computing – Fall 2025*  
**Author:** Pei Zheng  
**Date:** October 2025  

---

## 🎯 Research Question  
**How do economic indicators relate to social development?**  
Do wealthier countries have better social indicators such as education and digital access?

---

## 🌍 Data Source  
**World Bank Open Data API** (no API key required)  
- Base endpoint: https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json  

- Data range: **2010–2020**  
- Countries: 20 economies (USA, CHN, JPN, DEU, GBR, FRA, IND, BRA, CAN, AUS, etc.)  
- Indicators:

| Indicator Code | Description | Units |
|-----------------|--------------|--------|
| `NY.GDP.MKTP.CD` | GDP (current US$) | USD |
| `SE.ADT.LITR.ZS` | Adult literacy rate | % of adults (15+) |
| `IT.NET.USER.ZS` | Internet users | % of population |

---

## 📐 Methodology — Data Collection and Analytical Design  

### **1. Research Framework**
This study applies a **quantitative correlational approach** to explore how macroeconomic indicators (GDP) are associated with measures of social development (literacy and digital access).  
The analysis focuses on whether economic prosperity corresponds with improvements in social indicators between 2010 and 2020.

### **2. Data Collection**
- Data were gathered directly from the **World Bank API** using Python’s `requests` library.  
- Each country–indicator–year combination was queried systematically, totaling more than 60 API calls.  
- The resulting JSON payloads were parsed, cleaned, and merged into a single `processed_data.csv` file.  
- Missing or null observations were excluded; time-series alignment was performed by country and year.

### **3. Variables and Derived Features**
| Variable | Definition | Purpose |
|-----------|-------------|----------|
| `gdp_current_usd` | GDP (current US$) | Economic indicator |
| `internet_users_pct` | % of population using the Internet | Proxy for digital access |
| `adult_literacy_rate` | Literacy rate among adults (15+) | Proxy for education |
| `gdp_per_internet_user` | GDP normalized by Internet adoption | Measures economic resources per connected person |
| `gdp_yoy_growth` | Year-over-year GDP growth | Captures economic momentum |
| `internet_users_pct_yoy` | Year-over-year change in Internet usage | Captures social diffusion speed |

### **4. Analytical Steps**
1. **Descriptive Analysis:** Calculate yearly averages and visualize time trends (bubble charts).  
2. **Cross-sectional Analysis:** Compare GDP vs. social indicators using scatterplots (log-scale GDP).  
3. **Correlation Testing:** Compute Pearson and Spearman correlations for both multi-year averages and 2020 snapshot.  
4. **Interpretation:** Evaluate strength and direction of relationships; contextualize results within socioeconomic theory.  
5. **Validation:** Use visual patterns (e.g., saturation or convergence) to corroborate quantitative correlations.

### **5. Analytical Tools**
- **Python Libraries:** `requests`, `pandas`, `matplotlib`, `seaborn`, `json`, `dotenv`  
- **Computation Environment:** Jupyter Notebook (`analysis.ipynb`)  
- **Data Validation:** Assert file existence, handle retries and API timeouts gracefully  
- **Visualization:** Scatterplots, time-series bubble charts, and heatmaps for missingness patterns

---

## 🧩 Data Pipeline Overview  

| Step | Description |
|------|--------------|
| **1. API Requests** | Queried 20 countries × 3 indicators × 11 years → ≥ 60 API calls |
| **2. JSON Parsing** | Extracted country, year, indicator code, value |
| **3. Cleaning & Transformation** | Converted to wide panel (`country × year`), removed missing values |
| **4. Derived Variables** | Added `gdp_per_internet_user`, `internet_users_pct_yoy`, `gdp_yoy_growth` |
| **5. Outputs** | `raw_data.json` (sample) and `processed_data.csv` (clean dataset) |

---

## 💻 Files in Repository

| File | Purpose |
|------|----------|
| `data_collector.py` | Collects, cleans, and exports World Bank data |
| `processed_data.csv` | Cleaned panel data (country × year) |
| `raw_data.json` | 150-record sample of raw API responses |
| `analysis.ipynb` | Visualization, correlation analysis, and interpretation |
| `requirements.txt` | Python dependencies |
| `.env.template` | Example environment file (not used for World Bank) |

---

## 📊 Visualization Highlights

### **1️⃣ Internet Usage over Time (2010–2020)**  
Bubble chart showing Internet users (% of population) across 20 countries:  

- **X-axis:** Year  
- **Y-axis:** Internet Users (%)  
- **Bubble size:** GDP (Current US$)  
- **Color:** Country  

**Insights:**  
- Internet penetration rose globally from 2010–2020.  
- High-GDP countries (USA, JPN, DEU) were already near saturation (>80%) in 2010.  
- Emerging economies (CHN, BRA, IDN) showed rapid catch-up growth.  
- Low-income countries (IND, ZAF) lagged but improved steadily.  

→ **Interpretation:** Wealthier countries reached digital maturity earlier,  
while middle- and lower-income nations show strong upward convergence trends.

---

### **2️⃣ GDP vs. Social Indicators (2010–2020 averages)**  
- Scatterplots of GDP (log scale) vs. Internet usage & Literacy rate.  
- Overall pattern: weak but positive association between wealth and social development.  
- Saturation observed among high-income countries.

---

## 📈 Correlation Results

### **Evidence-based Conclusion**

**Summary of Correlations**
- Avg(2010–2020) — GDP vs internet_users_pct: **Pearson 0.088**, Spearman 0.162 *(very weak, positive)*; N=20  
- Avg(2010–2020) — GDP vs adult_literacy_rate: **Pearson 0.023**, Spearman 0.055 *(very weak, positive)*; N=11  
- Snapshot(2020) — GDP vs internet_users_pct: **Pearson 0.022**, Spearman -0.029 *(very weak, mixed)*; N=20  
- Snapshot(2020) — GDP vs adult_literacy_rate: **Pearson 0.068**, Spearman -0.357 *(weak, negative)*; N=7  

**Interpretation**
1. For 2010–2020 averages, GDP shows a very weak positive association with Internet usage, suggesting wealthier countries tend to have higher digital access.  
2. For 2010–2020 averages, GDP shows a very weak positive association with literacy, consistent with the idea that economic capacity supports education outcomes.  
3. The 2020 snapshot results are directionally similar, providing a contemporaneous cross-check.

**Caveats**
- Correlation ≠ causation. Unobserved confounders (institutions, policy, demographics) may drive both GDP and social indicators.  
- Some countries may be outliers due to data gaps or structural transitions.  
- Literacy data coverage is limited; interpret with caution.

**Answer to Research Question**  
> Overall, the evidence indicates that **wealthier countries generally exhibit better social indicators** (higher Internet usage and literacy),  
> though the strength varies by metric and country, and causality is not established here.

---

## ⚠️ Limitations — Caveats and Potential Biases

1. **Correlation ≠ Causation**  
 This analysis is descriptive. Institutions, governance quality, demographics, and policy choices may jointly affect both GDP and social indicators, confounding simple bivariate relationships.

2. **Data Coverage & Missingness**  
 Literacy data are sparse and clustered near high values for developed economies, which can compress variation and attenuate correlations. Countries with missing years reduce statistical power and may bias results toward countries with better reporting systems.

3. **Measurement & Comparability**  
 - **GDP in current US$** is affected by inflation and exchange rate movements; cross-country comparisons may be distorted without PPP adjustments.  
 - Internet user definitions can vary across national statistical offices.

4. **Saturation & Nonlinearity**  
 Social indicators (internet usage, literacy) exhibit ceilings. At high development levels, marginal gains are small, so linear correlation with GDP tends to weaken. Nonlinear models (e.g., splines or logistic curves) could capture this relationship better.

5. **Temporal Aggregation**  
 Averaging 2010–2020 smooths macro shocks but hides within-period events (policy reforms, currency crises). The 2020 snapshot reflects a single year and may be sensitive to anomalies.

6. **Sample Composition**  
 Results depend on which countries are included. Adding or removing small or low-income economies could shift observed correlation magnitudes.

7. **Omitted Variables**  
 Education quality, health outcomes, inequality, and infrastructure investment are excluded; they likely mediate the link between GDP and social development.

---

## ⚙️ How to Reproduce

### 1️⃣ Setup Environment
```bash
python3 -m venv .venv
source .venv/bin/activate      
pip install -r requirements.txt
```

### 2️⃣ Collect Data
```bash
python data_collector.py
```

### 3️⃣ Run Analysis
```bash
jupyter lab
# Open analysis.ipynb → Run All
```

---

## 🧠 Implications

- The weak correlation suggests that by 2010–2020, Internet usage had become nearly universal among many economies, reducing variation across GDP levels.

- Literacy rates may have reached saturation in developed regions, weakening observable linear relationships.

---

## 🏁 Conclusion

- Economic prosperity remains loosely correlated with social advancement, but as digital technologies diffuse globally, the marginal gains of wealth diminish.

- The convergence trend suggests that global digital access is no longer a privilege of high income — it’s becoming a shared global standard.