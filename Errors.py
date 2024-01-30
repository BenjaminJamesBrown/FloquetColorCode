import stim
import Navigation
import Edges

def Red_Edge_CNOT_1_NOISE(L, p):

    RedEdgeCNOTpairs1 = []

    for Hex in range(L*L):
        RedEdgeCNOTpairs1.append([15*Hex + 2, 15*Hex + 12])

        Hex1 = Navigation.HexBottomNeighbour(Hex,L)
        Hex2 = Hex
        RedEdgeCNOTpairs1.append([15*Hex1, 15*Hex2 + 13])

        RedEdgeCNOTpairs1.append([15*Hex + 4, 15*Hex + 14])

    Red_Z_Edge_CNOT1 = stim.Circuit()

    for edges in RedEdgeCNOTpairs1:
        Red_Z_Edge_CNOT1.append_operation("DEPOLARIZE2", edges, p)

    return Red_Z_Edge_CNOT1


def Red_Edge_CNOT_2_NOISE(L, p):

    RedEdgeCNOTpairs2 = []

    for Hex in range(L*L):

        Hex1 = Navigation.HexRightNeighbour(Hex, L)
        Hex2 = Hex
        RedEdgeCNOTpairs2.append([15*Hex1 + 5, 15*Hex2 + 12])

        RedEdgeCNOTpairs2.append([15*Hex + 3, 15*Hex + 13])

        Hex1 = Navigation.HexBottomLeftNeighbour(Hex, L)
        Hex2 = Hex
        RedEdgeCNOTpairs2.append([15*Hex1 + 1, 15*Hex2 + 14])

    Red_Edge_CNOT2 = stim.Circuit()

    for edges in RedEdgeCNOTpairs2:
        Red_Edge_CNOT2.append_operation("DEPOLARIZE2", edges, p)

    return Red_Edge_CNOT2

def Red_Edge_Qubit_Measurement_NOISE(L, p):

    RedEdgeMeasureSites = []

    for Hex in range(L*L):
        RedEdgeMeasureSites.append(15*Hex + 12)
        RedEdgeMeasureSites.append(15*Hex + 13)
        RedEdgeMeasureSites.append(15*Hex + 14)

    Single_Qubit_Measurements = stim.Circuit()

    Single_Qubit_Measurements.append_operation("X_ERROR", RedEdgeMeasureSites, p)

    return Single_Qubit_Measurements


def Green_Edge_CNOT1_NOISE(L, p):

    GreenEdgeCNOTpairs1 = []

    for Hex in range(L*L):
        GreenEdgeCNOTpairs1.append([15*Hex + 2, 15*Hex + 7])
        GreenEdgeCNOTpairs1.append([15*Hex + 4, 15*Hex + 9])
        GreenEdgeCNOTpairs1.append([15*Hex, 15*Hex + 11])

    Green_Z_Edge_CNOT1 = stim.Circuit()

    for edges in GreenEdgeCNOTpairs1:
        Green_Z_Edge_CNOT1.append_operation("DEPOLARIZE2", edges, p)

    return Green_Z_Edge_CNOT1

def Green_Edge_CNOT2_NOISE(L, p):

    GreenEdgeCNOTpairs2 = []

    for Hex in range(L*L):
        GreenEdgeCNOTpairs2.append([15*Hex + 1, 15*Hex + 7])
        GreenEdgeCNOTpairs2.append([15*Hex + 3, 15*Hex + 9])
        GreenEdgeCNOTpairs2.append([15*Hex + 5, 15*Hex + 11])

    Green_Z_Edge_CNOT2 = stim.Circuit()

    for edges in GreenEdgeCNOTpairs2:
        Green_Z_Edge_CNOT2.append_operation("DEPOLARIZE2", edges, p)

    return Green_Z_Edge_CNOT2


def Green_Edge_Qubit_Measurement_NOISE(L, p):

    GreenEdgeMeasureSites = []

    for Hex in range(L*L):
        GreenEdgeMeasureSites.append(15*Hex + 7)
        GreenEdgeMeasureSites.append(15*Hex + 9)
        GreenEdgeMeasureSites.append(15*Hex + 11)

    Green_Z_Edge_Qubit_Measurements = stim.Circuit()

    Green_Z_Edge_Qubit_Measurements.append_operation("X_ERROR", GreenEdgeMeasureSites, p)

    return Green_Z_Edge_Qubit_Measurements


def Blue_Edge_CNOT1_NOISE(L, p):

    BlueEdgeCNOTpairs1 = []

    for Hex in range(L*L):
        BlueEdgeCNOTpairs1.append([15*Hex, 15*Hex + 6])
        BlueEdgeCNOTpairs1.append([15*Hex + 2, 15*Hex + 8])
        BlueEdgeCNOTpairs1.append([15*Hex + 4, 15*Hex + 10])

    Blue_Z_Edge_CNOT1 = stim.Circuit()

    for edges in BlueEdgeCNOTpairs1:
        Blue_Z_Edge_CNOT1.append_operation("DEPOLARIZE2", edges, p)

    return Blue_Z_Edge_CNOT1


def Blue_Edge_CNOT2_NOISE(L, p):
    qHexRegister = []

    for k in range(L * L):
        HexagonQubitList = []
        HexagonQubitList.extend(range(15 * k, 15 * k + 15))
        qHexRegister.append(HexagonQubitList)

    BlueEdgeCNOTpairs2 = []

    for Hex in range(L*L):
        BlueEdgeCNOTpairs2.append([15*Hex + 1, 15*Hex + 6])
        BlueEdgeCNOTpairs2.append([15*Hex + 3, 15*Hex + 8])
        BlueEdgeCNOTpairs2.append([15*Hex + 5, 15*Hex + 10])

    Blue_Z_Edge_CNOT2 = stim.Circuit()

    for edges in BlueEdgeCNOTpairs2:
        Blue_Z_Edge_CNOT2.append_operation("DEPOLARIZE2", edges, p)

    return Blue_Z_Edge_CNOT2

