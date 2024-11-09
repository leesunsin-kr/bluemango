import numpy as np
import cv2

# 얼굴 인식을 위한 Haar cascade 분류기 로드
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

# 첫 번째 카메라 장치를 통해 영상 캡처 (카메라 인덱스 0 사용)
cap = cv2.VideoCapture(0, cv2.CAP_V4L)  

# 캡처 영상의 프레임 너비 설정 (640 픽셀)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

# 캡처 영상의 프레임 높이 설정 (480 픽셀)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 무한 루프를 통해 카메라 영상 지속적으로 처리
while (True):
    # 카메라로부터 프레임을 읽어옴
    ret, img = cap.read()
    
    # 영상을 상하 반전 (필요에 따라 방향 변경 가능)
    img = cv2.flip(img, -1)
    
    # 영상 컬러를 그레이스케일로 변환 (얼굴 인식을 위해)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 얼굴 인식 수행 (scaleFactor=1.2, minNeighbors=5 설정)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    print("Number of faces detected: " + str(len(faces)))  # 인식된 얼굴 개수 출력

    # 인식된 얼굴 영역에 대해 사각형을 그림
    for (x, y, w, h) in faces:
        # 얼굴 위치에 파란색 사각형 그리기
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        
        # 얼굴 부분을 ROI로 정의 (그레이스케일과 컬러 각각)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    # 이미지 창에 현재 프레임 표시
    cv2.imshow('img', img)

    # 키보드 입력 대기 (30ms) 및 Esc 키(27)를 누르면 루프 탈출
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# 카메라 자원 해제 및 모든 창 닫기
cap.release()
cv2.destroyAllWindows()