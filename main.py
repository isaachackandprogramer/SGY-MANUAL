import os

print('''\033[1;34;40m  #####     ####   ##  ##            ##   ##    ##     ##   ##  ##   ##    ##     ####
 ##   ##   ##  ##  ##  ##            ### ###   ####    ###  ##  ##   ##   ####     ##
 #        ##       ##  ##            #######  ##  ##   #### ##  ##   ##  ##  ##    ##
  #####   ##        ####             #######  ##  ##   ## ####  ##   ##  ##  ##    ##
      ##  ##  ###    ##              ## # ##  ######   ##  ###  ##   ##  ######    ##   #
 ##   ##   ##  ##    ##              ##   ##  ##  ##   ##   ##  ##   ##  ##  ##    ##  ##
  #####     #####   ####             ##   ##  ##  ##   ##   ##   #####   ##  ##   #######

''')
print('')
print('''\033[1;36;40m1-hacker
2-programer
-h | help (não funcionando)''')
print('\033[1;37;40m')

var1 = input(">")

if var1 == '1':    
    print('')
    print('''\033[1;35;40m1-essencial
2-full''')
    print('\033[1;37;40m')
    var2 = input('>')


    if var2 == '1':
        print('')
        print('baixando nivel 1')
        print('')

    if var2 == '2':
        print('')
        print('baixando nivel 2')
        print('')

if var1 == "2":
    print('')
    print('''\033[1;32;40m1-python
2-Javascript
3-C
4-Java''')
print('')
var4 = input('>')

if var4 == "1":
    os.system('apt install python3')

if var4 == "2":
    os.system('apt install nodejs')

if var4 == "3":
    os.system('apt install gcc')

if var4 == "4":
    os.system('sudo apt install openjdk-11-jdk')



     

        
