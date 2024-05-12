#Esta es la matriz de la que se va a tener utilidad dentro del algoritmo con emojis para tener un mejor diseño
matriz1 = [['🔲', '🔲', '🔲', '🔲', '🔲',],
           ['🔲', '🔲', '🔲', '🔲', '🔲',],
           ['🔲', '🔲', '🔲', '🔲', '🔲',],
           ['🔲', '🔲', '🔲', '🔲', '🔲',],
           ['🔲', '🔲', '🔲', '🔲', '🔲',],
           ['🔲', '🔲', '🔲', '🔲', '🔲',]]
#Estas opciones le permiten al usuario mirar si su respuesta es correcta o incorrecta 
correcto = '✔︎'
incorrecto = '✖︎'
#En esta parte el usuario podra elegir la pregunta que quiera mediante un numero donde siguiente a esto le va a aparecer su respectiva pregunta
ls_preguntas = ['¿Que es Python?\n1. Juego\n2. Lenguaje de programacion\n3. Marca de auto\n4. Ninguna de las anteriores',
                '¿Que es HTML?\n1. Lenguaje de programacion\n2. Marca de gaseosa\n3. Navegador\n4. Perro caliente',
                '¿Qué es algoritmo?\n1. Es algo que tiene ritmo (algo-ritmo)\n2. Es lo mismo que un lenguaje de programación\n3. Es una serie de pasos debidamente estructurados y secuenciales que ayudan a resolver un problema\n4. Es una representación gráfica de figuras',
                '¿Qué es un lenguaje de programación?\n1.Un conjunto de reglas que permiten crear instrucciones para que una computadora las ejecute\n2.Un software que traduce el código fuente escrito por un programador a lenguaje de máquina\n3.Un tipo de hardware que permite a las computadoras realizar cálculos y operaciones lógicas',
                '¿Cuáles son los dos tipos principales de lenguajes de programación?\n1.Lenguajes compilados e interpretados\n2. Lenguajes de alto nivel y bajo nivel\n3. Lenguajes imperativos y funcionales\n4. Todas las anteriores',
                '¿Qué es una variable?\n1. Un espacio en memoria donde se almacena un valor\n2. Un tipo de dato que puede almacenar diferentes valores\n3. Una instrucción que le dice a la computadora qué hacer',
                '¿Qué es un operador?\n1. Un símbolo que se utiliza para realizar una operación matemática o lógica\n2. Una variable que almacena un valor constante\n3. Una instrucción que le dice a la computadora qué hacer',
                '¿Qué es una condición?\n1. Una prueba que se realiza para determinar si una expresión es verdadera o falsa\n2. Un tipo de dato que puede almacenar diferentes valores\n3. Una instrucción que le dice a la computadora qué hacer',
                '¿Qué es un bucle?\n1. Una estructura de control que repite un bloque de código un número determinado de veces\n2. Una prueba que se realiza para determinar si una expresión es verdadera o falsa\n3. Un tipo de dato que puede almacenar diferentes valores',
                '¿Qué es una función?\n1. Un bloque de código reutilizable que realiza una tarea específica\n2. Una estructura de control que repite un bloque de código un número determinado de veces\n3.  Una prueba que se realiza para determinar si una expresión es verdadera o falsa',
                '¿Qué es la depuración?\n1. El proceso de identificar y corregir errores en un programa\n2. Una serie de pasos ordenados para resolver un problema\n3. Un bloque de código reutilizable que realiza una tarea específica',
                '¿Qué es la documentación?\n1. El proceso de escribir comentarios y explicaciones en el código para que sea más fácil de entender\n2. El proceso de identificar y corregir errores en un programa\n3. Una serie de pasos ordenados para resolver un problema',
                '¿Qué se utiliza para crear instrucciones que la computadora puede entender y ejecutar?\n1. Un compilador\n2. Un intérprete\n3. Un lenguaje de máquina\n4. Todas las anteriores',
                '¿Qué se utiliza para almacenar datos en la memoria de la computadora?\n1. Variables\n2. Ciclos\n3. Condiciones',
                '¿Qué estructura de control permite repetir un bloque de código un número determinado de veces?\n1. Condición\n2. Ciclo for\n3. Ciclo while',
                '¿Qué se utiliza para tomar decisiones dentro de un programa en función de una condición?\n1. Variables\n2. Ciclos\n3. Condiciones',
                '¿Cuál de las siguientes opciones NO es un tipo de dato básico en la mayoría de los lenguajes de programación?\n1. Entero\n2. Flotante\n3. Booleano\n4. Imagen',
                '¿Qué se utiliza para definir un bloque de código reutilizable que realiza una tarea específica?\n1. Variables\n2. Funciones\n3. Condicionales',
                '¿Qué se utiliza para agrupar y organizar el código en secciones lógicas?\n1. Modulos\n2. Paquetes\n3. Bibliotecas\n4. Todas las anteriores',
                '¿Qué se utiliza para almacenar datos de forma permanente, incluso después de apagar la computadora?\n1. Variables\n2. Memoria Ram\n3. Almacenamiento secundario',
                '¿Qué es una condición en programación?\n1.  Una estructura de control que permite ejecutar diferentes bloques de código según una condición\n2. Un tipo de dato en programación\n3. Una variable especial que almacena un valor booleano (verdadero o falso)\n4. Una función que devuelve un valor',
                '¿Qué es un ciclo en programación?\n1. Una estructura de control que repite un bloque de código un número determinado de veces\n2. Un tipo de dato en programación\n3. Una función que devuelve un valor',
                '¿Qué hace la función print() en Python?\n1.Solicita datos al usuario\n2. Imprime un mensaje en la consola\n3. Ninguna de las anteriores',
                '¿Qué es un operador en programación?\n1. Un espacio en memoria para almacenar datos\n2. Una instrucción en un lenguaje de programación\n3. Un símbolo que se utiliza para realizar operaciones matemáticas o lógicas\n4. Un tipo de dato en programación',
                '¿Cuál es la función de la palabra clave break en un bucle?\n1. Termina el programa\n2. Detiene la ejecución del bucle actual y sale del bucle\n3. Reanuda la ejecución del bucle desde el principio',
]
#Estas son las respuestas correctas de todas las preguntas
ls_respuestas = ['2','1','3','1','4','1','1','1','1','1','1','1','4','1','2','3','4','2','4','3','1','1','2','3','2']
#Esta es la matriz que contiene las respuestas correctas y incorrectas, se crea un contador 
def fnt_pintar_matriz():
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            print(matriz1[i][j], end='      ')
        print('\n\n')   
contador = 0
#Con este ciclo se miran las preguntas las respuesta y contiene una funcion de limpiar la consola
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        import os 
        os.system('cls')
        fnt_pintar_matriz()
        print()
        print(ls_preguntas[contador])
        print()
        r = input(' ->  ')
        if r == ls_respuestas[contador]:
            matriz1[i][j] = correcto
        else:
            matriz1[i][j] = incorrecto
        contador += 1
