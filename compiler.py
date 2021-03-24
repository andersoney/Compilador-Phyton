import ply.lex as lex
from ply.lex import TOKEN
import re
from sintatic_analize import LexAnalize 

reserved = {
    'Boolean': 'BOOLEAN',
    'false': 'FALSE',
    'true': 'TRUE',
    'integer': 'INTEGER',
    'size': 'SIZE',
    'read': 'READ',
    'real': 'REAL',
    'writeln': 'WRITELN',
    'readln': 'READLN',
    'program': 'FUNC_DEF',
    'begin': 'BLOCO_INIT',
    'end': 'BLOCO_END',
    'string': 'STRING',
}
aritmetcs_token = [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVISION',
    'MOD',
]

tokens = [
    'COMMENT',
    'COMMENT_MULT1',
    'COMMENT_MULT2',
    'ID',
    'END_LINE',
] + aritmetcs_token + list(reserved.values())

t_STRING = r'([\"].*[\"])|([\'].*[\'])'

digit = r'([0-9])'
nondigit = r'([_A-Za-z])'
identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'

@TOKEN(r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)')
def t_ID(t):
    t.type = reserved.get(t.value, 'ID')
    return t
t_END_LINE = r';'
t_ignore = ' \t'
t_ignore_COMMENT = r'\/\/.*\n'
t_ignore_COMMENT_MULT1 = r'\{((.*)\n)*(.*)\}'
t_ignore_COMMENT_MULT2 = r'\(\*((.*)\n)*(.*)\*\)'

def t_error(t):
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def build(self,**kwargs):
    self.lexer = lex.lex(module=self, **kwargs)


# Build the lexer
lexer = lex.lex(debug=True,optimize=1)
f = open("teste1.pp", "r")
data=f.read();
print(data)
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)