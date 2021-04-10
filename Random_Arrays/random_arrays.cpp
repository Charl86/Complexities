#include "MultiDimArray.cpp"
#include "Sequences.h"
#include "NTL/GF2.h"
#include <iostream>
#include <string>
#include <fstream>


using namespace std;


const unsigned int dim = 2;
typedef NTL::GF2 F;

template <typename F, int m>
const int populate2DArray(MultiDimArray<F, m> &, const int, const int);

void generateArrayFile(const int, const int);

int main() {
    srand(time(NULL));

    const int primeArray[] = {
       11
    };

    generateArrayFile(100, 1);
    // for (const int p : primeArray) {
    //     generateArrayFile(p - 1, p);
    // }

    return 0;
}

void generateArrayFile(const int colSize, const int rowSize) {
    ofstream outArrayFile;
    outArrayFile.open(
        "Results/RandomArrayResults/RARPrime_" + to_string(colSize) + "x" + to_string(rowSize) + ".txt"
    );

    blitz::TinyVector<int, dim> v(colSize, rowSize);

    outArrayFile << "Complexity" << string(10, ' ') << "Amount of 1's";
    for (int n = 0; n < 100; n++) {
        // cout << "Computing array no. " << (n + 1) << " of size " << colSize << "x" << rowSize;
        // if (n + 1 < 100) cout << endl; else cout << endl << endl;

        MultiDimArray<F, dim> A(v);
        const int onesCount = populate2DArray(A, colSize, rowSize);

        // A.complexity();
        A.RST_simple();
        cout << A.complexity() << endl;
        outArrayFile << endl << setw(10) << A.complexity() << setw(20) << onesCount;
        // A.print_array();
        // A.print_basis();
        cout << endl << endl;
        // outArrayFile << "Normalized:  " << A.normalized_complexity() << endl;
    }

    outArrayFile.close();
}

template <typename F, int m>
const int populate2DArray(MultiDimArray<F, m> &A, const int colSize, const int rowSize) {
    F zero(0);
    F one(1);
    int onesCount = 0;
    for (int i = 0; i < rowSize; i++) {
        for (int j = 0; j < colSize; j++) {
            blitz::TinyVector<int, dim> position(j, i);

            if (rand() % 2 == 0)
                A.set_at(position, zero);
            else {
                A.set_at(position, one);
                onesCount++;
            }
        }
    }

    return onesCount;
}
