#---Schonhage-Strassen Algorithm---

from scipy.fftpack import ifft, fft
linearConvolution = 0
length=0
def countDigits(num):
    count = 0
    while num > 1:
        num /= 10
        count+=1
    return count



def findLinearConvolution(a,b):
    global linearConvolution
    aDigitCount = countDigits(a)
    bDigitCount = countDigits(b)
    aDigits = [int(i) for i in str(a)]
    bDigits = [int(i) for i in str(b)]  
    temp = a
    global length
    length = int(aDigitCount + bDigitCount - 1)
    linearConvolution = [0]*length
    linearConvolution=ifft(fft(aDigits,length)*fft(bDigits,length))
    linearConvolution=linearConvolution.real
    # a different wat to get linear convolution
    # for i in range (0,aDigits,1) :    
    #     a = temp
    #     for j in range(bDigits):
            
    #         linearConvolution[i + j]+= int ((b % 10) * (a % 10))
    #         # print(linearConvolution[i + j], end=" ")
    #         a = int(a/10) 
    #     b = int(b/10)
    
    print("The Linear Convolution is: [ ", end=" ")
    for i in range(length-1):
        linearConvolution[i]=round(linearConvolution[i])
        print(round(linearConvolution[i]), end="  ")
    
    print("]")
      
    
def performCarry():
    
    
    product = 0
    carry = 0
    base = 1
    for i in range(length - 1, -1, -1):
      
        linearConvolution[i] += carry
        product = int(product + (base * (linearConvolution[i] % 10)))
        carry = int(linearConvolution[i] / 10)
        base *= 10
        
    print(f"\nThe Product is : {product}")
    
def schonhageStrassenMultiplication(a,b):
    
    findLinearConvolution(a,b)
    
    performCarry()

a = 2604
b = 1812
schonhageStrassenMultiplication(a,b)

#----------------------------------------------------------------

#---Karatsuba's Algorithm--


def karatsuba(m,n):    #Karatsuba's for Base 10 Representation
    if(m<10 or n<10):
        return m*n
    else:
        mstring = str(m)
        nstring = str(n)

        k = max(len(mstring), len(nstring))
        mid=int(k/2)

        a = int(mstring[:-mid])
        c = int(nstring[:-mid])
           
        b = int(mstring[-mid:])
        d = int(nstring[-mid:])
            
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd 

        return ac*10**(2 * mid) + ad_plus_bc*10**(mid) + bd

def multiply(X, Y):
  
    n = max(len(X), len(Y))
    X = X.zfill(n)
    Y = Y.zfill(n)
 
 
    if n == 0: return 0
    if n == 1: return int(X[0])*int(Y[0])
 
    fh = n//2  
    sh = n - fh  
 
   
    Xl = X[:fh]
    Xr = X[fh:]
 

    Yl = Y[:fh]
    Yr = Y[fh:]
 

    P1 = multiply(Xl, Yl)
    P2 = multiply(Xr, Yr)
    P3 = multiply(str(int(Xl, 2) + int(Xr, 2)), str(int(Yl, 2) + int(Yr, 2)))
 
    return P1*(1<<(2*sh)) + (P3 - P1 - P2)*(1<<sh) + P2

# ----------------------------------------------------------------

#Karatsuba's Algorithm for Base 2 Representation

def karatsubaBase2(m, n):    
    def multiply(X, Y):
  
        n = max(len(X), len(Y))
        X = X.zfill(n)
        Y = Y.zfill(n)
 
 
        if n == 0: return 0
        if n == 1: return int(X[0])*int(Y[0])
 
        fh = n//2  
        sh = n - fh  
 
   
        Xl = X[:fh]
        Xr = X[fh:]
 

        Yl = Y[:fh]
        Yr = Y[fh:]
 

        P1 = multiply(Xl, Yl)
        P2 = multiply(Xr, Yr)
        P3 = multiply(str(int(Xl, 2) + int(Xr, 2)), str(int(Yl, 2) + int(Yr, 2)))
 
        return P1*(1<<(2*sh)) + (P3 - P1 - P2)*(1<<sh) + P2
    mstr=str(m)
    nstr=str(n)
    return multiply(mstr, nstr)