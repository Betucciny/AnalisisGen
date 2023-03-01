import numpy as np
import matplotlib.pyplot as plt


def main():
    path = 'Binario/bin'
    binarios, tablab = archivo2array(path)
    mediab = np.mean(binarios, axis=0)
    print(mediab)
    print(tablab)

    path = 'Reales/reales'
    reales, tablar = archivo2array(path)
    mediar = np.mean(reales, axis=0)
    print(mediar)
    print(tablar)

    x = np.arange(1, 5001, 1)
    plt.plot(x, mediab, label='Binario')
    plt.plot(x, mediar, label='Real')
    plt.show()


def archivo2array(path):
    datos = []
    tabla = []
    for i in range(30):
        archivo = open(path + ' (' + str(i + 1) + ').txt', 'r')
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
