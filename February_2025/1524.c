#define MOD (int) (1e9 + 7)
int numOfSubarrays(int* arr, int arrSize) {
    int evenCnt = 0, oddCnt = 0;
    uint64_t rs = 0;
    for (int i = 0, temp; i < arrSize; i++) {
        if (arr[i] % 2) {
            temp = evenCnt;
            evenCnt = oddCnt;
            oddCnt = temp + 1;
        } else {
            evenCnt++;
        }
        rs = (rs + oddCnt) % MOD;
    }

    return (int)rs;
}