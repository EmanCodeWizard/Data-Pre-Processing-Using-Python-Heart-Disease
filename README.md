# Data-Pre-Processing-Using-Python-Heart-Disease
Heart Disease UCI Dataset - Data Preprocessing & EDA
This project focuses on preprocessing, cleaning, and exploring the UCI Heart Disease dataset. It applies a wide range of data preprocessing techniques such as missing value imputation, encoding, scaling, outlier detection/removal, and visualization using Python libraries like pandas, seaborn, matplotlib, and scikit-learn.

📁 Dataset
The dataset used is: heart_disease_uci.csv

Ensure the file is placed in the root directory of your project before running the code.

📚 Libraries Used
pandas
numpy
matplotlib
seaborn
scikit-learn
Install missing dependencies using:

pip install pandas numpy matplotlib seaborn scikit-learn
🧼 Preprocessing Steps
🔹 Data Cleaning
Removed irrelevant id column.

Checked and removed duplicate rows.

Identified and handled missing values:

Dropped missing values where applicable.

Imputed categorical missing values with mode.

Imputed numerical missing values using:

Mean/Median (based on distribution)

KNNImputer for multivariate imputation.

🔹 Encoding
Encoded ordinal categorical features (e.g., cp, restecg, slope, thal) using LabelEncoder.

Encoded binary features (e.g., sex, fbs, exang) using label encoding.

🔹 Scaling
Applied StandardScaler to normally distributed features.

Applied MinMaxScaler to features with wider ranges.

Scaled features include:

standard_scaled_features: ['age', 'thalch', 'oldpeak']

minmax_scaled_features: ['trestbps', 'chol']

📊 Exploratory Data Analysis (EDA)
Visualizations performed include:

Histograms and KDE plots for numerical features.

Box plots to detect outliers.

Count plots for categorical variables.

Distribution plots post-scaling.

📉 Outlier Handling
Applied IQR-based filtering to:

trestbps, chol, thalch

Winsorization to cap extreme values in:

oldpeak

🧠 Future Work
Although this notebook/code focuses on preprocessing and EDA, the cleaned and transformed data can be used for:

Building classification models (e.g., Logistic Regression, KNN, SVM).

Performing PCA and dimensionality reduction.

Hyperparameter tuning and cross-validation.

Deployment in a Flask app or API.

📎 Notes
The dataset includes both categorical and numerical features.
The final dataframe is ready for ML modeling after preprocessing.
Ensure proper Python environment with required packages before execution.

📧 Contact
For any queries, reach out to:

Noor ul Ieman
Roll Number: 2022-BSE-063
Semester: 6th, Section B
Email:iemannoorul614@gmail.com
