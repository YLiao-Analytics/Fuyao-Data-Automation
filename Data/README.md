# 📊 Manufacturing Data Automation & Analytics Dashboard
*Automating Production Reporting and KPI Visualization for Manufacturing Excellence*

## 🌟 Executive Summary
This project addresses the manual data consolidation challenges in a manufacturing environment (inspired by **Fuyao Glass**). By leveraging **Python** and **Streamlit**, I developed an end-to-end pipeline that transforms fragmented raw CSV data into an interactive, stakeholder-ready dashboard.

**Key Result:** Reduced data processing time by **95%** (from 30 mins manual work to <1s automation) and eliminated human transcription errors.

---

## 🛠️ Business Problem
Production lines generate independent daily reports. Analysts previously faced:
* **Data Silos**: Manually merging multiple CSV files from different lines.
* **Data Quality Issues**: Handling missing values and inconsistent formatting.
* **Lagging Insights**: Time spent on cleaning data instead of analyzing trends.

## 🚀 Technical Solution
### 1. Automated ETL Pipeline (`excel_automation.py`)
* Used **Pandas** for high-speed data manipulation.
* Implemented **Smart Data Cleaning**: Automatic imputation of missing production values using statistical averages.
* **Standardization**: Unified workshop naming conventions via regex and string parsing.

### 2. Interactive BI Dashboard (`app.py`)
* Developed a **Streamlit** web application for self-service analytics.
* **Real-time Visualization**: Dynamic bar charts for production volume comparison.
* **One-Click Export**: Automated generation of audit-ready Excel monthly reports.

---

## 📈 Live Demo
[![Streamlit App](https://app-workshop-w8qzri2vqcfauvolskfcbc.streamlit.app/)]

> **How to use:** > 1. Click the badge above to open the cloud app.
> 2. Upload the sample files from the `/Data` folder.
> 3. View instant KPI metrics and download the consolidated report.

---

## 🧰 Tech Stack
* **Language:** Python 3.10
* **Libraries:** Pandas, Openpyxl, Streamlit, Matplotlib
* **Version Control:** Git/GitHub
* **Environment:** VS Code (Miniconda)
