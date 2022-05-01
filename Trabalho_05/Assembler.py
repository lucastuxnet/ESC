#Trabalho 5 ESC
#Aluno: Lucas Albino Martins
#Matricula: 12011ECP022
#Assembly.py The Elements of Computing Systems - cap6.

import sys
import Parser
import Code
import SymbolTable

class Assembler(object):
    """Classes Assembly"""

    def __init__(self, in_file):
        """Construtor"""
        self.in_file = in_file
        self.out_file = self._get_out_file(in_file)
        self.symbol_table = SymbolTable.SymbolTable()
        self.symbol_address = 16 #  endereços de simbolo começam em 16

    def assemble(self):
        """Codigo em Assembly"""
        self.first_pass()
        self.second_pass()


    def first_pass(self):
        """Primeira passagem para construir a tabela de símbolos"""
        parser = Parser.Parser(self.in_file)
        cur_address = 0
        while parser.has_more_commands():
            parser.advance()
            if parser.command_type() == parser.A_COMMAND \
                    or parser.command_type() == parser.C_COMMAND:
                cur_address += 1
            elif parser.command_type() == parser.L_COMMAND:
                self.symbol_table.add_entry(parser.symbol(), cur_address)

    def second_pass(self):
        """Segunda passagem transforma em Assembly"""
        parser = Parser.Parser(self.in_file)
        outf = open( self.out_file, 'w')
        code = Code.Code()
        while(parser.has_more_commands()):
            parser.advance()
            if parser.command_type() == parser.A_COMMAND:
                outf.write(code.gen_a_code(self._get_address(parser.symbol()))
                        + '\n')
            elif parser.command_type() == parser.C_COMMAND:
                outf.write(code.gen_c_code(parser.comp(), parser.dest(),
                    parser.jump()) + '\n')
            elif parser.command_type == parser.L_COMMAND:
                pass
        outf.close()


    def _get_address(self, symbol):
        """Retorna o endereço do simbolo"""
        if symbol.isdigit():
            return symbol
        else:
            if not self.symbol_table.contains(symbol):
                self.symbol_table.add_entry(symbol, self.symbol_address)
                self.symbol_address += 1
            return self.symbol_table.get_address(symbol)

    @staticmethod
    def _get_out_file(in_file):
        """traduz o arquivo de entrada para o nome do arquivo de saida"""
        if in_file.endswith('.asm'):
            return in_file.replace('.asm', '.hack')
        else:
            return in_file + '.hack'


def main():
    """Corpo principal"""
    in_file = ""
    if len(sys.argv) !=2:
        print("Exemplo: Assembler.py arquivo.asm")
    else:
        in_file = sys.argv[1]

    asm = Assembler(in_file)
    asm.assemble()

main()
