from tkinter  import *

root = Tk()
root.title("Tkinter Calculator")

entry_box = Entry(root, width=35, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=5, padx=2, pady=8)


def button_click(number):
  current = entry_box.get()
  entry_box.delete(0, END)
  entry_box.insert(0, str(current) + str(number))

def button_add():
  f_num = int(entry_box.get())
  global f_num_gl
  global math_type
  math_type = "add"
  f_num_gl = int(f_num)
  entry_box.delete(0, END)
  return

def button_sub():
  f_num = int(entry_box.get())
  global f_num_gl
  global math_type
  math_type = "sub"
  f_num_gl = int(f_num)
  entry_box.delete(0, END)
  return

def button_mult():
  f_num = int(entry_box.get())
  global f_num_gl
  global math_type
  math_type = "mult"
  f_num_gl = int(f_num)
  entry_box.delete(0, END)
  return

def button_div():
  f_num = int(entry_box.get())
  global f_num_gl
  global math_type
  math_type = "div"
  f_num_gl = int(f_num)
  entry_box.delete(0, END)
  return

def button_clear():
  entry_box.delete(0, END)
  return

def button_equals():
  s_num = entry_box.get()
  entry_box.delete(0, END)
  if math_type == "add":
    entry_box.insert(0, f_num_gl + int(s_num))
  elif math_type =="sub":
    entry_box.insert(0, f_num_gl - int(s_num))
  elif math_type == "mult":
    entry_box.insert(0, f_num_gl * int(s_num))
  elif math_type == "div":
    entry_box.insert(0, f_num_gl / int(s_num))


button_1 = Button(root, text="1", padx=40, pady=20,command=lambda: button_click(1))
button_1.grid(row=3, column=0)
button_2 = Button(root, text="2", padx=40, pady=20,command=lambda: button_click(2))
button_2.grid(row=3, column=1)
button_3 = Button(root, text="3", padx=40, pady=20,command=lambda: button_click(3))
button_3.grid(row=3, column=2)
button_4 = Button(root, text="4", padx=40, pady=20,command=lambda: button_click(4))
button_4.grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=20,command=lambda: button_click(5))
button_5.grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=20,command=lambda: button_click(6))
button_6.grid(row=2, column=2)
button_7 = Button(root, text="7", padx=40, pady=20,command=lambda: button_click(7))
button_7.grid(row=1, column=0)
button_8 = Button(root, text="8", padx=40, pady=20,command=lambda: button_click(8))
button_8.grid(row=1, column=1)
button_9 = Button(root, text="9", padx=40, pady=20,command=lambda: button_click(9))
button_9.grid(row=1, column=2)
button_0 = Button(root, text="0", padx=40, pady=20,command=lambda: button_click(0))
button_0.grid(row=4, column=0)
button_clear = Button(root, text="clear", padx=27, pady=20,command=button_clear)
button_clear.grid(row=4, column=2)
button_equals = Button(root, text="=", padx=38, pady=20,command=button_equals)
button_equals.grid(row=4, column=1)
button_add = Button(root, text="+", padx=27, pady=20,command=button_add)
button_add.grid(row=1, column=4)
button_sub = Button(root, text="-", padx=30, pady=20,command=button_sub)
button_sub.grid(row=2, column=4)
button_mult = Button(root, text="X", padx=28, pady=20,command=button_mult)
button_mult.grid(row=3, column=4)
button_div = Button(root, text="/", padx=30, pady=20,command=button_div)
button_div.grid(row=4, column=4)