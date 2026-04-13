Sales Prediction and Analysis using Machine Learning

Project Overview

This project focuses on analyzing sales data and building a predictive model using Linear Regression. It integrates data processing, SQL-based analysis, visualization, and machine learning to generate meaningful business insights.

The project follows an end-to-end workflow including data cleaning, feature engineering, exploratory data analysis (EDA), and predictive modeling.

Objectives

- Analyze historical sales data  
- Identify top-performing products and monthly trends  
- Store and query data using MySQL  
- Build a Linear Regression model for sales prediction  
- Generate actionable business insights  

Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- MySQL  

Project Structure

sales_prediction_project/
sales_prediction_project/
| |— data/ | — amazon_sales_data.csv | — src/ | — main.py | — output/ | — sales_trend.png | — README.md  

Workflow

1. Data Collection  
Dataset includes sales, date, product, and region.

2. Data Loading  
Data is loaded using Pandas.

3. Data Cleaning  
- Handle missing values  
- Fix incorrect date formats  
- Convert numeric columns  

4. Feature Engineering  
Extract Month and Year from the Date column.

5. Database Integration  
Store cleaned data in MySQL and perform SQL queries for analysis.

6. Exploratory Data Analysis (EDA)  
- Monthly sales trend  
- Top-performing products  

7. Statistical Analysis  
- Mean sales calculation  
- Sales growth rate  

8. Data Visualization  
- Line chart for monthly sales trend  
- Saved in output folder  

9. Feature Selection  
Selected features include Month, Product, and Region.

10. Model Building  
Linear Regression model is applied to the dataset.

11. Prediction  
Future sales values are predicted using the trained model.

12. Insights  
- Best performing month identified  
- Peak sales value calculated  

Sample Output

- Total Sales Calculation  
- Top Products using SQL  
- Monthly Sales using SQL  
- Model Performance:
  MAE (Mean Absolute Error)  
  R² Score  
- Sales Prediction  
- Best Month and Peak Sales  

How to Run the Project

Step 1: Clone Repository  
git clone https://github.com/mariyaroseline/sales-prediction-ml.git
cd sales_prediction_project  

Step 2: Install Dependencies  
pip install -r requirements.txt  

Step 3: Setup MySQL  

Create database:  
CREATE DATABASE sales_project;

Update credentials in main.py:  
host="localhost"  
user="root"  
password="your_password"  

Step 4: Run the Project  
python src/main.py  

Key Results

- Identified top-selling products  
- Analyzed monthly sales trends  
- Built a regression model with good accuracy  
- Generated future sales predictions  
- Derived business insights for decision making  

Future Enhancements

- Build an interactive dashboard using Streamlit or Power BI  
- Deploy the model as a web application  
- Add advanced models such as Random Forest or XGBoost  
- Improve feature engineering for better accuracy  

Conclusion

This project demonstrates a complete data analysis and machine learning pipeline. It showcases practical skills in data preprocessing, SQL integration, visualization, and predictive modeling suitable for real-world applications.
