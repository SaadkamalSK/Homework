

#### Task 5 (Homework): Joins

# data1 = {
#     'ID': list(range(1, 21)),
#     'Name': ['Employee'+str(i) for i in range(1, 21)],
#     'Department': ['Sales', 'Marketing', 'HR', 'Sales', 'IT', 'Marketing', 'HR', 'IT', 'Sales', 'Marketing', 'HR', 'IT', 'Sales', 'Marketing', 'HR', 'IT', 'Sales', 'Marketing', 'HR', 'IT'],
#     'Start_Date': pd.date_range(start='01-01-2020', periods=20),
#     'Salary': [i*1000 for i in range(50, 70)]
#     }

#     # Creating DataFrame df2
# data2 = {
#     'Identifier': list(range(11, 31)),
#     'Role': ['Role'+str(i) for i in range(11, 31)],
#     'Years_of_Experience': [i for i in range(1, 21)]
#     }
# df2 = pd.DataFrame(data2)
# df1 = pd.DataFrame(data1)

##### 1. Write a line of code to perform an inner join of df1 and df2 on the ‘ID’ column. Note: The merge() function with how='inner' is useful for combining two DataFrames based on a common column, and only keeping rows that have matching values in both DataFrames.

# merged_data=pd.merge(df1, df2, left_on="ID", right_on='Identifier', how='inner')
# print(merged_data)


###### 2. Write a line of code to perform an outer join of df1 and df2 on the ‘ID’ column. Note: The merge() function with how='outer' is useful for combining two DataFrames based on a common column, and keeping all rows from both DataFrames.

# merged_data=pd.merge(df1, df2, left_on="ID", right_on='Identifier', how='outer')
# print(merged_data)

##### 4. Write a line of code to join df1 and df2 on their indices. Note: The join() function is useful for combining two DataFrames based on their indices.

# merged_data=pd.merge(df1, df2, left_index=True, right_index=True)
# print(merged_data)


##### 7. Write a line of code to join df1 and df2 on the ‘ID’ column, where ‘ID’ is the index in df1 and a regular column in df2. Note: The combination of the .set_index() function and the .join() function is useful when you want to join two DataFrames based on an index in one DataFrame and a regular column in another DataFrame.
# df1=df1.set_index("ID")
# merged_data=pd.merge(df1, df2, left_index=True, right_on="Identifier")
# print(merged_data)

##### 8. Write a line of code to join df1 and df2, where ‘ID’ is a regular column in both DataFrames, but treat it as an index only for the purpose of joining. Note: The combination of the .set_index(), .join(), and .reset_index() functions is useful when you want to join two DataFrames based on a common column, but don’t want this column to be the index in your resulting DataFrame.
# df1=df1.set_index("ID")
# merged_data=pd.merge(df1, df2, left_index=True, right_on="Identifier")
# df1=df1.reset_index("ID")
# print(merged_data)
