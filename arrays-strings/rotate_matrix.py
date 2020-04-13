import unittest

def rotate_matrix(matrix):
    if len(matrix)==0:
        return 
    if len(matrix) != len(matrix[0]):
        return 

    N = len(matrix)
    layers = len(matrix) // 2

    for layer in range(0, layers):
        for pos in range(layer, N-1-layer):
            temp = matrix[layer][pos]
            matrix[layer][pos] = matrix[N-1-pos][layer]
            matrix[N-1-pos][layer] = matrix[N-1-layer][N-1-pos]
            matrix[N-1-layer][N-1-pos] = matrix[pos][N-1-layer]
            matrix[pos][N-1-layer] = temp

    return matrix

class Test(unittest.TestCase):
    def test_rotate_matrix_1(self):
        self.matrix = [[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23],[24,25,26,27,28,29],[30,31,32,33,34,35]]
        self.answer = [[30,24,18,12,6,0],[31,25,19,13,7,1],[32,26,20,14,8,2],[33,27,21,15,9,3],[34,28,22,16,10,4],[35,29,23,17,11,5]]
        self.assertEqual(rotate_matrix(self.matrix), self.answer)

    def test_rotate_matrix_2(self):
        self.matrix = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
        self.answer = [[20,15,10,5,0],[21,16,11,6,1],[22,17,12,7,2],[23,18,13,8,3],[24,19,14,9,4]]
        self.assertEqual(rotate_matrix(self.matrix), self.answer)


if __name__=="__main__":
    unittest.main()