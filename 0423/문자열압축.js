//////////////// 오늘의 배움: list는 바로 비교가 안된다! ///////////////////////
/////////////// 오늘의 배움2: Math.max, Math.min 이라는게 있다! ////////////////

function solution(s) {
    var answer = s.length;
    const L = answer
    const half = parseInt(L / 2)
    for (let n = 1; n < half + 1; n++) {
        var cnt = 0
        let temp = []
        const stack = []
        for (let i = 0; i < L; i ++){
            temp.push(s[i])
            cnt += 1
            if (cnt === n){
                cnt = 0
                stack.push(temp)
                temp = [];
            }
        }
        if (temp.length > 0){
            stack.push(temp)
        }
        // console.log(stack)
        // console.log('끊어주기-----------------')
        // 1단계 끝.

        var tem = stack[0]
        let cnt2 = 1
        let temp_answer = ''
        for (let i = 1; i <= stack.length; i++) { // 설마 인덱스 넘어가는거 걱정 안해줘도 되는건가...?
            // console.log('stack이랑 tem:', stack[i], tem)
            if (JSON.stringify(stack[i]) == JSON.stringify(tem)) {
                // console.log('여기왔니')
                cnt2 += 1
            } else {
                if (cnt2 > 1) {
                    temp_answer += cnt2 + tem.join('')
                } else {
                    temp_answer += tem.join('')
                }
                tem = stack[i]
                cnt2 = 1
            }
        }
        // console.log(stack)
        // console.log(n, temp_answer)
        answer = Math.min(answer, temp_answer.length)
    }

    return answer;
}

solution("aabbaccc")
// solution("abcabcabcabcdededededede")