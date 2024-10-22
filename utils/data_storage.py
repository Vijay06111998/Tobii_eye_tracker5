# import pandas as pd

# class DataStorage:
#     def __init__(self, file_path='data/collected_eye_data.csv'):
#         self.file_path = file_path

#     def save_data(self, data, columns):
#         """Save collected data to a CSV file."""
#         df = pd.DataFrame(data, columns=columns)
#         df.to_csv(self.file_path, index=False)
#         print(f"Data saved to {self.file_path}")


import pandas as pd

class DataStorage:
    def __init__(self, file_path='data/collected_eye_data.csv'):
        self.file_path = file_path

    def save_data(self, data, columns):
        """Save the collected data to both CSV and Excel files."""
        collected_df = pd.DataFrame(data, columns=columns)
        
        # Save as CSV
        csv_file_path = self.file_path
        collected_df.to_csv(csv_file_path, index=False)
        print(f"Data saved to CSV: {csv_file_path}")

        # Save as Excel
        excel_file_path = csv_file_path.replace('.csv', '.xlsx')
        collected_df.to_excel(excel_file_path, index=False)
        print(f"Data saved to Excel: {excel_file_path}")

        return csv_file_path, excel_file_path





