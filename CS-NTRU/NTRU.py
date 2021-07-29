#Declared parameters
#Note that h is obtained using Maple. We don't have to find it each 
# time we run the program, since the declared parameters 
# aren't going to change.

#igcdexOfFG is also obtained using maple. It doesn't have to do
# anything with any changes to ASCII Values
q = 232092
f = 23
g = 241
h = 111011
r = 140
igcdexOfFG= 21


#Splits the whole string to individual characters and return them 
#into an array
def msg2Split(Message):
    msg = []
    msg.append(Message[:1])
    Message = Message.replace(Message[:1], '', 1)
    while len(Message) > 0:
        msg.append(Message[:1])
        Message = Message.replace(Message[:1], '', 1)

    return msg

#Takes the elements of passed array, converts them to ASCII Values, and 
#return an array of ASCII elements 
def char2Ascii( str ): 
    asciiArr =[]
    for i in str:
        asciiArr.append(ord(i))
    return asciiArr 

#Encrypts any passed ASCII array and return encrypted array
def encryption(asciiArr):
    E = []
    for i in asciiArr:
        e = (r * h + i) % q
        E.append(e)
    return E

#Decrypts any passed encrypted array and return decrypted array + 
#It calls method cipherSplitter
def decryption(encArr):
    encArr = cipherSplitter(encArr)
    D = []
    for i in encArr:
        a = (f * int(i)) % q
        b = (igcdexOfFG * a) % g
        D.append(b)
    return D

#This method takes input from the user as a cipher text and creates an array
#to put those splitted numbers in, each element is 6 digits.

#It creates an array for the sake of *decryption()* method.
def cipherSplitter(Cipher):
    msg = []
    msg.append(Cipher[:6])
    Cipher = Cipher.replace(Cipher[:6], '', 1)
    while len(Cipher) > 0:
        msg.append(Cipher[:6])
        Cipher = Cipher.replace(Cipher[:6], '', 1)
        
    return msg
