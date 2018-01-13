from tkinter import * 
import tkinter.filedialog
import os

root = Tk()
logo = tkinter.PhotoImage(file="zms.png")

w1 = tkinter.Label(root, image=logo).pack(side="right")

explanation = """El ejecutable que está utilizando sirve para ejecutar a su vez PotreeConverter. Le pedirá:
- Cómo quiere nombrar al archivo
- Dónde se encuentra el LAS a transformar
- El directorio donde quiere guardar los archivos generados"""

w2 = tkinter.Label(root, 
              justify=tkinter.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")


name = input("nombre archivo salida: ")


las = tkinter.filedialog.askopenfilename(filetypes = (("LAS files","*.las"),("all files","*.*")) )
directory = tkinter.filedialog.askdirectory()

infile=open(name, "w") #Opens the file
infile.write('PotreeConverter.exe '+ str(las) + ' -o ' + str(directory) + ' --generate-page ' + str(name))#Writes the desired contents to the file
run = infile.close()#Closes the file
run = os.rename(str(name), str(name)+".bat")
os.system(name)

root.mainloop()


