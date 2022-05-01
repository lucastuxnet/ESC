from ecs_simulator import *

Library.author("Lucas Albino Martins")

Not = Gate('Not', 1, ['in'], ['out'])
Not.set_as_vcc(0, 'C')
Not.set_as_gnd(0, 'E')
Not.set_as_input(0, 'B', 'in')
Not.set_as_output(0, 'C', 'out')
Not.save()

Not_b = Library.load('Not')
Not_b.test_all()

And = Gate('And', 2, ['a', 'b'], ['out'])
And.set_as_vcc(0, 'C')
And.set_as_gnd(1, 'E')
And.connect(0, 'E', 1, 'C')
And.set_as_input(0, 'B', 'a')
And.set_as_input(1, 'B', 'b')
And.set_as_output(1, 'E', 'out')
And.save()

And.test_all()

Or = Gate('Or', 2, ['a', 'b'], ['out'])
Or.set_as_vcc(0, 'C')
Or.set_as_gnd(1, 'E')
Or.connect(0, 'C', 1, 'C')
Or.connect(0, 'E', 1, 'E')
Or.set_as_input(0, 'B', 'a')
Or.set_as_input(1, 'B', 'b')
Or.set_as_output(1, 'E', 'out')
Or.save()

Or.test_all()

Nand = Gate('Nand', 2, ['a', 'b'], 'out')
Nand.set_as_vcc(0, 'C')
Nand.set_as_gnd(1, 'E')
Nand.set_as_input(0, 'B', 'a')
Nand.set_as_input(1, 'B', 'b')
Nand.set_as_output(1, 'C', 'out')
Nand.connect(0, 'E', 1, 'C')
Nand.test_all()
Nand.save()

Nand.test_all()

Xor = Circuit('Xor', ['a', 'b'], ['out'])
Xor.add_components(Nand, Library.load('Or'), Library.load('And'))
Xor.set_as_input(0, 'a', 'a')
Xor.set_as_input(0, 'b', 'b')
Xor.set_as_output(2, 'out', 'out')
Xor.connect(0, 'a', 1, 'a')
Xor.connect(0, 'b', 1, 'b')
Xor.connect(0, 'out', 2, 'a')
Xor.connect(1, 'out', 2, 'b')
Xor.save()

Xor.test_all()

Mux = Circuit('Mux', ['a', 'b', 'sel'], 'out')
Mux.add_components(Not, (And, 2), Or)
Mux.set_as_input(1, 'b', 'a')
Mux.set_as_input(2, 'b', 'b')
Mux.set_as_output(3, 'out', 'out')
Mux.connect(1, 'out', 3, 'a')
Mux.connect(2, 'out', 3, 'b')
Mux.set_as_input(0, 'in', 'sel')
Mux.set_as_input(2, 'a', 'sel')
Mux.connect(0, 'out', 1, 'a')
Mux.save()

Mux.test_all(label_display_order=['sel', 'a', 'b'])

DMux = Circuit('DMux', ['in', 'sel'], ['a', 'b'])
DMux.add_components(Not, (And, 2))
# PORTA NOT
# ENTRADA
DMux.set_as_input(0, 'in', 'sel')
# SAIDA
# VIROU O CONECT
# PRIMEIRA PORTA AND
# ENTRADA
DMux.set_as_input(1, 'a', 'in')
# VIROU O CONECT
# SAIDA
DMux.set_as_output(1, 'out', 'a')
# SEGUNDA PORTA AND
DMux.set_as_input(2, 'a', 'in')
DMux.set_as_input(2, 'b', 'sel')
# SAIDA
DMux.set_as_output(2, 'out', 'b')
# CONNECT
DMux.connect(0, 'out', 1, 'b')
DMux.save()

DMux.test_all(label_display_order=['sel', 'in'])

Not16 = Circuit('Not16', lbs('in', 16), lbs('out', 16))
Not16.add_components((Not, 16))
for i in range(16):
    Not16.set_as_input(i, 'in', f'in{i}')
    Not16.set_as_output(i, 'out', f'out{i}')
Not16.save()
Not16.test_set([
    [1]*16,
    [0]*16,
], label_display_order=lbs('in', 16))

Mux16 = Circuit('Mux16', lbs('a', 16)+lbs('b', 16)+['sel'], lbs('out', 16))
Mux16.add_components((Mux, 16))
for i in range(16):
    Mux16.set_as_input(i, 'a', f'a{i}')
    Mux16.set_as_input(i, 'b', f'b{i}')
    Mux16.set_as_input(i, 'sel', 'sel')
    Mux16.set_as_output(i, 'out', f'out{i}')
