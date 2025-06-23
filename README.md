# 🚢 Titanic Dataset Analysis - Data Cleaning & Exploratory Data Analysis

<div align="center">

![Titanic](https://img.shields.io/badge/Dataset-Titanic-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-red?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-orange?style=for-the-badge)

*A comprehensive data analysis project exploring survival patterns aboard the RMS Titanic*

</div>

---

## 📊 Project Overview

This project performs an in-depth **Exploratory Data Analysis (EDA)** on the famous Titanic dataset, focusing on understanding the factors that influenced passenger survival rates. Through systematic data cleaning and visualization, we uncover compelling insights about the tragic maritime disaster of 1912.

### 🎯 Key Objectives
- **Data Quality Assessment**: Identify and handle missing values, duplicates, and data inconsistencies
- **Feature Engineering**: Create meaningful variables to enhance analysis
- **Survival Analysis**: Explore survival patterns across different passenger demographics
- **Statistical Testing**: Perform hypothesis testing to validate findings
- **Visualization**: Create compelling charts and graphs to communicate insights

---

## 📁 Project Structure

```
📂 Titanic-Analysis/
├── 📄 eda.py                    # Main analysis script
├── 📊 train.csv                 # Training dataset (891 passengers)
├── 📊 test.csv                  # Test dataset (418 passengers)
├── 📋 gender_submission.csv     # Sample submission file
└── 📖 README.md                 # Project documentation
```

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.8+ |
| **Pandas** | Data manipulation and analysis | Latest |
| **NumPy** | Numerical computations | Latest |
| **Matplotlib** | Data visualization | Latest |
| **Seaborn** | Statistical data visualization | Latest |
| **SciPy** | Statistical testing | Latest |

---

## 📈 Key Features & Analysis

### 🧹 Data Cleaning
- **Missing Value Imputation**: Smart handling of Age, Embarked, and Cabin data
- **Feature Engineering**: Title extraction, age grouping, fare binning
- **Data Validation**: Duplicate detection and data type optimization

### 🔍 Exploratory Analysis
- **Survival Rate Analysis**: Overall and demographic-specific survival rates
- **Correlation Analysis**: Relationship between variables and survival
- **Statistical Testing**: T-tests and chi-square tests for significance
- **Advanced Segmentation**: Multi-dimensional survival analysis

### 📊 Visualizations
- Survival distribution pie charts
- Age and fare histograms
- Passenger class and gender breakdowns
- Correlation heatmaps
- Cross-tabulation analyses

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3.8+ installed with the following packages:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

### Installation & Usage

1. **Clone the repository**
```bash
git clone <repository-url>
cd titanic-analysis
```

2. **Run the analysis**
```bash
python eda.py
```

3. **View results**
The script will generate:
- Console output with statistical summaries
- Interactive plots and visualizations
- Data quality reports

---

## 📊 Key Insights Discovered

### 🎭 Survival by Demographics
- **Overall Survival Rate**: ~38.4%
- **Female Survival Rate**: ~74.2%
- **Male Survival Rate**: ~18.9%
- **First Class Survival Rate**: ~62.9%
- **Third Class Survival Rate**: ~24.2%

### 👥 Passenger Statistics
- **Average Age of Survivors**: ~28.3 years
- **Average Age of Non-survivors**: ~30.6 years
- **Most Common Title**: Mr. (517 passengers)
- **Highest Survival Title**: Mrs. (~79.2%)

### 🚢 Class Analysis
Passenger class significantly impacted survival chances, with first-class passengers having the highest survival rates.

---

## 📋 Dataset Information

### Training Data ([train.csv](train.csv))
- **Size**: 891 passengers
- **Features**: 12 columns including survival labels
- **Purpose**: Analysis and model training

### Test Data ([test.csv](test.csv))
- **Size**: 418 passengers  
- **Features**: 11 columns (no survival labels)
- **Purpose**: Model evaluation and predictions

### Key Variables
| Variable | Description | Type |
|----------|-------------|------|
| `Survived` | Survival indicator (0 = No, 1 = Yes) | Binary |
| `Pclass` | Passenger class (1st, 2nd, 3rd) | Categorical |
| `Name` | Passenger name | Text |
| `Sex` | Gender | Categorical |
| `Age` | Age in years | Numerical |
| `SibSp` | Number of siblings/spouses aboard | Numerical |
| `Parch` | Number of parents/children aboard | Numerical |
| `Fare` | Passenger fare | Numerical |
| `Embarked` | Port of embarkation | Categorical |

---

## 🔬 Statistical Analysis Highlights

The analysis includes comprehensive statistical testing:
- **T-tests** for age differences between survivors and non-survivors
- **Chi-square tests** for categorical variable associations
- **Correlation analysis** for feature relationships
- **Survival rate calculations** across all demographics

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📞 Contact

**Harsh Kadecha**
- GitHub: [@HarshKadecha11](https://github.com/HarshKadecha11)
- Email: kadechaharsh@gmail.com
- LinkedIn: [Harsh Kadecha](https://www.linkedin.com/in/harsh-kadecha-20b288330/)

---

<div align="center">

### 🌟 If you found this project helpful, please give it a star! ⭐

*"Remember, even the unsinkable can sink, but data insights are forever."* 🚢📊

---

**Made with ❤️ for Data Science**

</div>