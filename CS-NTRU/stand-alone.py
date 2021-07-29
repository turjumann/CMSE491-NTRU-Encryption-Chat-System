import NTRU
if __name__ == "__main__":

    print('NTRU for Integers stand-alone simple application')
    menu = '\n1.To Encrypt a plain-text'
    menu += '\n' + '2.To Decrypt a cipher text'
    menu += '\n' + '0.Exit'
    menu += '\n' + '> '

    ch = -1
    while(ch != 0):
        print(menu, end='')
        ch = int(input())

        if ch == 1:
            Message = input('Enter your plain-text to be encrypted: ')
            msg = NTRU.msg2Split(Message)
            m2Ascii = NTRU.char2Ascii(msg)
            encryptedArr = NTRU.encryption(m2Ascii)
            print('Cipher: ', end='')
            #print('Encrypted Array: ', encryptedArr) #Prints the encrypted elements of the array returned
            print(''.join([str(n) for n in encryptedArr]))
        
        elif ch == 2:
            Cipher = input('Enter your cipher text to be decrypted: ')
            decryptedArr = NTRU.decryption(Cipher)
            #print('Decrypted Array: ',decryptedArr) #Prints the decrypted elements of the array returned
            print('Decrypted Cipher text: ', end='')
            print(''.join(chr(i) for i in decryptedArr))
        elif ch == 0:
            print('Exit....')
            break

        else:
            print('Wrong input!')
   

