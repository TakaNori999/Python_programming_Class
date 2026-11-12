import cv2
src = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)
ret, bin = cv2.threshold(src, 100, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("binary", bin)
cv2.waitKey(0)
cv2.destroyAllWindows()