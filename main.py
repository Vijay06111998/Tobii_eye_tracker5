from utils.eye_tracker import EyeTracker
from utils.data_storage import DataStorage
from utils.data_analysis import DataAnalysis

def main():
    eye_tracker = EyeTracker()
    storage = DataStorage()
    
    # Collect data
    eye_data = eye_tracker.collect_eye_data()
    
    # Save collected data
    columns = ['timestamp', 'gaze_x', 'gaze_y']
    storage.save_data(eye_data, columns)

    # Analyze data
    analysis = DataAnalysis()
    analysis.analyze_eye_data()

if __name__ == "__main__":
    main()

