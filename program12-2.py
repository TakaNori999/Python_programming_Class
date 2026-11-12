import cv2

src = cv2.imread("building.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(src)
b = cv2.add(b, 100)
enhanced_image = cv2.merge((b, g, r))
cv2.namedWindow("Sorce")
cv2.imshow("Sorce", enhanced_image)
cv2.imwrite("program12-2.jpg", enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
