import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN
import re;


class AnalizeLexico(object):
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
        'if':"IF"
    }
    
    aritmetcs_token = [
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVISION',
        'MOD',
    ]
    # List of token names.   This is always required
    tokens = [
        'NUMBER',
        'LPAREN',
        'RPAREN',
        'ID',
        'END_LINE',
        'NEW_LINE',
        'EQ',
        'COMMENT_MULT1',
        'COMMENT_MULT2',
        'COMMENT',
        'FILE',
        'COMMA'
    ]+ aritmetcs_token + list(reserved.values())

    # Regular expression rules for simple tokens
    t_PLUS = r'\+';
    t_MINUS = r'-';
    t_TIMES = r'\*';
    t_DIVISION = r'/';
    t_LPAREN = r'\(';
    t_RPAREN = r'\)';
    digit = r'([0-9])';
    nondigit = r'([_A-Za-z])';
    t_END_LINE = r';'
    t_NEW_LINE=r'\n'
    t_STRING = r'([\"].*[\"])|([\'].*[\'])';
    t_EQ = r'=';
    t_FILE=r'[.*]'
    t_ignore = ' \t|\n'
    t_COMMENT = r'\/\/.*\n'
    t_COMMENT_MULT1 = r'\{((.*)\n)*(.*)\}'
    t_COMMENT_MULT2 = r'\(\*((.*)\n)*(.*)\*\)'
    t_COMMA = r',';

    def __init__(self,debuglog):
        self.debuglog=debuglog;

    @TOKEN(r'\d+')
    def t_NUMBER(self, t):
        t.value = int(t.value)
        return t
    
    @TOKEN(r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)')
    def t_ID(self,t):
        t.type = self.reserved.get(t.value, 'ID')
        return t
    @TOKEN(r'\n+')
    def t_newline(self, t):
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(debug = 1,module=self,debuglog=self.debuglog,reflags = re.UNICODE | re.VERBOSE, **kwargs)

    def getLex(self):
        return self.lexer;
    
    def getTokens(self):
        return self.tokens;

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