##from tkinter import messagebox
##from tkinter import ttk
##import tkinter as tk

import game_manager

manager = game_manager.Manager()
manager.start()
for i in range(2):
    manager.draw_one_player()
print(manager.player_totals(), manager.player)
print('Working')
