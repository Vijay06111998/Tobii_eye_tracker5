import pandas as pd
import matplotlib.pyplot as plt
import os

class DataAnalysis:
    def __init__(self, file_path="data/collected_eye_data.csv"):
        """Initialize the DataAnalysis class and load the data."""
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """Load data from CSV file if it exists, otherwise return an empty DataFrame."""
        if os.path.exists(self.file_path):
            df = pd.read_csv(self.file_path)
            if df.empty:
                print("Warning: The collected data file is empty.")
            return df
        else:
            print(f"File not found: {self.file_path}")
            return pd.DataFrame()

    def visualize_data(self):
        """Plot gaze position over time."""
        if self.data.empty:
            print("No data available for visualization.")
            return

        plt.figure(figsize=(10, 5))
        plt.plot(self.data['timestamp'], self.data['gaze_x'], label='Gaze X', color='blue')
        plt.plot(self.data['timestamp'], self.data['gaze_y'], label='Gaze Y', color='red')

        plt.title('Eye Tracking Data Visualization')
        plt.xlabel('Timestamp')
        plt.ylabel('Gaze Position')
        plt.legend()
        plt.grid()
        plt.show()

    def compare_with_reference(self, reference_df):
        """Compare collected eye-tracking data with a reference dataset."""
        if self.data.empty:
            print("No collected data available for comparison.")
            return
        
        if reference_df.empty:
            print("Reference dataset is empty. Cannot compare.")
            return
        
        # Ensure both datasets have the same columns
        common_cols = ['timestamp', 'gaze_x', 'gaze_y']
        if not all(col in self.data.columns for col in common_cols) or not all(col in reference_df.columns for col in common_cols):
            print("Reference dataset does not have the required columns for comparison.")
            return

        # Merge the collected data and reference data on 'timestamp'
        merged_data = self.data.merge(reference_df, on='timestamp', suffixes=('_collected', '_reference'))
        
        # Plot comparison
        plt.figure(figsize=(10, 5))
        plt.plot(merged_data['timestamp'], merged_data['gaze_x_collected'], label='Collected Gaze X', color='blue')
        plt.plot(merged_data['timestamp'], merged_data['gaze_x_reference'], label='Reference Gaze X', linestyle='dashed', color='lightblue')
        
        plt.plot(merged_data['timestamp'], merged_data['gaze_y_collected'], label='Collected Gaze Y', color='orange')
        plt.plot(merged_data['timestamp'], merged_data['gaze_y_reference'], label='Reference Gaze Y', linestyle='dashed', color='lightcoral')

        plt.title('Comparison of Collected vs. Reference Eye Tracking Data')
        plt.xlabel('Timestamp')
        plt.ylabel('Gaze Coordinates')
        plt.legend()
        plt.grid()
        plt.show()
