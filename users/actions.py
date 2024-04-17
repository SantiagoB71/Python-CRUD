import users.user as model
import notes.actions as note

class Actions:
    def login(self):
        print("Listo vamos a ingresar")
        email = input("Ingresar el correo: ")
        password = input("Ingresar la contraseña: ")

        try: 
            make = model.User(email, password, "", "")
            login = make.identify() 

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado el {login[5]}")
                self.nextStep(login)         
        except Exception as e: 
            print(e)
            print("login incorrecto, intentelo nuevamente")

    def nextStep(self, user):
        print("""
            Acciones disponibles:

            -Crear nota (crear)
            -Listar notas (listar)
            -Eliminar nota (eliminar)
            -Salir (salir)
          
        """)
        
        make = note.Actions()
        action = input("\n ¿Que quieres hacer?: ")

        if action == "crear":
            make.create(user)
            self.nextStep(user)
        elif action == "listar":
            make.show(user)
            self.nextStep(user)
        elif action == "eliminar":
            make.delete(user)
            self.nextStep(user)
        elif action == "salir":
            print(f"\nMuy bien {user[1]} hasta pronto")
            exit()
        else:
            print("Accion no disponible")

    def register(self):
         print("Este es el registro")

         name = input("Ingresar el nombre: ")
         lastName = input("Ingresar la apellido: ")
         email = input("Ingresar el correo: ")
         password = input("Ingresar la contraseña: ")
    
         make = model.User(email, password, name, lastName)
         register = make.register() 

         if register [0] >=1:
             print(f"\n {register[1].name} se ha registrado con el correo {register[1].email}")
         else:
            print("\nError al registrar el usuario")
    