import numpy as np
import networkx as nx
import Navigation


def Matching_Graph(L, p):

    g = nx.Graph()

    rounds = L+1

    for height in range(3*L + 1):

        layer = height * L * L
        layer_above = (height + 1) * L * L
        layer_two_above = (height + 2) * L * L

        for hex in range(L * L):

            vertex = layer + hex

            qubit_edge = 6*layer + 3*hex

            PHYS = 36 * p / 15

            w = np.log((PHYS * PHYS + (1 - PHYS) * (1 - PHYS)) / (2 * PHYS * (1 - PHYS)))

            if height % 3 == 0:

                g.add_edge(vertex, layer_above + hex, qubit_id = qubit_edge, weight=w)
                g.add_edge(vertex, layer_above + Navigation.HexTopNeighbour(hex, L), qubit_id = qubit_edge + 1, weight=w)
                g.add_edge(vertex, layer_above + Navigation.HexTopRightNeighbour(hex, L), qubit_id = qubit_edge + 2, weight=w)

            elif ((height + 2) % 3 == 0):

                g.add_edge(vertex, layer_above + Navigation.HexBottomNeighbour(hex, L), qubit_id = qubit_edge, weight=w)
                g.add_edge(vertex, layer_above + Navigation.HexRightNeighbour(hex, L), qubit_id = qubit_edge + 1, weight=w)
                g.add_edge(vertex, layer_above + hex, qubit_id = qubit_edge + 2, weight=w)


            elif ((height + 1) % 3 == 0):

                if height != 3 * rounds + 2:

                    g.add_edge(vertex, layer_above + Navigation.HexBottomLeftNeighbour(hex, L), qubit_id= qubit_edge, weight=w)
                    g.add_edge(vertex, layer_above + Navigation.HexLeftNeighbour(hex, L), qubit_id= qubit_edge + 1, weight=w)
                    g.add_edge(vertex, layer_above + hex, qubit_id= qubit_edge + 2, weight=w)



            qubit_edge = 6*layer + 3*L*L + 3*hex

            q = 38*p / 15
            #q = 3*p / 2
            w = np.log((1 - q) / q)

            if height % 3 == 0:

                g.add_edge(vertex, layer_two_above + hex, qubit_id= qubit_edge, weight=w)
                g.add_edge(vertex, layer_two_above + Navigation.HexRightNeighbour(hex, L), qubit_id= qubit_edge + 1, weight=w)
                g.add_edge(vertex, layer_two_above + Navigation.HexTopRightNeighbour(hex, L), qubit_id= qubit_edge + 2, weight=w)



            elif ((height + 2) % 3 == 0):

                    if height != (3 * rounds + 1):

                        g.add_edge(vertex, layer_two_above + Navigation.HexBottomNeighbour(hex, L), qubit_id= qubit_edge, weight=w)
                        g.add_edge(vertex, layer_two_above + Navigation.HexBottomLeftNeighbour(hex, L), qubit_id= qubit_edge + 1, weight=w)
                        g.add_edge(vertex, layer_two_above + hex, qubit_id= qubit_edge + 2, weight=w)


            elif ((height + 1) % 3 == 0):

                if height != 3 * rounds + 2:

                    g.add_edge(vertex, layer_two_above + hex, qubit_id= qubit_edge, weight=w)
                    g.add_edge(vertex, layer_two_above + Navigation.HexLeftNeighbour(hex, L), qubit_id= qubit_edge + 1, weight=w)
                    g.add_edge(vertex, layer_two_above + Navigation.HexTopNeighbour(hex, L), qubit_id= qubit_edge + 2, weight=w)



            else:
                print("ERROR: layer does not exist")

    return g


def Read_Error_On_Logical(c, L):

    height = L + 1

    No_Of_Flips_On_Logical = 0

    Logical_Support = []

    for layer in range(height):


        periodic_row = (L + 1 - layer) % L

        for hex in range(L):
            Logical_Support.append(18*L*L*layer + 3*L*periodic_row + 3*hex)

        for hex in range(L):
            Logical_Support.append(18*L*L*layer + 3*L*L + 3*L*periodic_row + 3*hex)
            Logical_Support.append(18*L*L*layer + 3*L*L + 3*L*periodic_row + 3*hex + 1)



        periodic_row = (L - layer) % L



        if layer != L:

            for hex in range(L):
                Logical_Support.append(18*L*L*layer + 6*L*L + 3*L*periodic_row + 3*hex)



            for hex in range(L):
                Logical_Support.append(18*L*L*layer + 9*L*L + 3*L*periodic_row + 3*hex)
                Logical_Support.append(18*L*L*layer + 9*L*L + 3*L*periodic_row + 3*hex + 1)



            for hex in range(L):
                Logical_Support.append(18*L*L*layer + 12*L*L + 3*L*periodic_row + 3*hex)


            for hex in range(L):
                Logical_Support.append(18*L*L*layer + 15*L*L + 3*L*periodic_row + 3*hex)
                Logical_Support.append(18*L*L*layer + 15*L*L + 3*L*periodic_row + 3*hex + 1)


    for site in Logical_Support:
        No_Of_Flips_On_Logical += c[site]

    No_Of_Flips_On_Logical = No_Of_Flips_On_Logical % 2

    return No_Of_Flips_On_Logical