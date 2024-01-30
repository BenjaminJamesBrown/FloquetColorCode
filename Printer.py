# Lattice printer. Adds the array 'Qubits' on qubit sites, and 'Syndrome' on hexagons

# A function that turns numbers into strings of length 4.
# It is used in the lattice printer function


def LengthFourString(String):
    OutputString = str(String)

    if len(OutputString) < 2:
        OutputString = " " + OutputString + "  "

    elif len(OutputString) < 3:
        OutputString = " " + OutputString + " "

    elif len(OutputString) < 4:
        OutputString = "" + OutputString + " "

    elif len(OutputString) < 5:
        OutputString = "" + OutputString + ""

    else:
        OutputString = "String length above 4"

    return OutputString



def Lattice(Qubits, Syndrome, L):
    print("Lattice printer")



    qHexRegister = []

    for k in range(L*L):
        HexagonQubitList = []
        HexagonQubitList.extend(range(15*k, 15*k+15))
        qHexRegister.append(HexagonQubitList)


    RowIndent = ""

    for y in range(L):

        Line1 = "  " + RowIndent
        Line2 = "  " + RowIndent
        Line3 = "  " + RowIndent
        Line4 = "  " + RowIndent
        Line5 = "" + RowIndent
        Line6 = "  " + RowIndent
        Line7 = "  " + RowIndent
        Line8 = "  " + RowIndent
        Line9 = "  " + RowIndent
        Line10 = "  " + RowIndent
        Line11 = "  " + RowIndent
        Line12 = "  " + RowIndent

        for x in range(L):
            Hexagon = L * y + x

            Qubit0 = LengthFourString(Qubits[qHexRegister[Hexagon][0]])
            Qubit6 = LengthFourString(Qubits[qHexRegister[Hexagon][6]])
            Qubit1 = LengthFourString(Qubits[qHexRegister[Hexagon][1]])

            Line1 += "  " + Qubit0 + "--" + Qubit6 + "--" + Qubit1 + "      " + Syndrome[3 * Hexagon + 1] + "     "
            Line2 += "  /              \               "

            Qubit11 = LengthFourString(Qubits[qHexRegister[Hexagon][11]])
            Qubit7 = LengthFourString(Qubits[qHexRegister[Hexagon][7]])

            Line3 += "" + Qubit11 + "             " + Qubit7 + "            "
            Line4 += "/                  \             "

            Qubit5 = LengthFourString(Qubits[qHexRegister[Hexagon][5]])
            Qubit2 = LengthFourString(Qubits[qHexRegister[Hexagon][2]])
            Qubit12 = LengthFourString(Qubits[qHexRegister[Hexagon][12]])

            Line5 += Qubit5 + "       " + Syndrome[3 * Hexagon] + "      " + Qubit2 + "--" + Qubit12 + "--"

            Qubit10 = LengthFourString(Qubits[qHexRegister[Hexagon][10]])
            Qubit8 = LengthFourString(Qubits[qHexRegister[Hexagon][8]])

            Line6 += "\                  /             "
            Line7 += "" + Qubit10 + "             " + Qubit8 + "            "
            Line8 += "  \              /               "

            Qubit4 = LengthFourString(Qubits[qHexRegister[Hexagon][4]])
            Qubit9 = LengthFourString(Qubits[qHexRegister[Hexagon][9]])
            Qubit3 = LengthFourString(Qubits[qHexRegister[Hexagon][3]])

            Line9 += "  " + Qubit4 + "--" + Qubit9 + "--" + Qubit3 + "      " + Syndrome[3 * Hexagon + 2] + "     "
            Line10 += "  /              \               "

            Qubit14 = LengthFourString(Qubits[qHexRegister[Hexagon][14]])
            Qubit13 = LengthFourString(Qubits[qHexRegister[Hexagon][13]])

            Line11 += "" + Qubit14 + "             " + Qubit13 + "            "
            Line12 += "/                  \             "

        print(Line1)
        print(Line2)
        print(Line3)
        print(Line4)
        print(Line5)
        print(Line6)
        print(Line7)
        print(Line8)
        print(Line9)
        print(Line10)
        print(Line11)
        print(Line12)

        RowIndent += "                 "

def PrintCNOTS(CNOTpairs, L):
    # Here we create a syndrome

    NoOfQubits = 15*L*L

    Syndrome = []

    for k in range(L * L):
        Syndrome.append(" R  ")
        Syndrome.append(" B  ")
        Syndrome.append(" G  ")


    CNOTgates = [" x "] * NoOfQubits

    EdgeNumber = 0

    for edges in CNOTpairs:
        ControlQubit = edges[0]
        TargetQubit = edges[1]

        CNOTgates[ControlQubit] = "C" + str(EdgeNumber)
        CNOTgates[TargetQubit] = "T" + str(EdgeNumber)
        EdgeNumber += 1

    Lattice(CNOTgates, Syndrome, L)
