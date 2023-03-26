import numpy as np
import matplotlib.pyplot as plt


def main():
    path = 'PSO/pso'
    FO, tabla = archivo2array(path)
    FO_mean = np.mean(FO, axis=0)
    for nl, linea in enumerate(tabla):
        print(nl + 1, end=' & ')
        for nc, num in enumerate(linea):
            if nc == len(linea) - 1:
                print(num, end=' \\\\')
            else:
                print(num, end=' & ')
        print()


    x = np.arange(1, 501)
    plt.plot(x, FO_mean, label='Binomial')
    plt.show()
    plt.clf()

    plt.plot(x[:50], FO_mean[:50], label='Binomial')
    plt.show()
    plt.clf()



def archivo2array(path):
    FO = []
    tabla = []
    for i in range(30):
        archivoFO = open(path + '(' + str(i + 1) + ').txt', 'r')
        datos = archivoFO.readline().split()
        FO.append(datos)
        archivoFO.close()
    return np.array(FO, dtype=float), tabla


if __name__ == '__main__':
    main()
