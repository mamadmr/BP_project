import database_maker
import run_main_menu
import os

try:
    import tkcalendar
except:
    os.system("pip install tkcalendar")

database_maker.run()
run_main_menu.Menu().run()
