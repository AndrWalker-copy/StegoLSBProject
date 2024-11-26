from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import Stego_Project
def click_button():
    # изменяем текст на кнопке
    labelLog["text"] = f"Mode: {mode.get()} Component: {components_var.get()} Bit: {bit_layer_var.get()} Step:{step_var.get()}"
    if "encrypt" == mode.get():
        try:
            labelLog["text"] = "Обработка..."
            Stego_Project.encrypt_LSB_file(input_path.get(),output_path.get(),file_path.get(),dict_companent[components_var.get()],int(bit_layer_var.get()),int(step_var.get()))
        except Exception as e:
            showerror(title="Ошибка", message=f"Ошибка: {e}")
    if "decrypt" == mode.get():
        try:
            labelLog["text"] = "Обработка..."
            Stego_Project.decrypt_LSB_file(input_path.get(),output_path.get(),dict_companent[components_var.get()],int(bit_layer_var.get()),int(step_var.get()))
        except Exception as e:
            showerror(title="Ошибка", message=f"Ошибка: {e}")
    labelLog["text"] = "Готово"

root = Tk()
root.title("StegoProject")
root.geometry("500x300")
dict_companent = {'Red': 0, 'Green': 1, 'Blue':2}
components = ["Red", "Green", "Blue"]
components_var = StringVar(value=components[0]) 
combobox_components = ttk.Combobox(state="readonly",textvariable=components_var,values=components)
combobox_components.pack(padx=6, pady=6)

bit_layer = ["1", "2", "3", "4"]
bit_layer_var = StringVar(value=bit_layer[0]) 
combobox_bit_layer = ttk.Combobox(state="readonly",textvariable=bit_layer_var,values=bit_layer)
combobox_bit_layer.pack(padx=6, pady=6)

step = ["1", "2", "3", "4"]
step_var = StringVar(value=step[0]) 
combobox_step = ttk.Combobox(state="readonly",textvariable=step_var,values=step)
combobox_step.pack(padx=6, pady=6)

combobox_components.place(x=20,y=30)
combobox_bit_layer.place(x=180,y=30)
combobox_step.place(x=340,y=30)

btn = ttk.Button(text="Button", command=click_button)
btn.pack()
btn.place(x=30,y=240, width=440, height=30)

input_path = ttk.Entry()
output_path = ttk.Entry()
file_path = ttk.Entry()

input_path.pack(padx=8, pady= 8)
output_path.pack(padx=8, pady=8)
file_path.pack(padx=8, pady= 8)

input_path.place(x=30,y=120, width=440, height=20)
output_path.place(x=30,y=160, width=440, height=20)
file_path.place(x=30,y=200, width=440, height=20)

mode = StringVar(value="encrypt")
python_btn_encrypt = ttk.Radiobutton(text="Встроить", value="encrypt", variable = mode)
python_btn_encrypt.pack()
python_btn_encrypt.place(x=30,y=55)

python_btn_decrypt = ttk.Radiobutton(text="Считать", value="decrypt", variable = mode)
python_btn_decrypt.pack()
python_btn_decrypt.place(x=30,y=75)

label1 = ttk.Label(text="Компонента")
label1.pack()
label1.place(x=30,y=10)

label2 = ttk.Label(text="Битовая плосоксть")
label2.pack()
label2.place(x=180,y=10)

label4 = ttk.Label(text="Интервал встраивания")
label4.pack()
label4.place(x=340,y=10)

label5 = ttk.Label(text="Путь изначального файла")
label5.pack()
label5.place(x=30,y=100)

label6 = ttk.Label(text="Путь встраимого файла")
label6.pack()
label6.place(x=30,y=180)

label7 = ttk.Label(text="Путь готового/считанного файла")
label7.pack()
label7.place(x=30,y=140)

labelLog = ttk.Label(text="Введите данные")
labelLog.pack()
labelLog.place(x=0,y=280)
root.mainloop()