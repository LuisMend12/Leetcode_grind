#include <string.h>
void dfs(int *cnts, int types, int len, int *rs) {
    if (len == 0){
        (*rs)++;
        return;   
    }
    for (int i = 0; i < types; i++) {
        if (cnts[i]){
            cnts[i]--;
            dfs(cnts, types, len - 1, rs);
            cnts[i]++;
        }
    }
}


int numTilePossibilities(char* tiles) {
    int types = 0, charCnts[26] = {0}, cnts[7] = {0}, rs = 0;
    for (int i = 0; i < strlen(tiles); i++) charCnts[tiles[i] - 'A'] ++;

    for (int i = 0; i < 26; i++) {
        if (charCnts[i]) cnts[types++] = charCnts[i];
    }

    for (int i = 1; i <= strlen(tiles); i++) dfs(cnts, types, i, &rs);

    return rs;
}  