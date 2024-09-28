from numpy import array, loadtxt
from LU_factorisation import eigenvalues_LU



def main():
    # чтение матрицы из файла
    matrix: array = loadtxt("Examples/example1.txt")
    try:
        # получение собственных чисел
        eigenvalues: array = eigenvalues_LU(matrix, 1e-10)
        print(eigenvalues)
    except Exception as ex:
        print("ОШИБКА: ", ex)
    

if __name__ == '__main__':
    main()