Mux16.save()

Mux16.test_set([
    [1]*16 + [0]*16 + [0],
    [0]*16 + [1]*16 + [1],
], label_display_order=['sel']+lbs('a', 16)+lbs('b', 16))

And16 = Circuit('And16', lbs('a', 16)+lbs('b', 16), lbs('out', 16))
And16.add_components((And, 16))
for i in range(16):
    And16.set_as_input(i, 'a', f'a{i}')
    And16.set_as_input(i, 'b', f'b{i}')
    And16.set_as_output(i, 'out', f'out{i}')
And16.save()
And16.test_set([
    [1]*16 + [0]*16,
    [0]*16 + [1]*16,
], label_display_order=lbs('a', 16)+lbs('b', 16))

Or16 = Circuit('Or16', lbs('a', 16)+lbs('b', 16), lbs('out', 16))
Or16.add_components((Or, 16))
for i in range(16):
    Or16.set_as_input(i, 'a', f'a{i}')
    Or16.set_as_input(i, 'b', f'b{i}')
    Or16.set_as_output(i, 'out', f'out{i}')
Or16.save()
Or16.test_set([
    [1]*16 + [0]*16,
    [0]*16 + [1]*16,
], label_display_order=lbs('a', 16)+lbs('b', 16))

Or8way = Gate('Or8way', 8, lbs('in', 8), 'out')
Or8way.set_as_vcc(0, 'C')
Or8way.set_as_gnd(0, 'E')
for i in range(1, 8):
    Or8way.connect(0, 'C', i, 'C')
    Or8way.connect(0, 'E', i, 'E')
for i in range(8):
    Or8way.set_as_input(i, 'B', f'in{i}')
Or8way.set_as_output(0, 'E', 'out')
Or8way.save()

Or8way.test_all()

And8Way = Gate('And8Way', 8, lbs('in', 8), 'out')
And8Way.set_as_vcc(0, 'C')
And8Way.set_as_gnd(1, 'E')
for i in range(1, 8):
    And8Way.connect(0, 'E', i, 'C')
for i in range(8):
    And8Way.set_as_input(i, 'B', f'in{i}')
And8Way.set_as_output(0, 'E', 'out')
And8Way.save()
And8Way.test_all()

Mux4way = Circuit('Mux4way', lbs('@', 4)+['sel1', 'sel0'], 'out')
Mux4way.add_components((Mux, 3))
Mux4way.set_as_input(2, 'sel', 'sel1')
Mux4way.set_as_input(0, 'sel', 'sel0')
Mux4way.set_as_input(1, 'sel', 'sel0')
Mux4way.set_as_input(0, 'a', 'a')
Mux4way.set_as_input(0, 'b', 'b')
Mux4way.set_as_input(1, 'a', 'c')
Mux4way.set_as_input(1, 'b', 'd')
Mux4way.set_as_output(2, 'out', 'out')
Mux4way.connect(0, 'out', 2, 'a')
Mux4way.connect(1, 'out', 2, 'b')
Mux4way.save()

Mux4way.test_all(label_display_order=['sel1', 'sel0']+lbs('@', 4))

DMux4Way = Circuit('DMux4Way', ['in']+lbs('sel', 2), ['a', 'b', 'c', 'd'])
DMux4Way.add_components((DMux, 3))
DMux4Way.set_as_input(0, 'in', 'in')
DMux4Way.set_as_input(0, 'sel', f'sel{0}')
DMux4Way.set_as_input(1, 'sel', f'sel{1}')
DMux4Way.set_as_output(1, 'a', 'a')
DMux4Way.set_as_output(1, 'b', 'c')
DMux4Way.set_as_input(2, 'sel', f'sel{1}')
DMux4Way.set_as_output(2, 'a', 'b')
DMux4Way.set_as_output(2, 'b', 'd')
DMux4Way.connect(0, 'a', 1, 'in')
DMux4Way.connect(0, 'b', 2, 'in')
DMux4Way.save()
DMux4Way.test_all()

Mux8Way = Circuit('Mux8Way', ['a', 'b', 'c', 'd',
                  'e', 'f', 'g', 'h']+lbs('sel', 3), ['out'])
