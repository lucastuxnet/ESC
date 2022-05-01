//Multiplica R0 e R1 e armazena o resultado em R2.
//(R0, R1, R2 referem-se a RAM [0], RAM [1] e RAM [2], respectivamente.)
//Soma R1 com ele mesmo a quantidade de vezes de R2

//Inicializa contador "i" para o R1
@R1
D=M
@i
M=D

// Inicializa o R2 em 0
@R2
M=0

// O loop irá diminuir i em 1 e se for maior que 0
// soma R1 ao resultado, senão vamos para o fim
(LOOP)
// Se i for 0 => sai do programa
@i
D=M
@END
D;JEQ

// Adiciona o resultado em R0
@R0
D=M
@R2
M=D+M

// Diminuir o valor de i "--i"
@i
M=M-1

@LOOP
0; JMP


(END)
@END
0; JMP
