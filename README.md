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
<img width="3356" height="1650" alt="image" src="https://github.com/user-attachments/assets/dcd2d6c3-e2d5-4522-b7e5-3f9c19bbe87c" />
<img width="3360" height="1644" alt="image" src="https://github.com/user-attachments/assets/4c26f7b6-e421-45b6-b5a4-c4353d048573" />
<img width="3358" height="1642" alt="image" src="https://github.com/user-attachments/assets/a0cbdb43-b976-406f-8337-641576c1aae2" />
<img width="3358" height="1638" alt="image" src="https://github.com/user-attachments/assets/828d1af3-0e94-46c3-bc73-05128a0da88c" />
<img width="3352" height="1636" alt="image" src="https://github.com/user-attachments/assets/427a5894-a6a1-4aca-9a83-4b04a7e1870f" />
<img width="3360" height="1634" alt="image" src="https://github.com/user-attachments/assets/eb188fb3-dcce-4607-8925-ddc8e932d749" />



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
