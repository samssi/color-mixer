import cv2
import imutils

width_height = (576, 1024)


def detect(contour):
    shape = "unidentified"
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
    print(approx)

    if len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx);
        ar = w / float(h)

        shape = "square" if 1.05 >= ar >= 0.95 else "rectangle"

    return shape


def compute_contours(image, contours):
    for c in contours:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        M = cv2.moments(c)
        #cX = int((M["m10"] / M["m00"]))
        #cY = int((M["m01"] / M["m00"]))
        shape = detect(c)
        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c = c.astype("int")
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        #cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
        #    0.5, (255, 255, 255), 2)


def start3():
    image = cv2.imread('red_768_432.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 130, 255, 1)

    cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        cv2.drawContours(image, [c], 0, (0, 255, 0), 3)

    cv2.imshow("result", image)
    cv2.waitKey(0)


def start2():
    image = cv2.imread('red_768_432.jpg')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    #thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

    displayed_image = image

    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    compute_contours(displayed_image, contours)
    cv2.imshow('result', displayed_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def start():
    image = cv2.imread('red.jpg')
    resized = cv2.resize(image, width_height)
    cv2.imshow('result', resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start3()
