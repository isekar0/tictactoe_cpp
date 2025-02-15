#include <bits/stdc++.h>
#define endl '\n'
#define N 3 // Does not work for grids larger than 3x3
#define SIZE N * N
using namespace std;

typedef struct Action{
    int player;
    int index;
} Action;


Action getOppositePlayer(Action action) {
    action.player = -action.player;
    return action;
}

const vector<int> getValidMoves(const vector<int> grid) {
    vector<int> valid_moves(SIZE, 0);
    for (int i = 0; i < SIZE; i++) {
        if (grid[i] == 0) {
            valid_moves[i] = 1;
        }
    }

    return valid_moves;
}

void getAction(vector<int> &grid, Action &action, const vector<int> valid_moves) {
    bool played_succesfully = false;
    while (played_succesfully == false) {
        do {
            cout << "Player #" << action.player << ", please enter a valid move (index 0 - 8): ";
            cin >> action.index;
            cout << endl;
        } while (action.index < 0 || action.index > 8);

        // cout << "You chose to play in tile " << action.index << endl;
        if (valid_moves[action.index] == 1) {
            // cout << "played once" << endl;
            // cout << action.index << endl;
            // cout << grid << endl;

            grid[action.index] = action.player;
            played_succesfully = true;
            break;
        }
        else {
            cout << "Enter valid action!" << endl;
        }
    }
}
int getTerminal(const int player, const vector<int> grid, const vector<int> valid_moves) {
    // Check for draw
    int counter = 0;
    for (int i = 0; i < SIZE; i++) {
        if (valid_moves[i] == 0) {
            counter += 1;
        }
        if (counter == SIZE) {
            return -2;
        }
    }
    // Check n in row
    for (int i = 0; i < SIZE - 2; i++) {
        if ((grid[i] != 0 && grid[i + 1] != 0 && grid[i + 2] != 0) && (grid[i] == grid[i + 1] == grid[i + 2]))
            return player;
    }
    // Check n in column
    for (int i = 0; i < N; i++) {
        if ((grid[i] != 0 && grid[i + N] != 0 && grid[i + 2 * N] != 0) && (grid[i] == grid[i + N] == grid[i + 2 * N])) {
            return player;
        }
    }
    // Check n in diag
    if ((grid[0] != 0 && grid[N + 1] != 0 && grid[2 * N + 2] != 0) && (grid[0] == grid[N + 1] == grid[2 * N + 2])) {
        return player;
    }
    // Check n in diag opposite
    if ((grid[N - 1] != 0 && grid[2 * N - 2] != 0 && grid[3 * N - 3] != 0) && (grid[N - 1] == grid[2 * N - 2] == grid[3 * N - 3])) {
        return player;
    }
    else {
        return 0;
        }
}

void printGrid(vector<int> grid) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << grid[N * i + j] << " | ";
        }
        cout << "\n-----------" << endl;
    }
    // for (int i = 0; i < SIZE; i++) 
    //     cout << grid[i] << " | " << endl;
}

void printGrid(vector<int> grid, vector<int> valid_moves) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << grid[N * i + j] << " | ";
        }
        cout << "\n-----------" << endl;
    }
    cout << endl;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << valid_moves[N * i + j] << " | ";
        }
        cout << "\n-----------" << endl;
    }
}

int main(void) {
    int player = 1, winner = 0;
    bool played_succesfully = false;
    vector<int> grid(SIZE, 0), valid_moves(SIZE, 0);
    Action action = {player, -1};
    
    while (winner == 0) {
        valid_moves = getValidMoves(grid);
        printGrid(grid);

        cout << "***************** NEXT TURN **********************" << endl;
        getAction(grid, action, valid_moves); 
        action = getOppositePlayer(action);
            
        winner = getTerminal(player, grid, valid_moves);
    } 
    if (winner == 1 || winner == -1) {
        cout << "Winner is Player #" << winner << "!\n" << endl;
    }
    else {
        cout << "Draw!" << endl;
    }

    return 0;
}

