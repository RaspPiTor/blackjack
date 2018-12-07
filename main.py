from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

import game_manager


class GUI(ttk.Frame):
    def __init__(self):
        ttk.Frame.__init__(self)
        score_frame = ttk.Frame(self)
        score_frame.grid(row=0, column=0, columnspan=10)
        ttk.Label(score_frame, text='Dealer score:').grid(row=0, column=0)
        self.dealer_score = ttk.Label(score_frame, text='0')
        self.dealer_score.grid(row=0, column=1)
        ttk.Label(score_frame, text='Player score:').grid(row=0, column=2)
        self.player_score = ttk.Label(score_frame, text='0')
        self.player_score.grid(row=0, column=3)

        ttk.Label(self, text='Your Hand').grid(row=1, column=0, sticky='w')
        ttk.Label(self, text='Totals:').grid(row=1, column=1)
        self.totals = ttk.Label(self)
        self.totals.grid(row=1, column=2)
        self.cards = ttk.Label(self)
        self.cards.grid(row=2, column=0, columnspan=2, sticky='w')
        ttk.Button(self, text='Stick', command=self.stick).grid(row=3, column=0)
        ttk.Button(self, text='Draw', command=self.draw).grid(row=3, column=1)

        self.manager = game_manager.Manager()
        self.start()

    def render_hand(self):
        self.cards['text'] = '\n'.join(map(lambda x: '%s of %s' % (x[1], x[0]),
                                           self.manager.player))
        self.totals['text'] = ', '.join(map(str, self.manager.totals(True)))

    def start(self):
        self.manager.start()
        self.render_hand()

    def stick(self):
        winner = self.manager.winner()
        if winner == 'PLAYER':
            self.player_score['text'] = str(int(self.player_score['text']) + 1)
            messagebox.Message(self, message='You won').show()
        else:
            self.dealer_score['text'] = str(int(self.dealer_score['text']) + 1)
            messagebox.Message(self, message='Dealer won').show()
        self.start()

    def draw(self):
        if self.manager.totals(True):
            self.manager.draw_one()
            self.render_hand()
            if self.manager.totals(True):
                self.render_hand()
            else:
                self.stick()
        else:
            self.stick()


if __name__ == '__main__':
    gui = GUI()
    gui.grid()
    gui.mainloop()
