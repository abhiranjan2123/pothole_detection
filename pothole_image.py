
from ultralytics import YOLO
import cv2

model = YOLO('pothole.pt')
results = model("pothole_images/pot2.jpg", show=True)
cv2.waitKey(0)