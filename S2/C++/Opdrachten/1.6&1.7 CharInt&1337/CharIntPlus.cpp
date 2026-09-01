#include <iostream>
using namespace std;

#define PRINT(var) cout << c << " + 32 = " << var << '\n'

int main() {
    char c;
    cout << "Enter a character: ";
    cin >> c;

    int som = c + 32;
    char somChar = char(som);
    
    PRINT(som);
    PRINT(somChar);
}