import tobii_research as tr
import time

class EyeTracker:
    def __init__(self):
        self.tracker = None
        self.setup_tracker()

    def setup_tracker(self):
        found_eyetrackers = tr.find_all_eyetrackers()
        if found_eyetrackers:
            self.tracker = found_eyetrackers[0]
            print(f"Using Tobii Eye Tracker: {self.tracker.model}")
            print(f"Address: {self.tracker.address}")
            
            time.sleep(10)
        else:
            raise Exception("No Tobii Eye Tracker found")
    time.sleep(10)

    def collect_eye_data(self):
        """Collect real-time eye tracking data and return it."""
        if not self.tracker:
            raise Exception("Eye Tracker is not set up.")
        
        gaze_data = []
        start_time = time.time()
        
        def gaze_callback(gaze_sample):
            timestamp = time.time() - start_time
            gaze_point = gaze_sample['left_gaze_point_on_display_area']
            gaze_data.append([timestamp, gaze_point[0], gaze_point[1]])

        self.tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_callback, as_dictionary=True)
        
        print("Collecting eye tracking data...")
        time.sleep(30)
        
        self.tracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_callback)
        print("Data collection complete.")
        
        return gaze_data