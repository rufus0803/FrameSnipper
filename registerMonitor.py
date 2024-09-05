import mmap
import os

UART_BASE_ADDR = 0x7E201000
UART_FR_OFFSET = 0x18
UART_DR_OFFSET = 0x0

with open("/dev/mem", "r+b") as f:
	mem = mmap.mmap(f.fileno(), 4096, offset=UART_BASE_ADDR)
	
	def read_register(offset):
		mem.seek(offset)
		return int.from_bytes(mem.read(4), 'little')

	while True:
		fr_value =  read_register(UART_FR_OFFSET)
		rsr_value = read_register(UART_DR_OFFSET)
		print(f"UART_FR:{hex(fr_value)}, UART_DR:{hex(rsr_value)}")
