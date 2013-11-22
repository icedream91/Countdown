import tkinter as tk
import datetime


deadline=datetime.date(2013,7,14) # fill deadline here
event='school' # fill event here


class Countdown(tk.Frame):

    def __init__(self):
        self.master=tk.Tk()
        tk.Frame.__init__(self,self.master)

        self.pack()
        self.master.title('Countdown')

        self.createWidgets()
        self.master.update_idletasks()

        screen_width=self.master.winfo_screenwidth()
        screen_height=self.master.winfo_screenheight()
        
        win_width,win_height=[int(n) for n in self.master.geometry().split('+')[0].split('x')]
        if win_width<200:
            win_width=200
        self.master.geometry('{}x{}+{}+{}'.format(win_width,win_height,\
                (screen_width-win_width)//2,(screen_height-win_height)//2))
        self.mainloop()


    def createWidgets(self):
        today=datetime.date.today()
        remainder_days=(deadline-today).days

        mesg=[]
        if remainder_days<0:
            mesg.append('Has exceeded the deadline of {}.'.format(event))
        else:
            mesg.append('There')
            if remainder_days<=1:
                mesg.append('is {} day'.format(remainder_days))
            elif 1<remainder_days:
                mesg.append('are {} days'.format(remainder_days))
            mesg.append('from {}.'.format(event))

        mesg=' '.join(mesg)
        self.info=tk.Label(self,text=mesg,height=4,padx=15)
        self.info.pack()

        self.ok=tk.Button(self,text='OK',command=self.master.destroy)
        self.ok.pack()
        self.ok.focus_force()


countdown=Countdown()
