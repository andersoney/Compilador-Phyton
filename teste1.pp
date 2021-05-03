program EXEMPLO1;
function hello():integer;
var
 A, B, MAIOR : integer;
begin
 MAIOR := 0;
 N:=TRUE;
 N:=FALSE;
 MAIOR := 0;
 write('Digite dois numeros: ');
 readln(A, B);
 if (B > A) then
 MAIOR:=B;
 writeln('O maior dos numeros ',A,' e ',B,' e ',MAIOR);
 s:=readln;
 while contad<10 do {Enquanto cont<10, condição é testada a cada repetição}
   begin
    writeln('7 x ',contad,' = ',7*contad);
    contad:=contad+1; {incrementamos o contador a cada repetição}
   end;
end.