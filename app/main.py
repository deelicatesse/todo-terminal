from blessed import Terminal

""" 
- INSTANCIA PARA PODER TRABAJAR CON BLESSED

"""
t= Terminal() 

class Task:
    def __init__(self, todos):
        self.todos= todos
        
    def input_todo(self):
        """
        METHOD:
            PASA LA ENTRADA DEL INPUT AL ARRAY
        """
        create_task= input('Add a task to do: ')
        return create_task
    
    
    def view(self):
        """
        Creadmos el background y el banner 
        """
        bg= f'{t.home}{t.on_maroon2}{t.clear}' # you can change the theme in this line
        bn= t.black_on_orchid1(t.center(t.bold("Add a taks or write ':q' to exit "))) 
        return bg + bn
    
    def corrector_bg(self):
        """
        -Rellena el background tras agregar una task
        """
        func_c= f'{t.on_maroon2}'
        return func_c



def todo_terminal():
    todos= []
    version_v1= Task(todos)
    banner= version_v1.view()
    """
    -INIT BANNER
    """
    print(banner)
      
    """
    -INIT CONDITIONAL
    """
    while True:
        fill_bg= version_v1.corrector_bg()
        print(fill_bg)
        ip= version_v1.input_todo()
        # ADD CONDITIONAL TO BREAK THE LOOP
        if ip.lower() == ':q':
            break
    
        else:
            todos.append(f'{t.on_maroon2}{t.underline(ip.capitalize())}{t.on_maroon2}')
            
            print(banner)
            print(fill_bg)
            for i, todo in enumerate(todos, start=1):
                print(f'{i}. {todo}')
    print("  ")
    print('Session ended...')
    print("  ")

    """
    Puedes agregar este fragmente si quieres limpiar la terminal al finalizar
    """
    #print(f'{t.normal} + {t.clear}')

    
if __name__=='__main__':
    todo_terminal()


