import pandas as pd

file_path = "data.xlsx"
raw_data = pd.read_excel(file_path)

def make_matrix(data):
    """
    Returns a 4x3x3x4 matrix of the data:
    data[i][j][k][a] represents the value of criterion k for alea a of variant j of action i.
    """
    matrix = []
    for i in range(len(data)):
        matrix.append(data.iloc[i].tolist())
    matrix = matrix[2:]

    D = [ # lines
        [ # variants
            [ # criteria
                [ # alea  for k in range(3)
                    round(matrix[3*i+j][4+3*a+k], 3) for a in range(4)
                ] for k in range(3)
            ] for j in range(3)
        ] for i in range(len(matrix)//3)
    ]

    C = [ # lines
            [
                matrix[3*i+j][3] for j in range(3)
            ] for i in range(len(matrix)//3)
    ]
    return matrix, D, C

def is_correct(A):
    """
    Returns True if A is a correct matrix of actions, False otherwise.
    """
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] not in [0, 1]:
                return False
            if A[i][j] == 1 and sum(A[i]) != 1:
                return False
    return True

def contrib(A, D, k, a):
    # assert is_correct(A)
    out = [0 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            out[i] += A[i][j] * D[i][j][k-1][a-1]
    return round(sum(out), 3)

def lex_ord(l1, l2):
    """
    Returns l1 < l2 in lexicographic order.
    """
    for i in range(len(l1)):
        if l1[i] > l2[i]:
            return False
        elif l1[i] < l2[i]:
            return True
    return False

def lex_ord_eq(l1, l2):
    """
    Returns l1 ≤ l2 in lexicographic order.
    """
    return l1 == l2 or lex_ord(l1, l2)

def lexmax(elements):
    # assert len(elements) > 0
    m = elements[0]
    for e in elements:
        if lex_ord(m, e): # m < e
            m = e
    return m

def cost(A, C):
    # assert is_correct(A)
    out = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            out += A[i][j] * C[i][j]
    return out

def get_actions(A, data):
    """
    Returns a list of the indices of the actions in A.
    """
    assert is_correct(A)
    out = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 1:
                out.append(data[3*i+j][2])
    return out

FULLDATA, D, C = make_matrix(raw_data)