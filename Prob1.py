a,b=eval(input("Dati valori:"))
if a>b:
    while a>=b:
        print(a,"la 2 e ",a**2)
        break
else:
    while b>=a:
        print(b, " la 2 e ",b**2)
        break