Mux8Way.add_components((Mux, 7))
Mux8Way.set_as_input(0, 'a', 'a')
Mux8Way.set_as_input(0, 'b', 'b')
Mux8Way.set_as_input(0, 'sel', f'sel{0}')
Mux8Way.connect(0, 'out', 4, 'a')
Mux8Way.set_as_input(1, 'a', 'c')
Mux8Way.set_as_input(1, 'b', 'd')
Mux8Way.set_as_input(1, 'sel', f'sel{0}')
Mux8Way.connect(1, 'out', 4, 'b')
Mux8Way.set_as_input(2, 'a', 'e')
Mux8Way.set_as_input(2, 'b', 'f')
Mux8Way.set_as_input(2, 'sel', f'sel{0}')
Mux8Way.connect(2, 'out', 5, 'a')
Mux8Way.set_as_input(3, 'a', 'g')
Mux8Way.set_as_input(3, 'b', 'h')
Mux8Way.set_as_input(3, 'sel', f'sel{0}')
Mux8Way.connect(3, 'out', 5, 'b')
Mux8Way.set_as_input(4, 'sel', f'sel{1}')
Mux8Way.connect(4, 'out', 6, 'a')
Mux8Way.set_as_input(5, 'sel', f'sel{1}')
Mux8Way.connect(5, 'out', 6, 'b')
Mux8Way.set_as_input(6, 'sel', f'sel{2}')
Mux8Way.set_as_output(6, 'out', 'out')
Mux8Way.save()


