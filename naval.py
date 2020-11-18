import string as st
import random as rm
import copy as cy

MAXIMA_DIMENSION = 26
MINIMA_DIMENSION = 10
PROBABILIDAD_GANAR_DEFENSA = 0.30

PROTAGONISTAS = ["Sandokán y sus valientes amigos", "Armada británica"]

# Tanto las piezas de la Armada británica y de Sandokan, cuentan con la misma cantidad de piezas
# y dichas piezas, tienen el mismo tamaño
PIEZAS_TAMANIO = [6, 3, 2, 2, 1]
# Cada lista guarda relación con los protagonistas, y la cantidad de elementos de cada una
# coincide con la cantidad de elementos en PIEZAS_TAMANIO
PIEZAS_ORIENTACION = [["H", "V", "H", "V", ""], ["V", "H", "V", "H", ""]]

# PRE: 'dimension' debe ser un número entero positivo mayor o igual a 10 y menor o igual a 26
# POST: Devuelve una lista de listas, donde 'dimension' representa la cantidad de listas y la longitud de cada lista
def crear_tablero(dimension):
    """
    - Crea un tablero de dimensiones 'dimension' x 'dimension', y los elementos de dicha matriz
      se setean con '*'
    - El parámetro es considerado int
    - Retorna una lista de listas
    """
    tablero = []

    for x in range(dimension):
        fila = []

        for y in range(dimension):
            fila.append("*")

        tablero.append(fila)

    return tablero

# PRE: 'tablero' debe ser una lista de listas de dimensiones n x n
#      'defensas' es una lista de listas
#      'piezas' es una lista, que contiene dos listas
# POST: Imprime el 'tablero' e imprime el estado de las 'defensas', con sus respectivas descripciones,
#       que se encuentran almacenadas en 'piezas'
def imprimir_tablero(tablero, defensas, piezas):
    """
    - Imprime la lista de listas 'tablero', se le da formato al output de modo que,
      los títulos de las columnas se correspondan con las letras y las filas, con los números
    - Los parámetros 'tablero', 'defensas' y 'piezas', son considerados listas
    """
    letras = []

    letras = list(st.ascii_uppercase)

    for i in range(len(tablero)):
        if(i == 0):
            print(f"      {letras[i]}", end="")
        else:
            print(f"    {letras[i]}", end="")
            
    print()

    print(" " * 4 + "-" * len(tablero) * 5)

    for fila in range(len(tablero)):
        if(fila <= 8):
            print(f"0{fila + 1} |  {'    '.join(tablero[fila])}  |    {obtener_estado_defensa(tablero, defensas, piezas, fila)}")
        else:
            print(f"{fila + 1} |  {'    '.join(tablero[fila])}  |    {obtener_estado_defensa(tablero, defensas, piezas, fila)}")

    print(" " * 4 + "-" * len(tablero) * 5)

# PRE: 'tablero' debe ser una lista de listas de dimensiones n x n
#      'defensas' es una lista de listas
#      'piezas' es una lista, que contiene dos listas
#      'indice' es un int
# POST: Devuelve el 'estado' de una de las 'defensas', de acuerdo al 'indice'. Las coordenadas de dicha defensa
#       se contrastan con el tablero, para verificar si dichas casillas, han sido atacadas o no
def obtener_estado_defensa(tablero, defensas, piezas, indice):
    """
    - Imprime el estado de las 'defensas', con sus respectivas descripciones recuperadas de 'piezas'. Se contrasta
      las coordenadas de cada defensa con el 'tablero', con el fin de recuperar el contenido de dicha casilla. 
    - Los parámetros 'tablero', 'defensas' y 'piezas', son considerados listas e 'indice' como int
    - Retorna un String
    """
    estado = ""

    if(indice < len(defensas)):
        estado = f"{piezas[indice]}: "

        for coordenadas in range(len(defensas[indice])):
            estado += f"{tablero[defensas[indice][coordenadas][0]][defensas[indice][coordenadas][1]]} "

    return estado

# PRE: 'dimension' debe ser un String
# POST: Devuelve 'dimension' validado, de modo que solo tome valores entre las constantes
#       'MINIMA_DIMENSION' y 'MAXIMA_DIMENSION'
def validar_dimension(dimension):
    """
    - Valida la variable dimension, de modo que se encuentre entre las constantes
      'MINIMA_DIMENSION' y 'MAXIMA_DIMENSION'
    - El parámetro es considerado String
    - Retorna un String
    """
    flagValido = False

    while(not flagValido):
        if(validar_numero_acotado(dimension, MINIMA_DIMENSION, MAXIMA_DIMENSION)):
            flagValido = True
        else:
            print("\n====== ADVERTENCIA ======\n")
            print("Las dimensión del tablero solo puede tomar valores desde el {0}, hasta el {1}"
                .format(
                    MINIMA_DIMENSION,
                    MAXIMA_DIMENSION
                )
            )
            print("\n====== ADVERTENCIA ======\n")

            dimension = ingresar_dimension()

    return dimension

# PRE: 'opcion' debe ser un String
# POST: Devuelve 'opcion' validado, de modo que solo tome valores entre 0 y 1
def validar_opcion(opcion):
    """
    - Valida la variable opcion, de modo que se encuentre entre el 1 y la longitud
      de la lista constante 'PROTAGONISTAS'
    - El parámetro es considerado String
    - Retorna un String
    """ 
    flagValido = False

    while(not flagValido):
        if(validar_numero_acotado(opcion, 1, len(PROTAGONISTAS))):
            flagValido = True
        else:
            print("\n====== ADVERTENCIA ======\n")
            print("Las opciones válidas para los personajes son desde el {0}, hasta el {1}"
                .format(
                    1,
                    len(PROTAGONISTAS)
                )
            )
            print("\n====== ADVERTENCIA ======\n")

            opcion = ingresar_opcion()

    return opcion      

