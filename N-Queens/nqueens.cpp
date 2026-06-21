#include <iostream>
#include <vector>

using namespace std;

bool isSafe(vector<vector<char>>& board, int x, int y, int n) {
    // Check column
    for (int row = 0; row < x; row++) {
        if (board[row][y] == 'Q')
            return false;
    }

    // Check top-left diagonal
    int row = x;
    int col = y;
    while (row >= 0 && col >= 0) {
        if (board[row][col] == 'Q')
            return false;
        row--;
        col--;
    }

    // Check top-right diagonal
    row = x;
    col = y;
    while (row >= 0 && col < n) {
        if (board[row][col] == 'Q')
            return false;
        row--;
        col++;
    }

    return true;
}

bool nQueen(vector<vector<char>>& board, int x, int n) {
    // Successfully placed all queens
    if (x >= n)
        return true;

    // Try each column in the current row
    for (int col = 0; col < n; col++) {
        if (isSafe(board, x, col, n)) {
            board[x][col] = 'Q';

            // Recur for next row
            if (nQueen(board, x + 1, n))
                return true;

            // Backtrack
            board[x][col] = ' ';
        }
    }

    return false;
}

int main() {
    int n;

    cout << "Enter number of Queens: ";
    cin >> n;

    vector<vector<char>> board(n, vector<char>(n, ' '));

    if (nQueen(board, 0, n)) {
        cout << "\nSolution:\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << (board[i][j] == 'Q' ? 'Q' : '.') << " ";
            }
            cout << endl;
        }
    } else {
        cout << "No Solution" << endl;
    }

    return 0;
}