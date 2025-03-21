bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    bool check[9] = {false};
    int i, j;

    // ROW CHECKS !!
    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            if (board[i][j] >= '0' && board[i][j] <= '9') {
                if (check[board[i][j] - '1'] == true)
                    return false;
                else
                    check[board[i][j] - '1'] = true;
            }
        }
        memset(check, 0, sizeof(check));
    }

    // COLUMNS CHECKS !!
    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            if (board[j][i] >= '0' && board[j][i] <= '9') {
                if (check[board[j][i] - '1'] == true)
                    return false;
                else
                    check[board[j][i] - '1'] = true;
            }
        }
        memset(check, 0, sizeof(check));
    }

    // 3x3 BOXES CHECKS !!
    int boxRow = 0 , boxCol = 0;
    for(boxRow = 0; boxRow < 9; boxRow +=3 ){
        for(boxCol = 0; boxCol < 9; boxCol +=3){
            for(i = 0; i < 3; i++){
                for(j = 0; j < 3; j++){
                    if(board[boxRow+i][boxCol+j] >= '0' && board[boxRow+i][boxCol+j] <= '9'){
                        if(check[board[boxRow+i][boxCol+j] - '1'] == true)
                            return false;
                        else
                            check[board[boxRow+i][boxCol+j] - '1'] = true;
                    }
                }
            }
            memset(check, 0, sizeof(check));
        }
    }

    return true;    
}