import pandas as pd
import os
from tabulate import tabulate
from termcolor import colored

def compare_files(file_path1, file_path2):

    print(file_path1, file_path2)
    df1 = pd.read_csv(file_path1, delimiter='|', dtype=str, keep_default_na=False, na_values=[])
    df2 = pd.read_csv(file_path2, delimiter='|', dtype=str, keep_default_na=False, na_values=[])

    # Compare columns
    different_columns = set(df1.columns).symmetric_difference(set(df2.columns))
    # Compare number of records
    record_diff = abs(len(df1) - len(df2))

    return different_columns, record_diff

def sort_and_compare(folder_path1, folder_path2):
    files1 = set(f for f in os.listdir(folder_path1) if f.endswith('.csv') and '-sorted' not in f)
    files2 = set(f for f in os.listdir(folder_path2) if f.endswith('.csv') and '-sorted' not in f)

    common_files = files1.intersection(files2)
    all_details = []

    for file in common_files:
        file_path1 = os.path.join(folder_path1, file)
        file_path2 = os.path.join(folder_path2, file)

        # Compare files
        different_columns, record_diff = compare_files(file_path1, file_path2)

        # Process files individually
        for folder_path in [folder_path1, folder_path2]:
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path, delimiter='|', dtype=str, keep_default_na=False, na_values=[])
            rows, cols = df.shape
            sorted_df = df.sort_values(by=list(df.columns))
            sorted_file_path = os.path.join(folder_path, file.split('.csv')[0] + '-sorted.csv')
            sorted_df.to_csv(sorted_file_path, index=False, sep='|')

            # Add file details to the all_details list
            all_details.append([
                f'{folder_path}/{file}',
                rows,
                cols,
                ', '.join(different_columns) if different_columns else 'None',
                record_diff
            ])

    # Print combined table
    print(tabulate(all_details, headers=["File Path", "Number of Rows", "Number of Columns", "Different Columns", "Record Difference"], tablefmt="grid"))

# Paths to the folders
ADF = 'files/ADF/reconreport/generaldetail'
DataStage = 'files/DataStage/reconreport/generaldetail'

# Process and compare
sort_and_compare(ADF, DataStage)