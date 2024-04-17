from users import actions

print("""
    Acciones disponibles :
     -Login
     -Registro
""")

make = actions.Actions()
action = input("¿Que accion desea realizar? ")

if action == "login":
    make.login()    
elif action == "registro":
    make.register()
else:
    print ("Accion no disponible")