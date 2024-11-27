"""
ALUMNO: PAZOS ACEBAL EZEQUIEL


CREDITS:

MUSIC:
Song: Dosi & Aisake - Cruising [NCS Release]
Music provided by NoCopyrightSounds
Free Download/Stream: http://ncs.io/Cruising
Watch: http://ncs.lnk.to/CruisingAT/youtube

"""

def generar_matriz_aleatoria(cant_filas:int, cant_columnas:int, desde:int, hasta:int)->list:
    from random import randint
    
    lista = []
    for fila in range(cant_filas):
        fila = []
        for columnas in range(cant_columnas):
            numero = randint(desde, hasta)
            fila.append(numero)
        lista.append(fila)
    return lista

def generar_buscaminas(cant_filas:int, cant_columnas:int, cant_minas):
    from random import randint
    
    lista = []
    for fila in range(cant_filas):
        fila = []
        for columna in range(cant_columnas):
            fila.append(0)  # 0 -> no hay minas
        lista.append(fila)
    
    for mina in range(cant_minas):
        fila = randint(0, cant_filas-1)
        columna = randint(0, cant_columnas-1)
        while lista[fila][columna] == -1:   # si ya hay una mina ahi recalcular coordenadas
            fila = randint(0, cant_filas-1)
            columna = randint(0, cant_columnas-1)
        lista[fila][columna] = -1   # -1 -> MINA    
        
    return lista

# buscaminas = generar_buscaminas(8, 8, 10) # CONSTANTES FACIL_FILAS, FACIL_COLUMNAS para mayor claridad y modificacion?

# print(buscaminas)

def numerar_casillas(buscaminas:list[list]):
    
    #recorrer la matriz
    for fila in range(len(buscaminas)):
        for columna in range(len(buscaminas[fila])):
            
            flag_arriba = True
            flag_abajo = True
            flag_derecha = True
            flag_izquierda = True
            
            #verifico la casilla
            if buscaminas[fila][columna] == -1:  # si es una mina
                #verifico arriba
                if fila == 0: #si es la primera fila no tiene arriba
                    flag_arriba = False
                #verifico abajo
                if fila == len(buscaminas)-1: # si es la ultima fila no tiene abajo
                    flag_abajo = False
                #verifico derecha
                if columna == len(buscaminas[fila])-1:   # si es la ultima columna no tiene derecha
                    flag_derecha = False
                #verifico izquierda
                if columna == 0:    # si es la primera columna no tiene izquierda
                    flag_izquierda = False
                
                #calculo valores en orden 123  M = MINA
                #                         4M6
                #                         789
                
                #le sumo un +1 a todas las casillas de su alrededor que no sean minas
                
                #ESCRIBIR CONSTANTES? EJ: ARRIBA = FILA-1 PARA MAYOR CLARIDAD?
                
                if flag_arriba and flag_izquierda:
                    if buscaminas[fila-1][columna-1] != -1:
                        buscaminas[fila-1][columna-1] += 1
                if flag_arriba:
                    if buscaminas[fila-1][columna] != -1:
                        buscaminas[fila-1][columna] += 1
                if flag_arriba and flag_derecha:
                    if buscaminas[fila-1][columna+1] != -1:
                        buscaminas[fila-1][columna+1] += 1
                if flag_izquierda:
                    if buscaminas[fila][columna-1] != -1:
                        buscaminas[fila][columna-1] += 1
                if flag_derecha:
                    if buscaminas[fila][columna+1] != -1:
                        buscaminas[fila][columna+1] += 1
                if flag_abajo and flag_izquierda:
                    if buscaminas[fila+1][columna-1] != -1:
                        buscaminas[fila+1][columna-1] += 1
                if flag_abajo:
                    if buscaminas[fila+1][columna] != -1:
                        buscaminas[fila+1][columna] += 1
                if flag_abajo and flag_derecha:
                    if buscaminas[fila+1][columna+1] != -1:
                        buscaminas[fila+1][columna+1] += 1
                        
