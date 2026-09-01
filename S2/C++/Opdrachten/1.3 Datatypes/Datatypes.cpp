// Sil Wever | Studenten nummer : 1921198
#include <iostream>
#include <string>

using namespace std;

#define PRINT(var) cout << #var << " = " << var << '\n'

void OpdrachtAB() {
    int x = 8.2; // 8
    int y = 18 / 5; // 3
    
    float e = 3.429; // 3.429
    float f = 18 / 5; // 3

    char a = 'a'; // a
    char b = 'e'; // e
    char c = b; // e

    bool r = true; // 1
    bool u = (1 & 0); // 0

    string p = "Klaar?"; // Klaar?
    string s = string("Nee, nog") + string(" niet"); // Nee, nog niet

    PRINT(x);
    PRINT(y);
    PRINT(e);
    PRINT(f);
    PRINT(a);
    PRINT(b);
    PRINT(c);
    PRINT(r);
    PRINT(u);
    PRINT(p);
    PRINT(s);
}

void OpdrachtCD() {
    int x = 8.2; // 8
    int y = 18 / 5; // 3
    int z = 18 / 5.0; // 3
    int f = '8' - '0'; // 8
    int e = 10 % 3; // 1
    
    float t = 18 / 5; // 3
    float s = 18 / 5.0; // 3.6

    char a = 'a'; // a
    char b = 'e'; // e
    char d = b; // e
    char c = 'b' + ('Z'- 'z'); // B

    bool r = true && (false || true); // 1
    bool u = 8 >= 10; // 0

    string p = "Utereg"; // Utereg - > Utereg Me Stadsie!
    p.append(" Me Stadsie!"); // Utereg Me Stadsie!
    string station = string("Heidel") + "berglaan"; // Heidelberglaan -> Heidelberg
    string plaats = station.erase(10, station.size()-10); // Heidelberg

    PRINT(x);
    PRINT(y);
    PRINT(z);
    PRINT(f);
    PRINT(e);
    PRINT(t);
    PRINT(s);
    PRINT(a);
    PRINT(b);
    PRINT(d);
    PRINT(c);
    PRINT(r);
    PRINT(u);
    PRINT(p);
    PRINT(station);
    PRINT(plaats);
}



int main() {
    cout << "Opdracht A+B\n\n";

    OpdrachtAB();
    
    cout << "\nExtra Opdracht C+D\n\n";
    
    OpdrachtCD();
}