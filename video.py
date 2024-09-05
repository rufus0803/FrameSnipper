import cv2

def record_video(output_file='300.mp4'):

    cap = cv2.VideoCapture(0)
    

    if not cap.isOpened():
        print("Error: Could not open video device.")
        return


    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (frame_width, frame_height))

    print("Recording... Press 'q' to stop.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break
        

        out.write(frame)
        

        cv2.imshow('Recording', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved as {output_file}")

if __name__ == "__main__":
    record_video()

