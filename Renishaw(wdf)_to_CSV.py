from tkinter import *
from renishawWiRE import WDFReader
from tkinter import filedialog
import numpy as np
import os



def DataMat(name): # Was DataMat2D
    # Reshapes the data into a data matrix (rows=specra,columns=wavelengths) 
    reader = WDFReader(name)
    spectra = reader.spectra
    shp = spectra.shape
    wn = reader.xdata
    data = spectra.reshape(shp[0]*shp[1], len(wn))
    return data



root = Tk()

root.geometry("400x400")


def SelectFile():
    file = filedialog.askopenfilename()

    path, extension = os.path.splitext(file)
    # you can use the name from this to make the name 
    # replacement automatic

    split_path = path.split('/')
    name_arr = np.array(split_path[len(split_path)-1:len(split_path)])[0]
    name = str(name_arr) + '.csv'


    
    if extension == '.wdf':
        data = DataMat(file)
        if file:
            np.savetxt(name, data, delimiter=",") # store as CSV file
            
            label = Label(root, text="A " + str(data.shape) + " matrix \n has been saved called: \n" + name).grid(row=2, column=0, padx=0, pady=10)
                                                     
        else:
            None               
    
    else:
        label = Label(root, text="File type error:\n wdf. file required").grid(row=2, column=0, padx=0, pady=10)
    

button = Button(root, text="Select File",height=5, width=15, font=('Arial 14'), command=SelectFile).grid(row=3, column=0, padx=0, pady=0)



root.mainloop()
