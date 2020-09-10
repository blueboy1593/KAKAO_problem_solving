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



### 3. 투포인터와 슬라이딩 윈도우

https://blog.naver.com/kks227/220795165570

위의 블로그에 자세하게 나와 있다.

투포인터 : pivot 같은 느낌 2개를 움직여가면서 구간합 구하기.

슬라이딩 윈도우 : 구하고 싶은 구간을 미리 정해놓고 훑어보기.



### 4. Dictionary 활용 중 Defaultdict

```python
gems_dict = defaultdict(lambda: 0)
del gems_dict[gems[sta]]
```

- 디폴트딕트는 자동으로 숫자가 0인 딕셔너리 구성해주는 것
- del은 딕셔너리에서 삭제. 유용하게 쓰일 듯.





