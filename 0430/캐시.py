from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cach = deque()
    if cacheSize != 0:
        for city in cities:
            city = city.lower() # 대소문자 구분 없게 하려면 이게 필수!! or upper를 사용하던가~
            if len(cach) < cacheSize: # 일단 더 넣을 수 있다면
                if city in cach:
                    answer += 1
                else:
                    answer += 5
                # 캐시에 있다면 1플러스, 없다면 5플러스
                cach.append(city)
            else: # 캐시가 일단 꽉 차있다면!!!
                if city in cach:
                    answer += 1
                    cach.remove(city)
                    cach.append(city)
                    # 이거 솔직히 될지 잘 모르겠어...
                else:
                    # 캐시에 안 들어있으면!!!
                    answer += 5
                    cach.popleft() # 왼쪽에서 하나 뺴야징
                    cach.append(city) # 새로 들어온거 
                # 똑같은 로직입니다.
    else:
        answer = len(cities) * 5

    return answer