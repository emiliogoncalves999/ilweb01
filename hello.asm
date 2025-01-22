section .data
    hello db 'Hello, World!', 0    ; String yang akan dicetak

section .text
    global _start                   ; Entry point untuk linker

_start:
    ; Tuliskan string ke stdout
    mov rax, 1                     ; syscall number untuk sys_write
    mov rdi, 1                     ; file descriptor 1 adalah stdout
    mov rsi, hello                 ; alamat string
    mov rdx, 13                    ; panjang string
    syscall                        ; panggil kernel

    ; Keluar dari program
    mov rax, 60                    ; syscall number untuk sys_exit
    xor rdi, rdi                   ; status keluar 0
    syscall                        ; panggil kernel
