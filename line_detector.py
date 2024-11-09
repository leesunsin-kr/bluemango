import cv2
import numpy as np

img = cv2.imread("./image/4.jpg", cv2.IMREAD_COLOR) # 1.jpg, 2.jpg, 3.jpg, 4.jpg로만 바꿔서 사용 

if img is not None:
    img = cv2.resize(img, (400, 300))
    print('img shape:', img.shape)
    
    lower_yellow = np.array([0, 100, 100])  # 노란색 범위 설정
    upper_yellow = np.array([50, 255, 255]) # 약간의 오차허용을 위해 블루 채널에 50 추가
    yellow_mask = cv2.inRange(img, lower_yellow, upper_yellow)  # lower_yellow에서 upper_yellow 사이의 값을 마스크로 추출(이 외 값은 제외)
    yellow_result = cv2.bitwise_and(img, img, mask=yellow_mask) # img에서 yellow_mask인 영역만 살림
    
    lower_white = np.array([200, 200, 200]) # 흰색 범위 설정
    upper_white = np.array([255, 255, 255])
    white_mask = cv2.inRange(img, lower_white, upper_white)
    white_result = cv2.bitwise_and(img, img, mask=white_mask)   # img에서 white_mask인 영역만 살림

    cv2.imshow("Yellow Channel", yellow_result) # 노란색만 추출
    cv2.imshow("White Channel", white_result)   # 흰색만 추출
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image file not found")