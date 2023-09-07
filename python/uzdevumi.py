from ipaddress import summarize_address_range


def tests(parametrs):
    a = parametrs
    return a 


#print(tests("kaķis"))

def pirmais(par1, par2):
    reizinajums = par1*par2
    summa = par1+par2
    if reizinajums<1000 :
        return reizinajums
    else:
        return summa

#print("The result is ", pirmais(40,30))

def otrais():
    esosais = 0
    ieprieksejais = 0
    for i in range(10):
        ieprieksejais = esosais
        esosais = i
        summa = ieprieksejais+esosais
        #print("current number", esosais, "previous number", ieprieksejais, "sum", summa)
    return
otrais() 

def tresais(teksts):
    print("sākotnējais teksts ir ", teksts)
    print("tikai para indeksa burti:")
    for i in range(0, len(teksts), 2):
        print(teksts [i]) 
        return

tresais("pynative")

def ceturtais(teksts, n):
    print("Teksts:", teksts)
    print("Noņemot pirmos", n, "burtus sanāk:", teksts[n:])
    return
ceturtais("pynative", 4)

