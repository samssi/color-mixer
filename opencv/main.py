import cv2

width_height = (576, 1024)


def start():
    image = cv2.imread('red_768_432.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 130, 255, 1)

    cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        cv2.drawContours(image, [c], 0, (0, 255, 0), 3)

    cv2.imshow("result", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    start()
