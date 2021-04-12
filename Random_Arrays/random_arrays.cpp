#include <iostream>
#include <string>
#include <fstream>
#include <random/discrete-uniform.h>
#include "MultiDimArray.cpp"
#include "Sequences.h"
#include "NTL/GF2.h"

using namespace std;
using namespace ranlib;


typedef NTL::GF2 F;

// template <typename F, int m>
// const int populate2DArray(MultiDimArray<F, m> &, const int, const int);

int main() {
    // srand(time(NULL));

    DiscreteUniform<int> discUniRand(2);
    discUniRand.seed((unsigned int)time(0));

    const int arrayPeriods[] = {
       2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
       14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
       24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
       44, 45, 46, 47, 48, 49, 50
    };

    for (const int period : arrayPeriods) {
        const unsigned int dim = 1;
        const int colSize = period;
        const int rowSize = 1;

        if (dim == 1 && rowSize != 1) {
            cout << "Error: dimension of 1 was specified, but rowSize value was greater than 1." << endl;
        }

        ofstream outArrayFile;
        outArrayFile.open(
            "Results/Randarray_" + to_string(colSize) + "x" + to_string(rowSize) + ".txt"
        );

        blitz::TinyVector<int, dim> v;
        if (dim == 1)
            v.;
        else
            blitz::TinyVector<int, dim> v(colSize, rowSize);

        outArrayFile << "Complexity" << string(10, ' ') << "Amount of 1's";
        for (int n = 0; n < 100; n++) {
            cout << "Computing array no. " << (n + 1) << " of size " << colSize << "x" << rowSize;
            if (n + 1 < 100)
                cout << endl;
            else
                cout << endl << endl;

            MultiDimArray<F, dim> A(v);

            F zero(0);
            F one(1);
            int onesCount = 0;
            for (int i = 0; i < rowSize; i++) {
                for (int j = 0; j < colSize; j++) {
                    if (dim == 1)
                        blitz::TinyVector<int, dim> position(j);
                    else
                        blitz::TinyVector<int, dim> position(j, i);

                    if (discUniRand.random() == 0)
                        A.set_at(position, zero);
                    else {
                        A.set_at(position, one);
                        onesCount++;
                    }
                }
            }

            // A.complexity();
            A.RST_simple();
            // cout << A.complexity() << endl;
            outArrayFile << endl << setw(10) << A.complexity() << setw(20) << onesCount;
            // A.print_array();
            // A.print_basis();
        }

        outArrayFile.close();
    }

    return 0;
}
