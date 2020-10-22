function solution(n, arr1, arr2) {
    const answer = [];

    for(let i = 0; i < n; i ++){
        let arr = arr1[i] | arr2[i]; // 이거 or 처리를 먼저 하는거네.... 흐음 이거 비트연산자자누...
        console.log('arr1: '+ arr1[i])  // + 로 하면 자동으로 string 변환
        console.log('arr2: ', arr2[i])  // int값은 노란색으로 되네 싱기 ㅇㅅㅇ
        console.log(arr)
        console.log('toString 결과: ', arr.toString(2).replace(/1/g, '#').replace(/0/g, ' '))
        console.log('padStart 결과: ', arr.toString(2).padStart(n, '0').replace(/1/g, '#').replace(/0/g, ' '))
        answer.push(arr.toString(2).padStart(n, '0').replace(/1/g, '#').replace(/0/g, ' ')); // 이거 뭔가 엄청 사기적이자나...
        console.log(answer)
    }

    return answer;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))  // 이렇게 해줘도 나옴.