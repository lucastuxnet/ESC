#Trabalho 5 ESC
#Aluno: Lucas Albino Martins
#Matricula: 12011ECP022
#Code.py The Elements of Computing Systems - cap6.

class Code(object):
    """Classes Code.py"""

    _dest_codes = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
    _comp_codes = {
            '0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100',
            'A':'0110000', '!D':'0001101', '!A':'0110001', '-D':'0001111',
            '-A':'0110011', 'D+1':'0011111','A+1':'0110111','D-1':'0001110',
            'A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111',
            'D&A':'0000000','D|A':'0010101',
            '':'xxxxxxx',
            'M':'1110000', '!M':'1110001', '-M':'1110011', 'M+1':'1110111',
            'M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111',
            'D&M':'1000000', 'D|M':'1010101' }
    _jump_codes = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']

    def __init__(self):
        """Construtor"""
        pass

    def gen_a_code(self, address):
        """Retorna codigo binario para uma instrução tipo A"""
        return '0' + self._bits(address).zfill(15)

    def gen_c_code(self, comp, dest, jump):
        """Retorna codigo binario para uma instrução tipo C"""
        return '111' + self.comp(comp) + self.dest(dest) + self.jump(jump)

    def dest(self, mnemonic):
        """Retorna o codigo binario para o dest mnemônico"""
        return self._bits(self._dest_codes.index(mnemonic)).zfill(3)

    def comp(self, mnemonic):
        """Retorna o codigo binario para o comp mnemônico"""
        return self._comp_codes[mnemonic]

    def jump(self, mnemonic):
        """Retorna o codigo binario para o jump mnemônico"""
        return self._bits(self._jump_codes.index(mnemonic)).zfill(3)

    @staticmethod
    def _bits(num):
        """Converte int n para binario"""
        return bin(int(num))[2:]
