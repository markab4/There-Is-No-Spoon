# Tests if a matrix is in Row Echelon Form / Reduced Row Echelon Form
# Mark Abramov

def isAll0s(matrixRow):
    for i in range (len(matrixRow)):
        if matrixRow[i] != 0:
            return False
    return True

def hasLeading1(matrixRow):
    for i in range (len(matrixRow)):
        if matrixRow[i] == 0:
            continue
        elif matrixRow[i] == 1:
            return True
    return False

def hasLeading1orIsAll0s(matrix):
    for row in matrix:
        if not (isAll0s(row) or hasLeading1(row)):
            return False
    return True

def are0edRowsAtBottom(matrix):
    for i in range (len(matrix)-1):
        if isAll0s(matrix[i]) and not isAll0s(matrix[i+1]):
            return False
    return True

def indexOfLeading1(matrixRow):
    for i in range (len(matrixRow)):
        if matrixRow[i] == 1:
            return i
    return -1

def areSuccessiveLeading1sToTheRight(matrix):
    for i in range (len(matrix)-1):
        if (indexOfLeading1(matrix[i]) >= indexOfLeading1(matrix[i+1])) and hasLeading1(matrix[i+1]):
            return False
    return True

def doColumnsWithLeading1sHave0sElsewhere(matrix):
    for row in matrix:
        leadingOneIndex = indexOfLeading1(row)
        if leadingOneIndex > -1:  ## if it has a leading one
            foundLeading1 = False
            for i in range (len(matrix)):
                if matrix[i][leadingOneIndex] != 0 and foundLeading1 == False:
                    foundLeading1 = True
                elif matrix[i][leadingOneIndex] != 0 and foundLeading1 == True:
                    return False
    return True

def isREF (matrix):
    return hasLeading1orIsAll0s(matrix) and are0edRowsAtBottom(matrix) and areSuccessiveLeading1sToTheRight(matrix)

def isRREF(matrix):
    return isREF(matrix) and doColumnsWithLeading1sHave0sElsewhere(matrix)

#Driver program. Takes a matrix as input from console. Tests if it is REF/RREF.
def main():
    rows = int(input('How many rows does your matrix have? '))
    columns = int(input('How many columns does your matrix have? '))
    matrix = []
    for i in range(rows):
        matrixRow = []
        for j in range(columns):
            matrixRow.append(int(input('Enter the entry for row ' + str(i + 1) +  ' and column ' + str(j + 1) + ': ')))
        matrix.append(matrixRow)
    print('You have entered the matrix: ' + str(matrix))
    print('Your matrix is ' + ('not ' if not isREF(matrix) else '') + 'in Row Echelon Echelon Form, and is ' + ('not ' if not isRREF(matrix) else '') + 'in Reduced Row Echelon Form.')

main()
