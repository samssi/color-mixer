import cv2


def start():
    video = cv2.VideoCapture(0)
    frame_nbr = 0
    while True:
        frame_nbr = frame_nbr + 1

        _, frame = video.read()
        overlay_frame = frame.copy()

        height, width = frame.shape[:2]
        sample_x = int(width / 2)
        sample_y = int(height / 2)

        color = (0, 255, 0)
        cv2.circle(overlay_frame, (sample_x, sample_y), 10, color, -1)

        if frame_nbr == 20:
            frame_nbr = 0
            print(frame[sample_y, sample_x])

        cv2.imshow("result", overlay_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start()
