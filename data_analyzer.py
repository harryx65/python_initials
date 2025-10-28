import pandas as pd

print("Welcome to HarryDatalyzer")
file_path = input("\n Enter Your File Path with Name: ")
data = pd.read_csv(file_path)
# print(data)

# E:\PureLogics\dataset_for_prac\sales_data.csv

print("\n Choose an option")
print("1. View first 5 rows")
print("2. View dataset info")
print("3. Check missing values")
print("4. Fill missing values")
print("5. Drop missing values")
print("6. Sort data")
print("8. Save cleaned data")
print("0. Exit")

choice = int(input("\n Enter your Choice: "))

if choice == 1:
    print(data.head())
elif choice == 2:
    print(data.info())
elif choice == 3:
    print(data.isnull().sum())
elif choice == 4:
    col = input("inter column name to fill: ")
    val = input("input value to fill: ")
    print(data[col].fillna(value=val))
elif choice == 5:
    print(data.dropna())
elif choice == 6:
    col = input("Enter COlumn to sort by: ")
    asc = input("Accending? (y/n): ").lower() == 'y'
    print(data.sort_values(by=col, ascending=asc))
