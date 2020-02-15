import cv2
import imutils

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


def start():
    video = cv2.VideoCapture(0)

    while True:
        _, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (25, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
        canny = cv2.Canny(thresh, 130, 255, 1)
        display_image = thresh

        #cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        if len(cnts) == 2 or len(cnts) == 3:
            contours = imutils.grab_contours(cnts)
            shape = detect(contours)
            if shape != 'unknown':
                bgr = calculate_center_bgr(frame, contours)
                # TODO: send as http request to LED
                print(bgr)

        for c in cnts:
            cv2.drawContours(display_image, [c], 0, (0, 255, 0), 3)

        cv2.imshow("result", display_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start()
