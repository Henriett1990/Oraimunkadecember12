import math

def beker(x, y):
    tti = x / ((y/100)**2)
    return(round(tti,1))

def kategoria():
    if beker(suly,magassag) < 18.5:
        print("Alultáplált")
    elif beker(suly,magassag) < 24.9:
        print("Normál testsúly")
    elif beker(suly,magassag) < 29.9:
        print("Túlsúlyos")
    else:
        print("Elhízott")

if __name__ == "__main__":
    suly = float(input("Adja meg a súlyát kg-ban: "))
    magassag = float(input("Adja meg a magasságát cm-ben: "))
    beker(suly,magassag)
    print((beker(suly,magassag)))
    kategoria()