# numerar_casillas(buscaminas)

def guardar_archivo_csv(ruta:str, dato:str):
    with open(ruta, "w") as archivo:
        archivo.write(dato)

def dar_formato_csv(matriz:list) -> str:
    texto = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j != len(matriz[i]) -1:
                texto += str(matriz[i][j]) + ","
            else:
                texto += str(matriz[i][j]) + "\n"
    return texto

ruta = "NUEVO PLAN/Proyecto Pygame/buscaminas.csv"

# print(dar_formato_csv(buscaminas))

# guardar_archivo_csv(ruta, dar_formato_csv(buscaminas))

def encontrar_casilla(posicion_click, ancho_cuadro, alto_cuadro):
    fila = (posicion_click[0] - 25 ) // ancho_cuadro
    columna = (posicion_click[1] - 100) // alto_cuadro
    
    return [fila, columna]

import pygame, funciones_buscaminas

pygame.init()
pygame.mixer.init()


# DISPLAY
PANTALLA_ANCHO = 800
PANTALLA_ALTO = 600
RESOLUCION_PANTALLA = (PANTALLA_ANCHO, PANTALLA_ALTO)

display = pygame.display.set_mode(RESOLUCION_PANTALLA) # Ventana maximizable

pygame.display.set_caption("Buscaminas")

# IMAGENES
imagen_mina = pygame.image.load("NUEVO PLAN/Proyecto Pygame/assets/images/mine.png") # Cargando una imagen de una mina
pygame.display.set_icon(imagen_mina) # Creo el icono de la ventana principal
#imagen_mina_pixel = pygame.Surface.convert(imagen_mina) # Paso la imagen a formato pixel ya que es el mejor formato para aplicar blit a una imagen
imagen_mina = pygame.transform.scale(imagen_mina, (300, 300))
imagen_bg = pygame.image.load("NUEVO PLAN/Proyecto Pygame/assets/images/buscaminas_bg.jpg")
imagen_bg = pygame.transform.scale(imagen_bg, (PANTALLA_ANCHO, PANTALLA_ALTO))
imagen_tablero_mina = pygame.transform.scale(imagen_mina, (30, 30))
imagen_explosion = pygame.image.load("NUEVO PLAN/Proyecto Pygame/assets/images/explosion.png")
imagen_tablero_explosion = pygame.transform.scale(imagen_explosion, (50, 50))
imagen_flag = pygame.image.load("NUEVO PLAN/Proyecto Pygame/assets/images/flag.png")
imagen_tablero_flag = pygame.transform.scale(imagen_flag, (30, 30))

# SFX

# cancion en loop a definir

pygame.mixer.music.load("NUEVO PLAN/Proyecto Pygame/assets/sfx/musica_bg.mp3")
pygame.mixer.music.set_volume(0.1)  # 0.5 == 50%

# COLORES

COLOR_AZUL_CLARO = (127, 157, 235)
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)
COLOR_AMARILLO = (255, 255, 0)
COLOR_MAGENTA = (255, 0, 255)
COLOR_ROJO = (255, 0, 0)
COLOR_MARRON = (135, 116, 89)

# TEXTOS

fuente = pygame.font.SysFont("Arial", 40, bold=True)
texto_nivel = fuente.render("NIVEL", True, COLOR_NEGRO)
texto_jugar = fuente.render("JUGAR", True, COLOR_NEGRO)
texto_puntajes = fuente.render("PUNTAJES", True, COLOR_NEGRO)
texto_salir = fuente.render("SALIR", True, COLOR_NEGRO)
texto_titulo = fuente.render("BUSCAMINAS", True, COLOR_NEGRO)
texto_reiniciar = fuente.render("REINICIAR", True, COLOR_NEGRO)
texto_atras = fuente.render("ATRAS", True, COLOR_NEGRO)
texto_usuario = ""
pedir_nombre = fuente.render("Ingrese su nombre: ", True, COLOR_NEGRO)

