# KAKAO_problem_solving

## 알고리즘 잡기술 readme에 정리



### 1. re로 스플릿하기

```python
import re
expression = "100-200*300-500+20"
ex = re.split(r'(\D)',expression)
```

정확하게는 다시 해봐야 할거같은데, 숫자가 아닌 것을 기준으로 분리하는건가 싶네.