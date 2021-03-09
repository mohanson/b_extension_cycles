.global _start
_start:
li zero, 0x7a45a3b734bca97d
li ra, 0x394022dada073792
li sp, 0x64172c9b7587f6c1
li gp, 0x6e7df12583a54159
li tp, 0x53b0788cdea5ddba
li t0, 0x60eb30c2d1ef7556
li t1, 0x7f14b47eb78fa647
li t2, 0x1ff98cd17d316e42
li s0, 0x21014346c758799f
li s1, 0x407e1e5e66b0fd9b
li a0, 0x2e7f10fd75e7f4b8
li a1, 0x6c8b1855dcc8f34a
li a2, 0x89f2e8841c8bd1c
li a3, 0x70f9d3eb49ed1660
li a4, 0x5f45893ce1b0fdf2
li a5, 0x398f3b20c9043617
li a6, 0x54fd004933a5ea06
li a7, 0x1ced796184ea8d73
li s2, 0x33ed2fbc1ee3e936
li s3, 0x326fe83ebbc6da40
li s4, 0x5ba452248bd4d52b
li s5, 0x69282d25e092913
li s6, 0x328bbed495e91988
li s7, 0x4edd0d9587e92002
li s8, 0x4061e89695ea4dfe
li s9, 0x2ff0a98703dbfed2
li s10, 0x31980a35ad9969f3
li s11, 0x3c9ae7c3b6b8237d
li t3, 0x1978c6dd4ea48f2a
li t4, 0x3018b52e29729ef2
li t5, 0x706b9557128902b1
li t6, 0x3b363b12dfde54f7
li t0, 1
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
