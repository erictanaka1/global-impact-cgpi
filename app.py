import numpy as np
import cv2

def center(x, y, w, h):
  x1 = int(w / 2)
  y1 = int(h / 2)
  cx = x + x1
  cy = y + y1
  return cx,cy

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

# COR 1
colorLower = np.array([10, 50, 50], dtype="uint8")
colorUpper = np.array([70, 255, 255], dtype="uint8")

while True:
	# Leitura do frame
	# ret, frame = cap.read()
	frame = cv2.imread("imagem-teste1.jpg")

	# Converte para HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Mascara Azul
	maskColor = cv2.inRange(hsv, colorLower, colorUpper)
	maskColor = cv2.erode(maskColor, None, iterations=2)
	maskColor = cv2.dilate(maskColor, None, iterations=2)

	contours, hierarchy = cv2.findContours(maskColor,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	i = 0
	for cnt in contours:
		(x,y,w,h) = cv2.boundingRect(cnt)

		area = cv2.contourArea(cnt)
		
		if int(area) > 100 :
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

	cv2.imshow("Global Impact", frame)

	if cv2.waitKey(30) & 0xFF == ord('q'):
		break

# cap.release()
cv2.destroyAllWindows()