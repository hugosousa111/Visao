import cv2

captura = cv2.VideoCapture("video.mp4")
frames = captura.get(cv2.CAP_PROP_FRAME_COUNT) #numero de frames, 510
print frames

#w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#fps = int(cap.get(cv2.CAP_PROP_FPS))
#n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#print captura.get(1) 

a = 0
while a < frames: #True, apaguei pq falha no ultimo
    ret, frame = captura.read()
    cv2.imshow("Imagem", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    a = a+1

captura.release()
cv2.destroyAllWindows()
