from AnalizeLexico import AnalizeLexico;
from AnalisadorSintatico import AnalisadorSintatico;
import ply.yacc as yacc
import logging

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parseloglexico.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
logLexico = logging.getLogger()
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselogsintatico.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
logSintatico = logging.getLogger()

f = open("teste1.pp", "r")
data=f.read();
print(data);
m = AnalizeLexico(debuglog=logLexico)
m.build()           # Build the lexer
m.test(data)     # Test it
lexer=m.getLex();
tokens=m.getTokens();

sintatico=AnalisadorSintatico();
sintatico.build(lexer,tokens,logSintatico);
sintatico.teste(data);



