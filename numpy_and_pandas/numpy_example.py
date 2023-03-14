import numpy as np


def unidimensional_array():
    # 1-dimension array
    custom_list = [1, 3, 4, 5, 6]
    array_np = np.array(custom_list)
    print(array_np * 2)


def bidimensional_array():
    # 2-dimension array
    array = [[1, 3, 4, 5, 6], [1, 3, 4, 5, 6], [1, 3, 4, 5, 6]]
    array_np = np.array(array)
    print(array_np.ndim)  # dimensions number
    print(array_np.shape)  # array area
    print(array_np.size)  # elements
    print(array_np.dtype)  # data type
    print(array_np * 3)
    print(array_np[:, 3:5])  # Get from the column 3 (including it) to column 5 (not including it), from all rows
    print(array_np[(array_np % 2 == 0) & (array_np > 4)])  # Sort the array by all pair elements and greater than 4


def array_operations():
    array_a = np.array([[1, 2, 3], [4, 5, 6]])
    array_b = np.array([[1, 1, 1], [2, 2, 2]])

    # These operations sum every element (so they need to have the same size)
    print(array_b + array_a)
    print(array_b * array_a)
    print(np.min(array_a))
    print(np.max(array_a))
    print(np.mean(array_a))
    print(np.std(array_a))
    # The next operation works when the arrays' size are symmetrical (ex. 2x3 * 3x2)
    array_c = np.array([[1, 1], [2, 2], [3, 3]])
    print(array_a.dot(array_c))


def linear_equations():
    # x + 2y = 1
    # 3x + 5y = 2
    constants = np.array([[1, 2], [3, 5]])
    results = np.array([1, 2])

    print(np.linalg.solve(constants, results))


# unidimensional_array()
# bidimensional_array()
# array_operations()
linear_equations()
