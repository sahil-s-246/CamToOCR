import os
import cv2
import matplotlib.pyplot as plt


class Image:
    def __init__(self):
        # Create the images directory if it doesn't exist
        if not os.path.exists("images"):
            os.makedirs("images")
            self.frame = []

    def get_cam_img(self):
        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        # Capture a frame from the webcam
        ret, self.frame = cap.read()

        # Save the captured frame as a JPEG file in the images directory
        cv2.imwrite("images/example.jpg", self.frame)

        # Convert BGR to RGB
        img = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

        # Display image using pyplot
        plt.xticks([]), plt.yticks([])
        plt.imshow(img)
        plt.show()

        # Release the webcam and destroy all windows
        cap.release()
        plt.close('all')
