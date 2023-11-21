# 예산 관리 어플리케이션
사용자들이 개인 재무를 관리하고 지출을 추적하는 데 도움을 주는 애플리케이션입니다. 
이 앱은 사용자들이 예산을 설정하고 지출을 모니터링하며 재무 목표를 달성하는 데 도움이 됩니다.

<br/>

## Table of Contents
- [개요](#개요)
- [Skils](#skils)
- [Installation](#Installation)
- [Running Tests](#running-tests)
- [API Reference](#api-reference)
- [프로젝트 진행 및 이슈 관리](#프로젝트-진행-및-이슈-관리)
- [구현과정(설계 및 의도)](#구현과정(설계-및-의도))
- [TIL 및 회고](#til-및-회고)
- [Authors](#authors)
- [References](#references)

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
    HTTP/1.1 201
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
    HTTP/1.1 201
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

### 예산

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

## 프로젝트 진행 및 이슈 관리

[![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://bow-hair-db3.notion.site/cdb6eb37500b4580a80252ea3d7c3963?pvs=4)

<br/>


## 구현과정(설계 및 의도) 
(노션, 블로그 등의 페이지로 안내 가능)
<details>
<summary>유저 모델과 실행결과 모델관의 관계 설정 시 00 고려 - click</summary>

- 의존성 문제
    1. Press `Ctrl` + `f` on your keyboard, to bring out the search modal.
    2. Enter the name of the badge you need.
    3. Copy the appropriate `![Name](link)` element and paste it in your Markdown file (e.g. README.md)
- 00가 00 하는 문제

</details>

<details>
<summary>00 구현 시 동시성 고려 - click</summary>

- 의존성 문제
    1. Press `Ctrl` + `f` on your keyboard, to bring out the search modal.
    2. Enter the name of the badge you need.
    3. Copy the appropriate `![Name](link)` element and paste it in your Markdown file (e.g. README.md)
- 00가 00 하는 문제

</details>

<details>
<summary>RESTful API 설계 - click</summary>

- 의존성 문제
    1. Press `Ctrl` + `f` on your keyboard, to bring out the search modal.
    2. Enter the name of the badge you need.
    3. Copy the appropriate `![Name](link)` element and paste it in your Markdown file (e.g. README.md)
- 00가 00 하는 문제

</details>

<br/>


## TIL 및 회고

<details>
<summary>Django ORM 조회 시 발생하는 00 버그 - click</summary>

- 의존성 문제
    1. Press `Ctrl` + `f` on your keyboard, to bring out the search modal.
    2. Enter the name of the badge you need.
    3. Copy the appropriate `![Name](link)` element and paste it in your Markdown file (e.g. README.md)
- 00가 00 하는 문제

</details>

<details>
<summary>Django ORM 조회 시 발생하는 00 버그 - click</summary>

- 의존성 문제
    1. Press `Ctrl` + `f` on your keyboard, to bring out the search modal.
    2. Enter the name of the badge you need.
    3. Copy the appropriate `![Name](link)` element and paste it in your Markdown file (e.g. README.md)

- 00가 00 하는 문제

</details>

(또는 블로그, 노션 등 링크 연동)

- [Django ORM 조회 시 발생하는 00 버그 발생](#google.com)
- [00 서비스 개발 회고록](#google.com)

<br/>


## Authors

- [@user1](https://www.github.com/2)
- [@user2](https://www.github.com/2)
- [@user3](https://www.github.com/2)

<br/>


## References

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)





