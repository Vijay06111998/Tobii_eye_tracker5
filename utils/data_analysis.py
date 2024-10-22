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
        
    def plot_trend(self, x, y, label):
        """Plot trend line with data points."""
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        trend_line = slope * x + intercept

        plt.figure(figsize=(10, 5))
        plt.scatter(x, y, label=label, alpha=0.5, color='blue')
        plt.plot(x, trend_line, color='red', label='Trend Line')
        plt.title(f'Trend Analysis of {label}')
        plt.xlabel('Time (s)')
        plt.ylabel('Gaze Coordinates')
        plt.legend()
        plt.grid()
        plt.show()

        print(f"Slope: {slope}, Intercept: {intercept}, R-squared: {r_value**2}")
    
    def compare_with_reference(self, reference_data):
        """Compare collected eye data with a reference."""
        reference_df = pd.DataFrame(reference_data, columns=['timestamp', 'gaze_x', 'gaze_y'])
        comparison = self.data[['gaze_x', 'gaze_y']].subtract(reference_df[['gaze_x', 'gaze_y']], axis=0)
        comparison.plot(title='Difference between recorded and reference gaze data')
        plt.xlabel('Sample Index')
        plt.ylabel('Difference in Gaze Coordinates')
        plt.show()


