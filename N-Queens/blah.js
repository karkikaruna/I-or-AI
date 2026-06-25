function isSafe(board, row, col, n){
    let i,j;
    for (i=0;i<row;i++){
        if (board[i][col]=='Q'){
            return false;
        }
    }

    for (i=row,j=col;i>=0&& j>=0; i--,j--){
        if(board[i][j]=='Q'){
            return false;
        }
    }
    for (i=row, j=col;i>=0 && j<n;i--, j++){
        if (board[i][j]=='Q'){
            return false;
        }
    }
  return true;

}
function nQueen(board, row, n){
    if (row>=n){
        return true;

    }
    for (let col=0;col <n;col++){
        if(isSafe(board, row, col, n)){
            board[row][col]='Q';
            if (nQueen(board, row+1, n)){
                return true;
            }

            board[row][col]='.';

        }
    }
    return false;
}

function printBoard(board, n){
    console.log("/nsolution: ");
    for (let i=0; i<n; i++){
        console.log(board[i].join(" "));
    }
}

const n=8;
const board=Array.from({length:n}, ()=>
Array(n).fill('.')
);
if (nQueen(board, 0,n)){
    printBoard(board,n);

}else{
    console.log("No solution");
}