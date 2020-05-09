function solution(m, n, board) {
    var answer = 0;
    // console.log(board)
    for (let i = 0; i < board.length; i++) {
        const temp = board[i];
        board[i] = temp.split('')
    }
    // console.log(board)

    // let flag = false
    while (true) {
        let flag = true
        const will_delete = [];
        for (let i = 0; i < m - 1; i++) {
            for (let j = 0; j < n - 1; j++) {
                const a = board[i][j]
                if (board[i + 1][j] === a && board[i][j+1] === a && board[i+1][j+1] === a && a !== 0) {
                    flag = false
                    // console.log('여기오냐 계속?')
                    // 똑같은 실수를...
                    will_delete.push([i, j])
                }
            }
        }
        if (flag === true) {
            break
        }

        // console.log(will_delete)
        will_delete.forEach(dell => {
            const y = dell[0]
            const x = dell[1]
            for (let i = 0; i < 2; i++) {
                for (let j = 0; j < 2; j++) {
                    const idy = y + i
                    const jdx = x + j
                    if (board[idy][jdx] !== 0) {
                        answer += 1
                    }
                    board[idy][jdx] = 0
                }
            }
        });
        // console.log(board)

        // 이거는 좀 대박인거같은데... 바꿔도 주소값 차이 없겠지??...
        // const new_board = Array(m).fill(Array(n).fill(0))
        const new_board = new Array(m);
        for (let q = 0; q < m; q++) {
            new_board[q] = new Array(n).fill(0);
        }
        // 이렇게 하면 된다!

        for (let i = 0; i < n; i++) {
            const stack = Array()
            for (let j = m - 1; j >= 0; j--) {
                if (board[j][i] !== 0) {
                    stack.push(board[j][i])
                }
            }
            // console.log(stack)
            for (let k = 0; k < stack.length; k++) {
                new_board[m - 1 - k][i] = stack[k]
            }
        }
        // console.log(new_board)
        // wow 드디어...ㄷㄷ
        board = new_board
        // console.log(board)
        }
    console.log(answer)
    return answer;
}

solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF'])
// solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'])