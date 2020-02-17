import cv2
import numpy
import requests

led_url = 'http://192.168.1.129:5000/color'


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
            b, g, r = frame[sample_y, sample_x]

            try:
                requests.post(led_url,
                              json={"r": numpy.int(r),
                                    "g": numpy.int(g),
                                    "b": numpy.int(b)}, timeout=0.1)
            except (ValueError, Exception):
                print(f'Failed to post rgb [{r} {g} {b}]')

        cv2.imshow("result", overlay_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start()
