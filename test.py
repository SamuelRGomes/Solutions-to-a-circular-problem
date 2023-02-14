linearConvolution = 0
length=0
def countDigits(num):
    count = 0
    while num > 1:
        num /= 10
        count+=1
    return count


from scipy.fftpack import fft,ifft
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