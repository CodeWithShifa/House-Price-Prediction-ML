import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Data load karein
df = pd.read_csv('house_prices.csv')

# 2. Sahi column names select karein (Jo humne terminal mein dekhe)
X = df[['Size_sqft']] 
y = df['Price']

# 3. Model train karein
model = LinearRegression()
model.fit(X, y)

# 4. Check karein ke 2000 sq ft ke ghar ki price kya hogi
prediction = model.predict([[2000]])
print(f"2000 sq ft ghar ki predicted price hai: {prediction[0]}")