import Ficheros
import Tokenizar


if __name__ == '__main__':
    texto_fichero = Ficheros.lee_fichero()
    texto_tokenizado = Tokenizar.tokeniza(texto_fichero)
    print(texto_fichero)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
