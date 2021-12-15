# **Workout Diary**

> 이 프로젝트는 `codestates section3 project`의 일환입니다.


### 프로젝트 설명
- 운동기구를 사용하여 운동을 한 기록을 남기는 app 입니다.


### 주요 화면 및 기능
- 운동 기록 : 운동 날짜 / 운동 기구 / 운동 기구 중량 / 1세트 당 운동 횟수 / 총 세트 횟수 `create` 
- 운동 별 코멘트(댓글) 기록 : `create`
- 기록 확인 및 수정 : 저장된 운동 기록, 댓글 `read`, `delete`, `update`
- 데이터 분석 : 입력 데이터 기반 운동기구 별 통계 그래프 (그래프 출력은 되지만, 완벽하게 데이터베이스와 연결해서 데이터 분석하는 것 까지는 추후 발전 사항)
- postgresql 연결 : 테이블 생성 및 컬럼 연결

### 사용 개념
- `flask`, `flask-sqlalchemy`, `postgresql`database

### entity relationship (schema)
   ![entity relationship(schema)](https://user-images.githubusercontent.com/74661937/146139648-b18f5c33-1a73-41ed-80e1-bd7df2c2fff8.png)
