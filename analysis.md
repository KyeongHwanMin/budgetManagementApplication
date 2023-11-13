# 예산관리 어플리케이션

### 모델링

A. 유저

- id

- 계정명(unique) : username
- 패스워드 : password

B. 카테고리

- Category
  - id
  - name
    - 식비 : foodExpenses
    - 교통비 : transportationFee
    - 통신료 : mobilePhonBill
    - 주거비: housingCost
    - 기타 : etc

- Budget
  - user(ForeignKey)
  - category(ForeignKey)
  - amount(금액)
  - period(기간)


C. 지출 기록

- Expenditure
  - user(ForeignKey)
  - category(ForeignKey)
  - amount(금액)
  - date(날짜)
  - mome(메모)
  - excluding_total





### API

회원가입

- api/signup

로그인

- api/login

카테고리 목록

- api/categories

예산설정

지출 기록

통계

- ?type
  - month
    - 지난달 기록
  - day
  - user





### Q

- 의아한 부분
- 이중적인 부분
- 질문들
- 서비스 추후 계획
  - 매출 포인트
  - 예상 사용자








===================================================
### 유저

- 회원 가입 
  - 계정(unique)
  - 패스워드
- 로그인
  - 계정, 비밀번호 맞으면 JWT 발급
  - 모든 API 요청시 Header에 JWT 포함 및 유효성 검사

    
### 예산 설정 및 설계 서비스
- 월별 총 예산 설정
- 카테고리 별 예산 설계
  - 카테고리(choice field)
    - 식비, 교통비, 유흥비, 통신료, 주거비
 
   
**<REST API 설계>**

카테고리 목록 API

GET /api/category
- 유저가 예산설정에 사용할 수 있도록 모든 카테고리 목록 반환
  - 식비 : foodExpenses
  - 교통비 : transportationFee
  - 유흥비 : entertainmentExpenses
  - 통신료 : mobilePhoneBill
  - 주거비 : housingCost

예산 설정 API

POST /api/budget
- 월 별 예산 설정(카테고리 필수)
- ex) 식비 : 40만원, 교통 : 20만원

예산 수정 API

PUT /api/budget

예산 설계(보류)

### 지출 기록
- 금액, 카테고리등을 지정하여 지출 등록, 수정 및 삭제
  - 지출 일시, 지출 금액, 카테고리, 메모
  - 권한 : 생성한 유저
  - 읽기(목록) 기능
    - 기간으로 조회 필수
    - 지출 합계, 카테고리 별 지출 합계 같이 반환
    - 특정 카테고리만 조회
    - 최소, 최대 금액으로 조회
      - 0~10000원 / 20000원 ~ 100000원
    - 합계제외 처리한 지출은 목록에 포함, 모든 지출 합계에서 제외
  
**<REST API 설계>**

지출 API
- POST /api/spending
  - 지출 일시 : dateTimeExpenditure
  - 지출 금액 : amountSpent
  - 카테고리 : category
  - 메모 : memo
- PUT /api/spending
- GET /api/spending/<id>
- GET /api/spending
- DELETE /api/spending
### 지출 컨설팅
    - 월별 예산을 기준으로 오늘 소비 가능한 지출 알려줌
    - 매일 발생한 지출을 카테고리 별로 안내
### 지출 통계
    - 지난달 대비, 지난 요일 대비, 다른 유저 대비  카테고리 별 지출 통계 확인