
from utils.eye_tracker import EyeTracker
from utils.data_storage import DataStorage
from utils.data_analysis import DataAnalysis
import pandas as pd 

def main():
    # Create instances of the classes
    eye_tracker = EyeTracker()
    storage = DataStorage(excel_file='data/collected_eye_data.xlsx')  # Ensure the correct path for Excel file
    analysis = DataAnalysis()

    # Define the columns for saving data
    columns = ['timestamp', 'gaze_x', 'gaze_y']

    # Suppose 'collected_data' is your list of eye-tracking data
    collected_data = [
        [0.1, 0.5, 0.7],
        [0.2, 0.55, 0.75],
        [0.3, 0.6, 0.8],
        [0.4, 0.65, 0.85]
    ]
    
    # Create a DataFrame from the collected data
    collected_df = pd.DataFrame(collected_data, columns=columns)

    # Save the data to a CSV file (if needed)
    csv_file_path = 'data/collected_eye_data.csv'
    collected_df.to_csv(csv_file_path, index=False)
    
    # Save the collected data to the Excel file (this method now appends data)
    storage.save_data(collected_data, columns)

    print(f"Data saved to {csv_file_path} and {storage.excel_file}")

    # Visualize the collected data
    analysis.visualize_data()

    # Define the reference data for comparison
    reference_data = [
        [0.1, 0.52, 0.72],
        [0.2, 0.54, 0.74],
        [0.3, 0.58, 0.78],
        [0.4, 0.60, 0.80]
    ]

    # Convert reference_data to a DataFrame for comparison if required by the method
    reference_df = pd.DataFrame(reference_data, columns=columns)

    # Compare collected data with the reference data
    analysis.compare_with_reference(reference_df)

if __name__ == "__main__":
    main()
