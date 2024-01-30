import stim

import Navigation
import Printer
import QEC
import Decoder

import numpy as np
import networkx as nx
from pymatching import Matching



'''
Qubits are indexed on red hexagons. There are 15 qubits per hexagon The qubits are indexed as follows

    0---6---1
   /         \
 11           7
 /             \
5               2---12---
 \             /
 10           8
   \         /
    4---9---3
   /         \
  14         13
 /             \
 
'''

# We create a lattice of L x L red hexagons
L = 4



def Threshold_Evaluation(System_Size, Error_Rate):


    QEC_Circuit = stim.Circuit()

    QEC_Circuit += QEC.Floquet_Color_Code_Circuit(L = System_Size, p = Error_Rate)


    g = Decoder.Matching_Graph(L = System_Size, p = Error_Rate)


    m = Matching(g)

    Failures = 0
    Total_Samples = 10

    for sample in range(Total_Samples):

        Detector_Outcomes = QEC_Circuit.compile_detector_sampler().sample(1)[0]


        Logical_Outcome = Detector_Outcomes[-1]

        s = np.delete(Detector_Outcomes, -1)
        c = m.decode(s)

        Decoder_Outcome = Decoder.Read_Error_On_Logical(c, L = System_Size)

        if Decoder_Outcome != Logical_Outcome:
            Failures += 1

        if sample % 100 == 0:
            print("sample " + str(sample) + " failure rate = " + str(Failures / (sample+1)))

        Output_String = str(L) + " " + str(Error_Rate) + " " + str(Failures) + " " + str(Total_Samples)
    return Output_String


with open('Outputdata3.txt', 'w') as f:
    for L in range(16,17,4):
        print("L = " + str(L))
        for p in range(10):
            print("p = " + str(0.0024 + p * 0.0001))
            f.write(Threshold_Evaluation(System_Size=L, Error_Rate=0.0024 + p * 0.0001))

            f.write('\n')

    f.close()