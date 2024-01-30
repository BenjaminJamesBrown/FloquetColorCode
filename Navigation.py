# Define functions to get the red hexagons coordinates.
# HexX gives the X coordinate of a red hexagon
def HexX(HexNumber, L):
    return HexNumber % L


# HexY gives the Y coordinate of a red hexagon
def HexY(HexNumber, L):
    return HexNumber // L


# Function to find the hexagon to the right of a given hexagon
def HexLeftNeighbour(HexNumber, L):
    X = HexX(HexNumber, L)
    Y = HexY(HexNumber, L)

    X = (X + L - 1) % L

    return L * Y + X



# Function to find the hexagon to the right of a given hexagon
def HexRightNeighbour(HexNumber, L):
    X = HexX(HexNumber, L)
    Y = HexY(HexNumber, L)

    X = (X + 1) % L

    return L * Y + X


# Function to find the hexagon above and to the right of a given hexagon
def HexTopNeighbour(HexNumber, L):
    X = HexX(HexNumber, L)
    Y = HexY(HexNumber, L)

    Y = (Y + L - 1) % L

    return L * Y + X


# Function to find the hexagon above and to the right of a given hexagon
def HexTopRightNeighbour(HexNumber, L):
    X = HexX(HexNumber, L)
    Y = HexY(HexNumber, L)

    X = (X + 1) % L
    Y = (Y + L - 1) % L

    return L * Y + X


# Function to find the hexagon underneath a given hexagon
def HexBottomNeighbour(HexNumber, L):
    X = HexX(HexNumber, L)
    Y = HexY(HexNumber, L)

    Y = (Y + 1) % L

    return L * Y + X


# Function to find a hexagon below and to the left
def HexBottomLeftNeighbour(HexNumber, L):
    X = HexX(HexNumber, L)
    Y = HexY(HexNumber, L)

    X = (X + L - 1) % L
    Y = (Y + 1) % L

    return L * Y + X
