#include <iostream>
#include <vector>
using namespace std;


vector<int> vec;
int main() {
    int a, b;
    for(int k = 0; k < 100; k++) {
        for(int i = 0; i < 1000000; i++) vec.push_back(1);
        for(int i = 0; i < 1000000; i++) vec.pop_back();
    }
    cin >> a >> b;
    cout << a + b<< endl;
    return 0;
}
