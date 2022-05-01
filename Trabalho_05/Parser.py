#Trabalho 5 ESC
#Aluno: Lucas Albino Martins
#Matricula: 12011ECP022
#Parser.py The Elements of Computing Systems - cap6.

import re

class Parser(object):
    """Classes Parser.py"""

    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2
    _comment = re.compile(r'//.*$')

    def __init__(self, in_file):
        """Construtor - leitura do arquivo"""
        with open(in_file, 'r') as myf:
            self.lines = myf.readlines()
        self.command = ''
        self.cur_line = 0

    def has_more_commands(self):
        """Retorna true se mais comandos estiverem na entrada"""
        if (self.cur_line + 1) < len(self.lines):
            return True
        else:
            return False

    def advance(self):
        """Lê o próximo comando, transforma no comando atual"""     
        self.cur_line += 1
        line = self.lines[self.cur_line]                
        line = self._comment.sub('', line)
        if line == '\n':
            self.advance()
        else:
            self.command = line.strip()

    def command_type(self):
        """Retorna o tipo de comando atual"""
        if re.match(r'^@.*', self.command):
            return Parser.A_COMMAND
        elif re.match(r'^\(.*', self.command):
            return Parser.L_COMMAND
        else:
            return Parser.C_COMMAND

    def symbol(self):
        """Retorna o simbolo do comando atual @Xxx ou (Xxx)"""
        matching = re.match(r'^[@\(](.*?)\)?$', self.command)
        symbol = matching.group(1)
        return symbol

    def dest(self):
        """Retorna o mnemônico dest dentro do C-command"""
        # dest=comp;jump
        matching = re.match(r'^(.*?)=.*$', self.command)
        if not matching:
            dest = ''
        else:
            dest = matching.group(1)
        return dest

    def comp(self):
        """Retorna o comp mnemônico dentro do C-command"""
        # dest=comp;jump
        # remove dest e jump (caso existirem) e obtem o comp
        comp = re.sub(r'^.*?=', '', self.command) # remove dest
        comp = re.sub(r';\w+$', '', comp) # remove jump
        if not comp:
            print("Sem comp!")
            print(self.command)
        return comp.strip()

    def jump(self):
        """Retorna o jump mnemônico dentro do C-command"""
        # dest=comp;jump
        matching = re.match(r'^.*;(\w+)$', self.command)
        if not matching:
            jump = ''
        else:
            jump = matching.group(1)
        return jump
