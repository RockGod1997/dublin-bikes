import pandas as pd
import glob

# Specify the path to the directory containing dublin bikes CSV files 2018 Q3 to 2021 Q4
csv_files_path = 'dataset/*.csv'

# Get a list of all CSV files in the specified directory
csv_files = glob.glob(csv_files_path)

# Initialize an empty list to store individual DataFrames
dfs = []

# Iterate through each CSV file, read it into a DataFrame, and append to the list
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

output_csv_path = 'merged_data.csv'
merged_df.to_csv(output_csv_path, index=False)
