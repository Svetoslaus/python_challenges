def get_matrix_product(a, b):
    if len(a[0]) != len(b):
        return None  # Matrices cannot be multiplied
    
    result = [[0] * len(b[0]) for _ in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    
    return result
