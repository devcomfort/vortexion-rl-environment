# Entity Configuration Guide

`entity_config.jsonl` 파일은 게임 내 모든 엔티티의 속성과 동작을 설정하는 JSONL 형식의 설정 파일입니다. 코드 수정 없이 이 파일만 수정하여 게임 밸런스를 조정할 수 있습니다.

## 파일 형식

각 줄은 하나의 엔티티 타입에 대한 JSON 객체입니다:

```jsonl
{"type": "enemy_a", "speed": 1, "bullet_speed": 2, "colour": 7, "u": 0, "v": 80, "hp": 2}
```

## 엔티티 타입별 설정

### Enemy 타입 (enemy_a ~ enemy_p)

모든 enemy 타입은 다음 공통 속성을 가집니다:

#### 그래픽 속성

- **`colour`** (int, 기본값: 15)
  - Pyxel 색상 팔레트 인덱스 (0-15)
  - enemy의 기본 색상
  - 예: `7` = cyan, `3` = light green, `13` = purple

- **`u`** (int, 기본값: 0)
  - 스프라이트 시트의 X 좌표 (픽셀 단위)
  - enemy 스프라이트의 텍스처 위치

- **`v`** (int, 기본값: 0)
  - 스프라이트 시트의 Y 좌표 (픽셀 단위)
  - enemy 스프라이트의 텍스처 위치

- **`w`** (int, 선택적)
  - enemy의 너비 (픽셀 단위)
  - 기본값: 16 (일반 enemy), 32 (보스)
  - 보스(enemy_k, l, m)만 설정 가능

- **`h`** (int, 선택적)
  - enemy의 높이 (픽셀 단위)
  - 기본값: 16 (일반 enemy), 32 (보스)
  - 보스(enemy_k, l, m)만 설정 가능

#### 게임플레이 속성

- **`hp`** (int, 기본값: 2)
  - enemy의 체력 (Hit Points)
  - 플레이어의 총알에 맞으면 감소
  - 0이 되면 파괴됨

#### 이동 속성

- **`speed`** (float, 선택적)
  - X축 이동 속도 (픽셀/프레임)
  - 양수: 왼쪽으로 이동, 음수: 오른쪽으로 이동
  - 사용: enemy_a, enemy_b, enemy_e, enemy_i, enemy_o, enemy_p

- **`speed_x`** (float, 선택적)
  - X축 이동 속도 (픽셀/프레임)
  - `speed`와 동일하지만 명시적으로 X축임을 표시
  - 사용: enemy_h, enemy_n

- **`speed_y`** (float, 선택적)
  - Y축 이동 속도 (픽셀/프레임)
  - 양수: 아래로 이동, 음수: 위로 이동
  - 사용: enemy_d, enemy_g, enemy_n

- **`speed_x_offset`** (float, 선택적)
  - 스크롤 속도에 더해지는 X축 오프셋
  - 배경 스크롤 속도 + 이 값으로 이동
  - 사용: enemy_d, enemy_g

- **`move_speed_y`** (float, 선택적)
  - Y축 이동 속도 (보스 전용)
  - 사용: enemy_k

- **`bounce_vel`** (float, 선택적)
  - 바닥에 튕길 때의 Y축 속도
  - 사용: enemy_h

- **`gravity`** (float, 선택적)
  - 중력 가속도 (매 프레임마다 Y축 속도에 더해짐)
  - 사용: enemy_h

- **`vel_y`** (array, 선택적)
  - Y축 속도 배열 (패턴 이동용)
  - 시간에 따라 순차적으로 적용됨
  - 사용: enemy_i
  - 예: `[-0.5, 1, -1.25, 1.25, -1, 0.5]`

- **`vel_y_change_interval`** (int, 선택적)
  - `vel_y` 배열의 인덱스를 변경하는 간격 (프레임 단위)
  - 사용: enemy_i

#### 공격 속성

- **`bullet_speed`** (float, 선택적)
  - enemy가 발사하는 총알의 속도 (픽셀/프레임)
  - 대부분의 enemy에서 사용

- **`shot_delay`** (int, 선택적)
  - 총알 발사 후 다음 발사까지의 대기 시간 (프레임 단위)
  - 사용: enemy_a, enemy_o, enemy_p

- **`initial_shot_delay`** (int, 선택적)
  - 화면에 나타난 후 첫 총알 발사까지의 대기 시간 (프레임 단위)
  - 사용: enemy_a, enemy_o, enemy_p

- **`shot_interval`** (int, 선택적)
  - 총알 발사 간격 (프레임 단위)
  - `shot_delay`와 유사하지만 다른 로직에서 사용
  - 사용: enemy_j

- **`shoot_interval_alone`** (int, 선택적)
  - 다른 enemy가 없을 때의 총알 발사 간격 (프레임 단위)
  - 보스 전용
  - 사용: enemy_k, enemy_l, enemy_m

- **`shoot_interval_with_enemies`** (int, 선택적)
  - 다른 enemy가 있을 때의 총알 발사 간격 (프레임 단위)
  - 보스 전용
  - 사용: enemy_k, enemy_l, enemy_m

### Player 타입

- **`move_speed`** (float, 기본값: 2.0)
  - 플레이어의 이동 속도 (픽셀/프레임)
  - 상하좌우 이동 시 사용

