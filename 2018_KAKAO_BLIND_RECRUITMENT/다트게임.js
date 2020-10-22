////////// 배움1: 일차원 배열 만들기! //////////////
////////// 배움2: or and 사용하는법 ////////////////
////////// 배움3: not 사용하는법 ///////////////////
////////// 배움4: 굳이 int로 안해줘도 알아서 계산////
////////// 배움5: int랑 str을 더하면 str가 되지만 곱하면 int가 된다./////

function solution(dartResult) {
    var answer = 0;
    var score_list = Array(4).fill(0)
    // console.log(score_list)
    var stack_list = Array()
    
    let num = ''
    for (let i = 0; i < dartResult.length; i++) {
        if (dartResult[i] === "S" || dartResult[i] === "D" || dartResult[i] === "T") {
            if (i !== dartResult.length - 1) {
                if (dartResult[i + 1] === "*" || dartResult[i + 1] === "#") {
                    stack_list.push([num, dartResult[i], dartResult[i + 1]])
                } else {
                    stack_list.push([num, dartResult[i], 0])
                }
                num = ''
            } else {
                stack_list.push([num, dartResult[i], 0])
            }
        } else {
            if (!(dartResult[i] === "*" || dartResult[i] === "#")) {
                num += dartResult[i]
            }
        }
    }
    // console.log(stack_list)

    for (let j = 0; j < 3; j++) {
        const stack = stack_list[j];
        let a = stack[0]
        let b = stack[1]
        let c = stack[2]
        console.log(a, b, c)
        const jpl = j + 1
        if (b === 'S') {
            score_list[jpl] = a
        } else if(b == "D") {
            score_list[jpl] = a**2
        } else {
            score_list[jpl] = a**3
        }
        if (c !== 0) {
            if (c === '*') {
                score_list[j] *= 2
                score_list[jpl] *= 2
            } else {
                score_list[jpl] = -score_list[jpl]
            }
        }
    }
    // console.log(score_list)
    
    answer = score_list.reduce((a, b) => a*1 + Number(b));
    // console.log(answer)
    return answer;
}

solution("1D2S#10S")
// solution('1D2S#10S')