# PRE: 'numero' debe ser un String
#      'minimo' y 'maximo' deben ser int. El primero debe ser igual o menor, al segundo.
# POST: Devuelve el boolean 'esValido', el cual toma su valor determinando si el 'numero' es un int 
#       y si el 'numero' se encuentra comprendido entre los valores de 'minimo' y 'maximo'
def validar_numero_acotado(numero, minimo, maximo):
    """
    - Valida que la variable numero supere o iguale el valor de la variable 'minimo'
    - Valida que la variable numero sea menor o iguale el valor de la variable 'maximo'
    - El parámetro 'numero', es considerado String, el parámetro 'minimo' y 'maximo', int
    - Retorna un boolean
    """
    esValido = False

    # Primero valido que sea un número, para luego poder castearlo
    # y poder realizar la expresión booleana con limite
    if(numero.isdecimal()): 
        if(int(numero) >= minimo and int(numero) <= maximo):
            esValido = True

    return esValido

# PRE: -
# POST: Imprime la lista constante 'PROTAGONISTAS', solicita ingresar una 'opcion' y la misma es devuelta
def ingresar_opcion():
    """
    - Imprime los protagonistas almacenados en la lista constante 'PROTAGONISTAS'
    - Capta el ingreso del usuario y almacena el input en la variable 'opcion'
    - Retorna un String
    """
    opcion = ""

    print("-------- 1° JUGADOR --------")
    print("\nPersonajes disponibles\n")

    for indice in range(len(PROTAGONISTAS)):
        print(indice + 1, "-", PROTAGONISTAS[indice])

    opcion = input("\nIngrese el personaje con el que desea jugar: ")

    return opcion

# PRE: -
# POST: Solicita ingresar una 'dimension' y la misma es devuelta
def ingresar_dimension():
    """
    - Capta el ingreso del usuario y almacena el input en la variable 'dimension'
    - Retorna un String
    """
    dimension = ""

    dimension = input("\nIngrese la dimensión para el tablero: ")

    return dimension

# PRE: 'rangoMaximo' debe ser int, mayor o igual a 0
# POST: Devuelve un 'numeroAleatorio', el cual puede tomar valores entre 0 y el 'rangoMaximo' incluido
def generar_numero_aleatorio(rangoMaximo):
    """
    - Genera un número aleatorio entre el 0 y la variable 'rangoMaximo', incluyendolos
    - El parámetro 'rangoMaximo', es considerado int
    - Retorna un int
    """
    numeroAleatorio = 0

    numeroAleatorio = rm.randint(0, rangoMaximo)

    return numeroAleatorio

# PRE: -
# POST: Devuelve una lista de listas, donde cada lista tiene una longitud de elementos, dada por la lista constante
#       'PIEZAS_TAMANIO'
def generar_defensas():
    """
    - Genera una lista por cada posicion (x, y), acorde a la lista constante 'PIEZAS_TAMANIO', de una defensa y setea
      las coordenadas en (0, 0), la defensa en si es una lista, y las defensas creadas, se almacenan en la lista defensas
    - Retorna una lista
    """
    defensas = []

    for tamanio in PIEZAS_TAMANIO:
        defensa = []

        for posicion in range(tamanio):
            coordenadas = [0, 0]
            defensa.append(coordenadas)

        defensas.append(defensa)

    return defensas

# PRE: 'tablero' debe ser una lista de listas de dimensiones n x n
#      'defensa' debe ser una lista de listas
#      'indiceDefensa' es un int, guarda relación con 'defensa'
#      'protagonista' es un int, sólo puede tomar valores entre 0 y 1
# POST: Devuelve la 'defensa', a la cual se le definió sus coordenadas y el 'tablero', al cual
#       se le modificó el valor contenido en las coordenadas de la 'defensa'. El valor '*', pasa a 'O'
def posicionar_defensa(tablero, defensa, indiceDefensa, protagonista):
    """
    - Posiciona la 'defensa' en el 'tablero'. La lista 'defensa' guarda relación con la lista constante 'PIEZAS_ORIENTACION'
      por lo tanto, con 'indiceDefensa' obtenemos la orientación que le corresponde a dicha 'defensa'. Al misma tiempo
      con el 'protagonista' sabemos que orientaciones le corresponden para sus defensas
    - El parámetro 'tablero' y 'defensa' son considerados listas e 'indiceDefensa' y 'protagonista' como int
    - Retorna dos listas
    """
    longitudFilas = 0
    longitudColumnas = 0
    orientaciones = []
    flagPosicionado = False

    longitudFilas = len(tablero) - 1
    longitudColumnas = len(tablero[0]) - 1
    orientaciones = PIEZAS_ORIENTACION[protagonista]

    while(not flagPosicionado):
        posicionX = 0
        posicionY = 0

        posicionX = generar_numero_aleatorio(longitudColumnas)
        posicionY = generar_numero_aleatorio(longitudFilas)

        # - La primera condición evalua si se trata de las defensas originales del protagonista, de no serlo
        #   se considera que fueron defensas ganadas a partir de la 'partida especial'
        # - La segunda condición evalua si se está tratando con una defensa con orientación vertical u horizontal
        if(indiceDefensa < len(orientaciones) and orientaciones[indiceDefensa] != ""):
            if(orientaciones[indiceDefensa] == "H"):
                tablero, defensa, flagPosicionado = posicionar_defensa_horizontal(posicionY, posicionX, tablero, defensa, flagPosicionado)

            elif(orientaciones[indiceDefensa] == "V"):
                tablero = transponer_matriz(tablero)

                tablero, defensa, flagPosicionado = posicionar_defensa_horizontal(posicionX, posicionY, tablero, defensa, flagPosicionado)                    

                tablero = transponer_matriz(tablero)

                if(flagPosicionado): defensa = transponer_defensa_coordenadas(defensa)

        # Los casos que entran por aca son aquellas defensas que fueron ganadas a partir de la 'partida especial' y
        # y las defensas de longitud 1
        else:
            ubicacion = 0

            ubicacion = generar_numero_aleatorio(1)
            
            # Con ubicacion = 0, se posicionará la defensa horizontalmente
            if(ubicacion == 0):
                tablero, defensa, flagPosicionado = posicionar_defensa_horizontal(posicionY, posicionX, tablero, defensa, flagPosicionado)
            # Caso contrario, se posicionará la defensa verticalmente
            else:
                tablero = transponer_matriz(tablero)

                tablero, defensa, flagPosicionado = posicionar_defensa_horizontal(posicionX, posicionY, tablero, defensa, flagPosicionado)                    

                tablero = transponer_matriz(tablero)

                if(flagPosicionado): defensa = transponer_defensa_coordenadas(defensa)

    return tablero, defensa
    
