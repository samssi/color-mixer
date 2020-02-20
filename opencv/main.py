import cv2
import requests

led_url = 'http://192.168.10.43:5000/color'


def create_rgb_json(r=0, g=0, b=0):
    return {"r": r, "g": g, "b": b}


def rgb_json(r, g, b):
    if r < 50 and g < 50 and b < 50:
        return create_rgb_json()
    elif b < r > g:
        return create_rgb_json(r=200)
    elif r < g > b:
        return create_rgb_json(g=200)
    elif r < b > g:
        return create_rgb_json(b=200)
    else:
        return create_rgb_json(200, 200, 200)


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
            json = rgb_json(r, g, b)

            try:
                requests.post(led_url, json=json, timeout=0.1)
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
