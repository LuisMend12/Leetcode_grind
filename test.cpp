#include <iostream>

int main() {

    using namespace std;
    int x = 10;
    const int* px = &x;
    cout << "px = " << px << endl;
    cout << "*px = " << *px << endl;
    *px = 20;
    return 0;
}