# PRE: 'posicionY' y 'posicionX' deben ser int
#      'tablero' debe ser una lista de listas de dimensiones n x n
#      'defensa' debe ser una lista de listas
#      'flagPosicionado' debe ser un boolean
# POST: Devuelve la 'defensa', a la cual se le definió sus coordenadas, el 'tablero', al cual
#       se le modificó el valor contenido en las coordenadas de la 'defensa', el valor '*' pasa a 'O',
#       y 'flagPosicionado' el cual nos indica, si se pudo posicionar la 'defensa', en el 'tablero',
#       de manera exitosa
def posicionar_defensa_horizontal(posicionY, posicionX, tablero, defensa, flagPosicionado):
    """
    - Posiciona la 'defensa' horizontalmente en el 'tablero', en las coordenadas dadas por 'posicionY' y 'posicionX'
    - El parámetro 'tablero' y 'defensa' son considerados listas, 'posicionY' y 'posicionX' son int, 'flagPosicionado' es boolean
    - Retorna dos listas y un boolean
    """
    longitudColumnas = 0
    longitudDefensa = 0
    posicionFinal = 0

    longitudColumnas = len(tablero[0]) - 1
    longitudDefensa = len(defensa)
    posicionFinal = posicionX + longitudDefensa

    # - Dada la posicionFinal, evaluamos si la misma no supera longitudColumnas
    # - Sólo se tuvo en consideración la situación borde hacia la derecha, aunque también se podría
    #   agregar la lógica correspondiente para considerar la situación borde hacia la izquierda
    #TODO: Mejorar performance, agregando lógica para situación borde izquierda
    if(posicionFinal <= longitudColumnas):
        posiciones = []
        cantPosLibres = 0
        cantPosBombardeadas = 0

        posiciones = tablero[posicionY][posicionX : posicionFinal]
        cantPosLibres = posiciones.count("*")
        cantPosBombardeadas = posiciones.count("#")

        if(cantPosLibres == longitudDefensa or cantPosLibres + cantPosBombardeadas == longitudDefensa):
            tablero, defensa = setear_tablero_y_defensa(posicionY, posicionX, posicionFinal, tablero, defensa)
            flagPosicionado = True

    return tablero, defensa, flagPosicionado

# PRE: 'posicionY', 'posicionX', 'posicionFInal' deben ser int
#      'tablero' debe ser una lista de listas de dimensiones n x n
#      'defensa' debe ser una lista de listas
# POST: Devuelve la 'defensa', a la cual se le definió sus coordenadas y el 'tablero', al cual
#       se le modificó el valor contenido en las coordenadas de la 'defensa', el valor '*' pasa a 'O',
def setear_tablero_y_defensa(posicionY, posicionX, posicionFinal, tablero, defensa):
    """
    - Setea en el 'tablero' la 'defensa', en la fila 'posicionY' desde la columna 'posicionX' hasta
      la columna 'posicionFinal'
    - El parámetro 'tablero' y 'defensa' son considerados listas, 'posicionY', 'posicionX', 'posicionFinal' son int
    - Retorna dos listas
    """
    #TODO: Verificar si al setear una defensa ganada por 'partida especial', si se posiciona la misma en una zona
    #      que ya fue atacada, es decir '#', cambia su valor por 'O'. De ser así, será necesario agregar lógica 
    #      de modo que esa casilla siga con '#', en ese sentido no habría problema, ya que las coordenadas están
    #      guardadas en la defensa.
    for x in range(posicionX, posicionFinal):
        if(tablero[posicionY][x] != "X"):
            tablero[posicionY][x] = "O"
        
        # Lógica que se itera una sola vez, de modo que el rango sea de tipo (0, 1), (1, 2), (2, 3), etc
        for coordenada in range(x - posicionX, x - posicionX + 1):
            defensa[coordenada][0] = posicionY
            defensa[coordenada][1] = x

    return tablero, defensa

# PRE: 'matriz' debe ser una lista de listas de dimensiones n x n
# POST: Devuelve la 'matriz' tranpuesta, las filas pasan a ser columnas, y las columnas pasan a ser filas
def transponer_matriz(matriz):
    """
    - Transpone una 'matriz'. Las filas se convierten en columnas, y las columnas en filas
    - El parámetro 'matriz', es considerado una lista
    - Retorna una lista
    """
    longitudFilas = 0
    longitudColumnas = 0
    matrizTranspuesta = []

    longitudFilas = len(matriz)
    longitudColumnas = len(matriz[0])    

    for y in range(longitudColumnas):
        fila = []

        for x in range(longitudFilas):
            fila.append(matriz[x][y])

        matrizTranspuesta.append(fila)

    return matrizTranspuesta