def Blue_Edge_Qubit_Measurement_NOISE(L, p):
    qHexRegister = []

    for k in range(L * L):
        HexagonQubitList = []
        HexagonQubitList.extend(range(15 * k, 15 * k + 15))
        qHexRegister.append(HexagonQubitList)


    BlueEdgeMeasureSites = []

    for Hex in range(L*L):
        BlueEdgeMeasureSites.append(15*Hex + 6)
        BlueEdgeMeasureSites.append(15*Hex + 8)
        BlueEdgeMeasureSites.append(15*Hex + 10)

    Blue_Z_Edge_Qubit_Measurements = stim.Circuit()

    Blue_Z_Edge_Qubit_Measurements.append_operation("X_ERROR", BlueEdgeMeasureSites, p)

    return Blue_Z_Edge_Qubit_Measurements





def Noisy_Measure_Red_Pauli_Z_Edges(L, p):
    Red_Z_Edge_Measurements = stim.Circuit()

    Red_Z_Edge_Measurements += Red_Edge_Qubit_Measurement_NOISE(L, p)

    Red_Z_Edge_Measurements += Edges.Red_Edge_CNOT_1(L)

    Red_Z_Edge_Measurements += Red_Edge_CNOT_1_NOISE(L, p)

    Red_Z_Edge_Measurements += Edges.Red_Edge_CNOT_2(L)

    Red_Z_Edge_Measurements += Red_Edge_CNOT_2_NOISE(L, p)

    Red_Z_Edge_Measurements += Red_Edge_Qubit_Measurement_NOISE(L, p)

    Red_Z_Edge_Measurements += Edges.Red_Edge_Qubit_Measurement(L)

    return Red_Z_Edge_Measurements

def Noisy_Measure_Green_Pauli_Z_Edges(L, p):
    Green_Z_Edge_Measurements = stim.Circuit()

    Green_Z_Edge_Measurements += Green_Edge_Qubit_Measurement_NOISE(L,p)

    Green_Z_Edge_Measurements += Edges.Green_Edge_CNOT1(L)

    Green_Z_Edge_Measurements += Green_Edge_CNOT1_NOISE(L,p)

    Green_Z_Edge_Measurements += Edges.Green_Edge_CNOT2(L)

    Green_Z_Edge_Measurements += Green_Edge_CNOT2_NOISE(L, p)

    Green_Z_Edge_Measurements += Green_Edge_Qubit_Measurement_NOISE(L,p)

    Green_Z_Edge_Measurements += Edges.Green_Edge_Qubit_Measurement(L)



    return Green_Z_Edge_Measurements


def Depolarizing_Errors(L, p):


    Depolarizing_Errors = stim.Circuit()

    DataQubits = []

    for k in range(L*L):
        DataQubits.extend(range( 15*k, 15*k + 6))

    Depolarizing_Errors.append_operation("DEPOLARIZE1", DataQubits, p)

    return Depolarizing_Errors



def Noisy_Measure_Blue_Pauli_Z_Edges(L, p):
    Blue_Z_Edge_Measurements = stim.Circuit()

    Blue_Z_Edge_Measurements += Blue_Edge_Qubit_Measurement_NOISE(L, p)

    Blue_Z_Edge_Measurements += Edges.Blue_Edge_CNOT1(L)
    Blue_Z_Edge_Measurements += Blue_Edge_CNOT1_NOISE(L, p)

    Blue_Z_Edge_Measurements += Edges.Blue_Edge_CNOT2(L)
    Blue_Z_Edge_Measurements += Blue_Edge_CNOT2_NOISE(L, p)

    Blue_Z_Edge_Measurements += Blue_Edge_Qubit_Measurement_NOISE(L, p)


    Blue_Z_Edge_Measurements += Edges.Blue_Edge_Qubit_Measurement(L)

    return Blue_Z_Edge_Measurements



def Data_Qubit_NOISE(L, p):

    DataQubits = []

    for k in range(L*L):
        DataQubits.extend(range( 15*k, 15*k + 6))

    Data_Qubit_Noise = stim.Circuit()
    Data_Qubit_Noise.append_operation("X_ERROR", DataQubits, p)

    return Data_Qubit_Noise





def Noisy_Measure_Red_Pauli_X_Edges(L, p):

    Red_X_Edge_Measurements = stim.Circuit()

    Red_X_Edge_Measurements += Edges.Global_Hadamard(L)
    Red_X_Edge_Measurements += Noisy_Measure_Red_Pauli_Z_Edges(L, p)
    Red_X_Edge_Measurements += Edges.Global_Hadamard(L)

    return Red_X_Edge_Measurements



def Noisy_Measure_Green_Pauli_X_Edges(L, p):

    Green_X_Edge_Measurements = stim.Circuit()

    Green_X_Edge_Measurements += Edges.Global_Hadamard(L)
    Green_X_Edge_Measurements += Noisy_Measure_Green_Pauli_Z_Edges(L, p)
    Green_X_Edge_Measurements += Edges.Global_Hadamard(L)

    return Green_X_Edge_Measurements



def Noisy_Measure_Blue_Pauli_X_Edges(L, p):

    Blue_X_Edge_Measurements = stim.Circuit()

    Blue_X_Edge_Measurements += Edges.Global_Hadamard(L)
    Blue_X_Edge_Measurements += Noisy_Measure_Blue_Pauli_Z_Edges(L, p)
    Blue_X_Edge_Measurements += Edges.Global_Hadamard(L)

    return Blue_X_Edge_Measurements