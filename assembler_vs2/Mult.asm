@R0
D=M
@counter
M=D
@0
D=A
@R2
M=D
(LOOP)
    @counter
    D=M
    @END
    D;JEQ
    @R1
    D=M
    @R2
    M=M + D
    @counter
    M=M-1
    @LOOP
    0;JMP
(END)
    @END
    0;JMP