#include <boost/range/combine.hpp>
#include <vector>
#include <list>
#include <string>
using namespace std;

int main() {
    vector<int> a {4, 5, 6};
    double b[] = {7, 8, 9};
    list<string> c {"a", "b", "c"};
    for (auto tup : boost::combine(a, b, c, a)) {
        int x, w;
        double y;
        string z;
        boost::tie(x, y, z, w) = tup;
        printf("%d %g %s %d\n", x, y, z.c_str(), w);
    }

    return 0;
}