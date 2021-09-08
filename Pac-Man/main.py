from app_class import *

# when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
# But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name
if __name__ == '__main__':
    app = App()
    app.run()