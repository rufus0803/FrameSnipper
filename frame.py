import cv2
import time

cap = cv2.VideoCapture(1)

if not cap.isOpened():
	print("cannot open camera")
	exit()

expected_fps = 30

start_time = time.time()

frame_count = 0

timestamps = []

while True:
	ret, frame = cap.read()
	if not ret:
		break

	timestamps.append(time.time())
	frame_count += 1

	cv2.imshow("frame", frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

end_time = time.time()

actual_fps = frame_count / (end_time - start_time)

expected_frame_count = (end_time - start_time) * expected_fps

dropped_frames = expected_frame_count - frame_count

print(f"Expected FPS:{expected_fps}")
print(f"Actual FPS:{actual_fps}")
print(f"Captured frames:{frame_count}")
print(f"Expected frames:{expected_frame_count}")
print(f"Dropped frames:{dropped_frames}")

cap.release()
cv2.destroyAllWindows()
