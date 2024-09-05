import cv2

filename = "/home/usslab/python/test_fps1.mp4"
video  = cv2.VideoCapture(filename)
print(video.get(cv2.CAP_PROP_FPS))