# PRE: 'defensa' debe ser una lista de listas
# POST: Devuelve la 'defensa' tranpuesta, las coordenadas se invierten, es decir, de [x, y]
#       pasa a ser [y, x]
def transponer_defensa_coordenadas(defensa):
    """
    - Transpone las coordenadas de una 'defensa'. 'defensa' es una lista de listas, cada lista almacenada en ella
      tiene el formato [y, x], lo que se busca lograr es dar vueltas las coordenadas, es decir, [x, y]
    - El parámetro 'defensa', es considerado una lista
    - Retorna una lista
    """
    longitudFilas = 0
    longitudColumnas = 0
    defensaTranspuesta = []

    longitudFilas = len(defensa)
    longitudColumnas = len(defensa[0])  

    for y in range(longitudFilas):
        coordenadas = []

        for x in range(longitudColumnas):
            coordenadas.append(defensa[y][-1 + x])

        defensaTranspuesta.append(coordenadas)

    return defensaTranspuesta      

# PRE: 'tablero' debe ser una lista de listas de dimensiones n x n
#      'defensasOcultar' y 'defensasJugador' deben ser listas de listas
#      'piezasJugador' debe ser una lista
# POST: Imprime el 'tablero', en el cual se muestra el estado de las 'defensasJugador' y al mismo tiempo,
#       se ocultan las 'defensasOcultar', que pertenecen al oponente
def filtrar_defensas_jugador(tablero, defensasOcultar, defensasJugador, piezasJugador):
    """
    - Imprime el 'tablero', el cual es previamente filtrado para ocultar 'defensasOcultar'
    - El parámetro 'tablero', 'defensasOcultar', 'defensasJugador' y 'piezasJugador' son considerados listas
    """
    # Es necesario hacer una copia profunda de tablero, de otro modo, se podría hacer la copia con
    # tablero[:], pero es necesario iterar los elementos, que al misma tiempo son listas y se debe
    # aplicar también fila[:] 
    tableroFiltrado = cy.deepcopy(tablero)

    tableroFiltrado = ocultar_mostrar_defensas(defensasOcultar, tableroFiltrado, "O", "*")
    tableroFiltrado = ocultar_mostrar_defensas(defensasJugador, tableroFiltrado, "*", "O")

    imprimir_tablero(tableroFiltrado, defensasJugador, piezasJugador)

# PRE: 'defensas' debe ser una lista de listas
#      'tablero' debe ser una lista de listas de dimensiones n x n
#      'aOcultar' y 'aMostrar', deben ser String
# POST: Filtra el tablero, de modo que las 'defensas', que toman el valor de 'aOcultar'
#       en el 'tablero', tomen el valor a 'aMostrar'
def ocultar_mostrar_defensas(defensas, tablero, aOcultar, aMostrar):
    """
    - Los parámetros 'defensas' y 'tablero', son considerados listas, 'aOculstar' y 'aMostrar' son String
    - Retorna una lista
    """
    longitudFilas = 0
    longitudColumnas = 0

    longitudFilas = len(defensas)

    for defensa in range(longitudFilas):
        longitudColumnas = len(defensas[defensa])

        for coordenadas in range(longitudColumnas):
            y = defensas[defensa][coordenadas][0]
            x = defensas[defensa][coordenadas][1]

            if(tablero[y][x] == aOcultar): tablero[y][x] = aMostrar

    return tablero

# PRE: 'jugador1' y 'jugador2' deben ser int
# POST: Retorna el indice, de alguno de los 2 jugadores
def definir_primero_jugar(jugador1, jugador2):
    """
    - Define quien va a ser el jugador en jugar primero. Se generá un número aleatorio entre 0 y 1,
      dicho número se compara con jugador1 y jugador2, que tienen asignados un valor o el otro
    - Los parámetros 'jugador1' y 'jugador2', son considerados int
    - Retorna un int
    """
    decision = ""
    opcionesNo = ["NO", "N"]    
    jugadorIndice = 0
    numeroAleatorio = 0

    numeroAleatorio = generar_numero_aleatorio(1)

    #TODO: Analizar si es posible generar una función para evitar ésta estructura 'repetitiva'
    if(numeroAleatorio == jugador1):
        print("\n<------- ¡Jugador 1 salió sorteado! ------->\n")

        decision = ingresar_decision(jugador1)
        decision = validar_decision(decision, jugador1)

        if(decision in opcionesNo):
            jugadorIndice = jugador2

            print("\n<------- ¡Jugador 2 será el primero en jugar! ------->\n")
        else:
            jugadorIndice = jugador1

            print("\n<------- ¡Jugador 1 será el primero en jugar! ------->\n")

    elif(numeroAleatorio == jugador2):
        print("\n<------- ¡Jugador 2 salió sorteado! ------->\n")

        decision = ingresar_decision(jugador2)
        decision = validar_decision(decision, jugador2)

        if(decision in opcionesNo):
            jugadorIndice = jugador1

            print("\n<------- ¡Jugador 1 será el primero en jugar! ------->\n")
        else:
            jugadorIndice = jugador2

            print("\n<------- ¡Jugador 2 será el primero en jugar! ------->\n")

    return jugadorIndice

# PRE: 'decision' debe ser un String
#      'jugador' debe ser int
# POST: Devuelve 'decision' validado, de modo que solo tome valores de afirmación o negación
def validar_decision(decision, jugador):
    """
    - Valida la 'decision' ingresada por el 'jugador'. Constata de que únicamente se ingresen valores
      que han sido predefinidos y almacenados en las listas 'opcionesSi' y 'opcionesNo'
    - El parámetro 'jugador', es considerado int y 'decision' como String
    - Retorna un String
    """
    opcionesSi = ["SI", "S", "YES", "Y"]
    opcionesNo = ["NO", "N"]
    flagDecision = False

    while(not flagDecision):
        if(decision in opcionesSi or decision in opcionesNo):
            flagDecision = True
        else:
            print("\n====== ADVERTENCIA ======\n")
            print("Las únicas opciones válidas son:", " - ".join(opcionesSi), "-", " - ".join(opcionesNo))
            print("\n====== ADVERTENCIA ======\n")

            decision = ingresar_decision(jugador)

    return decision

