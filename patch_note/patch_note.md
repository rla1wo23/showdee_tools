# 업데이트 내역

## 1. 공연 조회 속도 개선
- **성과**: 조회 속도가 `7.13s`에서 `1.32s`로 개선되었습니다.
- **개선 내역**:
  - ### 백엔드 최적화
    - **DB 인덱싱 적용**:
      - Django `model` 파일에 시간 인덱스를 적용 후, DB 스키마에 반영.
      - Django `view` 파일에 `order_by` 시간을 추가.
  - ### 프런트엔드 최적화
    - 불필요한 `jQuery` dependency 코드를 제거.
    - 불필요한 코드를 정리하여 경량화.

---

## 2. 달력 버튼 버그 수정
- **원인**: 코드 가독성 개선 과정에서 불필요한 반복문이 삽입된 것을 발견.
- **조치**: 반복문을 제거하여 정상 동작을 복구.

---

## 3. 스크롤 관련 버그 수정
- **이슈**: 스크롤 시 화면이 걸리는 문제 발생.
- **수정 내역**:
  - ### 이미지 최적화
    - 이미지의 **lazy loading** 적용으로 아이콘 이미지 로드 시점을 조정.
  - ### CSS 수정
    - 잘못된 상속 관계를 바로잡음.
    - `overflow-x`를 `hidden`으로 설정하여 가로 스크롤 문제 방지.
    - `body`의 너비를 `100vw`에서 `100%`로 변경하여 브라우저 스크롤 문제 해결.
  - ### 컴포넌트 스타일링 최적화
    - 중복된 CSS 속성을 제거하고 간결하게 변경.
    - `flex` 및 `align-items` 등을 활용하여 레이아웃 조정.
    - 불필요한 UI 요소를 `display: none`으로 숨김.
  - ### 폰트 설정 통합
    - `@font-face`를 활용하여 글로벌 폰트를 정의.
    - 중복된 폰트 로드 코드를 제거.
    - 폰트 패밀리를 `Vitro_core` 및 `KoPubDotumMedium`으로 통일.
  - ### 스크롤 관련 수정
    - `overflow-y: inherit` 또는 `overflow-y: scroll`로 설정 변경.
    - iOS 부드러운 스크롤을 위해 `webkit-overflow-scrolling: touch` 추가.
    - 커스텀 스크롤바 스타일(`::-webkit-scrollbar`)을 정의.
  - ### UI 요소 스타일링 업데이트
    - 버튼, 링크, 배너 등의 **패딩, 마진, 색상** 조정.
    - 특정 요소의 `display` 속성을 `block`, `flex`, `inline-block`으로 변경.
  - ### 불필요한 코드 제거
    - 중복된 CSS 속성 및 정의 제거.
    - 사용하지 않는 클래스와 속성을 제거하여 가독성 향상.

---

## 4. 코드 예시
```jsx
<img src="{{ i.photo.url }}" alt="" loading="lazy">

