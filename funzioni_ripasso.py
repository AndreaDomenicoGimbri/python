def saluta(nome):
    print(f"Ciao, {nome}! Benvenuto in Visual Studio con Python.")


def calcolo_fattoriale(valore):
    output = 1  # Deve iniziare da 1, non da 0
    for i in range(1, valore + 1):
        output *= i  # Equivale a output = output * i

    print(f"Il fattoriale di {valore} è {output}")


def funzione_ricorsiva(valore):
    if valore==1 or valore ==0:
        return valore
    else:
        return valore*funzione_ricorsiva(valore-1)
    
def calcolatrice (opd1,opd2,operatore): 
    if (opd2==0 and operatore == '/'):
        print("non puo essere diviso un valore per zero valore non definibile")
        raise ValueError
    
    
    if(operatore == '+'):
        return opd1+opd2
    elif(operatore == '-'):
        return opd1-opd2
    elif (operatore == '*'):
        return opd1*opd2
    elif (operatore =='/'):
        return opd1/opd2
    else:
        raise ValueError("operatore non conosciuto")
    
def palindroma (stringa):
    for i in range (int(len(stringa)/2)+1):
        if stringa[i]!=stringa[len(stringa)-i-1]:
            return ("stringa non palindroma")
    return ("palindricità verificata")


def unione_dizionari(diz1,diz2):
    output={}
    
    for key in diz1:
        if key in diz2:
            output[key]=diz1[key]+diz2[key]
        else:
            output[key]=diz1[key]
    for key2 in diz2:
        if not key2 in output:
            output[key2]=diz2[key2]
    return output


def contacaratteri (stringa):
    output={}
    for lettera in stringa :
        if(lettera in output):
            output[lettera]+=1
        else:
            output[lettera]=1
    return output


def tutto_maiuscolo(lista):
    if not lista:
        raise ValueError("lista vuota")
    lista_maiuscola=[]
    for parola in lista:
        nuova_maiuscola=""
        for lettera in parola:
            l1=lettera.upper()
            nuova_maiuscola+=l1
        lista_maiuscola.append(nuova_maiuscola)
    return lista_maiuscola
 
 
 
numeri="1234567890" 
def isanumber (x):
    
    if x  in numeri:
        return True
    return False

#è possibile usare is digit
def estrai_numeri(stringa_alphanumerica):
    output=""
    for x in stringa_alphanumerica:
        if isanumber(x):
            output+=x
    return output


def conta_parole(frase):
    count=0
    lista_parole=frase.split()
    for p in lista_parole:
        count+=1
    return count

def contaparolex(frase):
    lista_parole=frase.split
    return contaparoleric(lista_parole)

#slicing (frase[1:]) restituisce la lista frase che pero parte dal secondo elemento richiamando dunque ricorsivamente diminuisce di volta in 
#volta senza modificare la lista di partenza la lista di elementi da considerare
def contaparoleric(frase):
    if(not frase):
        return 0
    return 1+contaparolex(frase[1:])


def valore_unico(lista1,lista2):
    output=[]
    for elemento in lista1:
        if not elemento in lista2:
            output.append(elemento)
    for elemento1 in lista2:
        if not elemento1 in lista1:
            output.append(elemento1)
    return output

def conta_parole_che_iniziano_con_la_lettera_data(frase,lettera):
    output=0
    lista_parole_frase=frase.split()
    for parola in lista_parole_frase:
        if parola[0]==lettera:
            output+=1
    return output

def rimuovi_ripetute(parola):
    output=""
    for lettera in parola:
        if not lettera in output:
            output+=lettera
    return output


def rimuovi_ricorsivo(parola):
    output=""
    return rimuovi_ricorsivo_x(parola,output)

def rimuovi_ricorsivo_x(parola,output):
    if not parola:
        return output
    if not parola[0] in output:
        output+=parola[0]
        return rimuovi_ricorsivo_x(parola[1:],output)
    

    
     

    

       
            


        





    

if __name__=="__main__":
    print(palindroma("rutto"))
    print(contacaratteri("rutto"))


    



