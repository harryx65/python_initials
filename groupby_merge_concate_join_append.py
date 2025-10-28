import pandas as pd

df = pd.DataFrame({
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance', 'HR'],
    'Employee': ['Ali', 'Sara', 'Hassan', 'John', 'Ayesha', 'Zara', 'Ahmed'],
    'Salary': [50000, 80000, 52000, 85000, 75000, 78000, 51000]
})
# print(df)

departement_Avrg_salary = df.groupby("Department")["Salary"].sum()
departement_recourse = df.groupby("Department")["Salary"].count()

# print(departement_Avrg_salary)
# print(departement_recourse)

agg = df.groupby("Department")["Salary"].agg(['mean', 'max', 'min'])
# print(agg)


# Merge

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Ali', 'Sara', 'Hassan']
})


df2 = pd.DataFrame({
    'Emp_ID': [2, 3, 4],
    'Salary': [60000, 70000, 80000]
})

# print(pd.merge(df1, df2))
# print(pd.merge(df1, df2, how="outer"))
# print(pd.merge(df1, df2, left_on='ID', right_on='Emp_ID', how='inner'))


# Concate
df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})

df2 = pd.DataFrame({
    'B': [5, 6],
    'C': [7, 8]
})
df4 = pd.concat([df1, df2], ignore_index=True)
print(df4)


# Join

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Ali', 'Sara', 'Hassan']
})


df2 = pd.DataFrame({
    'Emp_ID': [2, 3, 4],
    'Salary': [60000, 70000, 80000]
})

df4 = df1.join(df2)
# print(df4)


#  concat() → “Just stick these DataFrames together.”

#  merge() → “Match rows based on a shared key.”

#  join() → “Attach using index or one key column.”
