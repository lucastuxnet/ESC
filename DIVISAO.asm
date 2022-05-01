//DIVISAO.asm

@13
D = M
@1
D = M
@0
M = M - D
@2
M = M + 1
@0
D = M
@1
M-D;JLE
@13
D;JMP

//Endereco ram 1 representa o resto
//Endereco ram 2 representa o resultado da divisao
