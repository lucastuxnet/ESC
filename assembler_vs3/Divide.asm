//A entrada do programa será em (R13,R14), enquanto o resultado da divisao (R13 / R14) será armazenado em R15.
//O programa deve ter um tempo de execução logarítmico em relação ao tamanho da entrada.


@curr
M=1 //curr=1

@R15
M=0 // R15=0


@R14
D=M
@denom
M=D

@R13
D=M
@dev
M=D


// if denominador==0: finaliza o programa
@denom
D=M 
@END
D;JEQ // IF(R14==0)

// if denominador > dividendendo: finaliza o programa
@denom
D=M //D=*(denominador)
@dev // dividendo
D=D-M // denominador - dividendo
@END
D;JGT // denominador > dividendo (denominador - dividendo>0) : return 0


// if denominador == dividendo: finaliza o programa
@denom
D=M
@dev // dividendo
D=D-M // denominador - dividendo
@EQUAL
D;JEQ // denominador == dividendo (denominador - dividendo = 0) : return 1

	
(LOOP1)	
	@dev // dividendo
	D=M //D=*(R13)
	@denom // denominador
	D=D-M // D =  dividendo - denominador
	@LOOP2
	D;JLT // if(denominador > dividendo): pula para o loop2
	
	@denom 
	D=M<<
	@LOOP3
	D;JLE //para antes de dar overflow e não passa pro LOOP2
	
	@denom 
	M=M<< // denominador * 2
	@curr 
	M=M<< // curr * 2
	
	@LOOP1
	0;JMP
	
(LOOP2)
	@denom 
	M=M>> // denominador / 2
	@curr 
	M=M>> // curr / 2

(LOOP3)
	@curr
	D=M 
	@END
	D;JEQ // IF(curr == 0): finaliza o programa
	
	// IF(dividendo >= denominador)
	@dev
	D=M 
	@denom
	D=D-M // D = dividendo - denominador
	@LOOP4
	D;JGE 
	
	@LOOP3_B
	0;JMP
	
	
(LOOP3_B)	
	@curr
	M=M>> // curr / 2
	@denom
	M=M>>// denominador / 2
	
	@LOOP3
	0;JMP

(LOOP4)
	
	@denom
	D=M 
	@dev
	M = M-D // dividendo = dividendo - denominador
	
	
	@curr
	D=M 
	@R15
	M=D+M // R15 = resposta+curr
	
	@LOOP3_B
	0;JMP

(EQUAL)
	@R15
	M=1 // coloca o valor 1 no resultado
		
(END)
0;JMP
