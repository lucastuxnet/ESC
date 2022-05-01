// Multiplica R0 com R1 e armazena o resultado em R2.
// (R0, R1, R2  são referentes a RAM[0], RAM[1], and RAM[2], respectivamente.)
// Iniciando a soma
// Initialize sum
@0   // Carrega 0 para dentro do registro A
D=A  // seta D para o valor do registro  que se encontra no endereço de A (0)
@R2  // R2 que sera armazenado os resultado
M=D  // seta  o valor dentro do registrador  D (0)
// Declarando o for
// Iniciando o contador i do for
@1   // inicia 1 dentro do registrador A
D=A  // defina D para o valor do endereço A (1)
@i   // registro de soma que detém "i" para incremento
M=D  // define o valor 1 em D (1)
// iniciando o loop
(LOOP)
  // Definindo as condições do loop
  @i     // inicia  i para o endereço de A
  D=M    // define D para o valor de i
  @R1    // define o valor de 1 para o registrador A
  D=M-D  // D = R1 - i
  @END
  D;JLT  // if i > R1 (D < 0 ) e fininaliza
  // Adicionado ao R2
  @R0    // inicia valor ao R0
  D=M    // coloca em D
  @R2   // carrega a soma ao registro
  M=D+M  // Adicione valor em R0, que deve estar em D
  // incrementa i
  @i
  M=M+1
  // Retorna para o inicio do loop
  @LOOP
  0;JMP
(END)
  @END
  0;JMP  // loop inifinito