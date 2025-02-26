import pandas as pd

file_path = "calendario.xlsx"

# dataframe
df = pd.read_excel(file_path)

#check for my lessons
matches = df.isin(["Paolo"])

for row_idx, col_idx in zip(*matches.to_numpy().nonzero()):
    print(f'Found Paolo at row {row_idx} and column {col_idx}')
    hours = df.iloc[row_idx, 0]
    subject = df.iloc[row_idx, col_idx - 1]  
    print(hours)
    print(subject)

    day = df.iloc[row_idx + 7 - int(hours.split(".")[0]), col_idx - 1]

    print(day)