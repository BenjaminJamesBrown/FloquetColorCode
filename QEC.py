import stim
import Edges
import Stabilizers
import Logical
import Errors
import Printer

def Floquet_Color_Code_Circuit(L, p):


    rounds = L

    Error_Probability = p

    Red_Z_Edge_Measurements = Edges.Measure_Red_Pauli_Z_Edges(L)
    Green_Z_Edge_Measurements = Edges.Measure_Green_Pauli_Z_Edges(L)
    Blue_Z_Edge_Measurements = Edges.Measure_Blue_Pauli_Z_Edges(L)

    Red_X_Edge_Measurements = Edges.Measure_Red_Pauli_X_Edges(L)
    Green_X_Edge_Measurements = Edges.Measure_Green_Pauli_X_Edges(L)
    Blue_X_Edge_Measurements = Edges.Measure_Blue_Pauli_X_Edges(L)

    Blue_Stabilizer_Measurements = Stabilizers.Blue_Stabilizers(L)
    Green_Stabilizer_Measurements = Stabilizers.Green_Stabilizers(L)
    Red_Stabilizer_Measurements = Stabilizers.Red_Stabilizers(L)


    Noisy_Red_Z_Edge_Measurements = Errors.Noisy_Measure_Red_Pauli_Z_Edges(L, Error_Probability)
    Noisy_Green_Z_Edge_Measurements = Errors.Noisy_Measure_Green_Pauli_Z_Edges(L, Error_Probability)
    Noisy_Blue_Z_Edge_Measurements = Errors.Noisy_Measure_Blue_Pauli_Z_Edges(L, Error_Probability)

    Noisy_Red_X_Edge_Measurements = Errors.Noisy_Measure_Red_Pauli_X_Edges(L, Error_Probability)
    Noisy_Green_X_Edge_Measurements = Errors.Noisy_Measure_Green_Pauli_X_Edges(L, Error_Probability)
    Noisy_Blue_X_Edge_Measurements = Errors.Noisy_Measure_Blue_Pauli_X_Edges(L, Error_Probability)

    Depolarizing_Errors = Errors.Depolarizing_Errors(L, Error_Probability)


    Data_Qubit_Errors = Errors.Data_Qubit_NOISE(L, Error_Probability)



    Initial_Stabilizer_Readout = stim.Circuit()
    Stabilizer_Readout = stim.Circuit()
    Final_Stabilizer_Readout = stim.Circuit()

    Initial_Stabilizer_Readout += Red_X_Edge_Measurements
    Initial_Stabilizer_Readout += Green_Z_Edge_Measurements
    Initial_Stabilizer_Readout += Blue_X_Edge_Measurements
    Initial_Stabilizer_Readout += Red_Z_Edge_Measurements
    Initial_Stabilizer_Readout += Green_X_Edge_Measurements
    Initial_Stabilizer_Readout += Blue_Z_Edge_Measurements


    Initial_Stabilizer_Readout += Data_Qubit_Errors




    Stabilizer_Readout += Noisy_Red_X_Edge_Measurements
    Stabilizer_Readout += Depolarizing_Errors

    Stabilizer_Readout += Noisy_Green_Z_Edge_Measurements
    Stabilizer_Readout += Depolarizing_Errors

    Stabilizer_Readout += Blue_Stabilizer_Measurements

    Stabilizer_Readout += Noisy_Blue_X_Edge_Measurements
    Stabilizer_Readout += Depolarizing_Errors


    Stabilizer_Readout += Noisy_Red_Z_Edge_Measurements
    Stabilizer_Readout += Depolarizing_Errors

    Stabilizer_Readout += Green_Stabilizer_Measurements

    Stabilizer_Readout += Noisy_Green_X_Edge_Measurements
    Stabilizer_Readout += Depolarizing_Errors

    Stabilizer_Readout += Noisy_Blue_Z_Edge_Measurements
    Stabilizer_Readout += Depolarizing_Errors

    Stabilizer_Readout += Red_Stabilizer_Measurements




    Final_Stabilizer_Readout += Data_Qubit_Errors

    Final_Stabilizer_Readout += Red_X_Edge_Measurements
    Final_Stabilizer_Readout += Green_Z_Edge_Measurements

    Final_Stabilizer_Readout += Blue_Stabilizer_Measurements

    Final_Stabilizer_Readout += Blue_X_Edge_Measurements
    Final_Stabilizer_Readout += Red_Z_Edge_Measurements

    Final_Stabilizer_Readout += Green_Stabilizer_Measurements

    Final_Stabilizer_Readout += Green_X_Edge_Measurements
    Final_Stabilizer_Readout += Blue_Z_Edge_Measurements

    Final_Stabilizer_Readout += Red_Stabilizer_Measurements



    Logical_Readout = stim.Circuit()

    Logical_Readout += Logical.Readout(rounds, L)

    Error_Correction_Circuit = stim.Circuit()



    Error_Correction_Circuit += Initial_Stabilizer_Readout

    Error_Correction_Circuit += Stabilizer_Readout * rounds

    Error_Correction_Circuit += Final_Stabilizer_Readout



    Error_Correction_Circuit += Logical_Readout

    return Error_Correction_Circuit