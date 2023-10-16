from tkinter import *

ventana = Tk()
#1
Widget_uno=Frame()
Widget_uno.grid(row='0',column='1',rowspan=2)
Widget_uno.config(width='50',height='100')
Widget_uno.config(bg='red')
#2
Widget_uno=Frame()
Widget_uno.grid(row='0',column='2')
Widget_uno.config(width='50',height='50')
Widget_uno.config(bg='green')

#3
# Widget_uno=Frame()
# Widget_uno.grid(row='1',column='1')
# Widget_uno.config(width='50',height='50')
# Widget_uno.config(bg='orange')

#4
Widget_uno=Frame()
Widget_uno.grid(row='1',column='2')
Widget_uno.config(width='50',height='50')
Widget_uno.config(bg='purple')

#5
Widget_uno=Frame()
Widget_uno.grid(row='2',column='1',columnspan=3)
Widget_uno.config(width='100',height='50')
Widget_uno.config(bg='yellow')

#6
# Widget_uno=Frame()
# Widget_uno.grid(row='2',column='2')
# Widget_uno.config(width='50',height='50')
# Widget_uno.config(bg='red')




ventana.mainloop()