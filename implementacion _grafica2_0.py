# Visualizacion de nonograma 3x3 a partir de
# una lista de literales. Cada literal representa una casilla del nonograma;
# el literal es positivo sii la casilla esta rellenada.

# Formato de la entrada: - las letras proposionales seran: chr(65, ..., 116);
#                        - solo se aceptan literales (ej. A, ~B, C, ~D, etc.)
# Requiere también un número natural, para servir de índice del nonograma,
# toda vez que pueden solicitarse varios nonogramas.

# Salida: archivo tablero_%i.png, donde %i es un número natural

#################
# importando paquetes para dibujar
print("Importando paquetes...")
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage

print("Listo!")


def dibujar_tablero(f, numero):
    # Visualiza un nonograma dada una formula f y los conjuntos de numeros que definen el nonograma
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen nonograma_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el nonograma
    step = 1. / 5
    tangulos = []
    # Creo los cuadrados oscuros en el tablero
    for i in range(5):

        tangulos.append(patches.Rectangle(*[(1 * step, i * step), step, step], \
                                          facecolor='lightslategrey'))
        tangulos.append(patches.Rectangle(*[(0 * step, i * step), step, step], \
                                          facecolor='lightslategrey'))
        tangulos.append(patches.Rectangle(*[(i * step, 4 * step), step, step], \
                                          facecolor='lightslategrey'))
        tangulos.append(patches.Rectangle(*[(i * step, 3 * step), step, step], \
                                          facecolor='lightslategrey'))

    # coloreo la esquina izquierda
    for i in range(2):
        for x in range(3,5):
            tangulos.append(patches.Rectangle(*[(i * step, x * step), step, step], \
                                              facecolor='black'))

    # Creo las líneas del tablero
    for j in range(7):
        locacion = j * step
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005], \
                                          facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1], \
                                          facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    # Cargando imagen de relleno color naranja
    arr_img = plt.imread("naranja.jpg", format='jpg')
    imagebox = OffsetImage(arr_img, zoom=0.043*1.75)
    imagebox.image.axes = axes

    arr_imgP = plt.imread("p.png", format='png')
    imageboxP = OffsetImage(arr_imgP, zoom=0.25)

    # Creando las direcciones en la imagen de acuerdo a literal

    #Direcciones de las casillas rellenadas
    direcciones = {}
    direcciones[chr(65)] = [8 * 0.063, 8 * 0.06]
    direcciones[chr(66)] = [11 * 0.0635, 8 * 0.06]
    direcciones[chr(67)] = [14 * 0.0645, 8 * 0.06]
    direcciones[chr(68)] = [8 * 0.063, 5 * 0.06]
    direcciones[chr(69)] = [11 * 0.0635, 5* 0.06]
    direcciones[chr(70)] = [14 * 0.0645, 5* 0.06]
    direcciones[chr(71)] = [8 * 0.063, 2 * 0.05]
    direcciones[chr(72)] = [11 * 0.0635, 2 * 0.05]
    direcciones[chr(73)] = [14 * 0.0645, 2* 0.05]
    #direccion de p
    direcciones[26] = [3 * 0.0625, 13 * 0.0625]

    #Direcciones de los numeros ubicados en las casillas p
    countx = 0
    for h in range(1, 4):
        for m in range(2):
            direcciones[1+countx] = [((5 + 3 * h) * 0.0625), ((15 - 3 * m) * 0.06)]
            countx += 1

    county = 0
    for g in range(1, 4):
        for n in range(2):
            direcciones[7 + county] = [((1+ 3.1 * n) * 0.067), ((11 - (g ) * 3) * 0.0625)]
            county += 1

    #cargando imagenes de los numeros
    num_img1 = plt.imread("1.png", format='png')
    imagebox1 = OffsetImage(num_img1, zoom=0.19*1.75)

    num_img2 = plt.imread("2.png", format='png')
    imagebox2 = OffsetImage(num_img2, zoom=0.19*1.75)

    num_img3 = plt.imread("3.png", format='png')
    imagebox3 = OffsetImage(num_img3, zoom=0.19*1.75)

    abP = AnnotationBbox(imageboxP, direcciones[26], frameon=False)
    axes.add_artist(abP)

    #ubicando las imagenes de los numeros con respecto a las letras proposicionales en p
    for l in range(1, 10):
        if f[chr(64+l)] != 0:
            ab = AnnotationBbox(imagebox, direcciones[chr(l+64)], frameon=False)
            axes.add_artist(ab)

    for m in range(1, 13):
        if f[chr(m+73)] != 0:
            abb2 = AnnotationBbox(imagebox1, direcciones[int(m)], frameon=False)
            axes.add_artist(abb2)

    for n in range(1, 6):
        if f[chr(n+85)] != 0:
            abb3 = AnnotationBbox(imagebox2, direcciones[int(n)], frameon=False)
            axes.add_artist(abb3)

    for n in range(1, 8):
        if f[chr(n+96)] != 0:
            abb3 = AnnotationBbox(imagebox2, direcciones[int(n+5)], frameon=False)
            axes.add_artist(abb3)

    for o in range(1, 13):      
        if f[chr(o+103)] != 0:
            abb4 = AnnotationBbox(imagebox3, direcciones[int(o)], frameon=False)
            axes.add_artist(abb4)

    fig.savefig("nonograma_" + str(numero) + ".png")

f={'A': 1, 'B': 0, 'C': 1, 'D': 0, 'E': 1, 'F': 0, 'G':1, 'H': 0, 'I': 1, 'J': 1, 'K':1, 'L': 1, 'M': 0, 'N': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 0, 'S': 1, 'T':1, 'U': 1, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 1, 'v': 1, 'w': 1,'à': 0, 'á': 1, 'â': 0, 'ã': 0, 'ä': 0, 'å': 0, 'æ': 0, 'ç': 0}
print(f.keys())
dibujar_tablero(f, 11)
