 Impact of Soil Quality and Weather Parameters on Crop Growth Analysis
 Project Overview:

This project focuses on analyzing the impact of soil nutrients and weather parameters on crop growth using Python-based data analysis and visualization techniques.
The study aims to understand relationships between soil properties, climatic conditions, and crop types to support data-driven crop recommendation and agricultural planning.

The analysis is performed on a structured agricultural dataset containing soil nutrients, environmental factors, and corresponding crop labels.

Objectives:

•To explore and understand soil and weather data affecting crop growth

•To clean and preprocess agricultural datasets

•To analyze statistical properties and correlations among features

•To visualize data distributions and inter-relationships

•To gain insights useful for crop recommendation systems

Dataset Description:

The dataset contains the following attributes:

N – Nitrogen content in soil

P – Phosphorus content in soil

K – Potassium content in soil

temperature – Average temperature (°C)

humidity – Relative humidity (%)

ph – Soil pH value

rainfall – Rainfall (mm)

label – Crop type

The dataset is loaded from a CSV file and checked for data quality issues such as missing values and duplicate entries.

Tools and Libraries Used:

Python

Pandas – Data handling and preprocessing

NumPy – Numerical operations

Scikit-learn – Label encoding and feature scaling

Matplotlib – Data visualization

Seaborn – Advanced statistical visualizations

Data Preprocessing Steps:

CSV File Loading

Dataset successfully loaded using Pandas.

Initial Data Inspection

Displayed head, info, and summary statistics.

Checked for missing values and duplicate rows.

Duplicate Handling

Duplicate records were identified and removed (if present).

Label Encoding

Crop labels were converted into numerical form using LabelEncoder.

Feature Scaling

Numerical features were standardized using StandardScaler to ensure uniform scale.

Exploratory Data Analysis (EDA):

The following analyses were performed:

• Statistical Analysis:

Descriptive statistics using describe()

Correlation matrix among numerical features

• Univariate Analysis:

Histograms to observe data distribution

Boxplots to identify outliers

• Multivariate Analysis:

Pair plots for overall feature interaction

Heatmap to visualize correlation strength

• Crop-wise Analysis:

Boxplots of N, P, K levels across different crops

Scatter plots showing:

Nitrogen vs Phosphorus

Phosphorus vs Potassium

Temperature vs Humidity

Soil pH vs Rainfall

Each visualization helps in understanding how soil and weather parameters vary for different crop types.

Key Insights:

Soil nutrients (N, P, K) show noticeable variation across crops

Certain crops are strongly associated with specific nutrient ranges

Weather parameters such as rainfall and humidity significantly influence crop suitability

Correlation analysis highlights relationships useful for crop recommendation models

Future Scope:

Implement machine learning models for crop prediction

Compare performance of classifiers (Random Forest, SVM, XGBoost, etc.)

Deploy the model as a web-based crop recommendation system

Integrate real-time weather and soil sensor data

👨‍💻 Author

Aditya Raj
M.Tech Student, IIT Kharagpur
Project Area: Agricultural Data Analysis | Python | Machine Learning

How to Run the Project:
pip install pandas numpy matplotlib seaborn scikit-learn
python main.py


Ensure the dataset path is correctly specified before execution.
