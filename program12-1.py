import cv2
src = cv2.imread("sample.jpg", cv2.IMREAD_COLOR)
src[330:420, 150:340, :] = [255, 0, 0]
cv2.imshow("Sorce", src)
cv2.imwrite("program12-1.jpg", src)
cv2.waitKey(0)
cv2.destroyAllWindows()