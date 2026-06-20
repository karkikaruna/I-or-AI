#include <stdio.h>
#include <stdlib.h>

int isSafe(char **board, int x, int y, int n) {
    int row, col;

    // Check column
    for (row = 0; row < x; row++) {
        if (board[row][y] == 'Q') {
            return 0;
        }
    }

    // Check top-left diagonal
    row = x;
    col = y;
    while (row >= 0 && col >= 0) {
        if (board[row][col] == 'Q') {
            return 0;
        }
        row--;
        col--;
    }

    // Check top-right diagonal
    row = x;
    col = y;
    while (row >= 0 && col < n) {
        if (board[row][col] == 'Q') {
            return 0;
        }
        row--;
        col++;
    }

    return 1;
}

int nQueen(char **board, int x, int n) {
    int col;

    // Successfully placed all queens
    if (x >= n) {
        return 1;
    }

    for (col = 0; col < n; col++) {
        if (isSafe(board, x, col, n)) {
            board[x][col] = 'Q';

            // Recur for next row
            if (nQueen(board, x + 1, n)) {
                return 1;
            }

            // Backtrack
            board[x][col] = ' ';
        }
    }

    return 0;
}

void printBoard(char **board, int n) {
    int i, j;

    printf("\nSolution:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%c ", board[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int n, i;

    printf("Enter number of Queens: ");
    scanf("%d", &n);

    char **board = (char **)malloc(n * sizeof(char *));

    for (i = 0; i < n; i++) {
        board[i] = (char *)malloc(n * sizeof(char));

        for (int j = 0; j < n; j++) {
            board[i][j] = ' ';
        }
    }

    if (nQueen(board, 0, n)) {
        printBoard(board, n);
    } else {
        printf("No Solution\n");
    }

    for (i = 0; i < n; i++) {
        free(board[i]);
    }
    free(board);

    return 0;
}