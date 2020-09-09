# KAKAO_problem_solving

## 알고리즘 잡기술 readme에 정리



### 1. re로 스플릿하기

```python
import re
expression = "100-200*300-500+20"
ex = re.split(r'(\D)',expression)
```

정확하게는 다시 해봐야 할거같은데, 숫자가 아닌 것을 기준으로 분리하는건가 싶네.



### 2. Inf 사용하기

```python
answer = float('inf')
answer = float('-inf')
```

위와 같이 최대값을 설정할 수 있다.

최소값 구할 때나, 다익스트라 할 때 유용함!



### 3. Counter, Reduce

```python
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
```

카운터...흠

reduce : 자바스크립트에서 내가 알던 그 리듀스인가?



### 4. 배열 90도 회전하기!

```python
arr = list(zip(*arr))
arr = list(zip(*arr[::-1])) # 이게 90도 회전임.
```

이거 굉장히 중요한 잡기술임. 기억해두자