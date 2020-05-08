function solution(cacheSize, cities) {
    var answer = 0;
    const cach = [];
    if (cacheSize !== 0) {
        cities.forEach(city => {
            city = city.toLowerCase()
            // console.log(city)
            if (cach.length < cacheSize){
                if (city in cach) {
                    answer += 1
                } else {
                    answer += 5
                }
                cach.push(city)
            } else {
                if (city in cach) {
                    answer += 1
                    // cach.remove(city)   // remove가 되나? 안되는거같어 실패작.
                    const idx = cach.indexOf(city)
                    cach.splice(idx, 1) // 이렇게 하라는 거지?
                    cach.push(city)
                } else {
                    answer += 5
                    cach.shift()
                    // cach.shift() 같은거?
                    cach.push(city)
                }
            }
        });
    } else {
        answer = cities.length * 5
    }
    console.log(cach)
    return answer;
}