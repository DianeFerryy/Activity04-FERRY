import cv2
filePath = 'yang.jpg'
wTitle = 'Ferry'
rImage = cv2.imread(filePath, 1)
cv2.imshow(wTitle, rImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
