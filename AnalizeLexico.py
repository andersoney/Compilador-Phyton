import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN
import re


class AnalizeLexico(object):
    reserved = {
        'boolean': 'BOOLEAN_TYPE',
        'integer': 'INTEGER_TYPE',
        'real': 'FLOAT_TYPE',
        'string': 'STRING_TYPE',
        'var': 'VAR',
        'false': 'FALSE',
        'true': 'TRUE',
        'size': 'SIZE',
        'read': 'READ',
        'write': 'WRITE',
        'writeln': 'WRITELN',
        'readln': 'READLN',
        'program': 'PROGRAM',
        'function': 'FUNC_DEF',
        'begin': 'BLOCO_INIT',
        'end': 'BLOCO_END',
        'if': "IF",
        'then': "THEN",
        'or': "OR",
        'and': "AND",
        'not': "NOT",
        'while': "WHILE",
        'do': "DO",
        'case': "CASE",
        'of': "OF",
        'repeat': "REPEAT",
        'until': "UNTIL",
    }

    aritmetcs_token = [
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVISION',
        'MOD',
    ]
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVISION = r'/'
    t_MOD = r'%'
    logic_tokens = [
        'DIF',
        'EQCOMP',
        'MENOR_QUE',
        'MENOR_IGUAL',
        'MAIOR_QUE',
        'MAIOR_IGUAL',
    ]
    t_DIF = r'\<\>'
    t_EQCOMP = r"=="
    t_MENOR_QUE = r'<'
    t_MENOR_IGUAL = r'<='
    t_MAIOR_QUE = r'>'
    t_MAIOR_IGUAL = r'\>='

    numeric_type = [
        'FLOAT',
        'INTEGER',
    ]
    digit = r'([0-9])'
    nondigit = r'([_A-Za-z])'

    @TOKEN(r'\d+\.\d*')
    def t_FLOAT(self, t):
        t.value = float(t.value)
        return t

    @TOKEN(r'\d+')
    def t_INTEGER(self, t):
        t.value = int(t.value)
        return t
    tokens = [
        'LPAREN',
        'RPAREN',
        'END_LINE',
        # 'NEW_LINE',
        'STRING',
        'ASSIGN',
        'COMMENT_MULT1',
        'COMMENT_MULT2',
        'COMMENT_LINE',
        # 'FILE',
        'COMMA',
        'SEMICOLON',
        'ID',
    ] + numeric_type + logic_tokens + aritmetcs_token + list(reserved.values())
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_END_LINE = r';'
    # t_NEW_LINE = r'\n'
    t_STRING = r'([\"].*[\"])|([\'].*[\'])'
    t_ASSIGN = r':='
    t_COMMENT_MULT1 = r'\{((.*)\n)*(.*)\}'
    t_COMMENT_MULT2 = r'\(\*((.*)\n)*(.*)\*\)'
    t_COMMENT_LINE = r'\/\/.*\n'
    # t_FILE = r'[.*]'
    t_COMMA = r','
    t_SEMICOLON = r':'

    @TOKEN(r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)')
    def t_ID(self, t):
        t.type = self.reserved.get(t.value, 'ID')
        return t


    def __init__(self, debuglog):
        self.debuglog = debuglog

    

    @TOKEN(r'\n+')
    def t_newline(self, t):
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t'
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(debug=1, module=self, debuglog=self.debuglog,
                             reflags=re.UNICODE | re.VERBOSE, **kwargs)

    def getLex(self):
        return self.lexer

    def getTokens(self):
        return self.tokens

    def test(self, data):
        self.lexer.input(data)
        print(data)
        print(f"\n\n\n {'*'*50} \n\n\n")
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
        print(f"\n\n\n {'*'*50} \n\n\n")
