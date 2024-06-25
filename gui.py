import tkinter as tk 
from tkinter import * 
import ttkbootstrap as ttk 
from main import *














#intializing window
window = ttk.Window(themename='superhero')
window.title('Cryptography')
window.geometry('600x400')

#declaring variables
sentence = ttk.StringVar()
encrypted_numbers = ttk.StringVar()
encrypted_text = ttk.StringVar()

#widgets
input_frame = ttk.Frame(master=window,padding=50)
# button_frame = ttk.Frame(master=window)
label = ttk.Label(master=input_frame,text='Enter your message')
sentence_entry = ttk.Entry(master=input_frame,justify='center',textvariable=sentence)
Encrypt_button = ttk.Button(master=window,text="Encrypt",command=Encryption,padding=10)
Decrypt_button = ttk.Button(master=window,text="Encrypt",command=Encryption,padding=10)
output_label = ttk.Label(master=window,text='Your Message',padding=10)
number_label = ttk.Label(master=window,textvariable=encrypted_numbers,padding=10)
message_label = ttk.Label(master=window,textvariable=encrypted_text,padding=10)

#packing widgets
input_frame.pack()
label.pack()
sentence_entry.pack(side='left')
sentence_entry.focus()
# button_frame.pack()
Encrypt_button.pack(pady=10)
Decrypt_button.pack(pady=10)
output_label.pack()
number_label.pack()
message_label.pack()

window.mainloop()