#include <iostream>
#include <random/discrete-uniform.h>
#include <NTL/GF2.h>


using namespace std;


int main() {
    NTL::GF2 F2;

    for (int i = 0; i < 10; i++) {
        cout << random(F2);
    }

    return 0;
}
