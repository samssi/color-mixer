import cv2
import imutils

width_height = (576, 1024)


def calculate_center_bgr(image, cnts):
    M = cv2.moments(imutils.grab_contours(cnts))

    # TODO: add null check
    # if M["m00"]:
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    return image[cY, cX]


def start():
    image = cv2.imread('red_768_432.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 130, 255, 1)

    cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    bgr = calculate_center_bgr(image, cnts)

    # TODO: send as http request to LED
    print(bgr)

    for c in cnts:
        cv2.drawContours(image, [c], 0, (0, 255, 0), 3)

    cv2.imshow("result", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    start()
