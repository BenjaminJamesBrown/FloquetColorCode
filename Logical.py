import stim

def Readout(Rounds, L):



    Readout_Circuit = stim.Circuit()

    Readout_Qubits = []

    for qubits in range(L):
        Readout_Qubits.append(15*qubits + 5)
        Readout_Qubits.append(15*qubits + 2)


    Readout_Circuit.append_operation("M", Readout_Qubits)

    Detector_Sites = range(-2*L, 0)



    Record_Targets = []

    for a in Detector_Sites:
        Record_Targets.append(stim.target_rec(a))

    Number_Of_Rows = Rounds + 2

    for row in range(Number_Of_Rows):
        Edge_Locations = []

        Periodic_Row = row % L

        Start_Of_Measurement_Round = -(3 + 18*row)*L*L + 3*L*Periodic_Row - 2*L

        for edge in range(L):
            Edge_Locations.append(Start_Of_Measurement_Round + 3*edge + 2)
            Edge_Locations.append(Start_Of_Measurement_Round + 3*edge + 1)

        for a in Edge_Locations:
            Record_Targets.append(stim.target_rec(a))



        Edge_Locations = []

        Start_Of_Measurement_Round = -(9 + 18*row)*L*L + 3*L*Periodic_Row - 2*L

        for edge in range(L):
            Edge_Locations.append(Start_Of_Measurement_Round + 3 * edge + 2)
            Edge_Locations.append(Start_Of_Measurement_Round + 3 * edge + 1)

        for a in Edge_Locations:
            Record_Targets.append(stim.target_rec(a))



        Edge_Locations = []

        Periodic_Row = (row + 1) % L


        Start_Of_Measurement_Round = -(15 + 18*row)*L*L + 3*L*Periodic_Row - 2*L

        for edge in range(L):
            Edge_Locations.append(Start_Of_Measurement_Round + 3 * edge + 2)
            Edge_Locations.append(Start_Of_Measurement_Round + 3 * edge + 0)

        for a in Edge_Locations:
            Record_Targets.append(stim.target_rec(a))


    Readout_Circuit.append_operation("DETECTOR", Record_Targets)

    return Readout_Circuit