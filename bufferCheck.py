import cv2


cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


buffer_size = cap.get(cv2.CAP_PROP_BUFFERSIZE)
print(f"Buffer size: {buffer_size}")

cap.release()