DMux8Way = Circuit('DMux8Way', ['in']+lbs('sel', 3),
                   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
DMux8Way.add_components(DMux, (DMux4Way, 2))
DMux8Way.set_as_input(0, 'in', 'in')
DMux8Way.set_as_input(0, 'sel', f'sel{2}')
DMux8Way.connect(0, 'a', 1, 'in')
DMux8Way.connect(0, 'b', 2, 'in')
DMux8Way.set_as_input(1, f'sel{0}', f'sel{0}')
DMux8Way.set_as_input(1, f'sel{1}', f'sel{1}')
DMux8Way.set_as_output(1, 'a', 'a')
DMux8Way.set_as_output(1, 'b', 'b')
DMux8Way.set_as_output(1, 'c', 'c')
DMux8Way.set_as_output(1, 'd', 'd')
DMux8Way.set_as_input(2, f'sel{0}', f'sel{0}')
DMux8Way.set_as_input(2, f'sel{1}', f'sel{1}')
DMux8Way.set_as_output(2, 'a', 'e')
DMux8Way.set_as_output(2, 'b', 'f')
DMux8Way.set_as_output(2, 'c', 'g')
DMux8Way.set_as_output(2, 'd', 'h')
DMux8Way.save()

Mux4Way16 = Circuit('Mux4Way16', lbs('a', 16)+lbs('b', 16) +
                    lbs('c', 16)+lbs('d', 16)+lbs('sel', 2), lbs('out', 16))
Mux4Way16.add_components((Mux4way, 16))
for i in range(16):
    Mux4Way16.set_as_input(i, 'a', f'a{i}')
    Mux4Way16.set_as_input(i, 'b', f'b{i}')
    Mux4Way16.set_as_input(i, 'c', f'c{i}')
    Mux4Way16.set_as_input(i, 'd', f'd{i}')
    Mux4Way16.set_as_input(i, f'sel{0}', f'sel{0}')
    Mux4Way16.set_as_input(i, f'sel{1}', f'sel{1}')
    Mux4Way16.set_as_output(i, 'out', f'out{i}')
Mux4Way16.save()

Mux8Way16 = Circuit('Mux8Way16', lbs('a', 16)+lbs('b', 16)+lbs('c', 16)+lbs('d', 16) +
                    lbs('e', 16)+lbs('f', 16)+lbs('g', 16)+lbs('h', 16)+lbs('sel', 3), lbs('out', 16))
Mux8Way16.add_components((Mux8Way, 16))
for i in range(16):
    Mux8Way16.set_as_input(i, 'a', f'a{i}')
    Mux8Way16.set_as_input(i, 'b', f'b{i}')
    Mux8Way16.set_as_input(i, 'c', f'c{i}')
    Mux8Way16.set_as_input(i, 'd', f'd{i}')
    Mux8Way16.set_as_input(i, 'e', f'e{i}')
    Mux8Way16.set_as_input(i, 'f', f'f{i}')
    Mux8Way16.set_as_input(i, 'g', f'g{i}')
    Mux8Way16.set_as_input(i, 'h', f'h{i}')
    Mux8Way16.set_as_input(i, f'sel{0}', f'sel{0}')
    Mux8Way16.set_as_input(i, f'sel{1}', f'sel{1}')
    Mux8Way16.set_as_input(i, f'sel{2}', f'sel{2}')
    Mux8Way16.set_as_output(i, 'out', f'out{i}')
Mux8Way16.save()

DMux4Way16 = Circuit('DMux4Way16', lbs('in', 16)+lbs('sel', 2),
                     lbs('a', 16)+lbs('b', 16)+lbs('c', 16)+lbs('d', 16))
DMux4Way16.add_components((DMux4Way, 16))
for i in range(16):
    DMux4Way16.set_as_input(i, 'in', f'in{i}')
    DMux4Way16.set_as_input(i, f'sel{0}', f'sel{0}')
    DMux4Way16.set_as_input(i, f'sel{1}', f'sel{1}')
    DMux4Way16.set_as_output(i, 'a', f'a{i}')
    DMux4Way16.set_as_output(i, 'b', f'b{i}')
    DMux4Way16.set_as_output(i, 'c', f'c{i}')
    DMux4Way16.set_as_output(i, 'd', f'd{i}')
DMux4Way16.save()

DMux8Way16 = Circuit('DMux8Way16', lbs('in', 16)+lbs('sel', 3), lbs('a', 16)+lbs(
    'b', 16)+lbs('c', 16)+lbs('d', 16)+lbs('e', 16)+lbs('f', 16)+lbs('g', 16)+lbs('h', 16))
DMux8Way16.add_components((DMux8Way, 16))
for i in range(16):
    DMux8Way16.set_as_input(i, 'in', f'in{i}')
    DMux8Way16.set_as_input(i, f'sel{0}', f'sel{0}')
    DMux8Way16.set_as_input(i, f'sel{1}', f'sel{1}')
    DMux8Way16.set_as_input(i, f'sel{2}', f'sel{2}')
    DMux8Way16.set_as_output(i, 'a', f'a{i}')
    DMux8Way16.set_as_output(i, 'b', f'b{i}')
    DMux8Way16.set_as_output(i, 'c', f'c{i}')
    DMux8Way16.set_as_output(i, 'd', f'd{i}')
    DMux8Way16.set_as_output(i, 'e', f'e{i}')
    DMux8Way16.set_as_output(i, 'f', f'f{i}')
    DMux8Way16.set_as_output(i, 'g', f'g{i}')
    DMux8Way16.set_as_output(i, 'h', f'h{i}')
DMux8Way16.save()

HalfAdder = Circuit('HalfAdder', ['a', 'b'], ['sum', 'carry'])
HalfAdder.add_components(Xor, And)
HalfAdder.set_as_input(0, 'a', 'a')
HalfAdder.set_as_input(0, 'b', 'b')
HalfAdder.set_as_output(0, 'out', 'sum')
HalfAdder.set_as_input(1, 'a', 'a')
HalfAdder.set_as_input(1, 'b', 'b')
HalfAdder.set_as_output(1, 'out', 'carry')
HalfAdder.save()
HalfAdder.test_all()

FullAdder = Circuit('FullAdder', ['a', 'b', 'c'], ['sum', 'carry'])
FullAdder.add_components((HalfAdder, 2), Or)
FullAdder.set_as_input(0, 'a', 'a')
FullAdder.set_as_input(0, 'b', 'b')
FullAdder.connect(0, 'sum', 1, 'a')
FullAdder.connect(0, 'carry', 2, 'a')
FullAdder.set_as_input(1, 'b', 'c')
FullAdder.set_as_output(1, 'sum', 'sum')
FullAdder.connect(1, 'carry', 2, 'b')
FullAdder.set_as_output(2, 'out', 'carry')
FullAdder.save()
FullAdder.test_all()

FullAdd16 = Circuit('FullAdd16', lbs('a', 16)+lbs('b', 16) +
                    ['carryin'], lbs('out', 16) + ['carryout'])
FullAdd16.add_components((FullAdder, 16))
FullAdd16.set_as_input(0, 'a', f'a{0}')
FullAdd16.set_as_input(0, 'b', f'b{0}')
FullAdd16.set_as_input(0, 'c', 'carryin')
FullAdd16.set_as_output(0, 'sum', f'out{0}')
FullAdd16.connect(0, 'carry', 1, 'c')
for i in range(1, 14):
    FullAdd16.set_as_input(i, 'a', f'a{i}')
    FullAdd16.set_as_input(i, 'b', f'b{i}')
    FullAdd16.connect(i, 'carry', (i+1), 'c')
    FullAdd16.set_as_output(i, 'sum', f'out{i}')
FullAdd16.set_as_input(15, 'a', f'a{15}')
FullAdd16.set_as_input(15, 'b', f'b{15}')
FullAdd16.set_as_output(15, 'sum', f'out{15}')
FullAdd16.set_as_output(15, 'carry', 'carryout')
FullAdd16.save()

Add16 = Circuit('Add16', lbs('a', 16)+lbs('b', 16),
                lbs('out', 16))
Add16.add_components(Not, And, FullAdd16)
Add16.set_as_input(0, 'in', f'a{0}')
Add16.connect(0, 'out', 1, 'b')
Add16.set_as_input(1, 'a', f'a{0}')
Add16.connect(1, 'out', 2, 'carryin')
for i in range(16):
    Add16.set_as_input(2, f'a{i}', f'a{i}')
    Add16.set_as_input(2, f'b{i}', f'b{i}')
    Add16.set_as_output(2, f'out{i}', f'out{i}')
Add16.save()

Inc16 = Circuit('Inc16', lbs('in', 16), lbs('out', 16)+['carryout'])
Inc16.add_components(Not16, And16, Not, Or, FullAdd16)
for i in range(16):
    Inc16.set_as_input(0, f'in{i}', f'in{i}')
    Inc16.connect(0, f'out{i}', 1, f'b{i}')
    Inc16.connect(1, f'out{i}', 4, f'b{i}')
    Inc16.set_as_input(4, f'a{i}', f'in{i}')
    Inc16.set_as_output(4, f'out{i}', f'out{i}')
Inc16.set_as_input(2, 'in', f'in{0}')
Inc16.connect(2, 'out', 3, 'b')
Inc16.set_as_input(3, 'a', f'in{0}')
Inc16.connect(3, 'out', 4, 'carryin')
#Inc16.set_as_input(4, 'carryout', False)
Inc16.save()

Or16Way = Circuit('Or16Way', lbs('in', 16), ['out'])
Or16Way.add_components((Or8way, 2), Or)
Or16Way.connect(0, 'out', 2, 'a')
Or16Way.connect(1, 'out', 2, 'b')
Or16Way.set_as_output(2, 'out', 'out')
for i in range(8):
    Or16Way.set_as_input(0, f'in{i}', f'in{i}')
    Or16Way.set_as_input(1, f'in{i}', f'in{i+8}')
Or16Way.save()

ALU = Circuit('ALU', lbs('x', 16)+lbs('y', 16)+['zx', 'nx', 'zy', 'ny', 'f', 'no'], lbs('out', 16)+['zr', 'ng'])
ALU.add_components((Not16, 6), (And16, 2), (Mux16, 6), Add16, Or16Way, Not)
ALU.set_as_input(8, 'sel', 'zx')
ALU.set_as_input(9, 'sel', 'zy')
ALU.set_as_input(10, 'sel', 'nx')
ALU.set_as_input(11, 'sel', 'ny')
ALU.set_as_input(12, 'sel', 'f')
ALU.set_as_input(13, 'sel', 'no')
ALU.connect(15, 'out', 16, 'in')
ALU.set_as_output(16, 'out', 'zr')
for i in range(16):
    ALU.set_as_input(0, f'in{i}', f'x{i}')
    ALU.connect(0, f'out{i}', 6, f'b{i}')
    ALU.set_as_input(6, f'a{i}', f'x{i}')
    ALU.connect(6, f'out{i}', 8, f'b{i}')
    ALU.connect(6, f'out{i}', 9, f'b{i}')
    ALU.set_as_input(8, f'a{i}', f'x{i}')
    ALU.connect(8, f'out{i}', 1, f'in{i}')
    ALU.connect(8, f'out{i}', 10, f'a{i}')
    ALU.set_as_input(9, f'a{i}', f'y{i}')
    ALU.connect(9, f'out{i}', 2, f'in{i}')
    ALU.connect(9, f'out{i}', 11, f'a{i}')
    ALU.connect(1, f'out{i}', 10, f'b{i}')
    ALU.connect(2, f'out{i}', 11, f'b{i}')
    ALU.connect(10, f'out{i}', 14, f'a{i}')
    ALU.connect(10, f'out{i}', 7, f'a{i}')
    ALU.connect(11, f'out{i}', 14, f'b{i}')
    ALU.connect(11, f'out{i}', 7, f'b{i}')
    ALU.connect(14, f'out{i}', 12, f'b{i}')
    ALU.connect(7, f'out{i}', 12, f'a{i}')
    ALU.connect(12, f'out{i}', 3, f'in{i}')
    ALU.connect(12, f'out{i}', 13, f'a{i}')
    ALU.connect(3, f'out{i}', 13, f'b{i}')
    ALU.connect(13, f'out{i}', 4, f'in{i}')
    ALU.connect(13, f'out{i}', 15, f'in{i}')
    ALU.connect(4, f'out{i}', 5, f'in{i}')
    ALU.set_as_output(5, f'out{i}', f'out{i}')
ALU.set_as_output(13, f'out{15}', 'ng')
ALU.save()
