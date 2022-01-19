"""check if library exists if not install them """

import database_maker
import run_main_menu
import os

try:
    import tkcalendar
    import matplotlib.pyplot as plt
except:
    os.system("pip install tkcalendar")
    os.system("pip install matplotlib")

database_maker.run()
run_main_menu.Menu().run()
