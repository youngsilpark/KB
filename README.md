# NER을 활용한 한국어 개인정보 마스킹 모델
 개인간의 대화 및 SNS를 통해 본인도 모르게 유출되는 개인정보를 자동으로 마스킹하여, 개인정보 유출에 의한 피해를 방지하는 모델 작성 프로젝트

# 1. Preparing Dataset

- [AI HUB 한국어 SNS 데이터셋](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=114)  
  수집된 SNS 대화 데이터에서 개인정보에 해당하는 부분을 익명화 및 비식별화 처리한 데이터셋

![image](https://user-images.githubusercontent.com/63226383/206382292-0cd40ad6-b885-43fd-aa7c-e2e0b0e40070.png)


## 1-1. 마스킹 카테고리 선택 및 개인정보 데이터 생성 전략
  익명화 처리된 개인정보를 역으로 재생성

 1) 이름  
  : 받침에 따라 가상 이름 생성
 2) 계정  
  : email@domain 형태의 가상 이메일 생성
 3) 신원  
  : 주민등록번호 총 13자리 (123456-12345789) , "-" 유무 고려 
 4) 번호  
  : 4자리 또는 6자리의 숫자비밀번호
 5) 전화번호    
  : 총 11자리의 전화번호, "-" 유무 고려
 6) 주소  
  : 한국에 존재하는 지명들의 무작위로 조합한 가상 주소 생성
 7) 금융정보  
  : 은행명과 계좌번호 조합

![image](https://user-images.githubusercontent.com/63226383/206383150-e8167cab-6359-42fc-87f4-a27ddb8a41bd.png)


## 1-2. 데이터 전처리 및 생성
  - [Code(ipynb)](https://github.com/youngsilpark/KB/blob/main/Preprocessing/KB_data_prep.ipynb.ipynb)


# 2. NER Modeling

![image](https://user-images.githubusercontent.com/63226383/206385072-2098ab60-9eb1-40fa-aefe-99d89688e833.png)

![image](https://user-images.githubusercontent.com/63226383/206385119-c6887e76-be18-4c6a-ad99-6aa06df1d29d.png)


## 2-1. KoBERT 학습
[Code(ipynb)](https://github.com/youngsilpark/KB/blob/main/KoBERT/KB_KoBERT.ipynb)


# 3. 사용 예시

![image](https://user-images.githubusercontent.com/63226383/206389024-d03152c0-764d-4e01-a19f-9c6271dd05f9.png)



# References
- [Monologg KoBERT-NER](https://github.com/monologg/KoBERT-NER)
- [AIHUB](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=114)



