import pandas as pd


def clean_numeric_column(row):
    clean = row.split()

    if len(clean) > 1:
        return int(clean[0])
    else:
        return 0


df = pd.read_csv("news.csv")

# Printing the data read
# print(df.sample(5))
# print(df.describe())

# Getting specific info
# columns = ["score", "comments"]
# print(df.loc[3: 5, columns])  # df.loc["As"]
# print(df[columns].loc[3: 5])  # Get the defined indexes based on index at the csv
# print(df.iloc[3: 5, [2, 4]])  # Get the defined indexes based on list position

# Get the column score, split each value and return the first element of the list as int
# example: 252 comments -> 252
# print(df.score.apply(clean_numeric_column))
# print(df.comments.apply(clean_numeric_column))
# df.date = df.date.apply(lambda x: x.replace("T", " "))  # Replace every row within a column where "T", setting " "

# print(df.date)
df.date = pd.to_datetime(df.date)  # Cast a column as a datetime (could be more data types)
print(df.date.value_counts())  # Count the instances of a value
