from Persona import Persona

unaPersona = Persona("mario","aguero", "obando", "Puris", "1974-01-31")
otraPersona = Persona("arelys", "mena", "esquivel", "Guapiles", "1981-03-18")
elClon = Persona("mario","aguero", "obando", "Puris", "1974-01-31")
print(unaPersona)
print(otraPersona)
print(elClon)
otroClon = unaPersona
print(otroClon)

if unaPersona == elClon:
    print("Son la misma vara")
else:
    print("No son la misma vara")

if unaPersona == otroClon:     
    print("Son la misma vara")
else:
    print("No son la misma vara")
