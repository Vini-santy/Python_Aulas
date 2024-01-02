a = 'A'
b = 'B'
c = 1.1

# strings = 'a={} b={} c={:.2f}' -> sem indice
strings = 'a={nome1} b={nome2} c={nome3:.2f}' 
# formato = strings.format(a,b,c) -> sem parametro
formato = strings.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)