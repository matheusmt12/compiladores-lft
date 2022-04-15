import ply.lex as lex
reserved = {
    'Abstract': 'ABSTRACT',
    'as': 'AS',
    'base': 'BASE',
    'Bool': 'BOOL',
    'break': 'BREAK',
    'byte': 'BYTE',
    'case': 'CASE',
    'Catch': 'CATCH',
    'checked': 'CHECKED',
    'class': 'CLASS',
    'Const': 'CONST',
    'continue': 'CONTINUE',
    'decimal': 'DECIMAL',
    'default': 'DEFAULT',
    'Delegate': 'DELEGATE',
    'do': 'DO',
    'double': 'DOUBLE',
    'else': 'ELSE',
    'Enum': 'ENUM',
    'event': 'EVENT',
    'explicit': 'EXPLICIT',
    'extern': 'EXTERN',
    'false': 'FALSE',
    'finally': 'FINALLY',
    'fixed': 'FIXED',
    'float': 'FLOAT',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'goto': 'GOTO',
    'if': 'IF',
    'implicit': 'IMPLICIT',
    'in': 'IN',
    'int': 'INT',
    'interface': 'INTERFACE',
    'internal': 'INTERNAL',
    'is': 'IS',
    'lock': 'LOCK',
    'long': 'LONG',
    'namespace': 'NAMESPACE',
    'new': 'NEW',
    'null': 'NULL',
    'object': 'OBJECT',
    'operator': 'OPERATOR',
    'out': 'OUT',
    'override': 'OVERRIDE',
    'params': 'PARAMS',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'public': 'PUBLIC',
    'readonly': 'READONLY',
    'ref': 'REF',
    'return': 'RETURN',
    'sbyte': 'SBYTE',
    'sealed': 'SEALED',
    'short': 'SHORT',
    'sizeof': 'SIZEOF',
    'stackalloc': 'STACKALLOC',
    'static': 'STATIC',
    'struct': 'STRUCT',
    'this': 'THIS',
    'throw': 'THROW'
}
tokens = ['string', 'char', 'newLine',
          "soma", "sub", "div", "mod", "incremento", "decremento", "mul",
          "igual", "diferente", "maior", "menor", "maiorIgual", "menorIgual",
          "AND", "OR", "NOT", "bitAND", "bitOR", "bitNOT", "XOR", "deslocaRight",
          "deslocaLeft","ponto", "pontoVirgula", "parenteseL", "parenteseR", "chaveL",
          "chaveR", "numero", "palavra",'virgula','comment'] + list(reserved.values())
t_ignore = ' \t'
t_chaveL = r'{'
t_chaveR = r'}'
t_virgula = r','
t_ponto = r'\.'
t_pontoVirgula = r';'
t_parenteseL = r'\('
t_parenteseR = r'\)'
# operadores bit a bit
t_bitAND = r'&'
t_bitOR = r'\|'
t_bitNOT = r'~'
t_XOR = r'\^'
t_deslocaRight = r'>>'
t_deslocaLeft = r'<<'
# operadores logico
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
# operadores relacionais
t_igual = r'=='
t_diferente = r'=!'
t_maior = r'>'
t_menor = r'<'
t_maiorIgual = r'>='
t_menorIgual = r'<='
# operadores aritimeticos
t_soma = r'\+'
t_sub = r'-'
t_div = r'/'
t_mod = r'%'
t_mul = r'\*'
t_incremento = '\+\+'
t_decremento = '--'
def t_numero (t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_palavra (t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'palavra')
    return t
def t_comment (t):
    r'(//.*)|(/\*(.|\n)*?\*/)'
    pass
def t_string(t):
    r'\"([^\\]|(\\.))*?\"'
    return t
def t_char(t):# tirar
    r'\'([^\\]|(\\.))\''
    return t
def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print("Token inválido!!!!! '%s'" % t.value[0])
    print("Token inválido!!!!! '", t.value[0], "'")

    t.lexer.skip(1)
lexer = lex.lex()
lexer.input("15Abstract as base Bool break byte case Catch char checked class Const continue decimal default Delegate dodouble else Enum event explicit extern false finally fixed float for foreach goto if implicit in int interface internal is lock long namespace new null object operator out override params private protected public readonly ref return sbyte sealed short sizeof stackalloc static string struct this throw")
for tok in lexer:
    print(tok.type, tok.lineno, tok.value, tok.lexpos)
lexer.input("as{}(()(+---*%++++>=<===<>=!&&||!|<<>>&^~..;;1 2 23 /*1110*/Abstract@:\'\n\"rei\nnan\"\'@\''\n'' ' '@'math/*eus*/ \"\\\\n\"")
for tok in lexer:
    print(tok.type, tok.lineno, tok.value, tok.lexpos)
