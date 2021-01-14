# mariah_carey_christmas


### Mariah Carey의 'All I want for Christmas is you'의 연간 음원 순위와 주요 국가의 순위, 기후 간의 상관관계를 확인하고자 한다.


### 1. Mariah Carey의 'All I want for Christmas is you'의 일간 음원순위(2011.02 - 2021.01) 수집

### 2. 주요 국가(미국, 영국)의 일간 음원순위(2011.02-2021.01) 수집

### 3. 주요 국가(미국, 영국)의 일 평균 기온(주요 1개 도시) 수집

- 무료로 음원순위를 열람할 수 있고, 장기간의 음원순위 데이터를 수집할 수 있는 'i-tunes'의 음원순위를 활용하였다.
  'BillBoard'는 장기간 순위권에 있는 음원은 강제로 하차시키는 등의 기준이 있어, 대중성을 가지기는 어렵다는 판단이 있었고, 장기간의 음원순위 데이터는 유료로 판매되고 있었다.


- 시계열 데이터의 한 종류인 음원순위와 기온 데이터를 분석하여,  음원순위를 예측해보고자 하였다.

- 10년 이상 매년 규칙적으로 음원 순위 상위권에 재진입하는 곡인
   'Mariah Carey'의 'All I want for Chrstmas is you'를 선정하였다.
   
- 기온 데이터를 활용하여 음원순위 예측을 위해서는 특정 국가의 기온을 수집해야했는데,
  이를 위해서, 세계 음악시장 규모가 가장 큰 미국과 영국 두 국가의 음원순위와,
  각 국가의 주요 1개 도시를 선정하여 기온을 수집하였다(New York, London).
  
- Google COLAB : 가상 환경 제공으로, 보다 신속한 프로그램 구동을 가능하게 한다.
  
- TensorFlow2 : Keras로 손쉬운 접근이 가능하고, 다양한 모듈 사용 가능, COLAB과의 호환성이 좋다.
  
 - Python3, Keras : 데이터 분석을 보다 수월하게 진행할 수 있는 기반이 된다.
  
- BeautifulSoup : 단순 'html'을 활용한 사이트의 데이터 수집에 용이하다.
  
- Selenium : 동적인 입력을 받아 데이터를 수집하는 것에 용이하다.
  
- Pandas, Numpy : 분석 대상이 되는 데이터를 가공하는 데 활용이 다양한 기능들을 제공한다.
