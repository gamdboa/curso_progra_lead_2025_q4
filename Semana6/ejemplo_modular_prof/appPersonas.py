import menu_manager
import io_utils
import controller

def ejecutar():
    opcion = 0
    while opcion != 3:
        menu_manager.display_menu()
        opcion = io_utils.read_int("Seleccione su opcion: ")
        controller.process(opcion)