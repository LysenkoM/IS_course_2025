import numpy as np

def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n)


def cyclic123_array(n):
    """2. Генерирует numpy массив длины 3n, заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    return np.tile([1, 2, 3], n)


def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    return np.arange(1, 2 * n, 2)


def zeros_array_with_border(n):
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""
    arr = np.zeros((n, n))
    arr[[0, -1], :] = 1
    arr[:, [0, -1]] = 1
    return arr


def chess_board(n):
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    m = np.zeros((n, n))
    m[::2, ::2] = 1
    m[1::2, 1::2] = 1
    return m


def matrix_with_sum_index(n):
    """6. Создаёт n × n матрицу с (i,j)-элементами равными i+j."""
    rows = np.arange(n).reshape(-1, 1)
    cols = np.arange(n)
    return rows + cols


def cos_sin_as_two_rows(a, b, dx):
    """7. Вычислите cos(x) и sin(x) на интервале [a, b) с шагом dx,
    а затем объедините оба массива чисел как строки в один массив."""
    x = np.arange(a, b, dx)
    cos_x = np.cos(x)
    sin_x = np.sin(x)
    return np.vstack((cos_x, sin_x))


def compute_mean_rowssum_columnssum(A):
    """8. Для numpy массива A вычисляет среднее всех элементов, сумму строк и сумму столбцов."""
    return np.mean(A), np.sum(A, axis=0), np.sum(A, axis=1)


def sort_array_by_column(A, j):
    """9. Сортирует строки numpy массива A по j-му столбцу в порядке возрастания."""
    return A[A[:, j].argsort()]


def compute_integral(a, b, f, dx, method):
    """10. Считает определённый интеграл функции f на отрезке [a, b] с шагом dx 3-мя методами:
    method == 'rectangular' - методом прямоугольника
    method == 'trapezoidal' - методом трапеций
    method == 'simpson' - методом Симпсона
    """
    x = np.arange(a, b, dx)
    if method == 'rectangular':
        return np.sum(f(x)) * dx
    elif method == 'trapezoidal':
        return (np.sum(f(x)) + np.sum(f(x + dx))) * dx / 2
    elif method == 'simpson':
        if len(x) % 2 == 0:
            x = x[:-1]
        y = f(x)
        return (np.sum(f(x)) + np.sum(f(x + dx))) * dx / 2