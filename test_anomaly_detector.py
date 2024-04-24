from pyimagesearch.features import quantify_image
import argparse
import pickle
import cv2

# 명령행 인수를 파싱
ap = argparse.ArgumentParser()
ap.add_argument('-m', "--model", required=True, help="path to pre-trained anomaly detection model")
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

# 모델을 로드
print("[INFO] loading anomaly detection model...")
model = pickle.loads(open(args["model"], "rb").read())

# 입력 이미지를 로드하여 HSV 색상 공간으로 변환
image = cv2.imread(args["image"])
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
features = quantify_image(hsv, bins=(3, 3, 3))

# 모델을 사용하여 예측
preds = model.predict([features])[0]
label = "anomaly" if preds == -1 else "normal"
color = (0, 0, 255) if preds == -1 else (0, 255, 0)

# 예측 결과 텍스트를 이미지에 표시
cv2.putText(image, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

cv2.imshow("Output", image)
cv2.waitKey(0)