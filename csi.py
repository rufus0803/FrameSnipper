import cv2

def main():

    cap = cv2.VideoCapture(0)  


    if not cap.isOpened():
        print("无法打开摄像头")
        return


    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter('csi.mp4', fourcc, 20.0, (640, 480)) 

    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法接收帧，可能是摄像头断开连接")
            break

   
        out.write(frame)

        cv2.imshow('Frame', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    out.release()
    cv2.destroyAllWindows()

