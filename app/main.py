
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
    
  
        """
        -ADD AT THE V1.1
        remote a task method
        """
        #time.sleep(5)
        """
        funciona, prodria agregar un inp
        -para eliminar un index en especifico
        """
        if not self.todos: # comprueba si no hay task antes de borrar
            print('no hay por borrar')
            return self.todos
        
        #print('Removing a task....')
        #time.sleep(1)
        removed_task= self.todos.pop()
        #print(t.clear_eol, end=" ")
        #print(f'item removed {removed_task}')
        #return self.todos
        #return removed_task
    
    def view(self):
        """
        add view
        """
        bg= f'{t.home}{t.on_maroon2}{t.clear}' # you can change the theme in this line
        bn= t.black_on_orchid1(t.center(t.bold("Add a taks or write ':q' to exit "))) 
        return bg + bn
    
    def corrector_bg(self):
        """
        -Corrige el error del input y rellena el background
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


    """
    -v1.0 IS WORKING (CREATE TASK AND BREAK THE LOOP)
    -V1.1 UNDEFINED (ADD RM METHOD, ADD INSERT METHOD, ?)
    -V1.2 IS WORKING (FASTAPI, SQLITE, STREAMLIT)
    """