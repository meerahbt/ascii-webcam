import cv2

class VideoHandler:
    def __init__(self):
        self.cap = None

    def start_capture(self, device_id=0):
        """Initialize video capture"""
        self.cap = cv2.VideoCapture(device_id)
        return self.cap.isOpened()

    def read_frame(self):
        """Read a frame from the video capture"""
        if self.cap is None:
            return False, None
        return self.cap.read()

    def release(self):
        """Release the video capture"""
        if self.cap is not None:
            self.cap.release()
            cv2.destroyAllWindows()