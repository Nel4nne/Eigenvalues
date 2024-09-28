from numpy import array, loadtxt, set_printoptions
from LU_factorisation import eigenvalues_LU
from printing import Printer



def main():
    # чтение матрицы из файла
    matrix: array = loadtxt("Examples/example1.txt")
    # установка параметров формата вывода
    set_printoptions(precision=8, suppress=True, formatter={'all': lambda x: f'{x:0.8f}'})
    Printer.print("Входная матрица:\n" + str(matrix))
    try:
        # получение собственных чисел
        eigenvalues: array = eigenvalues_LU(matrix, 1e-10)
        Printer.print("Собственные значения:\n" + str(eigenvalues))
    except Exception as ex:
        print("ОШИБКА: ", ex)
    

if __name__ == '__main__':
    main()