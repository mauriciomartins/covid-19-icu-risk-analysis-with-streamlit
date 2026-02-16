# COVID-19 ICU Risk Analysis

## 📊 Project Overview

This project performs exploratory data analysis and visualization of clinical data from COVID-19 patients to investigate factors associated with ICU admission.

The dataset was made publicly available through a research initiative involving Hospital Sírio-Libanês (Brazil) and released via Kaggle for predictive modeling purposes.

## 🏥 Data Source

The dataset originates from Hospital Sírio-Libanês and contains anonymized clinical data including demographic information, laboratory test results, vital signs, time-windowed measurements, and ICU admission outcome.

## 🎯 Objectives

- Perform data cleaning and preprocessing
- Aggregate patient-level data to avoid duplication bias
- Analyze ICU admission rates by age group and time window
- Create interactive visualizations using Plotly and Streamlit
- 
## Demo
https://1homepy-6je2radiiqytcu8hg8pxvg.streamlit.app/

## 🛠 Technologies

- Python
- pandas
- numpy
- openpyxl
- plotly
- streamlit
- vega-datasets

Note: The project does not use Altair / Vega-Lite in its source files, so `altair` is not required and is not listed in `requirements.txt`. If you have `altair` installed in your virtual environment, it is optional for this repository.

## 🚀 Run Locally

1. Clone the repository (or your fork):

```bash
git clone <REPO_URL>
cd covid-icu-risk-analysis
```

2. Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Run the Streamlit app (from repository root):

```bash
streamlit run 1_home.py
```

4. Git commit & push suggestions:

```bash
git add requirements.txt .gitignore README.md
git commit -m "chore: prepare project for GitHub (minimal requirements, gitignore, README)"
git push origin main
```

## 📌 Important Note

This project is intended for educational and analytical purposes only. The dataset contains anonymized patient information and does not include personally identifiable data.

---

If you'd like, I can also:

- Add a `.github/workflows` GitHub Actions CI workflow to run linting/tests
- Create a `CONTRIBUTING.md` with contribution guidelines
