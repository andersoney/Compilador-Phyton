from AnalizeLexico import AnalizeLexico;
from AnalisadorSintatico import AnalisadorSintatico;
import ply.yacc as yacc
import logging

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

f = open("teste1.pp", "r")
data=f.read();
m = AnalizeLexico(debuglog=log)
m.build()           # Build the lexer
m.test(data)     # Test it
lexer=m.getLex();
tokens=m.getTokens();

sintatico=AnalisadorSintatico();
sintatico.build(lexer,tokens,log);
sintatico.teste(data)



