import ply.yacc as yacc

class AnalisadorSintatico:
    def p_s(self,p):
        """
        s : function
          | COMMENT_MULT1
          | COMMENT_MULT2
          | COMMENT
        """
    def p_function(self,p):
        """
        function : FUNC_DEF func_name END_LINE bloco
        """
    
    def p_func_name(self,p):
        """
        func_name : ID
        """
    def p_bloco(self,p):
        """
        bloco : BLOCO_INIT instrucoes BLOCO_END
        """
        pass;

    def p_instrucoes(self,p):
        """
        instrucoes : instrucao END_LINE instrucoes
                   | instrucao
        """
        pass;
    def p_instrucao(self,p):
        """
        instrucao : ID LPAREN variaveis RPAREN
        """
        pass;
    def p_variaveis(self,p):
        """
        variaveis : variavel 
                  | variavel COMMA variaveis
        """
        pass;
    def p_variavel(self, p):
        """
        variavel : ID
                 | STRING
        """
        pass;
    # def p_function(self,p):
    #     """
    #     instrucions : BLOCO_INIT instrucions BLOCO_END
        
    #     """

    # def p_instrucions(self,p):
    #     """
    #     instrucions : ID LPAREN STRING RPAREN END_LINE NEW_LINE
    #                 | ID END_LINE NEW_LINE
    #                 | IF LPAREN expression_boolean RPAREN THEN BLOCO_INIT instructions BLOCO_END
    #                 | IF LPAREN TRUE RPAREN THEN BLOCO_INIT instructions BLOCO_END
    #                 | IF LPAREN FALSE RPAREN THEN BLOCO_INIT instructions BLOCO_END
    #                 | WRITELN RPAREN STRING LPAREN
    #     """

    def p_error(self,p):
        print(f"Syntax error in input!'{p}'")

    def build(self,lex,tokens,log):
        self.tokens=tokens;
        self.lexer=lex;
        self.parser = yacc.yacc(debug = 1,module=self,check_recursion=False,debuglog=log)

    def teste(self,file):
        result=self.parser.parse(file);
        print(result)
    pass;