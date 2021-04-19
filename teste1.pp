program EXEMPLO1;
var
 A, B, MAIOR : integer;
begin
 write('Digite dois numeros: ');
 readln(A, B);
 MAIOR := A;
 if (B > A) then
 MAIOR:=B;
 writeln('O maior dos numeros ',A,' e ',B,' e ',MAIOR);
 readln;
end.