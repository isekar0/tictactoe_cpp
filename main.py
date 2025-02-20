#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

typedef vector<vector<char>> square; 

class Board {
    private:
        int N = 3;
        int SIZE = N * N;
        char player;
        square grid;
        vector<int> valid_moves;
        bool is_terminal;
        
    public:
        char winner;

    Board(const int user_n) {
        if (user_n > 2 && user_n < 10) {
            initGridSize(user_n);
        }
        grid = initGrid();
        player = initRandPlayer();
        valid_moves = vector<int>(SIZE, 1);
        is_terminal = false;
        winner = 'n';
    }

    int getSize() {
        return SIZE;
    }

    char getPlayer() {
        return player;
    }

    square getGrid() {
        return grid;
    }
    
    vector<int> getValidMoves() {
        return valid_moves;
    }
    
    bool getIsTerminal() {
        return is_terminal;
    }
    
    void initGridSize(const int user_n) {
        N = user_n; 
        SIZE = N * N;
    }
    
    square initGrid() {
        square board = square(N, vector<char>(N, '.'));
        return board;
    }

    // Initialize starting player at random, x will be human and o will be computer.
    char initRandPlayer() {
        char player_ = '\0';
        int random_player_int = rand() % 2;
        switch (random_player_int) {
            case 0: player_ = 'x'; break;
            case 1: player_ = 'o'; break;
            default: initRandPlayer();
        }

        return player_;
    }

    void getOppositePlayer() {
        if (player == 'x') {
            player = 'o';
            return;
        }
        else if (player == 'o') {
            player = 'x';
            return;
        }
        else {
            cerr << "Invalid player value!" << endl;
            exit(EXIT_FAILURE);
        }
    }

    void printGrid() {
        vector<string> seperater_line(11 + 4 * (N - 3), "-"); // Found this to make nice lines
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << grid.at(i).at(j) << " | ";
            }
            cout << '\n';
            for (int j = 0; j < seperater_line.size(); j++) {
                cout << seperater_line.at(i);
            }
            cout << '\n';    
        }
    }

    void updateValidMoves() {
        vector<int> new_valid_moves(SIZE, 0);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (grid.at(i).at(j) == '.') {
                    new_valid_moves[N * i + j] = 1;
                }
            }
        }
        valid_moves = new_valid_moves;
    }

    void printValidActions() {
        cout << "Available Moves (by index): ";
        for (int i = 0; i < SIZE; i++) {
            if (valid_moves[i] == 1) {
                cout << i << ", ";
            }
        }
        cout << endl;
    }

    int getHumanAction() {
        int player_action = -1;
        do {
            cout << "Choose available index to play in [0 - " << SIZE - 1 << "]: "; 
            cin >> player_action;
        } while (valid_moves[player_action] != 1);

        return player_action;
    }

    int getComputerAction() {
        int computer_action = -1;
        vector<int> available_moves = vector<int>(0,0);
        
        for (int i = 0; i < SIZE; i++) {
            
            if (valid_moves.at(i) == 1) {
                available_moves.push_back(i);
            }
        }
        computer_action = rand() % available_moves.size();

        return available_moves[computer_action];
    }

    void updateIsTerminal() {
        if (checkWin()) {
            is_terminal = true;
            return;
        }
        
        bool emptyFound = false;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == '.') {
                    emptyFound = true;
                    break;
                }
            }
            if (emptyFound) break;
        }
        
        if (!emptyFound) {
            is_terminal = true;
            winner = 'd'; 
        } else {
            is_terminal = false;
        }
    }
    

    bool checkWin() {
        for (int i = 0; i < N; i++) {
            char first = grid[i][0];
            if (first == '.') continue; 
            bool win = true;
            for (int j = 1; j < N; j++) {
                if (grid[i][j] != first) {
                    win = false;
                    break;
                }
            }
            if (win) {
                winner = first;
                return true;
            }
        }
        
        for (int j = 0; j < N; j++) {
            char first = grid[0][j];
            if (first == '.') continue; 
            bool win = true;
            for (int i = 1; i < N; i++) {
                if (grid[i][j] != first) {
                    win = false;
                    break;
                }
            }
            if (win) {
                winner = first;
                return true;
            }
        }
      
        char first = grid[0][0];
        if (first != '.') {
            bool win = true;
            for (int i = 1; i < N; i++) {
                if (grid[i][i] != first) {
                    win = false;
                    break;
                }
            }
            if (win) {
                winner = first;
                return true;
            }
        }
        
        first = grid[0][N - 1];
        if (first != '.') {
            bool win = true;
            for (int i = 1; i < N; i++) {
                if (grid[i][N - 1 - i] != first) {
                    win = false;
                    break;
                }
            }
            if (win) {
                winner = first;
                return true;
            }
        }
        
        return false;
    }
    
    void playAction(const int action) {
        int column = 0, row = 0;
        column = action % N;
        row = action / N;
        grid.at(row).at(column) = player;
    }
};

void game() {
    int user_n = 3;
    char play_again = '\0';
    cout << "Let's play Tic Tac Toe!" << endl;
    cout << "What size board would you like to play in: ";
    cin >> user_n;
    if (user_n < 2 || user_n > 10) {
        cout << "Please be reasonable! Board size will default to 3!" << endl;
        user_n = 3;
    }
    
    Board tictactoe(user_n);
    
    while (!tictactoe.getIsTerminal()) { 
        tictactoe.updateValidMoves();
        
        int action = -1;
        if (tictactoe.getPlayer() == 'x') {
            cout << "Your turn!" << endl;
            tictactoe.printGrid();
            tictactoe.printValidActions();
            action = tictactoe.getHumanAction();
        } else {
            action = tictactoe.getComputerAction();
        }
        
        tictactoe.playAction(action);
        tictactoe.updateIsTerminal();
        
        if (!tictactoe.getIsTerminal())
            tictactoe.getOppositePlayer();
    }
    tictactoe.printGrid();
    
    if (tictactoe.winner == 'd') {
        cout << "It's a draw!" << endl;
    } else {
        if (tictactoe.winner == 'x') {
            cout << "You win!" << endl;
        } else if (tictactoe.winner == 'o') {
            cout << "Computer wins!" << endl;
        }
    }
    
    while (play_again != 'y' && play_again != 'n') {
        cout << "Play again? (y/n): ";
        cin >> play_again;
        if (play_again != 'y' && play_again != 'n') {
            cout << "Please enter [y/n]..." << endl;
        }
    }
    
    if (play_again == 'y') {
        game();  
    } else {
        cout << "Bye bye!" << endl;
    }
}

int main(void) {
    srand(time(0));
    game();
    return 0;
}