# PRE: -
# POST: Solicita ingresar una 'decision' y la misma es devuelta
def ingresar_decision(jugador):
    """
    - Imprime un mensaje personalizado acorde al 'jugador' y capta la 'decision' del usuario. Dicho input
      se formatea a mayúsculas
    - El parámetro 'jugador', es considera int y 'decision' como String
    - Retorna un String
    """
    decision = ""

    decision = input(f"|Jugador| {PROTAGONISTAS[jugador]} - ¿Desea ser el primero en empezar <S/N>?").upper()

    return decision

# PRE: -
# POST: Devuelve el boolean 'hayPartidaEspecial', el cual tomará un determinado valor, acorde
#       a si un número aleatorio, se encuentra dentro del rango de la constante 'PROBABILIDAD_GANAR_DEFENSA'
def iniciar_partida_especial():
    """
    - Evalua si se va iniciar una 'partida especial'. Se genera un número aleatorio del 0 al 100, y el mismo
      se contrasta con la constante 'PROBABILIDAD_GANAR_DEFENSA'
    - Retorna un boolean
    """
    numeroAleatorio = 0
    hayPartidaEspecial = False

    numeroAleatorio = generar_numero_aleatorio(100)

    if(numeroAleatorio <= PROBABILIDAD_GANAR_DEFENSA * 100):
        hayPartidaEspecial = True

    return hayPartidaEspecial

# PRE: 'tablero' debe ser una lista de listas de dimensiones n x n
#      'defensa' deben ser lista de listas
# POST: Devuelve el 'tablero', en el cual, se eliminó la visualización de la 'defensa'
#       ,es decir, aquellas casillas con valor 'O', pasan a ser '*' y las casillas con
#       con valor 'X', pasan a ser '#'
def quitar_defensa_tablero(tablero, defensa):
    """
    - Elimina la visualización de la 'defensa' en el 'tablero'. Aquellas coordenadas almacenadas en 'defensa'
      que en el 'tablero' estén marcadas con 'O' pasarán a ser '*', y aquellas que estén marcadas con 'X'
      pasarán a ser '#'
    - Los parámetros 'tablero' y 'defensa', son considerados listas
    - Retorna una lista
    """
    posicionX = 0
    posicionY = 0

    for coordenada in range(len(defensa)):
        posicionY = defensa[coordenada][0]
        posicionX = defensa[coordenada][1]

        if(tablero[posicionY][posicionX] == "O"):
            tablero[posicionY][posicionX] = "*"

        elif(tablero[posicionY][posicionX] == "X"):
            tablero[posicionY][posicionX] = "#"

    return tablero

# PRE: 'deDefensas' y 'aDefensas' deben ser lista de listas
# POST: Devuelve las listas 'deDefensas', 'aDefensas' y el int 'indiceUltimaOcurrencia'.
#       Se debe sustraer la última defensa de 'deDefensas', es decir, la de menor tamaño,
#       y se adiciona la misma a 'aDefensas'. 'indiceUltimaOcurrencia' es la posición en donde
#       se inserto dicha defensa en a 'aDefensas'
def quitar_sumar_menor_defensa(deDefensas, aDefensas):
    """
    - Sustrae la defensa de menor longitud de 'deDefensas' y la adiciona a 'aDefensas'. Se tiene en consideración que,
      si se adiciona una defensa con una longitud n, donde en 'aDefensas' no existe una defensa con dicha longitud n,
      se ubicará la nueva defensa, en un punto intermedio o al final de las defensas. Caso contrario, de existir una defensa
      con dicha longitud n, en 'aDefensas', se posicionará la nueva defensa, como el último elemento de la misma longitud
    - Los parámetros 'deDefensas' y 'aDefensas', son considerados listas
    - Retorna dos listas y un int
    """
    defensaSacada = []
    longitudesDefensas = []
    longitudDefensa = 0
    indiceUltimaOcurrencia = 0
    
    defensaSacada = deDefensas.pop(-1)

    for defensa in range(len(aDefensas)):
	    longitudesDefensas.append(len(aDefensas[defensa]))

    longitudDefensa = len(defensaSacada)

    if(longitudDefensa in longitudesDefensas):
        indiceUltimaOcurrencia = len(longitudesDefensas) - 1 - longitudesDefensas[::-1].index(longitudDefensa)

        # Se suma 1 ya que, si bien se cuenta con el último índice de un determinado valor  
        # de la lista longitudDefensas, se buscar insertar la defensa sustraida, como el 
        # último elemento con ese mismo valor, y no que mueva la defensa correspondiente al
        # indiceUltimaOcurrencia hacía la derecha
        aDefensas.insert(indiceUltimaOcurrencia + 1, defensaSacada)

        indiceUltimaOcurrencia += 1
    else:
        # Se reutiliza la variable, para este caso, como no existe ninguna defensa con la misma
        # cantidad de coordenadas en la lista destino, se agregará dicha defensa en una posición
        # intermedia, teniendo en cuenta el valor de longitudDefensa.
        # De no existir alguna posición intermedia, la defensá se agregará al final de la lista

        for longitud in range(len(longitudesDefensas)):
            if(longitudesDefensas[longitud] > longitudDefensa):
                indiceUltimaOcurrencia = longitud + 1

        aDefensas.insert(indiceUltimaOcurrencia, defensaSacada)

    return deDefensas, aDefensas, indiceUltimaOcurrencia

