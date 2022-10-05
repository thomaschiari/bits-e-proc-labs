; faz a troca do valor de RAM[0] com RAM[1] e coloca o valor 1 em RAM[3]

    leaw $R0, %A
    movw (%A), %D
    leaw $R2, %A
    movw %D, (%A)
    leaw $R1, %A
    movw (%A), %D
    leaw $R0, %A
    movw %D, (%A)
    leaw $R2, %A
    movw (%A), %D
    leaw $R1, %A
    movw %D, (%A)
    leaw $1, %A
    movw %A, %D
    leaw $R3, %A
    movw %D, (%A)
