import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
import math
from word2number import w2n
import joblib

# PRACTICE ONE


# diabetes = datasets.load_diabetes()
# # diabetes_x = diabetes.data[:, np.newaxis, 2]
# diabetes_x = diabetes.data[:, np.newaxis, 2]
# diabetes_x_train = diabetes_x[:10]
# diabetes_x_test = diabetes_x[-5:]

# diabetes_y_train = diabetes.target[:10]
# diabetes_y_test = diabetes.target[-5:]

# model = linear_model.LinearRegression()
# model.fit(diabetes_x_train, diabetes_y_train)

# diabetes_y_predicet = model.predict(diabetes_x_test)

# print("mean squared", mean_squared_error(diabetes_y_test, diabetes_y_predicet))
# print(f"weight: {model.coef_}")
# print(f"intercept: {model.intercept_}")


# plt.scatter(diabetes_x_test, diabetes_y_test)
# plt.plot(diabetes_x_test, diabetes_y_predicet)
# plt.show()


# PRACTICE TWO


# df = pd.read_csv("E:\PureLogics\dataset_for_prac\house_prices.csv")
# df = df.interpolate()
# print(df)
# x_features = df[['area', 'bedrooms', 'age']]
# y_target = df['price']

# model = linear_model.LinearRegression()
# model.fit(x_features, y_target)

# print(f"Coeffiecient(m): {model.coef_}")
# print(f"Intercept(b): {model.intercept_}")

# predicted_price = model.predict([[3000, 3, 15]])
# print(predicted_price)

# val = 198.47159002*3000 + -116583.73881651 * \
#     3 + -14267.77585936*15 + 656046.539004866
# print(val)


# PRACTICE THREE

df = pd.read_csv("E:\PureLogics\dataset_for_prac\hiring.csv")
df.experience.fillna("zero", inplace=True)
df['experience'] = df['experience'].apply(w2n.word_to_num)
df.interpolate(inplace=True)
print(df)
model = linear_model.LinearRegression()
x = df[['experience', 'test_score(out of 10)',
        'interview_score(out of 10)']]
y = df['salary($)']

model.fit(x, y)

print(f"coeffecients: {model.coef_}")
print(f"intercept: {model.intercept_}")

# predicted_price = math.floor(model.predict([[11, 7, 8]]))
# print(f"Predicted price: {predicted_price}")

joblib.dump(model, "linear_regression_interview_model.pkl")
md = joblib.load("linear_regression_interview_model.pkl")

predicted_price = md.predict([[11, 7, 7]])
print(f"Predicted price: {predicted_price}")
