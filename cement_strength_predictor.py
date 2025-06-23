# cement_strength_predictor.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

# Load dataset
cement = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/Concrete%20Compressive%20Strength.csv')

# Features and target
y = cement['Concrete Compressive Strength(MPa, megapascals) ']
x = cement.drop(columns='Concrete Compressive Strength(MPa, megapascals) ')

# Display parameter ranges
parameter_ranges = x.describe().loc[['min', 'max']]

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=2)

# Train model
model = LinearRegression()
model.fit(x_train, y_train)

# Evaluate model
y_pred = model.predict(x_test)
print("\n📊 Model Evaluation:")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"MAPE: {mean_absolute_percentage_error(y_test, y_pred)*100:.2f}%")
print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")

# Predict for user input
def predict_strength():
    print("\n🏗️ Predict Cement Compressive Strength")
    try:
        user_input = []
        for column in x.columns:
            min_val = parameter_ranges.loc['min', column]
            max_val = parameter_ranges.loc['max', column]
            val = float(input(f"{column} (range: {min_val:.2f} – {max_val:.2f}): "))
            user_input.append(val)
        
        result = model.predict([user_input])
        print(f"\n🧾 Estimated Cement Strength: {result[0]:.2f} MPa")

    except Exception as e:
        print("⚠️ Invalid input:", e)

# Run
if __name__ == "__main__":
    predict_strength()
