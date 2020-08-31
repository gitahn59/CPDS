# Detector
----
디텍터는 YOLO tiny를 기반으로 생성한 Object Detection 모델로 횡단보도와 보행자 객체를 인식한다.     
이 디렉토리에서는 디텍터를 생성하는데 필요한 세부 구성요소들을 포함한다.    
세부 요소들의 사용 방법은 각 폴더의 readme 또는 ipynb 파일에서 제공한다.

## 1. ImageCrawler
----
모델을 훈련시키기 위한 이미지를 모으는데 사용된다.

## 2. YOLO_train
----
수집된 데이터셋을 기반으로 훈련하여 YOLO weight를 생성한다.

## 3. Converter
----
YOLO weight를 tflite 로 변환한다.

## 4. Android Demo
----
Objection Detection 모델을 간단하게 실행해볼 수 있는 Android 프로젝트를 제공한다.