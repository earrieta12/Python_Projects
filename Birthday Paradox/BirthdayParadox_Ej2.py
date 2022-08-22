





import datetime, random
from inspect import isdatadescriptor
from urllib import response


def getBirthdays(numberOfBirthdays):
    "Return a list of number random date objects for birthdays"
    birthdays=[]
    for i in range(numberOfBirthdays):
        #The year is not important in this simulation"
        
        startOfYear = datetime.date(2001,1,1)
        
        #Obtenemos un dia Random de el año
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Aqui se retorna el objeto fecha que ocurre mas de una sola vez en la lista."""
    if len(birthdays) == len(set(birthdays)):
        return None #todos los cumpleaños ocurren solo una vez, so retorna None

    
    ##Comparar cada cumpleaños cada otro.
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA==birthdayB:
                return birthdayA #Retorna el cumpleaños repetido


###Mostrar la intro del programa
print('''Birthday Paradox(Paradoja del cumpleaños), del libro Python Projects by Al Sweigart
La paradoja del cumpleaños muestra que en un grupo de N personas las probabilidades de que 
2 personas tengan el mismo cumpleaños es sorprendentemente alta.
Este programa hace una simulacion Monte Carlo(repetir simulaciones aleatorias) para explorar 
este concepto.''')




#Creamos una lista de los meses en orden
MONTHS=('ENE', 'FEB','MAR','ABR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DIC')

while True:
    print('Cuantos cumpleaños debería generar? (Máximo 100)')
    response=input('> ')
    if response.isdecimal() and (0 < int(response)<=100):
        numBdays = int(response)
        break #el usuario ingreso un valor incorrecto
print()

#Generar y mostrar los cumpleaños
print('Aquí hay', numBdays, 'cumpleaños:')
birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #Muestra una coma después de cada cumpleaños.
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print (dateText, end='')
print()
print()

#Determinar si dos cumpleaños se repiten
match = getMatch(birthdays)

#Muestra los resultados
print('En esta simulación, ', end='')
if match != None:
    monthName = MONTHS[match.month -1]
    dateText = '{} {}'.format(monthName, match.day)
    print('Varias personas cumpleaños en:', dateText)
else:
    print('No hay cumpleaños que coincidan')
print()

#Correr 100.000 simulaciones
print('Generando ', numBdays, 'cumpleaños aleatorios 100.000 veces')
input('Presione enter para iniciar')

print('Corramos 100.000 simulaciones')
simMatch = 0 #Contador de simulaciones que tienen cumpleaños que han coincidido.
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simuaciones realizadas')
    birthdays = getBirthdays(numBdays)
    if getMatch(birthdays)!= None:
        simMatch=simMatch+1
print('100.000 simulaciones corriendo')


#Mostrar resultados de la simulacion
probability = round(simMatch / 100_000 * 100, 2)
print('De 100.000 simulaciones de', numBdays, 'personas, hay una probabilidad de')
print('coincidir in ese grupo', simMatch, 'veces. Esto significa')
print('que ', numBdays, 'personas tienen un', probability, '% de probabilidad de ')
print('tener una coincidencia en su cumpleaños en este grupo.')
print('Que es probablemente mucha mas alta de lo que tu pensabas')