# PRE: 'posicionY' debe ser un String
#      'tablero' debe ser una lista de listas de dimensiones n x n
# POST: Devuelve 'posicionY' validado, de modo que solo tome valores entre 1
#       y la longitud del 'tablero'
def validar_fila_elegida(posicionY, tablero):
    """
    - Valida la 'posicionY' ingresada por el jugador. Constata de que únicamente se ingresen valores
      que estén dentro de la longitud de la fila del 'tablero'
    - El parámetro 'posicionY' es considerado int, y 'tablero' como lista
    - Retorna un String
    """
    flagValido = False

    while(not flagValido):
        if(validar_numero_acotado(posicionY, 1, len(tablero))):
            flagValido = True
        else:
            print("\n====== ADVERTENCIA ======\n")
            print("Las opciones válidas para las filas son desde el {0}, hasta el {1}"
                .format(
                    1,
                    len(tablero)
                )
            )
            print("\n====== ADVERTENCIA ======\n")

            posicionY = ingresar_fila()

    return posicionY

# PRE: -
# POST: Solicita ingresar una 'fila' y la misma es devuelta
def ingresar_fila():
    """
    - Solicita el ingreso de la fila de la casilla a atacar
    - Retorn un String
    """
    posicionY = ""

    posicionY = input("Ingrese la fila de la casilla a la que desee atacar: ")

    return posicionY

# PRE: 'posicionX' debe ser un String
#      'tablero' debe ser una lista de listas de dimensiones n x n
# POST: Devuelve 'letraIndice', que es 'posicionX' validado, de modo que solo tome valores entre 1
#       y la longitud del 'tablero'
def validar_columna_elegida(posicionX, tablero):
    """
    - Valida la 'posicionX' ingresada por el jugador. Constata de que únicamente se ingresen valores
      que estén dentro de la longitud de la columna del 'tablero'
    - El parámetro 'posicionY' es considerado int, y 'tablero' como lista
    - Retorna un String
    """
    letras = []
    letraIndice = ""
    flagValido = False

    letras = list(st.ascii_uppercase)

    while(not flagValido):
        if(posicionX in letras):
            letraIndice = str(letras.index(posicionX) + 1)

            if(validar_numero_acotado(letraIndice, 1, len(tablero))):
                flagValido = True
            else:
                print("\n====== ADVERTENCIA ======\n")
                print("Las opciones válidas para las columnas son desde la letra {0}, hasta la letra {1}"
                    .format(
                        letras[0],
                        letras[len(tablero) - 1]
                    )
                )
                print("\n====== ADVERTENCIA ======\n")
        else:
            print("\n====== ADVERTENCIA ======\n")
            print("Recuerde que únicamente son válidas las letras del abecedario")
            print("\n====== ADVERTENCIA ======\n")

        if(not flagValido): posicionX = ingresar_columna()

    return letraIndice

# PRE: -
# POST: Solicita ingresar una 'columna' y la misma es devuelta
def ingresar_columna():
    """
    - Solicita el ingreso de la columna de la casilla a atacar
    - Retorn un String
    """
    posicionX = ""

    posicionX = input("Ingrese la columna de la casilla a la que desee atacar: ").upper()

    return posicionX

# PRE: 'posicionY' y 'posicionX', deben ser int
#      'tablero' debe ser una lista de listas de dimensiones n x n
#      'defensasPropias' debe ser una lista de listas
# POST: Devuelve 'posicionY' y 'posicionX' validados, de modo que solo tomen valores del 'tablero'
#       donde no se encuentren ubicadas 'defensasnPropias'
def validar_casilla_elegida(posicionY, posicionX, tablero, defensasPropias):
    """
    - Valida que la 'posicionY' y la 'posicionX' ingresadas por el jugador, es decir, la casilla en el 'tablero', 
      no se encuentre una 'defensaPropias' del jugador y también, que no haya sido impactado esa casilla previamente
    - Los parámetros 'posicionY' y 'posicionX' son considerados String, 'tablero' y 'defensasPropias'
      son listas
    - Retorna dos int
    """
    defensaIndice = ""
    flagValido = False

    defensaIndice = encontrar_indice_defensa(posicionY, posicionX, defensasPropias)

    while(not flagValido):
        if(tablero[posicionY][posicionX] != "X"):
            if(defensaIndice == ""):
                flagValido = True
            else:
                print("\n====== ADVERTENCIA ======\n")
                print("¡Estás atacando una coordenada de una de tus defensas!")
                print("\n====== ADVERTENCIA ======\n")                
        else:
            print("\n====== ADVERTENCIA ======\n")
            print("La casilla seleccionada ya ha sido atacada")
            print("\n====== ADVERTENCIA ======\n")

        if(not flagValido):
            posicionY = ingresar_fila()
            posicionY = validar_fila_elegida(posicionY, tablero)
            posicionY = int(posicionY) - 1

            posicionX = ingresar_columna()
            posicionX = validar_columna_elegida(posicionX, tablero)
            posicionX = int(posicionX) - 1

            defensaIndice = encontrar_indice_defensa(posicionY, posicionX, defensasPropias)             

    return posicionY, posicionX

# PRE: 'posicionY' y 'posicionX', deben ser int
#      'defensas' debe ser una lista de listas
# POST: Devuelve el indice de alguna defensa de 'defensas', que tenga como
#       coordenadas 'posicionY' y 'posicionX', caso contrario, devuelve ""
def encontrar_indice_defensa(posicionY, posicionX, defensas):
    """
    - Verifica si en las 'defensas' hay algunas coordenada que coincida con la 'posicionY' y la 'posicionX',
      de ser así, devuelve el indice de la defensa, en donde se encuentra dicha coordenada. Caso contrario,
      devolverá un String vacío
    - Los parámetros 'posicionY' y 'posicionX' son considerados int y 'defensas' como lista
    - Retorna un int o String
    """
    defensaIndice = ""

    for defensa in range(len(defensas)):
        if([posicionY, posicionX] in defensas[defensa]):
            defensaIndice = defensa

    return defensaIndice

