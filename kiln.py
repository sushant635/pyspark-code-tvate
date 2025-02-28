import pandas as pd 


# File path to the Excel file
file_path = "DATA (1).xlsx"

# Read all sheets into a dictionary of DataFrames
dfs = pd.read_excel(file_path, sheet_name=None)

print(dfs)

# Access a specific sheet (Example: "Sheet1")
df_sheet1 = dfs["Limestone pile"]

print(df_sheet1)