function solution(board, moves) {
    var answer = 0;
    const arr = []
    moves.forEach(a => {
        const doll = pickup(board, a - 1);
        if(doll){
            if(arr[arr.length - 1] === doll){
                arr.pop();
                answer += 2;
            } else {
                arr.push(doll);
            }
        }
        
    });
    console.log(answer)
    return answer;
}

function pickup(board, index) {
    const nboard = board;
    for (let i = 0; i < nboard.length; i++) {
        if (nboard[i][index] !== 0) {
            const doll = nboard[i][index];
            nboard[i][index] = 0;
            return doll;    
        }
    }
}

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])