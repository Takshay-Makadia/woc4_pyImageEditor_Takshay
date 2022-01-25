from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk,ImageOps

root = Tk()
root.title("woc-4_Python Image Editor")

global output_image

#{Fuctions

def open_image():
    global final_label
    global img_label
    global output_image
    global image_resized
    image_type = [('JPG File','*.JPG'),('PNG File','*.PNG'),('jpeg File','*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=image_type)
    opened_image = Image.open(filename)
    image_resized = opened_image.resize((1150,652), Image.ANTIALIAS)
    image_frame.delete("final_label")
    final_label = ImageTk.PhotoImage(image_resized)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    open_button["state"] = "disable"
    output_image = image_resized
    save_button["state"] = 'normal'

    
def black_white():
    global final_label
    global output_image
    global img_label
    image_frame.delete("final_label")
    final_image_bw = turn_blackwhite()
    final_label = ImageTk.PhotoImage(final_image_bw)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    output_image = final_image_bw

def flip_l_r():
    global img_label
    global output_image
    global final_label
    image_frame.delete("final_label")
    final_image_flip_lr = flip_lr()
    final_label = ImageTk.PhotoImage(final_image_flip_lr)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    output_image=final_image_flip_lr

def flip_u_d():
    global img_label
    global output_image
    global final_label
    image_frame.delete("final_label")
    final_image_flip_lr = flip_ud()
    final_label = ImageTk.PhotoImage(final_image_flip_lr)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    output_image=final_image_flip_lr

def invert_image():
    global img_label
    global output_image
    global final_label
    image_frame.delete("final_label")
    final_image_invert = img_invert()
    final_label = ImageTk.PhotoImage(final_image_invert)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    output_image=final_image_invert

def crop():
    global final_label
    global output_image
    global image_frame
    image_frame.delete('final_label')
    f_i_c = output_image.crop((287,163,862,489))
    final_label = ImageTk.PhotoImage(f_i_c)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    output_image = f_i_c
    applycrop_button["state"] = 'disabled'

def save_image():
    image_type = [('JPG File','*.JPG'),('PNG File','*.PNG'),('jpeg File','*.jpeg')]
    filename = filedialog.asksaveasfile(filetypes=image_type, defaultextension=image_type)
    output_image.save(filename)

def remove_image():
    global final_label
    image_frame.delete("final_label")
    final_label = image_frame.create_text(0,0,text="Upload New Image")
    open_button["state"] = 'normal'
    save_button["state"] = 'disabled'




#}



#{Page Layout
space_label = Label(root, text = '    ')
space_label.grid(row=0,column=0)

open_button = Button(root, text = "Open Image", command = open_image)
open_button.grid(row=1,column=1)

save_button = Button(root, text = "Save",width=10, command = save_image,state=DISABLED)
save_button.grid(row=1,column=2)

space_label = Label(root, text = '  ')
space_label.grid(row=1,column=3)

image_frame = Canvas(root, bg='black',height=652,width=1100)
image_frame.grid(row=2,column=4)

button_frame = LabelFrame(root, borderwidth=0)
button_frame.grid(row=2,column=5)

space_label = Label(button_frame, text = '  \n\n\n  ')
space_label.grid(row=0,column=0)

button_bw = Button(button_frame, text = "Turn to Black and White", command = black_white)
button_bw.grid(row=1,column=1)

space_label = Label(button_frame, text = '  \n\n\n  ')
space_label.grid(row=2,column=0)

button_flip_lr = Button(button_frame, text='Flip Left/Rigth', command=flip_l_r)
button_flip_lr.grid(row=3,column=1)

space_label = Label(button_frame, text = '  \n\n\n  ')
space_label.grid(row=4,column=0)

button_flip_tb = Button(button_frame, text='Flip Up/Down', command=flip_u_d)
button_flip_tb.grid(row=5,column=1)

space_label = Label(button_frame, text = '  \n\n\n  ')
space_label.grid(row=6,column=0)

button_invert = Button(button_frame, text='Invert Image', command = invert_image)
button_invert.grid(row=7,column=1)

crop_frame = LabelFrame(root, borderwidth=0)
crop_frame.grid(row=4,column=4)

space_label = Label(crop_frame, text = '  \n  ')
space_label.grid(row=0,column=0)

applycrop_button = Button(crop_frame,text='Apply crop',command=crop)
applycrop_button.grid(row=1,column=3)

space_label = Label(crop_frame, text = '    ')
space_label.grid(row=1,column=4)

label_crop = Label(crop_frame, text = "Crop button will give image of 1/2 size at the center")
label_crop.grid(row=1,column=5)

remove_button = Button(root, text = "Remove Image", command = remove_image)
remove_button.grid(row=2,column=2)

#}

#{Functions for image Manipulation

def flip_lr():
    w = output_image.width
    h = output_image.height


    arr = []

    for y in range(0,h):
        for x in range(0,w):
            coordinate1 = x, y 
            coordinate2 = w-x-1, y
            data1 = output_image.getpixel(coordinate1)
            data2 = output_image.getpixel(coordinate2)
            list(data1)
            data1 = data2
            arr.append(data1)

    image_out = Image.new(output_image.mode,output_image.size)
    image_out.putdata(arr)
    return image_out

def flip_ud():
    w = output_image.width
    h = output_image.height


    arr = []

    for y in range(0,h):
        for x in range(0,w):
            coordinate1 = x, y 
            coordinate2 = x, h-y-1
            data1 = output_image.getpixel(coordinate1)
            data2 = output_image.getpixel(coordinate2)
            list(data1)
            data1 = data2
            arr.append(data1)

    image_out = Image.new(output_image.mode,output_image.size)
    image_out.putdata(arr)
    return image_out

def img_invert():
    w = output_image.width
    h = output_image.height


    arr = []

    for y in range(0,h):
        for x in range(0,w):
            coordinate1 = x, y 
            data1 = output_image.getpixel(coordinate1)
            list(data1)
            data1=255-data1[0],255-data1[1],255-data1[2]
            arr.append(data1)

    image_out = Image.new(output_image.mode,output_image.size)
    image_out.putdata(arr)
    return image_out

def turn_blackwhite():
    w = output_image.width
    h = output_image.height


    arr = []

    for y in range(0,h):
        for x in range(0,w):
            coordinate1 = x, y 
            data1 = output_image.getpixel(coordinate1)
            list(data1)
            sum = data1[0]+data1[1]+data1[2]
            average = int(sum/3)
            data1=average,average,average
            arr.append(data1)

    image_out = Image.new(output_image.mode,output_image.size)
    image_out.putdata(arr)
    return image_out
# }        

root.mainloop()