import ply.yacc as yacc

def print_to_view(p):
    # print(p.slice)
    # print(p.slice[1].value);
    pass;
class AnalisadorSintatico:
    def p_s(self, p):
        """
        s : PROGRAM ID END_LINE bloco
        """
    def p_bloco(self,p):
        """
        bloco : comandos_compostos
              | parte_de_definicao_de_constante
              | parte_de_definicao_de_tipos
              | parte_de_definicao_de_variaveis
              | parte_de_definicao_de_sub_rotinas
        """
    def p_parte_de_definicao_de_constante(self,p):
        """
        parte_de_definicao_de_constante : CONST definicao_de_constante END_LINE
                                        | CONST definicao_de_constante
                                        | CONST definicao_de_constante END_LINE parte_de_definicao_de_constante
        """

    def p_definicao_de_constante(self,p):
        """
        definicao_de_constante : ID ASSIGN constante
        """

    def p_constante(self,p):
        """
        constante : positivo_e_negativo ID 
                  | positivo_e_negativo INTEGER
        """

    def p_parte_de_definicao_de_tipos(self, p):
        """
        parte_de_definicao_de_tipos : TYPE definicao_de_tipo 
                                    | TYPE definicao_de_tipo END_LINE
                                    | TYPE definicao_de_tipo END_LINE parte_de_definicao_de_tipos
        """
    
    def p_definicao_de_tipo(self,p):
        """
        definicao_de_tipo : ID ASSIGN tipo
        """
    def p_tipo(self,p):
        """
        tipo : ID
             | enumerator
             | record
             | ARRAY LCHAVE index OF tipo RCHAVE
             | STRING_TYPE LCHAVE INTEGER RCHAVE
             | INTEGER_TYPE
             | BOOLEAN_TYPE
             | FLOAT_TYPE
             | STRING_TYPE
        """
    def p_index(self,p):
        """
        index : INTEGER
              | INTEGER index
        """
    def p_enumerator(self,p):
        """
        enumerator : LPAREN lista_indentificadores RPAREN
        """
    def p_record(self,p):
        """
        record : RECORD lista_de_campos BLOCO_END
        """
    def p_lista_de_campos(self,p):
        """
        lista_de_campos : lista_indentificadores SEMICOLON tipo
                        | lista_indentificadores SEMICOLON tipo END_LINE lista_de_campos
        """
    def p_parte_de_definicao_de_variaveis(self,p):
        """
        parte_de_definicao_de_variaveis : VAR declaracao_de_variaveis 
                                        | VAR declaracao_de_variaveis END_LINE parte_de_definicao_de_variaveis
        """
    def p_declaracao_de_variaveis(self,p):
        """
        declaracao_de_variaveis : lista_indentificadores SEMICOLON tipo
        """

    def p_lista_indentificadores(self,p):
        """
        lista_indentificadores : ID
                               | ID COMMA lista_indentificadores
        """

    def p_parte_de_definicao_de_sub_rotinas(self,p):
        """
        parte_de_definicao_de_sub_rotinas : parte_de_definicao_de_sub_rotina
                                          | parte_de_definicao_de_sub_rotina parte_de_definicao_de_sub_rotinas
        """
    def p_parte_de_definicao_de_sub_rotina(self,p):
        """
        parte_de_definicao_de_sub_rotina : declaracao_de_procedimento END_LINE
                                         | declaracao_de_funcao END_LINE
        """

    def p_declaracao_de_procedimento(self,p):
        """
        declaracao_de_procedimento : PROCEDURE ID LCHAVE parametros_formais RCHAVE END_LINE bloco
        """
    def p_declaracao_de_funcao(self, p):
        """
        declaracao_de_funcao : FUNC_DEF ID LPAREN parametros_formais RPAREN SEMICOLON tipo END_LINE parametros_formais bloco
                             | FUNC_DEF ID LPAREN parametros_formais RPAREN END_LINE parametros_formais bloco
        """
    def p_parametros_formais(self,p):
        """
        parametros_formais : secao_de_parametros_formais 
                           | secao_de_parametros_formais parametros_formais
                           | 
        """
    def p_secao_de_parametros_formais(self,p):
        """
        secao_de_parametros_formais : lista_indentificadores SEMICOLON tipo END_LINE
                                    | VAR lista_indentificadores SEMICOLON tipo END_LINE
        """
    def p_comandos_compostos(self,p):
        """
        comandos_compostos : BLOCO_INIT comandos BLOCO_END
        """
    def p_comandos(self,p):
        """
        comandos : comando END_LINE comandos
                 | comando END_LINE
                 |
        """
    def p_comando(self,p):
        """
        comando : atribuicao
                | chamada_de_procedimento
                | comando_composto
                | comando_condicional_1
                | comando_condicional_2
                | comando_repetitivo_1
                | comando_repetitivo_2
                | comando_repetitivo_3
        """
    def p_comando_composto(self,p):
        """
        comando_composto : BLOCO_INIT comandos BLOCO_END
        """
    def p_atribuicao(self,p):
        """
        atribuicao : variavel ASSIGN expressao
        """
    def p_chamada_de_procedimento(self,p):
        """
        chamada_de_procedimento : ID
                                | ID LPAREN lista_de_expressoes RPAREN
                                | WRITE LPAREN lista_de_expressoes RPAREN
                                | WRITELN LPAREN lista_de_expressoes RPAREN
                                | READLN LPAREN lista_de_expressoes RPAREN
                                | READLN 
                                | READ LPAREN lista_de_expressoes RPAREN
        """
    def p_comando_condicional_1(self,p):
        """
        comando_condicional_1 : IF expressao THEN comando_composto
                              | IF expressao THEN comando_composto ELSE comando_composto
        """
    def p_elementos_do_case(self,p):
        """
        elementos_do_case : elemento_do_case END_LINE
                          | elemento_do_case END_LINE elementos_do_case
        """
    def p_comando_condicional_2(self,p):
        """
        comando_condicional_2 : CASE expressao OF elementos_do_case  BLOCO_END
        """

    def p_elemento_do_case(self,p):
        """
        elemento_do_case : constante
                         | constante SEMICOLON comando
                         | constante SEMICOLON comandos_compostos
                         | constante COMMA elemento_do_case SEMICOLON comandos
                         | constante COMMA elemento_do_case SEMICOLON comandos_compostos
        """
    def p_comando_repetitivo_1(self,p):
        """
        comando_repetitivo_1 : WHILE expressao DO comandos_compostos
        """
    def p_comando_repetitivo_2(self,p):
        """
        comando_repetitivo_2 : FOR ID ASSIGN expressao TO expressao DO comandos_compostos
                             | FOR ID ASSIGN expressao DOWNTO expressao DO comandos_compostos
        """
    def p_comando_repetitivo_3(self,p):
        """
        comando_repetitivo_3 : REPEAT comandos
                             | REPEAT comandos UNTIL expressao
        """

    def p_expressao(self, p):
        """
        expressao : expressao_simples 
                  | expressao_simples relacao expressao_simples
                  | ID relacao ID
                  | ID relacao fator
                  | READLN
                  | READ
        """

    def p_relacao(self,p):
        """
        relacao : EQCOMP
                | DIF
                | MENOR_QUE
                | MENOR_IGUAL
                | MAIOR_IGUAL
                | MAIOR_QUE
        """
    def p_positivo_e_negativo(self, p):
        """
        positivo_e_negativo : PLUS
                            | MINUS
                            | 
        """
    def p_expressao_simples(self,p):
        """
        expressao_simples : termo
                          | positivo_e_negativo termo
                          | positivo_e_negativo termo PLUS termo
                          | positivo_e_negativo termo MINUS termo
                          | positivo_e_negativo termo OR termo
        """
    def p_termo(self,p):
        """
        termo : fator 
              | fator TIMES fator
              | fator DIV fator
              | fator AND fator
              | fator DIVISION fator
        """
    def p_fator(self,p):
        """
        fator : variavel
              | INTEGER
              | FLOAT
              | STRING
              | CHAR
              | chamada_de_funcao
              | LPAREN expressao RPAREN
              | NOT fator
        """
    def p_variavel(self,p):
        """
        variavel : ID 
                 | ID LPAREN expressao RPAREN
                 | ID LPAREN campo RPAREN
        """
    def p_lista_de_expressoes(self,p):
        """
        lista_de_expressoes : expressao 
                            | expressao COMMA lista_de_expressoes
        """
    def p_chamada_de_funcao(self, p):
        """
        chamada_de_funcao : ID
                          | ID lista_de_expressoes
        """
    def p_campo(self, p):
        """
        campo : ID
        """



    def p_error(self, p):
        print(f"Syntax error in input!'{p}'")

    def build(self, lex, tokens, log):
        self.tokens = tokens
        self.lexer = lex
        self.parser = yacc.yacc(debug=1, module=self,
                                check_recursion=False, debuglog=log)

    def teste(self, file):
        result = self.parser.parse(file)
        print(result)
    pass
