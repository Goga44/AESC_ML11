section .data
    num1 dq 10  ; первое число
    num2 dq 20  ; второе число
    newline db 10
    
section .bss
    buffer resb 12

section .text
    global _start
    
_start:
    ; Вычисляем сумму
    mov rax, [num1]
    add rax, [num2]
    
    mov rdi, buffer + 11 
    mov byte [rdi], 10   
    mov rbx, 10          
    
convert:
    xor rdx, rdx
    div rbx            
    add dl, '0'         
    dec rdi
    mov [rdi], dl
    test rax, rax
    jnz convert
    
print:
    mov rsi, rdi        
    mov rdx, buffer + 12
    sub rdx, rdi      
    
    ; Выводим результат
    mov rax, 1          
    mov rdi, 1          
    syscall
    
    mov rax, 60
    xor rdi, rdi
    syscall