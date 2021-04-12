import random
import subprocess
import re


arrayPeriods = [2, 3, 5, 7, 11, 13, 17, 19, 23]

for period in arrayPeriods:
    colSize = period - 1
    rowSize = period
    dim = 2

    if dim == 1 and rowSize > 1:
        raise TypeError("Dim is 1 but rowSize is greater than 1.")

    randarrayFile = open(f"Results/Randarray_{colSize}x{rowSize}.txt", 'w')
    randarrayFile.write("Complexity\t\t\tAmount of 1's\n")
    for n in range(100):
        print(f"Computing array no. {n + 1} of size {colSize}x{rowSize}.txt")
        if n == 99:
            print()

        amountOnes = 0
        randarray = list()
        if dim == 1:
            for j in range(colSize):
                randentry = random.randint(0, 1)
                if randentry == 1:
                    amountOnes += 1

                randarray.append(f"{j} {randentry}")
        elif dim == 2:
            randarray = list(list())
            for i in range(rowSize):
                for j in range(colSize):
                    randentry = random.randint(0, 1)
                    if randentry == 1:
                        amountOnes += 1

                    randarray.append(f"{j} {i} {randentry}")

        randarrayStr = '\n'.join(randarray)
        arrayPeriodStr = f"{colSize}" if dim == 1 else f"{colSize} {rowSize}"

        stdIn = f"2\n{arrayPeriodStr}\n{randarrayStr}".encode("utf-8")

        process = subprocess.Popen([f'./mainDim{dim}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate(input=stdIn)

        stdout = stdout.decode("utf-8")
        complexity = re.search(re.compile(r"Complexity: (.*)"), stdout).groups()[0]

        randarrayFile.write(f"{' ' * 7}{complexity}\t\t\t\t{amountOnes}\n")
    randarrayFile.close()
