program EXEMPLO1;
function hello():integer;
var A, B, MAIOR : integer;
var C : real;
var D : boolean;
begin
    MAIOR := 0;
    N:=TRUE;
    N:=FALSE;
    MAIOR := 0;
    write('Digite dois numeros: ');
    readln(A, B);
    if (B > A) then
    begin
        MAIOR:=B;
        writeln('O maior dos numeros ',A,' e ',B,' e ',MAIOR);
        s:=readln;
    end;
    while contad<10 do {Enquanto cont<10, condição é testada a cada repetição}
    begin
        writeln('7 x ',contad,' = ',7*contad);
        contad:=contad+1; {incrementamos o contador a cada repetição}
    end;
    for CONT:=1 to 10 do	 {para cont de 1 a 10 faça}
    begin
        write('Digite o nome e as 3 notas do ',cont,'o  aluno ');
        read(NOME,N1,N2,N3);
        if (N1>=0) then
        begin
            MEDIA:=(N1+N2+N3)/3;
            writeln('O aluno de nome ',NOME,' tem a média ',MEDIA,' em suas notas ');
        end
        else
        begin
            writeln('Notas invalidas!');
        end;
    end;
    repeat 
        clrscr;
        write('Digite um número para ver sua tabuada de multiplicação ');
        read(num);
        cont:=0;
        while cont<10 do  {temos aqui uma repetição dentro de outra}
        begin
            writeln((num*4)*2,' x ',cont,' = ',num*cont*6*2);
            cont:=cont+1; {a cada repetição o cont aumenta +1}
        end;
        readkey; {parada para ver o resultado até ser teclado algo}
    until num=0; {condição para parar a repetição principal}
    if (X > Y) then {Condição - SE X for maior que Y}
    begin
       writeln ('X é Maior que Y, e seu valor é = ', X);
    end;
    case X of
          1 : writeln ('Ola Mundo'); { E o valor de X for igual a 1, irá executar essa linha }
          2 : writeln ('GNOIA');     { X = 2, essa linha será executada }
          3 : writeln ('Software Livre'); { X = 3 - essa linha será executada }
     end;
end