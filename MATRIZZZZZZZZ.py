matriz1 = [['🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
           ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
           ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
           ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
           ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
           ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲']]
correcto = '✔︎'
incorrecto = '✖︎'
ls_preguntas = ['¿Que es Python?\n1. Juego\n2. Lenguaje de programacion\n3. Marca de auto\n4. Ninguna de las anteriores',
                '¿Que es HTML?\n1. Lenguaje de programacion\n2. Marca de gaseosa\n3. Navegador\n4. Perro caliente',
                '¿Qué es algoritmo?\n1. Es algo que tiene ritmo (algo-ritmo)\n2. Es lo mismo que un lenguaje de programación\n3. Es una serie de pasos debidamente estructurados y secuenciales que ayudan a resolver un problema\n4. Es una representación gráfica de figuras',
                '¿Qué es un lenguaje de programación\n1.Un conjunto de reglas que permiten crear instrucciones para que una computadora las ejecute\n2.Un software que traduce el código fuente escrito por un programador a lenguaje de máquina\n3.Un tipo de hardware que permite a las computadoras realizar cálculos y operaciones lógicas?'
                '¿'

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                ]
ls_respuestas = ['2','1','3','2']
def fnt_pintar_matriz():
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            print(matriz1[i][j], end='      ')
        print('\n\n')
contador = 0
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