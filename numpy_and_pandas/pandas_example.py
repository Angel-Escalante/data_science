import pandas as pd

data = {
    "name": ["Maria", "Luis", "Carmen", "Miguel"],
    "age": [23, 24, 23, 24],
    "degree": ["LI", "LIN", "LIN", "LI"]
}
df_data = pd.DataFrame(data)

"""
DataFrame methods
"""
# print(df_data.head(2))  # Get the first x rows, 5 by default
# print(df_data.tail(2))  # Get the last x rows, 5 by default
# print(df_data.sample())  # Get x random rows, 1 by default
# print(df_data.info())  # Get all columns, their non-null elements and their data type
# print(df_data.describe())  # Get all numeric columns (if none, it will use the text columns) and fast stats about them
print(df_data.set_index("name"))  # Set the index of all rows as the desired column, returns a DataFrame

"""
DataFrame properties
"""
# print(df_data.shape)  # Get the rows count and the columns count
# print(df_data.size)  # Get data count (rows * columns)
# print(df_data.columns)  # Get the column names
# print(df_data.dtypes)  # Get the data type of each column
# print(df_data.index)  # Get the indexes of all data; on default, will return the RangeIndex object used to create them
