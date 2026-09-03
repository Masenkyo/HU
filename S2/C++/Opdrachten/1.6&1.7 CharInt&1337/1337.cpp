// Sil Wever | Studenten nummer : 1921198
#include <iostream>
#include <string>
using namespace std;

char CharInt(char c) {
    return char(c - 32);
}

int main() {
    string zin;
    cout << "Maak een zin: ";
    getline(cin, zin);

    for (int i = 0; i < zin.length(); i++) {
        if (zin[i] == 'e')
            zin[i] = '3';
        else if (zin[i] == 'l')
            zin[i] = '1';
        else if (zin[i] == 'o')
            zin[i] = '0';
        else if (zin[i] == 't')
            zin[i] = '7';
        else if (zin[i] == 's')
            zin[i] = '5';
        else if (zin[i] == 'a')
            zin[i] = '4';
        else if (zin[i] == 'b')
            zin[i] = '8';
        else if (zin[i] == 'g')
            zin[i] = '9';
        else if (zin[i] >= 'a' && zin[i] <= 'z')
            zin[i] = CharInt(zin[i]);
    }
    cout << zin;
}