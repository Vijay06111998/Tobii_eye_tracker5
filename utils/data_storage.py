import pandas as pd
import os

class DataStorage:
    def __init__(self, excel_file='data/collected_eye_data.xlsx'):
        self.excel_file = excel_file

    def save_data(self, collected_data, columns):
        # Create DataFrame from collected data
        collected_df = pd.DataFrame(collected_data, columns=columns)

        # Check if the Excel file exists
        if os.path.exists(self.excel_file):
            # Append new data to the existing Excel file
            with pd.ExcelWriter(self.excel_file, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                collected_df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row, sheet_name='Sheet1')
        else:
            # Create a new Excel file and write the DataFrame with headers
            with pd.ExcelWriter(self.excel_file, engine='openpyxl') as writer:
                collected_df.to_excel(writer, index=False, header=True, sheet_name='Sheet1')

        print(f"Data saved to Excel: {self.excel_file}")
