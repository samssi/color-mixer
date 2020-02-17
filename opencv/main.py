import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt

width_height = (576, 1024)


def calculate_center_bgr(image, cnts):
    M = cv2.moments(cnts)

    # TODO: add null check
    # if M["m00"]:
    if M["m00"] > 0:
        cX = int((M["m10"] / M["m00"]))
        cY = int((M["m01"] / M["m00"]))

        return image[cY, cX]

    return None


def detect(contour):
    shape = "unidentified"
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * peri, True)

    if len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx);
        ar = w / float(h)
        shape = "square" if 1.05 >= ar >= 0.95 else "rectangle"
        print(shape)

    return shape


def draw_contours(image, cnts):
    for c in cnts:
        cv2.drawContours(image, [c], 0, (0, 255, 0), 3)


def find_countours(image):
    cnts = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return cnts[0] if len(cnts) == 2 else cnts[1]

# https://stackoverflow.com/questions/2068013/finding-location-of-rectangles-in-an-image-with-opencv

def start():
    video = cv2.VideoCapture(0)

    while True:
        _, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (25, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
        display_image = frame

        #cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = find_countours(thresh)

        if len(cnts) == 2 or len(cnts) == 3:
            contours = imutils.grab_contours(cnts)
            shape = detect(contours)
            if shape != 'unknown':
                bgr = calculate_center_bgr(frame, contours)
                # TODO: send as http request to LED
                print(bgr)

        draw_contours(display_image, cnts)
        cv2.imshow("result", display_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def start2():
    video = cv2.VideoCapture(0)

    while True:
        _, image = video.read()

        blur = cv2.pyrMeanShiftFiltering(image, 11, 21)
        gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.015 * peri, True)

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(image, (x, y), (x+w, y+h), (36, 255, 12), 2)

        #cv2.imshow('thresh', thresh)
        cv2.imshow('image', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def start3():
    video = cv2.VideoCapture(0)

    while True:
        _, image = video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray, 130, 255, 1)

        cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        for c in cnts:
            cv2.drawContours(image, [c], 0, (0, 255, 0), 3)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

def start4():
    video = cv2.VideoCapture(0)

    while True:
        _, image = video.read()
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        template = cv2.imread('template-jack-diamonds_300_429.png', 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.5
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        cv2.imshow("result", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def start5():
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
    start5()
