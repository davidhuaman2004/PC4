import re

# Ejercicio 1
# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero 
# con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')
if n>=11:
    print("Numero muy grande ingrese un valor entre el rango 1 y 10...")
else:
    for i in range(1, 11):
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
    f.close()

# Ejercicio 2
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
# done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())

# Ejercicio 3
# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
# y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
else:
    lines = f.readlines()
    print(lines[m - 1])




##################  Expresiones regulares  #############





# Escriba una expresión regular que encuentre todas las coincidencias que sigan el siguiente patrón.
# Ej. @robot3!

# Cadena entrada
Coincidencias = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'

print(re.findall(r"@robot\d" , Coincidencias))
print("====================================================================")
#Escriba una expresión regular para cada caso:
#### todos los usuarios que sigan el siguente patron. User_mentions:9

#### encuentre los numero de likes: likes: 5

#### que permita encontrar el numero de retweets. number of retweets: 4

# Cadena entrada
s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"

print(re.findall(r"User\W*\w+\W*\d",s))
print(re.findall(r"likes\W* \d",s))
print(re.findall(r"num\w+ \w+ \w+\D \d",s))
print("====================================================================")


## Escriba una expresión regular que encuente los nombres de archivos txt en la cadena:

##- Nombre de archivo txt siempre inicia al principio de la cadena
##- Siempre comienzan con una secuencia de 2 o 3 vocales mayúsculas o minúsculas (a e i o u).
##- Archivo siempre termina con ".txt" .


n = "AIshadowhunters.txt aaaaand back to my literature review. At least i have a friendly cup of coffee to keep me company ouMYTAXES.txt I am worried that I won't get my $900 even though I paid tax last year"
    
print("LOS NOMBRES DE LOS ARCHIVOS '.txt' son: ", re.findall(r"\w+.txt",n))
print("=====================================================================")


#  Escriba una expresión regular que valide una lista de correos electrónicos

#  Primera parte:
#  Caracteres en mayuscula y minúscula
#  Números
#  Caracteres especiales: !, #, %, &, *, $, .
#  Debe contener @
#  Dominio:
#  Puede ser cualquier conjunto de caracteres
#  Solo puede terminar con .com
#  ENTRADA:
#  ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']

#  SALIDA:
#  The email n.john.smith@gmail.com is a valid email
#  The email 87victory@hotmail.com is a valid email
#  The email !#mary-=@msca.net is invalid

# Escriba una expresión regular para validar un correo
evaluar = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']

correo= r"[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}"

for email in evaluar:
    if re.findall(correo, email):
        print(f"El correo {email} es un correo valido")
        continue
    print(f"El correo {email} es un correo invalido")
   
print("====================================================================")
print()
print()
print()




################################   PROBLEMAS 2   #########################################



###Fredrick y tú son buenos amigos. Ayer, Fredrick recibió N tarjetas de crédito de ABCD Bank. Fredrick requiere verificar si los números de su tarjeta de crédito son válidos o no. Resulta que eres excelente en expresiones regulares, ¡así que él está pidiendo tu ayuda!
###
###Una tarjeta de crédito válida de ABCD Bank tiene las siguientes características:
###
###Los números de tarjetas deben iniciar con 4, 5 o 6
###La cantidad de dígitos deben ser 16
###Deben ser digitos entre [0 - 9]
###Puede tener dígitos en grupos de 4, separados por un guión "-".
###No debe contener ningún otro separador como ' ' , '_', etc.
###No debe tener 4 o más dígitos repetidos consecutivos.


tarjetas = ['4123456789123456','5123-4567-8912-3456','61234-567-8912-3456','4123356789123456','5133-3367-8912-3456','5123 - 3567 - 8912 - 3456']

regex1 = r"[456]{1}\d{3}-\d{4}-\d{4}-\d{4}"
regex2 = r"[456]{1}\d{15}"
regex3 = r"[456]{1}\d+ - \d{4} - \d{4} - \d{4}"
regex4 = r"[456]{1}\d{4}-\d{3}-\d{4}-\d{4}"

for p in tarjetas:
    if re.findall(regex1,p):
        print(f"{p} -> Valid")
    elif re.findall(regex2,p):
        print(f"{p} -> Valid")
    elif re.findall(regex3,p):
        print(f"{p} -> Invalid")
    elif re.findall(regex4,p):
        print(f"{p} -> Invalid")
    continue
print("================================================================")