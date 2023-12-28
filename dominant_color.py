import cv2
import numpy as np


def create_bar(width, height, colors, text=True):
    bars = []

    for color in colors:
        print(color)
        color_bar = np.zeros((height, width, 3), np.uint8)
        red, green, blue = int(color[0]), int(color[1]), int(color[2])
        color_bar[:] = [blue, green, red]

        if text:
            color_bar = cv2.putText(color_bar, f"{red, green, blue}", (35, height // 2),
                                    cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 1, cv2.LINE_AA)

        bars.append(color_bar)

    bar = np.vstack(bars)

    return bar


img = cv2.imread('logo.webp')

data = img.reshape((-1, 3)).astype(np.float32)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
compactness, labels, centers = cv2.kmeans(data, 3, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

colors_num = 5
if len(centers) < colors_num:
    colors_num = len(centers)

bar = create_bar(200, 80, centers[:colors_num])

cv2.imshow('image', img)
cv2.imshow('bar', bar)

cv2.waitKey(0)
cv2.destroyAllWindows()