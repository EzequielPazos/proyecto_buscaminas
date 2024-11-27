import pygame
# def dibujar_tablero(matriz:list[list], coordenadas_tablero:tuple):
#     for fila in range(len(matriz)):
#         if fila != 0:   # modifico coordenadas para dibujar
#             coordenadas_tablero = list(coordenadas_tablero)
#             coordenadas_tablero[0] += ancho_cuadro
#             coordenadas_tablero[1] = 100
#             coordenadas_tablero = tuple(coordenadas_tablero)
#         for columna in range(len(matriz[fila])):
#             if matriz[fila][columna] == -1:    # mina
#                 pygame.draw.rect(display, COLOR_BLANCO, (coordenadas_tablero, dimensiones_cuadro))
#                 display.blit(imagen_tablero_mina, (coordenadas_tablero[0] + 35, coordenadas_tablero[1] + 15))
#             elif matriz[fila][columna] == 0:    # cuadro vacio
#                 pygame.draw.rect(display, COLOR_BLANCO, (coordenadas_tablero, dimensiones_cuadro))
#             else:
#                 pygame.draw.rect(display, COLOR_BLANCO, (coordenadas_tablero, dimensiones_cuadro))
#                 numero = fuente.render(f"{matriz[fila][columna]}", True, COLOR_NEGRO)
#                 display.blit(numero, (coordenadas_tablero[0] + 40, coordenadas_tablero[1] + 5))
            
#             # modifico coordenadas para dibujar
#             coordenadas_tablero = list(coordenadas_tablero)
#             coordenadas_tablero[1] += alto_cuadro
#             coordenadas_tablero = tuple(coordenadas_tablero)

def crear_casillas(matriz:list[list], coordenadas_tablero:tuple, ancho_cuadro:int, alto_cuadro:int, display, dimensiones_cuadro:tuple, color_1:tuple, color_2:tuple)->None:
    """Crea un tablero de casillas adaptable utilizando dos colores para intercalarse

    Args:
        matriz (list[list]): buscaminas
        coordenadas_tablero (tuple): coordenadas de origen del tablero
        ancho_cuadro (int): ancho de cada cuadro
        alto_cuadro (int): alto de cada cuadro
        display (_type_): superficie donde se refleja el tablero
        dimensiones_cuadro (tuple): dimensiones de cada cuadro (tamaño)
        color_1 (tuple): color 1 para las casillas
        color_2 (tuple): color 2 para las casillas
    """
    i = 0
    for fila in range(len(matriz)):
        if fila != 0:   # modifico coordenadas para dibujar
            coordenadas_tablero = list(coordenadas_tablero)
            coordenadas_tablero[0] += ancho_cuadro
            coordenadas_tablero[1] = 100
            coordenadas_tablero = tuple(coordenadas_tablero)
            i += 1
        for columna in range(len(matriz[fila])):
            if i % 2 == 0:
                pygame.draw.rect(display, color_1, (coordenadas_tablero, dimensiones_cuadro))
            else:
                pygame.draw.rect(display, color_2, (coordenadas_tablero, dimensiones_cuadro))
            
            coordenadas_tablero = list(coordenadas_tablero)
            coordenadas_tablero[1] += alto_cuadro
            coordenadas_tablero = tuple(coordenadas_tablero)
            i += 1