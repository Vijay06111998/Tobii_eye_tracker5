import pandas as pd
import matplotlib.pyplot as plt

class DataAnalysis:
    def __init__(self, file_path='data/collected_eye_data.csv'):
        self.file_path = file_path
        self.data = pd.read_csv(self.file_path)

    def analyze_eye_data(self):
        """Analyze and plot eye tracking data."""
        eye_data = self.data[['timestamp', 'gaze_x', 'gaze_y']]
        plt.figure(figsize=(10, 5))
        plt.plot(eye_data['timestamp'], eye_data['gaze_x'], label='Gaze X')
        plt.plot(eye_data['timestamp'], eye_data['gaze_y'], label='Gaze Y')
        plt.title('Gaze Points Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Gaze Coordinates')
        plt.legend()
        plt.show()
