import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# LOAD DATA
df = pd.read_csv("data/amazon_sales_data .csv")


# DATA CLEANING

# Standardize column names
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Convert date column
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')

# Convert numeric columns
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

# Remove missing values
df = df.dropna()


# FEATURE ENGINEERING

# Extract month and year
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year


# MYSQL CONNECTION

# Establish database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",   
    database="sales_db"
)

cursor = conn.cursor()

# CREATE TABLE


cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_data (
    Order_ID VARCHAR(20),
    Date DATE,
    Product VARCHAR(100),
    Category VARCHAR(50),
    Price FLOAT,
    Quantity INT,
    Sales FLOAT,
    Customer_Name VARCHAR(100),
    Region VARCHAR(50),
    Payment_Method VARCHAR(50),
    Status VARCHAR(50)
)
""")


# INSERT DATA INTO MYSQL

for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO sales_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row[['Order_ID','Date','Product','Category','Price',
                    'Quantity','Sales','Customer_Name','Region',
                    'Payment_Method','Status']]))

conn.commit()


# SQL ANALYSIS

# Total sales
cursor.execute("SELECT SUM(Sales) FROM sales_data")
print("Total Sales:", cursor.fetchone()[0])

# Top 5 products
cursor.execute("""
SELECT Product, SUM(Sales) 
FROM sales_data 
GROUP BY Product 
ORDER BY SUM(Sales) DESC 
LIMIT 5
""")

print("\nTop Products (SQL):")
for row in cursor.fetchall():
    print(row)

# Monthly sales
cursor.execute("""
SELECT MONTH(Date), SUM(Sales) 
FROM sales_data 
GROUP BY MONTH(Date)
""")

print("\nMonthly Sales (SQL):")
for row in cursor.fetchall():
    print(row)


# EXPLORATORY DATA ANALYSIS (EDA)

monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(kind='line', marker='o', figsize=(10,5))
plt.title("Monthly Sales Trend")

# Save visualization
plt.savefig("output/sales_trend.png")

plt.show()


# MACHINE LEARNING

# Encode categorical variables
df_encoded = pd.get_dummies(df, columns=['Product', 'Region'], drop_first=True)

# Define features and target
X = df_encoded.drop(['Sales','Date','Order_ID','Customer_Name',
                     'Category','Payment_Method','Status'], axis=1)

y = df_encoded['Sales']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate model
print("\nMAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


# SAMPLE PREDICTION

future_sales = model.predict(X_test.iloc[0:1])
print("\nSample Prediction:", future_sales)


# BUSINESS INSIGHTS

best_month = monthly_sales.idxmax()
peak_sales = monthly_sales.max()

print("\nBest Month:", best_month)
print("Peak Sales:", peak_sales)


# CLOSE CONNECTION

conn.close()