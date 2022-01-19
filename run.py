"""check if library exists if not install them """


try:
    import tkcalendar
    import matplotlib.pyplot as plt
    import database_maker
    import run_main_menu
    import os
except:
    os.system("pip install tkcalendar")
    os.system("pip install matplotlib")

import database_maker
import run_main_menu
import os
database_maker.run()
run_main_menu.Menu().run()
