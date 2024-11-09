import cv2

# 이미지를 컬러 모드로 불러옴
img = cv2.imread("./image/messi.jpg", cv2.IMREAD_COLOR)

# 이미지가 정상적으로 로드되었는지 확인
if img is not None:
    # 이미지를 600x400 크기로 리사이즈
    img = cv2.resize(img, (600, 400))
    
    # 이미지의 크기를 출력
    print('img shape : ', img.shape)

    # 이미지를 복사하여 단일 채널로 수정할 버전 생성
    img_1ch = img.copy()
    
    # Green과 Blue 채널을 0으로 설정하여 Red 채널만 남김
    img_1ch[:, :, 1] = 0  # Green 채널
    img_1ch[:, :, 2] = 0  # Blue 채널

    # 원본 이미지와 수정된 이미지(단일 채널 이미지)를 각각 출력
    cv2.imshow("img", img)
    cv2.imshow("img_1ch", img_1ch)

    # 키 입력을 대기하고, 아무 키나 누르면 창을 닫음
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    # 이미지 파일을 찾을 수 없는 경우 오류 메시지 출력
    print("Image file not found")