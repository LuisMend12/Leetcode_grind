char* intToRoman(int num) {
    int n[13] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    char* s[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    int i = 0;
    static char ch[20] = "\0";

    ch[0] = '\0';

    while (num > 0) {
        if (num>=n[i]) {
            strcat(ch, s[i]);
            num-=n[i];
        } else i++;
    }

    return ch;
}