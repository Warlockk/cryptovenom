from main import *
from bruteforce import *

print '''

-=[OPTIONS]=-

   1) Hash Encrypt
   
   2) Hash Brute Force
   
   '''
   
opt = raw_input('\033[1;34m[=]\033[0m Option: ')


hash1 = raw_input('\033[1;34m[=]\033[0m Hash/Text: ')
user1 = raw_input('\033[1;34m[=]\033[0m Username: ')

if opt == '1':

    h = hash(hash1, user1)
    print('\033[1;32m[+]\033[0m h(x) = ' + h)

elif opt == '2':

    dic = raw_input('\033[1;34m[=]\033[0m Dictionary path: ')

    bf(hash1, dic)

else:

    print('\033[1;31m[-]\033[0m Unknown option')
