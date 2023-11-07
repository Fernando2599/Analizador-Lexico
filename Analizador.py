import ply.lex as lex

# Lista de palabras reservadas personalizadas
reservadas = {
    'PROBABILIDAD': 'PROBABILIDAD',
}

# Lista de tokens
tokens = ['NUMERO', 'MAS', 'MENOS', 'POR', 'ENTRE'] + list(reservadas.values())

# Reglas de tokens
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_ENTRE = r'/'

# Regla para números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para palabras reservadas personalizadas
def t_PROBABILIDAD(t):
    r'\bPROBABILIDAD\b'
    #r'PROBABILIDAD'
    # Llama a la función o método que calcula la probabilidad
    t.lexer.probabilidad = calcular_probabilidad()
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Función para calcular la probabilidad (necesita una funcion como tal)
def calcular_probabilidad():
    return 2.7  # aqui se debe poner una operacion como tal

# Crear el analizador léxico
lexer = lex.lex()

# Ejemplo de uso
datos = "PROBABILIDAD + 1.5 * 1.3"
lexer.input(datos)
for token in lexer:
    if token.type == 'PROBABILIDAD':
        print("La probabilidad calculada es:", token.lexer.probabilidad)
        print("Este es el token:", token.type)
    else:
        print("Este es el token",token)
