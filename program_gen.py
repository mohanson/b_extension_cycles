import random
import os
import shutil
import subprocess
import typing

import convention

c_binary_as = '/opt/riscv64b/bin/riscv64-unknown-elf-as'
c_binary_as_args = '-march=rv64gcb'
c_binary_ld = '/opt/riscv64b/bin/riscv64-unknown-elf-ld'


def rand_idel_registers():
    return random.choice(convention.registers[:-1])


def rand_u64():
    return hex(random.randint(0, 63))


def rand_u32():
    return hex(random.randint(0, 31))


class Writer:

    def __init__(self, name: str):
        self.name = name
        self.f = open(self.name, 'w')

    def line(self, line: str):
        self.f.write(line)
        self.f.write('\n')


shutil.rmtree('program', ignore_errors=True)
os.mkdir('program')

for rule in [
    ['nop', [], ['nop'], []],
    ['ecall', ['li a7, 1111'], ['ecall'], []],
    ['grevi', [], ['grevi t6, t6, 63'], []],
    ['shfli', [], ['shfli t6, t6, 31'], []],
    ['gorci', [], ['gorci t6, t6, 63'], []],
    ['bfp', [], ['bfp t6, t6, t5'], []],
    ['bext', [], ['bext t6, t6, t5'], []],
    ['clmul', [], ['clmul t6, t6, t5'], []],
    ['crc32.b', [], ['crc32.b t6, t5'], []],
    ['bmatflip', [], ['bmatflip t6, t5'], []],
    ['bmator', [], ['bmator t6, t6, t5'], []],
    ['bmatxor', [], ['bmatxor t6, t6, t5'], []],
]:
    inst = rule[0]
    for c in [1, 1001]:
        name = f'{inst}_{c}'
        w = Writer(f'program/{name}.S')
        w.line('.global _start')
        w.line('_start:')
        for j in convention.registers:
            w.line(f'li {j}, {hex(random.randint(0, 1<<64 - 1))}')
        for j in rule[1]:
            w.line(j)
        w.line(f'li t0, {c}')
        w.line('li t1, 1')
        w.line('loop:')
        w.line('beq t0, zero, done')
        for i in rule[2]:
            w.line(i)
        w.line('sub t0, t0, t1')
        w.line('j loop')
        w.line('done:')
        w.line('li a0, 0')
        w.line('li a7, 93')
        w.line('ecall')
        w.f.close()
        subprocess.call(f'{c_binary_as} {c_binary_as_args} -o program/{name}.o program/{name}.S', shell=True)
        subprocess.call(f'{c_binary_ld} -o program/{name} program/{name}.o', shell=True)
