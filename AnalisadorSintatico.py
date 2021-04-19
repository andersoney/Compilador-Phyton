import ply.yacc as yacc

def print_to_view(p):
    # print(p.slice)
    # print(p.slice[1].value);
    pass;
class AnalisadorSintatico:
    def p_s(self, p):
        """
        s : program_declaration s
          | comentario s
          | 
        """
    def p_program_declaration(self,p):
        """
        program_declaration : PROGRAM func_name END_LINE declaration_var END_LINE program
        """
    def p_program(self,p):
        """
        program : function program
                | function
        """
    def p_comentario(self, p):
        """
        comentario : COMMENT_MULT1 s
                   | COMMENT_MULT2 s
                   | COMMENT_LINE s
        """
        print_to_view(p);
        pass

    def p_function(self, p):
        """
        function : FUNC_DEF func_name LPAREN declaration_var RPAREN SEMICOLON return_type END_LINE declaration_var END_LINE bloco
        """
        
    def p_declaration_var(self, p):
        """
        declaration_var : VAR ids SEMICOLON type
        """
    def p_ids(self, p):
        """
        ids : ID
            | ID COMMA ids
        """
    def p_return_type(self, p):
        """
        return_type : type
        """
    def p_type(self, p):
        """
        type : INTEGER_TYPE 
             | FLOAT_TYPE
             | STRING_TYPE

        """

    def p_func_name(self, p):
        """
        func_name : ID
        """
        print_to_view(p);
        

    def p_bloco(self, p):
        """
        bloco : BLOCO_INIT instrucoes BLOCO_END
              | BLOCO_INIT BLOCO_END
        """
        print_to_view(p);
        pass

    def p_instrucoes(self, p):
        """
        instrucoes : instrucao instrucoes
                   | instrucao
        """
        print_to_view(p);
        pass

    def p_instrucao(self, p):
        """
        instrucao : call_func comentario
                  | atribuir comentario
                  | create_variable comentario
                  | ID END_LINE comentario
                  | if_logic comentario
        """
        pass

    def p_if_logic(self, p):
        """
        if_logic : IF LPAREN logic_test RPAREN BLOCO_INIT instrucoes BLOCO_END
        """

    def p_logic_test(self, p):
        """
        logic_test : logic OR logic_test
                   | NOT logic OR logic_test
                   | logic AND logic_test
                   | NOT logic AND logic_test
                   | logic
                   | NOT logic
        """

    def p_logic(self, p):
        """
        logic : TRUE
              | FALSE
              | ID DIF ID
              | ID EQCOMP ID
              | ID MENOR_QUE ID
              | ID MENOR_IGUAL ID
              | ID MAIOR_QUE ID
              | ID MAIOR_IGUAL ID
        """

    def p_atribuir(self, p):
        """
        atribuir : ID ASSIGN ID END_LINE
                 | ID ASSIGN call_func
                 | ID ASSIGN mat_result
        """
        print_to_view(p);
    def p_call_func(self, p):
        """
        call_func : ID LPAREN variaveis RPAREN END_LINE
                  | READ LPAREN variaveis RPAREN END_LINE
                  | READLN LPAREN variaveis RPAREN END_LINE
                  | WRITE LPAREN variaveis RPAREN END_LINE 
                  | WRITELN LPAREN variaveis RPAREN END_LINE
                  | SIZE LPAREN variaveis RPAREN END_LINE
        """

    def p_mat_result(self, p):
        """
        mat_result : type_and_id mat_operator type_and_id
        """
    def p_mat_operator(self, p):
        """
        mat_operator : PLUS
                     | MINUS
                     | MOD
                     | DIVISION
                     | TIMES
        """
    def p_type_and_id(self, p):
        """
        type_and_id : ID
                    | INTEGER
                    | FLOAT
        """
    def p_variaveis(self, p):
        """
        variaveis : variavel 
                  | variavel COMMA variaveis
        """
        pass

    def p_variavel(self, p):
        """
        variavel : ID
                 | STRING
        """
        pass

    def p_create_variable(self, p):
        """
        create_variable : BOOLEAN_TYPE ID assign
                        | INTEGER_TYPE ID assign
                        | FLOAT_TYPE ID assign
                        | STRING_TYPE ID assign
        """

    def p_assign(self, p):
        """
        assign : ASSIGN call_func
               | ASSIGN INTEGER END_LINE
               | ASSIGN FLOAT END_LINE

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
