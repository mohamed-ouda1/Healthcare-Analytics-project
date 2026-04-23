# 🏥 Healthcare Cost Analysis & Optimization

## 📌 Project Overview
This project provides a comprehensive analysis of healthcare data to identify cost drivers, patient demographics, and hospital performance. Using Python and data science libraries, we perform deep exploratory data analysis (EDA) to uncover insights that can help healthcare providers optimize billing and resource allocation.

## 📊 Key Objectives
- **Clean and Normalize Data**: Handle outliers, missing values, and inconsistent formatting.
- **Identify Cost Drivers**: Analyze how admission types and medical conditions affect billing.
- **Demographic Insights**: Understand the age and gender distribution of patients.
- **Hospital Performance**: Rank hospitals based on patient volume and billing efficiency.

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **Libraries**: 
  - `Pandas`: Data manipulation and cleaning
  - `NumPy`: Numerical computations
  - `Matplotlib` & `Seaborn`: Advanced data visualization

## 📈 Key Insights Summary
- **Admission Impact**: Emergency admissions are significantly costlier than elective ones.
- **Stay Duration**: A direct correlation exists between length of stay and total billing amount.
- **Outliers**: Identified and handled erroneous negative billing entries to ensure data integrity.

## 📂 Project Structure
- `Healthcare Project.ipynb`: The main analysis notebook.
- `healthcare_dataset.csv`: Raw dataset.
- `clean_healthcare__dataset.csv`: Processed and cleaned dataset used for final insights.

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies: `pip install pandas matplotlib seaborn streamlit plotly`.
3. Open `Healthcare Project.ipynb` in Jupyter Notebook to see the deep analysis.
4. Run the interactive dashboard:
   ```bash
   streamlit run dashboard.py
   ```

---
*Created by [Your Name] - Data Analyst Portfolio Project*
