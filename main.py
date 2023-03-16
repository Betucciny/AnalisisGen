import numpy as np
import matplotlib.pyplot as plt


def main():
    path = 'diffB/dif'
    binarios, tablab = archivo2array(path)
    mediab = np.mean(binarios, axis=0)
    print(mediab)

    path = 'diffE/difE'
    reales, tablar = archivo2array(path)
    mediar = np.mean(reales, axis=0)
    print(mediar)
    print(tablar)
    for nl, linea in enumerate(tablar):
        print(nl+1, end=' & ')
        for nc, num in enumerate(linea):
            if nc == len(linea) - 1:
                print(num, end=' \\\\')
            else:
                print(num, end=' & ')
        print()

    x = np.arange(1, 201, 1)
    plt.plot(x, mediab, label='Binomial')
    plt.plot(x, mediar, label='Exponencial')
    plt.show()


def archivo2array(path):
    datos = []
    tabla = []
    for i in range(30):
        archivo = open(path + '(' + str(i + 1) + ').txt', 'r')
        corrida = archivo.readline().split()
        var = archivo.readline().split()
        fo = archivo.readline().split()
        tabla.append(var+fo)
        datos.append(corrida)
        archivo.close()
    datos = np.array(datos, dtype=float)
    return datos, tabla


if __name__ == '__main__':
    main()
