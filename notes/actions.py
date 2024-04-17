import notes.note as model 


class Actions: 
    def create(self, user):
        print(f"\nListo! {user[1]} vamos a crear una nota")
        title = input("\nIngresa el titulo de la nota: ")
        description = input("Ingresa la descripcion de la nota: ") 


        make = model.note(user[0],title,description)
        response = make.store()


        if response[0] >= 1:
            print(f"\n Perfecto! Se a creado la nota con titulo {make.title} de forma correcta.")
        else: 
            print("\n Hubo un error al crear la nota")

    def show(self, user):
        print(f"\n Muy bien {user[1]} estas son tus notas creadas")
        make = model.note(user[0])
        make.show() 

    
    def delete(self, user): 
        print(f"\nMuy bien {user[1]} vamos a eliminar una nota")
        title = input("\n ¿Cual es el titulo ?")
        
        make = model.note(user[0], title)
        response = make.delete() 
        
        if response[0] >= 1:
            print(f"\n La nota con titulo {make.title} se ha borrado la nota")
        else:
            print("\n Hubo un problema al eliminar la nota")
        
        
        