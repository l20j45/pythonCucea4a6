nombre = "rafa"
print(nombre.upper().center(100,"x"))
nombre = "RAFA"
print(nombre.lower())
print(len(nombre))
print(reversed(nombre))
for letter in nombre : 
    print(letter)
    
if 'a' in nombre:
    print("si esta la letra a")
    
print(nombre[0])
print(nombre[::-1])