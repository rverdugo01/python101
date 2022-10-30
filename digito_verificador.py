
#string
#rut="12345678"
rut="14073720"
serie=[2,3,4,5,6,7]

#print(len(rut))
#sprint(int(rut[1]) * int(rut[2]) )

pos=0
digitosRut=[]

#extraer digitos
for  digito in rut:
     digitosRut.append(int(digito))
    
#invierto lista
digitosRut=list(reversed(digitosRut))

aux=0
s=0
for posx in range(8):
    print("for",posx)
    print("for aux",aux)

    if posx == 6 :
        aux=0
        s+= digitosRut[posx]*serie[aux]
        print(s)
        
    else:
        s+= digitosRut[posx]*serie[aux]
        print(s)
    
    aux=aux+1
    
    print("for aux",aux)

print("sumatoria",s)

print(s%11)


#calcula digito verificador
#hacer refactoring para que reciba el rut y retorne el digito verificador
def  calcularDigitoVerificador(s):
    
    #modulo
    modulo= s%11

    #calculo digito
    if ( (11-modulo) >= 1 ) and ( (11- modulo) <= 9 ):
        return (11-modulo)
    
    elif ( (11-modulo ) == 10 ):
        return 'k'

    else:
        if ((11-modulo == 11) ):
            return 0
    

print(calcularDigitoVerificador(s))
        


