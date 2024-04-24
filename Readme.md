## Novelty Detection Tutorial with OpenCV, Computer Vision, and Scikit-learn


###  Overview


[이 게시물](https://pyimagesearch.com/2020/01/20/intro-to-anomaly-detection-with-opencv-computer-vision-and-scikit-learn/
)의 예제를 따라하여 굼벵이 질병 예찰 모델에 사용할 수 있는지 검토함

scikit-learn 기반 모델
가상환경 novelty 사용

기반 논문: [Isolation Forest](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/tkdd11.pdf)   
데이터셋 다운로드: https://people.csail.mit.edu/torralba/code/spatialenvelope/

또다른 게시글
https://partrita.github.io/posts/isolation-forest/


### 환경
Python 3.11

설치 패키지
```angular2html
pip install numpy
pip install opencv-contrib-python
pip install imutils
pip install scikit-learn
```

훈련 명령어
```angular2html
python train_anomaly_detector.py --dataset forest --m anomaly_detector.model
```

테스트 명령어
```angular2html
python test_anomaly_detector.py --model anomaly_detector.model --image examples/forest_cd
mc290.jpg
```
