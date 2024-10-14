import pandas as pd

class DataStorage:
    def __init__(self, file_path='data/collected_eye_data.csv'):
        self.file_path = file_path

    def save_data(self, data, columns):
        """Save collected data to a CSV file."""
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(self.file_path, index=False)
        print(f"Data saved to {self.file_path}")
