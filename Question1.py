import numpy as np  # Import numpy library for matrix operations

def read_matrices(filename):
    # Function to read matrices from a file
    with open(filename, 'r') as file:
        n, m = map(int, next(file).split())  # Read the dimensions of the matrices from the first line of the file
        matrices = []
        for i in range(n):
            matrix = [list(map(int, next(file).split())) for i in range(m)]  # Read each matrix from the file
            matrices.append(np.array(matrix))  # Convert the matrix to a numpy array and add it to the list
        return matrices  # Return the list of matrices

def main(filename):
    # Main function to perform matrix operations
    matrices = read_matrices(filename)  # Read matrices from the file
    max_det = None  # Initialize variable to store maximum determinant
    result_matrix = None  # Initialize variable to store the resulting matrix
    for i in range(len(matrices)):  # Iterate through the list of matrices
        for j in range(len(matrices)):
            if i != j:  # Ensure that i and j are not the same
                product = np.dot(matrices[i], matrices[j])  # Calculate the dot product of two matrices
                det = np.linalg.det(product)  # Calculate the determinant of the product
                if max_det is None or det > max_det:  # Check if the current determinant is greater than the maximum determinant
                    max_det = det  # Update the maximum determinant
                    if np.linalg.det(matrices[i]) > np.linalg.det(matrices[j]):  # Compare determinants of individual matrices
                        result_matrix = np.dot(matrices[i], matrices[j])  # Set result_matrix to the product of matrices[i] and matrices[j]
                    else:
                        result_matrix = np.dot(matrices[j], matrices[i])  # Set result_matrix to the product of matrices[j] and matrices[i]
                        
    inverted_matrix = np.linalg.inv(result_matrix)  # Calculate the inverse of the resulting matrix
    for row in inverted_matrix:  # Iterate through the rows of the inverted matrix
        print(' '.join(f'{val:.3f}' for val in row))  # Print each value in the row with 3 decimal places

