<h2>CPDS(Crossing Pedestrian Detection System)</h2>

<h3>1. 소개</h3>

>CPDS는 횡당보도를 건너는 사람들을 감지하는 시스템이다.
>실시간으로 횡단보도를 탐지하고 횡단보도내에 있는 보행자가 있는지를 탐지한다. 보행자 존재 여부 정보를 서버로 전송을 한 후 서버는 주변에 있는 클라이언트에게 정보를 전송한다.

<img src = 'https://user-images.githubusercontent.com/38209962/91653694-efcbbc00-eadd-11ea-918f-5f06aed738ed.PNG'/>

<h5>프로젝트 목적</h5>

>운전자 시점에서 횡단 보도 내에 있는 사각 지대를 컴퓨터 비전 객체 인식 기술을 사용하여 횡단보도 위에 보행자가 있는지를 인식을 한 후, 근접하는 차량 운전자의 모바일 디바이스에 횡단보도에 보행자가 있다는 것을 알려줌으로써, 운전자의 경각심을 높여 교통사고 발생율을 줄이는 것이다. 

<h5>프로젝트 구성도</h5>
<img src = 'https://user-images.githubusercontent.com/38209962/91659631-f4a76480-eb0b-11ea-84dd-9979c8e596c9.PNG' />

----

<h3>2. Demo</h3>

![cpds.gif](https://user-images.githubusercontent.com/16396879/91698344-87e4a680-ebad-11ea-90da-9abd8bb8ea50.gif)

Trained CPDS model : [CPDS_tflite](https://drive.google.com/file/d/1ZxObpKaG8bLLwvwBY0cmXj0ptHm-z54C/view?usp=sharing)

----

<h3>3. 기능</h3>

>1. 횡단보도 탐지 (Detector) 
>2. 보행자 탐지 (Detector)

----

<h3>4. To do</h3>

>1. 근접하는 차량 계산
>2. 횡단보도 내에 보행자 있는지 여부 계산
>3. 운전자에게 경고

----

<h3>5. 개발환경</h3>

>리눅스 커맨드를 실행할 수 있는 colab 혹은 jupyter notebook

>안드로이드 데모를 실행시킬 수 있는 안드로이드 스튜디오 4.0 이상 버전

----

<h3>6. 사용방법</h3>

> 각 디렉토리의 readme 혹은 ipynb 파일을 참고.

----

<h3>7. 라이센스</h3>

>이 프로젝트는 MIT 라이센스를 사용한다.