# PRE: 'tablero' debe ser una lista de listas de dimensiones n x n
#      'defensa' debe ser una lista de listas
# POST: Devuelve el boolean 'estaDestruida', la cual toma su valor, si en todas
#       las coordenadas de la 'defensa', que se contrastan en el 'tablero', están
#       marcadas con una 'X', es decir, si fueron destruidas
def verificar_defensa_destruida(tablero, defensa):
    """
    - Verifica, acorde al 'tablero', si en las coordenadas de la 'defensa', está marcada con una "X", 
      lo cual constata de que ya fue destruido
    - Los parámetros 'tablero' y 'defensa' son considerados listas
    - Retorna un boolean
    """
    contadorCoordenadasAtacadas = 0
    posicionY = 0
    posicionX = 0
    estaDestruida = False

    for coordenada in range(len(defensa)):
        posicionY = defensa[coordenada][0]
        posicionX = defensa[coordenada][1]

        if(tablero[posicionY][posicionX] == "X"):
            contadorCoordenadasAtacadas += 1

    if(contadorCoordenadasAtacadas == len(defensa)):
        estaDestruida = True

    return estaDestruida

# PRE: 'tablero' debe ser una lista de listas de dimensiones n x n
#      'defensas' debe ser una lista de listas
# POST: Devuelve el boolean 'estasDestruida', la cual toma su valor, si en todas
#       las coordenadas de las 'defensas', que se contrastan en el 'tablero', están
#       marcadas con una 'X', es decir, si fueron destruidas
def verificar_defensas_destruidas(tablero, defensas):
    """
    - Verifica, acorde al 'tablero', si en las coordenadas de las 'defensas', están marcadas con una "X", 
      lo cual constata de que ya fueron destruidas
    - Los parámetros 'tablero' y 'defensas' son considerados listas
    - Retorna un boolean
    """
    contadorDefensasDestruidas = 0
    estaDestruida = False
    estanDestruidas = False

    for defensa in range(len(defensas)):
        estaDestruida = verificar_defensa_destruida(tablero, defensas[defensa])

        if(estaDestruida):
            contadorDefensasDestruidas += 1
    
    if(contadorDefensasDestruidas == len(defensas)):
        estanDestruidas = True

    return estanDestruidas

# PRE: 'tablero' debe ser una lista de listas de dimensiones n x n
#      'jugador' y 'oponente', deben ser int
#      'defensasPropias' y 'defensasOponente', deben ser listas de listas
#      'piezasDescripcion' debe ser una lista de dos listas
# POST: Devuelve el 'tablero', el cual se vio modificado por el 'jugador'
#       de modo que, las coordenadas que haya elegido, de encontrarse alguna defensa
#       de 'defensasOponente', se informará si se 'IMPACTÓ' o si se 'DESTRUYO', a la vez
#       a partir de 'piezasDescripcion' del 'oponente', se recuperará la descripción del objetivo
#       destruido. También mostrará el 'tablero' filtrado, en el cual se ocultarán las defensas
#       del oponente, que no hayan sido atacadas y mostrar las defensas del jugador, ya sea si
#       fueron atacadas o no
def jugar_turno(tablero, jugador, oponente, defensasPropias, defensasOponente, piezasDescripcion):
    """
    - Lógica dura del juego. Muestra el 'tablero' filtrado con las 'defensasPropias' del 'jugador'. Se solicita la posición de una casilla al 'jugador'
      y se verifica si dicha coordenada, se corresponde a la coordenada de alguna defensas de 'defensasOponente', de ser así marca el 'tablero' con "X",
      caso contrario, marca el 'tablero' con "#". Si una defensa es destruida del 'oponente', se imprime un mensaje indicando a que defensa se corresponde según
      'piezasDescripcion'. Al finalizar el turno, muestra otra vez el 'tablero' filtrado.
    - Los parámetros 'tablero', 'defensasPropias', 'defensasOponentes' y 'piezasDescripcion' son consideradas listas, 'jugador' y 'oponente' como int
    - Retorna una lista
    """
    posicionY = ""
    posicionX = ""
    defensaIndice = ""
    estaDestruida = False

    print(f"\nTurno de {PROTAGONISTAS[jugador]}\n")
    print("Defensas propias\n")
    filtrar_defensas_jugador(tablero, defensasOponente, defensasPropias, piezasDescripcion[jugador])

    posicionY = ingresar_fila()
    posicionY = validar_fila_elegida(posicionY, tablero)
    posicionY = int(posicionY) - 1

    posicionX = ingresar_columna()
    posicionX = validar_columna_elegida(posicionX, tablero)
    posicionX = int(posicionX) - 1

    posicionY, posicionX = validar_casilla_elegida(posicionY, posicionX, tablero, defensasPropias)
    defensaIndice = encontrar_indice_defensa(posicionY, posicionX, defensasOponente)

    # - Ingresará en la condición, si hay una defensa enemiga en la coordenada o si dicha coordenada ya fue atacada
    #   o si hay alguna defensa del oponente posicionada en dicha coordenada
    if(tablero[posicionY][posicionX] == "O" or tablero[posicionY][posicionX] == "#" or defensaIndice != ""):
        if(defensaIndice != ""):
            tablero[posicionY][posicionX] = "X"

            estaDestruida = verificar_defensa_destruida(tablero, defensasOponente[defensaIndice])

            if(estaDestruida):
                print(f"DESTRUIDO {piezasDescripcion[oponente][defensaIndice].upper()}")
            else:
                print("¡IMPACTADO!")
        else:
            tablero[posicionY][posicionX] = "#"
    else:
        tablero[posicionY][posicionX] = "#"

    filtrar_defensas_jugador(tablero, defensasOponente, defensasPropias, piezasDescripcion[jugador])

    return tablero

