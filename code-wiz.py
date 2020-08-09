import random
def encode(word):
 encoded_word=""
 leng=0
 for c in word:
  leng=leng+1
  if c=="A":
   encoded_word=encoded_word+"Z"
  elif ord(c)==32:
   encoded_word=encoded_word+"$"
  else:
   prev=chr(ord(c)-1)
   encoded_word=encoded_word+prev
 #encoding stage 1 complete
 encoded_word=encoded_word+" "
 leng=leng+1
 p1=random.randint(0,leng)
 p2=random.randint(0,leng)
 w1=encoded_word[0:p1]
 w2=encoded_word[p1:leng]
 num1=random.randint(0,9)
 encoded_word=w1+str(num1)+w2+" "
 leng=leng+1
 w1=encoded_word[0:p2]
 w2=encoded_word[p2:leng]
 num2=random.randint(0,9)
 encoded_word=w1+str(num2)+w2
 print("After Encryption :")
 print(encoded_word)
def decode(word2):
 decoded_word=""
 for ch in word2:
  if ch=="$":
   decoded_word=decoded_word+" "
  elif ch=="Z":
   decoded_word=decoded_word+"A"
  elif ch=="0" or ch=="1" or ch=="2" or ch=="3" or ch=="4" or ch=="5" or ch=="6" or ch=="7" or ch=="8" or ch=="9":
   continue
  else:
   decoded_word=decoded_word+chr(ord(ch)+1)
 print("After Decrypting:")
 print(decoded_word)
print('Enter 1 to encode and 2 to decode')
choi=int(input())
if choi== 1:
 print("Enter String to be encrypted")
 st=input()
 encode(st)
elif choi== 2:
 print("Enter String to be decrypted")
 str=input()
 decode(str)
else:
 print('Please choose either 1 or 2')