# BOTONES
ANCHO_BOTON = 200
ALTURA_BOTON = 100
coordenadas_tablero = (25, 100)

clock = pygame.time.Clock()
corriendo = True
pantalla = "Inicio"
puntaje = "0000"
dificultad = "Facil"
buscaminas_generado = False
lista_casillas = []
lista_casillas_flag = []
ingresado = False
# SI NO EXISTE QUE PUNTUACIONES SEA ESTO
puntuaciones_csv = "usuario, puntaje"
# SINO QUE LEA EL CSV CON DATOS

pygame.mixer.music.play(-1)

while corriendo == True:
    
    #CHECKEO PANTALLA
        
    if pantalla == "Inicio":    # DENTRO DE LA PANTALLA INICIO
        
        #CHECKEO EVENTOS
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = pygame.mouse.get_pos()
                if posicion_click[0] >= 50 and posicion_click[0] <= (ANCHO_BOTON + 50):
                    if posicion_click[1] >= 25 and posicion_click[1] <=  125:
                        pantalla = "Niveles"
                    if posicion_click[1] >= 175 and posicion_click[1] <=  275:
                        pantalla = "Jugar"
                    if posicion_click[1] >= 325 and posicion_click[1] <=  425:
                        pantalla = "Puntajes"
                    if posicion_click[1] >= 475 and posicion_click[1] <=  575:
                        corriendo = False
                    # CAMBIAR A COLLIDEPOINT DE LOS BOTONES CLASS RECT
        # BG
        
        display.blit(imagen_bg, (0, 0))
        
        # TITULO
        
        display.blit(imagen_mina, (375, 25))    # Muestro imagen en superficie
        display.blit(texto_titulo, (415, 325))
        
        # BOTONES -------
        
        # NIVEL
        pygame.draw.rect(display, (COLOR_BLANCO), (50, 25, ANCHO_BOTON, ALTURA_BOTON), 0, 3)
        display.blit(texto_nivel, (60, (ALTURA_BOTON/2)))
        
        # JUGAR
        pygame.draw.rect(display, (COLOR_BLANCO), (50, 175, ANCHO_BOTON, ALTURA_BOTON), 0, 3)
        display.blit(texto_jugar, (60, 175 + (ALTURA_BOTON/2) - 25))
        
        # PUNTAJES
        pygame.draw.rect(display, (COLOR_BLANCO), (50, 325, ANCHO_BOTON, ALTURA_BOTON), 0, 3)
        display.blit(texto_puntajes, (60, 325 + (ALTURA_BOTON/2) - 25))
        
        # SALIR
        pygame.draw.rect(display, (COLOR_BLANCO), (50, 475, ANCHO_BOTON, ALTURA_BOTON), 0, 3)
        display.blit(texto_salir, (60, 475 + (ALTURA_BOTON/2) - 25))
        
        # ------------
        
    elif pantalla == "Niveles":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
                
        display.fill(COLOR_MAGENTA)
        
    elif pantalla == "Jugar":
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                botones = pygame.mouse.get_pressed(3)
                posicion_click = pygame.mouse.get_pos()
                if botones[0]: #click izquierdo
                    if boton_reinicio.collidepoint(posicion_click):
                        puntaje = "0000"
                        buscaminas_generado = False    # Asi se vuelve a generar uno
                        lista_casillas.clear()    # Limpio la lista de casillas que desmarque
                    if boton_atras.collidepoint(posicion_click):
                        pantalla = "Inicio"
                    #print(posicion_click)
                    if posicion_click[0] >= 25 and posicion_click[0] <= 25 + (ancho_cuadro * cantidad_columnas) and posicion_click[1] >= 100 and posicion_click[1] <= 100 + (alto_cuadro * cantidad_filas):
                        # DENTRO DEL TABLERO
                        
                        casilla_clickeada = encontrar_casilla(posicion_click, ancho_cuadro, alto_cuadro)
                        if casilla_clickeada not in lista_casillas:
                            lista_casillas.append(casilla_clickeada)
                        
                        
                        def checkear_casilla(buscaminas:list[list], casilla_clickeada:list, coordenadas_tablero:tuple, dimensiones_cuadro:tuple)->int:
                            coordenadas_tablero = list(coordenadas_tablero)
                            coordenadas_tablero[0] = casilla_clickeada[0] * dimensiones_cuadro[0] + 25
                            coordenadas_tablero[1] = casilla_clickeada[1] * dimensiones_cuadro[1] + 100
                            coordenadas_tablero = tuple(coordenadas_tablero)
                            
                            if buscaminas[casilla_clickeada[0]][casilla_clickeada[1]] == -1:
                                pygame.draw.rect(display, COLOR_ROJO, (coordenadas_tablero, dimensiones_cuadro))
                                display.blit(imagen_tablero_mina, (coordenadas_tablero[0] + 35, coordenadas_tablero[1] + 15))
                                display.blit(imagen_tablero_explosion, (coordenadas_tablero[0] + 20, coordenadas_tablero[1] + 5))
                                codigo = -1
                            elif buscaminas[casilla_clickeada[0]][casilla_clickeada[1]] == 0:    # cuadro vacio
                                pygame.draw.rect(display, COLOR_BLANCO, (coordenadas_tablero, dimensiones_cuadro))
                                codigo = 0
                            else:   # casilla numerada
                                pygame.draw.rect(display, COLOR_BLANCO, (coordenadas_tablero, dimensiones_cuadro))
                                numero = fuente.render(f"{buscaminas[casilla_clickeada[0]][casilla_clickeada[1]]}", True, COLOR_NEGRO)
                                display.blit(numero, (coordenadas_tablero[0] + 40, coordenadas_tablero[1] + 5))
                                codigo = numero
                            
                            return codigo

                if botones[2]: #click derecho
                    if posicion_click[0] >= 25 and posicion_click[0] <= 25 + (ancho_cuadro * cantidad_columnas) and posicion_click[1] >= 100 and posicion_click[1] <= 100 + (alto_cuadro * cantidad_filas):
                        casilla_clickeada = encontrar_casilla(posicion_click, ancho_cuadro, alto_cuadro)
                        if casilla_clickeada not in lista_casillas_flag:
                            lista_casillas_flag.append(casilla_clickeada)
                        else:
                            lista_casillas_flag.remove(casilla_clickeada)
        # BG     
        display.fill(COLOR_MARRON)
        
        # BOTONES ----
        
        # REINICIAR
        
        boton_reinicio = pygame.draw.rect(display, COLOR_BLANCO, (25, 25, 200, 50))
        display.blit(texto_reiniciar, (40, 25))
        
        #funcion de reinicio
        
        # ATRAS
        
        boton_atras = pygame.draw.rect(display, COLOR_BLANCO, (575, 25, 200, 50))
        display.blit(texto_atras, (620, 25))
        
        # ----
        
        # PUNTAJE
        
        fondo_puntaje = pygame.draw.rect(display, COLOR_AZUL_CLARO, (300, 25, 200, 50))
        texto_puntaje = fuente.render(f"{puntaje}", True, COLOR_NEGRO)
        display.blit(texto_puntaje, (365, 25))
        
        # TABLERO
        
        #checkear dificultad
        match dificultad:
            case "Facil":
                cantidad_filas = 8
                cantidad_columnas = 8
                cantidad_minas = 10
            case "Medio":
                cantidad_filas = 16
                cantidad_columnas = 16
                cantidad_minas = 40
            case "Dificil":
                cantidad_filas = 16
                cantidad_columnas = 30
                cantidad_minas = 100
        
        #generar tablero random
        #tamaño q depende de dificultad y de la pantalla
        
        ancho_cuadro = (PANTALLA_ANCHO - 50) // cantidad_columnas
        alto_cuadro = (PANTALLA_ALTO - 125) // cantidad_filas
        
        dimensiones_cuadro = (ancho_cuadro, alto_cuadro)
        
        if buscaminas_generado == False:
            buscaminas = generar_buscaminas(cantidad_filas, cantidad_columnas, cantidad_minas)
            numerar_casillas(buscaminas)
            buscaminas_generado = True
        
        #dibujar_tablero(buscaminas)
        
        funciones_buscaminas.crear_casillas(buscaminas, coordenadas_tablero, ancho_cuadro, alto_cuadro, display, dimensiones_cuadro, COLOR_AZUL_CLARO, COLOR_NEGRO)
        
        lista_libres = []
        
        if len(lista_casillas) > 0:
            for casilla in lista_casillas:       
                if checkear_casilla(buscaminas, casilla, coordenadas_tablero, dimensiones_cuadro) == -1:
                    #muerto
                    pygame.time.wait(1000)
                    pantalla = "Explosion"
                elif checkear_casilla(buscaminas, casilla, coordenadas_tablero, dimensiones_cuadro) == 0:
                    #vacio
                    #puntaje = (str(int(puntaje) + 1)).zfill(4)
                    lista_libres.append(casilla)
                    puntaje = str(len(lista_libres)).zfill(4)
                else:
                    #numero
                    #puntaje = (str(int(puntaje) + 1)).zfill(4)
                    lista_libres.append(casilla)
                    puntaje = str(len(lista_libres)).zfill(4)

        
        def flagear_casilla(casilla_clickeada:list, coordenadas_tablero:tuple, dimensiones_cuadro:tuple):
            coordenadas_tablero = list(coordenadas_tablero)
            coordenadas_tablero[0] = casilla_clickeada[0] * dimensiones_cuadro[0] + 25
            coordenadas_tablero[1] = casilla_clickeada[1] * dimensiones_cuadro[1] + 100
            coordenadas_tablero = tuple(coordenadas_tablero)
            
            display.blit(imagen_tablero_flag, (coordenadas_tablero[0] + 35, coordenadas_tablero[1] + 15))

        
        if len(lista_casillas_flag) > 0:
            for casilla_flag in lista_casillas_flag:
                if casilla_flag not in lista_casillas:
                    flagear_casilla(casilla_flag, coordenadas_tablero, dimensiones_cuadro)
        
    elif pantalla == "Puntajes":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
    
                
        display.fill(COLOR_ROJO)
    
    elif pantalla == "Explosion":
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    ingresado = True
                    buscaminas_generado = False
                    pantalla = "Inicio"
                elif evento.key == pygame.K_BACKSPACE:
                    texto_usuario = texto_usuario[0:-1]
                else:
                    texto_usuario += evento.unicode

        display.fill(COLOR_ROJO)
        
        rectangulo_nombre = pygame.draw.rect(display, COLOR_BLANCO, (250, 250, 310, 50))
        display.blit(pedir_nombre, (250, 200))
        superficie_texto = fuente.render(texto_usuario, True, COLOR_NEGRO)
        display.blit(superficie_texto, (250, 250))

        def usuario_puntaje_csv(puntuaciones_csv:str, usuario:str, puntaje:str)->str:
            texto = f"{usuario}, {puntaje}"
            return texto
        
        datos_csv = usuario_puntaje_csv(puntuaciones_csv, texto_usuario, puntaje)
        
        def guardar_archivo_csv(ruta:str, dato:str):
            with open(ruta, "w") as archivo:
                archivo.write(dato)
        
        if ingresado:
            guardar_archivo_csv("NUEVO PLAN/Proyecto Pygame/puntuaciones.csv", datos_csv)
        
    pygame.display.flip() # Actualizo display
    
    clock.tick(60) # 60 FPS limite
    
pygame.quit()