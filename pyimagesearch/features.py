from imutils import paths
import numpy as np
import cv2

# 색상 히스토그램 구하기
def quantify_image(image, bins=(4, 6, 3)): # 빈이 뭐고??
    hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 180, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten() # 정규화 코드. 원시 빈도 수가 아닌 백분율을 계산할 수 있음. 일부 이미지가 다른 이미지보다 크거나 작을 때 유용

    return hist

def load_dataset(datasetPath, bins):
    imagePaths = list(paths.list_images(datasetPath))
    data = []


    for (i, imagePath) in enumerate(imagePaths):
        # 이미지를 로드하고 HSV 색상 공간으로 변환
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # 히스토그램 구하기
        features = quantify_image(image, bins)
        data.append(features)

    return np.array(data)