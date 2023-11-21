# 예산 관리 어플리케이션
사용자들이 개인 재무를 관리하고 지출을 추적하는 데 도움을 주는 애플리케이션입니다. 
이 앱은 사용자들이 예산을 설정하고 지출을 모니터링하며 재무 목표를 달성하는 데 도움이 됩니다.

<br/>

## Table of Contents
- [개요](#개요)
- [Skils](#skils)
- [Installation](#Installation)
- [API Reference](#api-reference)

<br/>


## 개요
사용자는 간편한 인터페이스를 통해 예산을 계획하고, 
지출을 기록 및 분석할 수 있으며, 예산 설정과 지출 추적을 통해 재정 상태를 명확하게 이해하고 관리할 수 있습니다. 사용자가 재정적으로 어떻게 성장하고 있는지, 
어디에 초점을 맞춰야 할지를 파악하는 데 도움을 줍니다.

<br/>


## Skils
가상환경: ![Static Badge](https://img.shields.io/badge/venv-8A2BE2)
<br/>
언어 및 프레임워크: ![Static Badge](https://img.shields.io/badge/Python-3.12-blue) ![Static Badge](https://img.shields.io/badge/Django-REST-red)
<br/>
데이터 베이스: ![Static Badge](https://img.shields.io/badge/sqlite-green) <br/>
<br/>

## Installation

```bash
  # python 설치
  pyenv install 3.12.x
  # 가상환경 설치
  python -m venv venv
  # 가상환경 활성화
  venv/Scripts/activate
  # 의존성 설치
  pip install -r requirements.txt
  # 데이터베이스 마이그레이션
  python manage.py migrate
```

## 서버 정상 실행 확인
```bash
python manage.py runserver
```
위 명령 실행 결과로 아래와 같은 콘솔 출력이 뜨고, http://127.0.0.1:8000/ 접속이 되면 정상이다.
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2023 - 13:40:31
Django version 4.0.10, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
<br/>

## API Reference

### 회원가입

#### Request
```javascript
  POST api/v1/user/signup
```

| Parameter   | Type     | Description |
|:------------| :------- |:------------|
| `username`  | `string` | **유저 ID**   |
| `password`  | `string` | **비밀번호**    |
| `password2` | `string` | **비밀번호**    |

#### Response
```http
    HTTP/1.1 201
    Content-Type: application/json

    [{
        "회원가입 되었습니다."
      },...
    ]
```

### 로그인

#### Request
```javascript
  POST api/v1/user/login
```

| Parameter   | Type     | Description |
|:------------| :------- |:------------|
| `username`  | `string` | **유저 ID**   |
| `password`  | `string` | **비밀번호**    |


#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json

    [{
        "refresh" : JWT TOKEN,
        "access" : JWT TOKEN,
      },...
    ]
```

### 카테고리 목록 조회

#### Request
```javascript
  GET api/v1/budget/categories
```

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json

    [
      {
          "id": 1,
          "name": "foodExpenses"
      },
      {
          "id": 2,
          "name": "transportationFee"
      },
      {
          "id": 3,
          "name": "mobilePhonBill"
      },
      {
          "id": 4,
          "name": "housingCost"
      },
      {
          "id": 5,
          "name": "etc"
      }
    ]
```

### 예산 설정

#### Request
```javascript
  POST api/v1/budget/
```

| Parameter  | Type     | Description |
|:-----------| :------- |:------------|
| `amount`   | `DecimalField` | **금액**      |
| `period` | `DateTimeField` | **날짜**      |
| `category_name` | `string` | **카테고리명**   |

#### Response
```http
    HTTP/1.1 201
    Content-Type: application/json

    [
      {
        "user": 2,
        "amount": "500000.00",
        "period": "2023-11-13T00:00:00Z"
      }
    ]
```

### 예산 수정

#### Request
```javascript
  PUT api/v1/budget/<pk>
```

| Parameter  | Type     | Description |
|:-----------| :------- |:------------|
| `amount`   | `DecimalField` | **금액**      |
| `period` | `DateTimeField` | **날짜**      |
| `category_name` | `string` | **카테고리명**   |

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json

    [
      {
        "user": 2,
        "amount": "500000.00",
        "period": "2023-11-13T00:00:00Z"
      }
    ]
```

### 지출 목록 조회

#### Request
```javascript
  GET api/v1/expenditure
```

#### Response
```http
    HTTP/1.1 200
    Content-Type: application/json

    [
      {
    "지출": [
              {
                  "id": 1,
                  "date": "2023-11-13T00:00:00Z",
                  "amount": "10000.00",
                  "category": 1,
                  "memo": "점심 값",
                  "user": 1,
                  "excluded_total": false
              },
              {
                  "id": 2,
                  "date": "2023-11-13T00:00:00Z",
                  "amount": "15000.00",
                  "category": 1,
                  "memo": "저녁 값",
                  "user": 1,
                  "excluded_total": false
              },
              {
                  "id": 3,
                  "date": "2023-11-13T00:00:00Z",
                  "amount": "50000.00",
                  "category": 5,
                  "memo": "술 값",
                  "user": 1,
                  "excluded_total": false
              }
          ]
       }
    ]
```

### 지출 등록

#### Request
```javascript
  POST api/v1/expenditure
```

| Parameter  | Type     | Description |
|:-----------| :------- |:------------|
| `date`     | `DateTimeField` | **날짜**      |
| `amount`   | `DecimalField` | **금액**      |
| `category` | `string` | **카테고리ID**  |
| `memo`     | `string` | **메모**      |

#### Response
```http
    HTTP/1.1 201
    Content-Type: application/json

    [
      {
        "id": 7,
        "date": "2023-11-15T00:00:00Z",
        "amount": "100000.00",
        "category": 5,
        "memo": "술 값",
        "user": 1,
        "excluded_total": false
      }
    ]
```

### 오늘 지출 목록 조회

#### Request
```javascript
  GET api/v1/expenditure/spending
```

#### Response
```http
    HTTP/1.1 201
    Content-Type: application/json

    [
      {
        "total_expenditure": 605000.0,
        "category_totals": [
          {
              "category__name": "etc",
              "total": 580000.0
          },
          {
              "category__name": "foodExpenses",
              "total": 25000.0
          }
        ],
    "statistics": [
        {
            "category": "transportationFee",
            "expected_amount": 9523.809523809523,
            "spent_amount": 0,
            "risk_percentage": 0.0
        },
        {
            "category": "foodExpenses",
            "expected_amount": 19047.619047619046,
            "spent_amount": 25000.0,
            "risk_percentage": 131.25
        },
        {
            "category": "etc",
            "expected_amount": 23809.52380952381,
            "spent_amount": 580000.0,
            "risk_percentage": 2436.0
        }
    ]
    }]
```