"""check if library exists if not install them """

import os

try:
    import tkcalendar
    import matplotlib.pyplot as plt
    import database_maker
    import run_main_menu
except:
    os.system("pip install tkcalendar")
    os.system("pip install matplotlib")

import database_maker
import run_main_menu

database_maker.run()
run_main_menu.Menu().run()
