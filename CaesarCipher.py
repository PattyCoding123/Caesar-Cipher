# The following program will allow us to encrypt and decrypt messages utilizing the Caesar Cipher
import string

alphabet = list(string.ascii_lowercase) #alphabet list

class Solution(object):
    def caesarEncrypt(self, msg):
        msg = msg.lower() #to keep uniformity in string
        encryptedMsg = ""
        for ch in msg: #loop through each character in the string
            if ch not in alphabet:
                encryptedMsg = encryptedMsg + ch
            else:
                i = alphabet.index(ch)
                j = i + 3
                if j > len(alphabet) - 1:
                    j = j - len(alphabet) - 1
                encryptedMsg = encryptedMsg + alphabet[j] #add each character into the new message
        return encryptedMsg


    def caesarDecrypt(self, msg):
        msg = msg.lower()
        decryptedMsg = ""
        for ch in msg:
            if ch not in alphabet:
                decryptedMsg = decryptedMsg + ch
            else:
                i = alphabet.index(ch)
                j = i - 3
                if j < 0:
                    j = j + (len(alphabet) - 1)
                decryptedMsg = decryptedMsg + alphabet[j]
        return decryptedMsg

x = Solution()
test = x.caesarEncrypt("The mitochondria is the powerhouse of the cell.")
print(test)

decryptTest = x.caesarDecrypt(test)
print(decryptTest)