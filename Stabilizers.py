import stim
import Navigation


def Blue_Stabilizers(L):

    Blue_Stabilizer_Detector = stim.Circuit()


    for block in range(L*L):
        Red_Edge_1 = -15*L*L + 3*block
        Red_Edge_2 = -15*L*L + 3*Navigation.HexTopRightNeighbour(block, L) + 1
        Red_Edge_3 = -15*L*L + 3*Navigation.HexTopRightNeighbour(block, L) + 2

        Green_Edge_1 = -3*L*L + 3*block
        Green_Edge_2 = -3*L*L + 3*Navigation.HexRightNeighbour(block, L) + 2
        Green_Edge_3 = -3*L*L + 3*Navigation.HexTopRightNeighbour(block, L) + 1



        Blue_Stabilizer_Detector.append_operation("DETECTOR", [stim.target_rec(Red_Edge_1), stim.target_rec(Red_Edge_2),
                                                               stim.target_rec(Red_Edge_3), stim.target_rec(Green_Edge_1),
                                                               stim.target_rec(Green_Edge_2),
                                                               stim.target_rec(Green_Edge_3)])

    return Blue_Stabilizer_Detector


def Green_Stabilizers(L):

    Green_Stabilizer_Detector = stim.Circuit()

    for block in range(L*L):
        Blue_Edge_1 = -15*L*L + 3*block + 1
        Blue_Edge_2 = -15*L*L + 3*Navigation.HexRightNeighbour(block, L) + 2
        Blue_Edge_3 = -15*L*L + 3*Navigation.HexBottomNeighbour(block, L)

        Red_Edge_1 = -3*L*L + 3*block
        Red_Edge_2 = -3*L*L + 3*block + 1
        Red_Edge_3 = -3*L*L + 3*Navigation.HexRightNeighbour(block, L) + 2

        Green_Stabilizer_Detector.append_operation("DETECTOR",
                                                   [stim.target_rec(Blue_Edge_1), stim.target_rec(Blue_Edge_2),
                                                    stim.target_rec(Blue_Edge_3), stim.target_rec(Red_Edge_1),
                                                    stim.target_rec(Red_Edge_2), stim.target_rec(Red_Edge_3)])

    return Green_Stabilizer_Detector


def Red_Stabilizers(L):

    Red_Stabilizer_Detector = stim.Circuit()

    for block in range(L*L):
        Green_Edge_1 = -15*L*L + 3*block
        Green_Edge_2 = -15*L*L + 3*block + 1
        Green_Edge_3 = -15*L*L + 3*block + 2

        Blue_Edge_1 = -3*L*L + 3*block
        Blue_Edge_2 = -3*L*L + 3*block + 1
        Blue_Edge_3 = -3*L*L + 3*block + 2

        Red_Stabilizer_Detector.append_operation("DETECTOR", [stim.target_rec(Green_Edge_1), stim.target_rec(Green_Edge_2),
                                                              stim.target_rec(Green_Edge_3), stim.target_rec(Blue_Edge_1),
                                                              stim.target_rec(Blue_Edge_2), stim.target_rec(Blue_Edge_3)])

    return Red_Stabilizer_Detector



