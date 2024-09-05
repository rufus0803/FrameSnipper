import mmap
import os
import struct
import time

# Constants
BCM2835_PERI_BASE = 0x3F000000
UART0_BASE = BCM2835_PERI_BASE + 0x201000
UART0_FR = UART0_BASE + 0x18

UART_FR_TXFE = 0x80  # Transmit FIFO empty
UART_FR_RXFF = 0x40  # Receive FIFO full
UART_FR_TXFF = 0x20  # Transmit FIFO full
UART_FR_RXFE = 0x10  # Receive FIFO empty
UART_FR_BUSY = 0x08  # UART busy

PAGE_SIZE = mmap.PAGESIZE
BLOCK_SIZE = 4096

def setup_io():
    # Open /dev/mem
    mem_fd = os.open("/dev/mem", os.O_RDWR | os.O_SYNC)
    # Memory map the UART registers
    mem = mmap.mmap(
        fileno=mem_fd,
        length=BLOCK_SIZE,
        flags=mmap.MAP_SHARED,
        prot=mmap.PROT_READ | mmap.PROT_WRITE,
        offset=UART0_BASE & ~(BLOCK_SIZE - 1)
    )
    os.close(mem_fd)
    return mem

def read_register(mem, offset):
    # Seek to the register offset
    mem.seek(offset & (BLOCK_SIZE - 1))
    # Read 4 bytes from the memory map
    return struct.unpack('I', mem.read(4))[0]

def check_uart_fifo(mem):
    fr = read_register(mem, UART0_FR)
    
    if fr & UART_FR_TXFF:
        print("UART Transmit FIFO is full")
    if fr & UART_FR_RXFE:
        print("UART Receive FIFO is empty")
    # Add more checks for other flags if needed

def main():
    mem = setup_io()
    try:
        while True:
            check_uart_fifo(mem)
            time.sleep(0.1)  # Sleep for 100ms
    finally:
        mem.close()

if __name__ == "__main__":
    main()
