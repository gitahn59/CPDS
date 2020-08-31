# CPDS Android Demo
----
이 디렉토리에서는 CPDS의 데모 프로그램의 안드로이드 프로젝트를 제공한다.    

## 1. Demo
----
![cpds.gif](https://user-images.githubusercontent.com/16396879/91698344-87e4a680-ebad-11ea-90da-9abd8bb8ea50.gif)

## 2. Description
----
이 데모는 [tensorflow-yolov4-tflite](https://github.com/hunglc007/tensorflow-yolov4-tflite/tree/master/android) 의 안드로이드 프로젝트를 기반으로 제작되었다.     
기본적으로 보행자와, 횡단보도를 인식하기 위해 제작된 YOLO 모델을 변환한 tflite 모델을 사용하도록 설정 되어있지만, 다른 custom tiny 모델 역시 사용 가능하다.    
데모를 실행하면 카메라가 실행되며 촬영되는 영상 위의 모든 보행자와 횡단보도 객체를 인식한다.
    
## 3. Demo 사전 준비
----
>1. Detector/YOLO_train을 이용하여 데이터를 학습한 weights 파일 생성한다.
>2. Detector/converter를 이용하여 학습 된 weights를 tflite로 변환한다.

Trained CPDS model : [CPDS_tflite](https://drive.google.com/file/d/1ZxObpKaG8bLLwvwBY0cmXj0ptHm-z54C/view?usp=sharing)


## 4. Running the Demo
-----
>1. 안드로이드 스튜디오 4.0 이상 버전에서 이 디렉토리를 루트로하여 프로젝트를 생성한다.
>2. app/src/main/assets/ 폴더에 model.tflite로 복사한다.
>3. app/src/main/assets/ 폴더의 obj.names를 custom data에 맞게 수정한다. 
>3. 안드로이드 디바이스를 연결하고 컴파일한다.

