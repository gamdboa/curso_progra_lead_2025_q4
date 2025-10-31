from Persona import Persona

unaPersona = Persona("mario","aguero", "obando", "Puris", "1974-01-31")
otraPersona = Persona("arelys", "mena", "esquivel", "Guapiles", "1981-03-18")

if otraPersona < unaPersona:
    print("Arelys es menor")
else: 
    print("Mario es menor")

print(unaPersona._nombre)
unaPersona.nombre = "cua cua"
print(unaPersona._nombre) 