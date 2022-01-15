# 03. 실수

---

### 부동소수점

![https://www.wikihow.com/images/thumb/e/ea/Teachme.jpg/728px-Teachme.jpg](https://www.wikihow.com/images/thumb/e/ea/Teachme.jpg/728px-Teachme.jpg)

- 파이썬은 실수를 **부동 소수점** 방식으로 표현한다.
    - 배정도 `double` 실수로 64비트(8바이트)
- 기본 수식으로 (−1)S(−1)S x MM x 2E2E로 표현할 수 있으며, 각각의 역할은 다음과 같다.
    - S: 부호부(Sign) 1비트를 의미하며 0이면 양수고, 1이면 음수가 된다.
    - M: 가수부(Mantissa) 23비트를 의미하며, 양의 정수로 표현한다.
    - E: 지수부(Exponent) 8비트를 의미하며, 소수점의 위치를 나타낸다.

### 정밀도

```python
>>> 0.1 + 0.2
0.30000000000000004
```

- 부동소수점은 실수를 정확하게 표현할 수 없는 문제가 있음
- 실수 연산은 소수점 단위 값을 정확히 표현하는 것이 아니라, 특정 시점에 반올림하여 비슷한 근사값을 구함
- 근사한 차이라고 하지만, 숫자에 민감한 업무 일수록 오차가 커질 수 있기에 주의를 요함

### 엡실론

- 엡실론이란 1.0과 그 다음으로 표현가능 한 수 사이의 차이
- 이 차이는 항상 머신 엡실론(machine epsilon)값 보다 작다.

```python
>>> import math, sys
>>> x = 0.1 + 0.2
>>> math.fabs(x - 0.3) <= sys.float_info.epsilon

True
```

### +고정소수점

- 반올림 오차는 decimal 모듈의 Decimal을 사용
- Decimal은 숫자를 10진수로 처리하여 정확한 소수점 자릿수를 표현

```python
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.2')
Decimal('0.3')
```