.global _start
_start:
li zero, 0x2bdfaaeaec83074b
li ra, 0x77e40efca33660f2
li sp, 0x4b17a83ca823fd2
li gp, 0x34085d499dbbd461
li tp, 0x5de18be5300c5cce
li t0, 0xb40f931d9521ead
li t1, 0xdb980a6b8aa5cde
li t2, 0x4fde9d426dc2945a
li s0, 0x1baad4ad2949ad11
li s1, 0x2ef3cec5effa9fc2
li a0, 0x3afed78788b481b9
li a1, 0x699f65e608238a39
li a2, 0x16642d890efe5bc8
li a3, 0x4a5c2ee5462beb7d
li a4, 0x67502cc465614f6b
li a5, 0x52d48041a837eef2
li a6, 0x17f0ae31f9e5752c
li a7, 0x5e4e60270fcc991d
li s2, 0x41667f320c7f2d31
li s3, 0x6dd866563c4ed97a
li s4, 0x19eb69684ecfc345
li s5, 0x1534f6b084a19c31
li s6, 0x4231cf083073058d
li s7, 0x74e0f0659ca94beb
li s8, 0x533d7c3da1b85761
li s9, 0x7b1e7bdac528ae05
li s10, 0x13cdc6b2a66ef048
li s11, 0x57cc00799c3e1193
li t3, 0x30a922c4faa1f89b
li t4, 0x5a0455c0bd40016a
li t5, 0x7b051a2c399d2806
li t6, 0x254780b18724bfc1
li t0, 11
li t1, 1
loop:
beq t0, zero, done
nop
sub t0, t0, t1
j loop
done:
li a0, 0
li a7, 93
ecall
