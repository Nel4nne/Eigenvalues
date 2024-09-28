from numpy import array, eye, zeros, tril, dot, sum, diag
from printing import Printer



def eigenvalues_LU(matrix: array, eps: float) -> array:
    # количество строк и столбцов в матрице
    n: int = matrix.shape[0]
    m: int = matrix.shape[1]
    # количество итераций алгоритма
    cnt_iter: int = 0
    # все элементы нижнетреугольной матрицы должны быть как можно ближе к 0
    # берется сумма всех элементов нижнетреугольной матрицы и сравнивается с eps по модулю
    while abs(sum(tril(matrix, -1))) > eps:
        try:
            # получение LU-разложения матрицы
            L, U = simple_LU(matrix)
            # основной шаг алгоритма нахождения собственных значений
            matrix: array = dot(a=U, b=L)
            cnt_iter += 1
        except Exception as ex:
            raise ex
    Printer.print(f'Количество итераций: {cnt_iter}')
    Printer.print(f'Матрица после {cnt_iter} итераций:\n' + str(matrix))
    # результат - собственные значение стоят на главной диагонали
    return diag(matrix)


def simple_LU(matrix: array) -> tuple[array, array]:
    # константа для сравнения чисел с 0
    eps: float = 1e-10
    # количество строк и столбцов в матрице
    n: int = matrix.shape[0]
    m: int = matrix.shape[1]
    # нижнетреугольная матрица с единицами на главной диагонали
    L: array = eye(N=n, M=m)
    # верхнетреугольная матрица
    U: array = zeros(matrix.shape)
    for i in range(n):
        for j in range(m):
            # основной шаг алгоритма получения LU-разложения
            if i <= j:
                U[i][j] = matrix[i][j] - sum(L[i,0:i] * U[0:i, j])
            else:
                if abs(U[j][j]) < eps:
                    raise ZeroDivisionError(
                        "При получениее LU-разложения прозошло деление на 0: " +
                        "возможно для входной матрицы не выполнены необходимые условия."
                    ) 
                L[i][j] = 1 / U[j][j] * (matrix[i][j] - sum(L[i,0:i] * U[0:i, j]))
    return L, U