# PRE: 'deJugador', 'aJugador' e 'indiceDescripcion', deben ser int
#      'piezasDescripcion' debe ser una lista de dos listas
# POST: Devuelve 'piezasDescripcion', el cual se vio modificado, ya que una de las piezas
#       de 'deJugador' se sustrae y se adiciona a 'aJugador', en la posición indicada por
#       'indiceDescripcion'
def quitar_sumar_descripcion_menor_defensa(deJugador, aJugador, indiceDescripcion, piezasDescripcion):
    """
    - Quita la descripción en 'piezasDescripcion' que le corresponde a 'deJugador' y agrega esa descripción
      en 'piezasDescripcion' pero a 'aJugador' en el índice 'indiceDescripcion'
    - Los parámetros 'deJugador', 'aJugador' e 'indiceDescripcion' son considerados int, y 'piezasDescripcion' como lista
    - Retorna una lista
    """
    descripcionDefensaSacada = ""

    descripcionDefensaSacada = piezasDescripcion[deJugador].pop(-1)
    piezasDescripcion[aJugador].insert(indiceDescripcion, descripcionDefensaSacada)

    return piezasDescripcion

# PRE: 'tablero' debe ser una lista de listas de dimensiones n x n
#      'jugador', 'oponente' e 'indiceGanador', deben ser int
#      'defensasJug' y 'defensasOpo', deben ser listas de listas
#      'flagHayGanador' debe ser un boolean
#      'piezasDescripcion' debe ser una lista de dos listas
# POST: 
def iniciar_turno(tablero, jugador, oponente, defensasJug, defensasOpo, indiceGanador, flagHayGanador, piezasDescripcion):
    if(not flagHayGanador):
        if((verificar_defensas_destruidas(tablero, defensasOpo) or len(defensasOpo) == 0)):
            flagHayGanador = True
            indiceGanador = jugador
        else:
            if(iniciar_partida_especial()):
                indiceNuevaDefensa = 0

                print("¡Hay ronda especial!")

                tablero = quitar_defensa_tablero(tablero, defensasOpo[-1])
                defensasOpo, defensasJug, indiceNuevaDefensa = quitar_sumar_menor_defensa(defensasOpo, defensasJug)
                piezasDescripcion = quitar_sumar_descripcion_menor_defensa(oponente, jugador, indiceNuevaDefensa, piezasDescripcion)
                tablero, defensasJug[indiceNuevaDefensa] = posicionar_defensa(tablero, defensasJug[indiceNuevaDefensa], indiceNuevaDefensa, jugador)

            tablero = jugar_turno(tablero, jugador, oponente, defensasJug, defensasOpo, piezasDescripcion)

    return tablero, defensasJug, defensasOpo, indiceGanador, flagHayGanador, piezasDescripcion

def main():
    opcion = ""
    dimension = ""
    tablero = []
    defensasJug1 = []
    defensasJug2 = []
    # Cada jugador se corresponde con el indice de la lista PROTAGONISTAS
    jugador1 = 0
    jugador2 = 0
    primeroEnJugar = 0
    indiceGanador = 0
    flagHayGanador = False

    # Guarda relación con los protagonistas, y la cantidad de elementos que se les asigna como defensas
    piezasDescripcion = [["Fuerte", "Campamento de defensa", "Depósito de armas", "Defensa Norte", "Defensa Sur"], ["Crucero pesado", "Galeón", "Cañonero", "Galera", "Barcaza"]]

    opcion = ingresar_opcion()
    opcion = validar_opcion(opcion)
    jugador1 = int(opcion) - 1

    print("\n-------- JUGADORES --------\n")
    print("1° JUGADOR ------>", PROTAGONISTAS[jugador1])

    for indice in range(len(PROTAGONISTAS)):
        if(indice != jugador1):
            jugador2 = indice

            print("2° JUGADOR ------>", PROTAGONISTAS[indice])

    dimension = ingresar_dimension()
    dimension = validar_dimension(dimension)
    dimension = int(dimension)

    tablero = crear_tablero(dimension)

    defensasJug1 = generar_defensas()
    defensasJug2 = generar_defensas()

    for defensa in range(len(defensasJug1)):
        tablero, defensasJug1[defensa] = posicionar_defensa(tablero, defensasJug1[defensa], defensa, jugador1)

    for defensa in range(len(defensasJug2)):
        tablero, defensasJug2[defensa] = posicionar_defensa(tablero, defensasJug2[defensa], defensa, jugador2)

    primeroEnJugar = definir_primero_jugar(jugador1, jugador2)

    if(primeroEnJugar == jugador1):
        contadorRonda = 1

        while(not flagHayGanador):

            print(f"<-------- RONDA {contadorRonda} -------->")

            tablero, defensasJug1, defensasJug2, indiceGanador, flagHayGanador, piezasDescripcion = iniciar_turno(tablero, jugador1, jugador2, defensasJug1, defensasJug2, indiceGanador, flagHayGanador, piezasDescripcion)

            tablero, defensasJug2, defensasJug1, indiceGanador, flagHayGanador, piezasDescripcion = iniciar_turno(tablero, jugador2, jugador1, defensasJug2, defensasJug1, indiceGanador, flagHayGanador, piezasDescripcion)

            contadorRonda += 1
    else:
        contadorRonda = 1

        while(not flagHayGanador):

            print(f"<-------- RONDA {contadorRonda} -------->")

            tablero, defensasJug2, defensasJug1, indiceGanador, flagHayGanador, piezasDescripcion = iniciar_turno(tablero, jugador2, jugador1, defensasJug2, defensasJug1, indiceGanador, flagHayGanador, piezasDescripcion)

            tablero, defensasJug1, defensasJug2, indiceGanador, flagHayGanador, piezasDescripcion = iniciar_turno(tablero, jugador1, jugador2, defensasJug1, defensasJug2, indiceGanador, flagHayGanador, piezasDescripcion)

            contadorRonda += 1

    print(f"Ganador {PROTAGONISTAS[indiceGanador]}")

main()