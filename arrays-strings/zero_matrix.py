import unittest

def zero_matrix(matrix):
    rows = [None] * len(matrix)
    cols = [None] * len(matrix[0])

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[row][col] == 0:
                rows[row] = True
                cols[col] = True

    for i, row in enumerate(rows):
        if row:
            matrix = nullifyRow(i, matrix)
    
    for i, col in enumerate(cols):
        if col:
            matrix = nullifyCol(i, matrix)
    return matrix

def nullifyRow(row, matrix):
    for col in range(0, len(matrix[0])):
        matrix[row][col] = 0
    return matrix

def nullifyCol(col, matrix):
    for row in range(0, len(matrix)):
        matrix[row][col] = 0
    return matrix

class Test(unittest.TestCase):
    def setUp(self):
        self.matrix = [[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23],[24,25,26,27,28,29],[30,31,32,33,34,35]]

    def test_nullifyRow(self):
        matrix = nullifyRow(4, self.matrix)
        self.assertEqual(matrix, [[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23],[0,0,0,0,0,0], [30,31,32,33,34,35]])

    def test_nullifyCol(self):
        matrix = nullifyCol(4, self.matrix)
        self.assertEqual(matrix, [[0,1,2,3,0,5],[6,7,8,9,0,11],[12,13,14,15,0,17],[18,19,20,21,0,23],[24,25,26,27,0,29],[30,31,32,33,0,35]])

    def test_zero_matrix(self):
        matrix = zero_matrix(self.matrix)
        m = zero_matrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
        self.assertEqual(matrix, [[0,0,0,0,0,0],[0,7,8,9,10,11],[0,13,14,15,16,17],[0,19,20,21,22,23],[0,25,26,27,28,29],[0,31,32,33,34,35]])
        self.assertEqual(m, [[0,0,2,0],[0,0,0,0],[1,0,1,5]])

if __name__=="__main__":
    unittest.main()
        