- **`move_speed_diagonal`** (float, 기본값: 1.414)
  - 대각선 이동 속도 (픽셀/프레임)
  - `move_speed * 0.707` (√2/2)로 계산됨
  - 대각선 이동 시 속도 보정

- **`shot_delay`** (int, 기본값: 10)
  - 총알 발사 후 다음 발사까지의 대기 시간 (프레임 단위)

- **`invincibility_frames`** (int, 기본값: 120)
  - 피격 후 무적 시간 (프레임 단위)
  - 이 시간 동안은 추가 피해를 받지 않음

### Player Shot 타입

- **`max_shots`** (int, 기본값: 4)
  - 화면에 동시에 존재할 수 있는 최대 총알 개수

- **`size`** (int, 기본값: 14)
  - 총알의 크기 (픽셀 단위, 정사각형)

- **`speed_lvl`** (array, 기본값: [10, 10, 11, 11, 12, 12])
  - 무기 레벨별 총알 속도 배열
  - 인덱스는 무기 레벨 (0-5)
  - 예: 레벨 0 = 속도 10, 레벨 5 = 속도 12

- **`damage`** (object, 기본값: {"0": [1,1,1,1,1,2], "1": [1,1,1,2,2,3], "2": [1,1,2,2,3,3]})
  - 무기 타입별, 레벨별 데미지
  - 키: 무기 타입 (0=전방, 1=확산, 2=전후방)
  - 값: 레벨별 데미지 배열 (0-5)
  - 예: 무기 타입 0, 레벨 5 = 데미지 2

- **`spread_diagonal_x`** (float, 기본값: 0.894)
  - 확산 무기(타입 1)의 대각선 X축 속도 배율
  - `speed_lvl * spread_diagonal_x`로 계산

- **`spread_diagonal_y`** (float, 기본값: 0.447)
  - 확산 무기(타입 1)의 대각선 Y축 속도 배율
  - `speed_lvl * spread_diagonal_y`로 계산

### Enemy Shot 타입

- **`size`** (int, 기본값: 4)
  - enemy 총알의 크기 (픽셀 단위, 정사각형)

- **`colour_change_interval`** (int, 기본값: 10)
  - 총알 색상 변경 간격 (프레임 단위)
  - 깜빡이는 효과를 위해 주기적으로 색상 변경

### Powerup 타입

- **`speed`** (float, 기본값: 0.5)
  - 파워업 아이템의 이동 속도 (픽셀/프레임)
  - 왼쪽으로 이동하는 속도

## 설정 예시

### Enemy 속도 조정

```jsonl
{"type": "enemy_a", "speed": 2, "bullet_speed": 3, "colour": 7, "u": 0, "v": 80, "hp": 2}
```

- `speed`를 1에서 2로 증가 → enemy가 2배 빠르게 이동
- `bullet_speed`를 2에서 3으로 증가 → 총알이 더 빠르게 발사

### Enemy 체력 조정

```jsonl
{"type": "enemy_h", "speed_x": 1.5, "bounce_vel": 5, "gravity": 0.2, "colour": 6, "u": 112, "v": 80, "hp": 8}
```

- `hp`를 4에서 8로 증가 → enemy가 더 강해짐

### Enemy 색상 변경

```jsonl
{"type": "enemy_a", "speed": 1, "bullet_speed": 2, "colour": 11, "u": 0, "v": 80, "hp": 2}
```

- `colour`를 7(cyan)에서 11(yellow)로 변경 → 색상 변경

### 보스 크기 조정

```jsonl
{"type": "enemy_k", "bullet_speed": 2.5, "move_speed_y": 0.5, "shoot_interval_alone": 60, "shoot_interval_with_enemies": 200, "colour": 11, "u": 160, "v": 80, "hp": 200, "w": 48, "h": 48}
```

- `w`, `h`를 32에서 48로 증가 → 보스가 더 커짐

## 주의사항

1. **JSONL 형식**: 각 줄은 유효한 JSON 객체여야 하며, 마지막 줄 뒤에도 줄바꿈이 있어야 합니다.

2. **타입 일치**: 숫자 값은 적절한 타입(int/float)으로 설정해야 합니다. 배열과 객체는 올바른 형식으로 작성해야 합니다.

3. **기본값**: 설정 파일에 없는 속성은 코드에서 정의된 기본값이 사용됩니다.

4. **빌드**: 설정 파일 변경 후 `just dev-setup`을 실행하거나, 빌드 시 자동으로 포함됩니다.

5. **테스트**: 설정 변경 후 게임을 실행하여 의도한 대로 동작하는지 확인하세요.

## 색상 팔레트 참조

Pyxel 기본 색상 팔레트 (인덱스 0-15):
- 0: 마젠타
- 1: 검정
- 2: 초록
- 3: 연한 초록
- 4: 파랑
- 5: 연한 파랑
- 6: 빨강
- 7: 시안
- 8: 빨강
- 9: 핑크
- 10: 노랑
- 11: 노랑
- 12: 연한 노랑
- 13: 보라
- 14: 회색
- 15: 흰색

## 관련 파일

- `src/entity_config.py`: 설정 파일 로더 모듈
- `src/entities/enemy.py`: Enemy 기본 클래스 (자동으로 설정 로드)
- `src/entities/enemies/*.py`: 각 enemy 구현체

