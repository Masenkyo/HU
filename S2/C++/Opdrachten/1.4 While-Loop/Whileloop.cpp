// Sil Wever | Studenten nummer : 1921198
#include <iostream>
using namespace std;

int main(){
    int number = 65;
    int loop = 0;
    while( number < 90){
        if(number < 70){
            number = 70;
        }else if( number < 80){
            number++;
        }
        number += 3;
        loop++;
        cout << "dit is loop: " << loop << " en het nummer is: " << number << '\n';
    }
}
// hij gaat op de eerste loop checken of hij kleiner is dan 70 en dat is hij dus hij word 70 gemaakt en +3 dus 73
// op de 2de loop gaat hij over die if statement en gaat hij naar else if kleiner dan 80, en dat is hij dus hij doet +1 en weer +3 = 77
// op de derde loop is hij nogsteeds onder de 80 dus krijgt hij weer +1 +3 = 81
// op de vierde loop doet hij alleen +3 omdat de if statements niet meer true zijn, dus 84
// op de 5de loop 87
// op de 6de loop 90, hij is nu groter dan 90 en de while loop kijkt of hij kleiner is dan 90 en dat is hij niet meer.
// De while loop gaat dus door 6 loops heen.