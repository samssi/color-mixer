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
        overlay_frame = cv2.flip(frame, 1)

        height, width = frame.shape[:2]
        sample_x = int(width / 2)
        sample_y = int(height / 2)

        color = (0, 255, 0)
        cv2.circle(overlay_frame, (sample_x, sample_y), 10, color, -1)

        if frame_nbr == 20:
            frame_nbr = 0
            b, g, r = frame[sample_y, sample_x]

            if r < 50 and g < 50 and b < 50:
                r_out = 0
                g_out = 0
                b_out = 0
            elif b < r > g:
                r_out = 200
                g_out = 0
                b_out = 0
            elif r < g > b:
                r_out = 0
                g_out = 200
                b_out = 0
            elif r < b > g:
                r_out = 0
                g_out = 0
                b_out = 200

            try:
                requests.post(led_url,
                              json={"r": r_out,
                                    "g": g_out,
                                    "b": b_out}, timeout=0.1)
                print(f'Posted rgb [{r} {g} {b}]')

            except (ValueError, Exception):
                print(f'Failed to post rgb [{r} {g} {b}]')

        cv2.imshow("result", overlay_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start()
