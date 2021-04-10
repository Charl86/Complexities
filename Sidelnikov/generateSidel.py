import argparse
from sidelnikov import Sidelnikov
from sage.all import *


sidelParser = argparse.ArgumentParser(prog="sidelnikov")

sidelParser.add_argument(
    "-p", "--prime-power", help="specify prime power to be used for sequence",
    required=True, type=int
)

sidelParser.add_argument(
    "-a", "--generate-array", help="specify if 3d-array is to be generated",
    action="store_true"
)

sidelParser.add_argument(
    "-o", "--output", help="whether the result should be redirected to file",
    type=str, default=False
)

sidelParser.add_argument(
    "-v", "--verbose", help="specify verbosity of program", action="store_true"
)

args = sidelParser.parse_args()

prime_power = int(args.prime_power)

sidelnikov = Sidelnikov(prime_power)

if not args.generate_array:
    lines = []
    for t in range(len(sidelnikov.galoisFieldq))[1:]:
        if args.verbose:
            print(f"{t} {sidelnikov(t)}")
        if args.output:
            lines.append(f"{t} {sidelnikov(t)}")
    if args.output:
        outputFile = open(f"{args.output}.txt", 'w')

        outputFile.write("2\n")
        outputFile.write(f"{prime_power}\n")

        outputFile.write('\n'.join(lines))
        outputFile.close()
if args.generate_array:
    prime = prime_divisors(prime_power)[-1]
    T = matrix(ZZ, prime, prime)

    gfq = GF(prime_power, 'a')

    for elm in gfq:
        if elm != 0:
            elmCoeffs = elm.polynomial().list()

            if len(elmCoeffs) == 1:
                x = 0
            else:
                x = elmCoeffs[1]
            y = elmCoeffs[0]

            power = elm.log(gfq.primitive_element())

            T.add_to_entry(y, x, power)
        else:
            T.add_to_entry(0, 0, -1)

    # T.matrix_from_rows(reversed(range(prime)))

    A = list()
    for elm in gfq:
        elmCoeffs = elm.polynomial().list()

        if elm != 0:
            if len(elmCoeffs) == 1:
                i = 0
            else:
                i = elmCoeffs[1]
            j = elmCoeffs[0]
        else:
            i, j = 0, 0

        for k in range(prime_power - 1):
            if i == 0 and j == 0:
                entry = 0
            else:
                entry = sidelnikov((k - T[j % prime][i % prime]) % (prime_power - 1))

            coordentry = [(i,j,k), entry]

            if args.verbose:
                print(f"{i} {j} {k} {entry}")
            A.append(coordentry)

    if args.output:
        with open(f"{args.output}.txt", 'w') as outputFile:
            lines = []
            for tup, val in A:
                lines.append(f"{' '.join([str(i) for i in tup])} {val}")

            outputFile.write(f"2\n{prime} {prime} {prime_power - 1}\n")
            outputFile.write('\n'.join(lines))
