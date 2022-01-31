from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter.messagebox import askyesno
from PIL import Image,ImageTk,ImageOps,ImageEnhance

root = Tk()
root.title("woc-4_Python Image Editor")

global output_image

#{Fuctions

def open_image():
    global final_label
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
    image_frame.delete("final_label")
    final_image_bw = output_image.convert("L")
    final_label = ImageTk.PhotoImage(final_image_bw)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    output_image = final_image_bw

def flip_l_r():
    global output_image
    global final_label
    image_frame.delete("final_label")
    final_image_flip_lr = output_image.transpose(Image.FLIP_LEFT_RIGHT)
    final_label = ImageTk.PhotoImage(final_image_flip_lr)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    output_image=final_image_flip_lr

def flip_u_d():
    global output_image
    global final_label
    image_frame.delete("final_label")
    final_image_flip_lr = output_image.transpose(Image.FLIP_TOP_BOTTOM)
    final_label = ImageTk.PhotoImage(final_image_flip_lr)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    output_image=final_image_flip_lr

def invert_image():
    global output_image
    global final_label
    image_frame.delete("final_label")
    final_image_invert = ImageOps.invert(output_image)
    final_label = ImageTk.PhotoImage(final_image_invert)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    output_image=final_image_invert

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

def img_brightness(event):
    global output_image
    global final_label,final_image_brightness
    image_frame.delete("final_label")
    filter_bri = ImageEnhance.Brightness(output_image)
    final_image_brightness = filter_bri.enhance(brightness_slider.get())
    final_label = ImageTk.PhotoImage(final_image_brightness)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    bri_button["state"] = 'normal'

def apply_bri():
    global output_image,final_label
    res = askyesno(title = "Set Brightness", message = "Apply Current Brightness?")
    if res==1:
        output_image=final_image_brightness
    else:
        final_label = ImageTk.PhotoImage(output_image)
        image_frame.create_image(575,326,image = final_label, anchor='center')
    bri_button["state"] = 'disabled'

def img_contrast(event):
    global output_image
    global final_label,final_image_contrast
    image_frame.delete("final_label")
    filter_con = ImageEnhance.Contrast(output_image)
    final_image_contrast = filter_con.enhance(contrast_slider.get())
    final_label = ImageTk.PhotoImage(final_image_contrast)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    con_button["state"] = 'normal'

def apply_con():
    global output_image,final_label
    res = askyesno(title = "Set Contrast", message = "Apply Current Contrast?")
    if res==1:
        output_image=final_image_contrast
    else:
        final_label = ImageTk.PhotoImage(output_image)
        image_frame.create_image(575,326,image = final_label, anchor='center')
    con_button["state"] = 'disabled'

def img_sharpness(event):
    global output_image
    global final_label,final_image_sharpness
    image_frame.delete("final_label")
    filter_sha = ImageEnhance.Sharpness(output_image)
    final_image_sharpness = filter_sha.enhance(sharpness_slider.get())
    final_label = ImageTk.PhotoImage(final_image_sharpness)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    sha_button["state"] = 'normal'

def apply_sha():
    global output_image,final_label
    res = askyesno(title = "Set Sharpness", message = "Apply Current Sharpness?")
    if res==1:
        output_image=final_image_sharpness
    else:
        final_label = ImageTk.PhotoImage(output_image)
        image_frame.create_image(575,326,image = final_label, anchor='center')
    sha_button["state"] = 'disabled'

def img_saturation(event):
    global output_image
    global final_label,final_image_saturation
    image_frame.delete("final_label")
    filter_sat = ImageEnhance.Color(output_image)
    final_image_saturation = filter_sat.enhance(saturation_slider.get())
    final_label = ImageTk.PhotoImage(final_image_saturation)
    image_frame.create_image(575,326,image = final_label, anchor='center')
    sat_button["state"] = 'normal'

def apply_sat():
    global output_image,final_label
    res = askyesno(title = "Set Saturation", message = "Apply Current Saturation?")
    if res==1:
        output_image=final_image_saturation
    else:
        final_label = ImageTk.PhotoImage(output_image)
        image_frame.create_image(575,326,image = final_label, anchor='center')
    sat_button["state"] = 'disabled'

#}

#{button images

o = Image.open("open.png")
o_r = o.resize((30,30))
o_l = ImageTk.PhotoImage(o_r)

s = Image.open("save.png")
s_r = s.resize((30,30))
s_l = ImageTk.PhotoImage(s_r)

f_rl =Image.open("flip_rl.png")
f_rl_r = f_rl.resize((30,30))
f_rl_l = ImageTk.PhotoImage(f_rl_r)

f_ud =Image.open("flip_ud.png")
f_ud_r = f_ud.resize((30,30))
f_ud_l = ImageTk.PhotoImage(f_ud_r)

bw =Image.open("bw.jpg")
bw_r = bw.resize((150,25))
bw_l = ImageTk.PhotoImage(bw_r)

r =Image.open("remove.jpg")
r_r = r.resize((30,30))
r_l = ImageTk.PhotoImage(r_r)

i =Image.open("invert.png")
i_r = i.resize((30,30))
i_l = ImageTk.PhotoImage(i_r)
#}

#{Page Layout
space_label = Label(root, text = '    ')
space_label.grid(row=0,column=0)

open_button = Button(root, image = o_l, command = open_image)
open_button.grid(row=1,column=1)

save_button = Button(root, image = s_l, command = save_image,state=DISABLED)
save_button.grid(row=1,column=2)

space_label = Label(root, text = '  ')
space_label.grid(row=1,column=3)

image_frame = Canvas(root, bg='black',height=652,width=1100)
image_frame.grid(row=2,column=4)

button_frame = LabelFrame(root, borderwidth=0)
button_frame.grid(row=2,column=5)

space_label = Label(button_frame, text = '  \n\n  ')
space_label.grid(row=0,column=0)

button_bw = Button(button_frame, image = bw_l, command = black_white)
button_bw.grid(row=1,column=1,padx=0)

space_label = Label(button_frame, text = '  \n\n  ')
space_label.grid(row=2,column=0)

button_flip_lr = Button(button_frame, image = f_rl_l, command=flip_l_r)
button_flip_lr.grid(row=3,column=1,padx=0)

space_label = Label(button_frame, text = '  \n\n  ')
space_label.grid(row=4,column=0)

button_flip_tb = Button(button_frame, image = f_ud_l, command=flip_u_d)
button_flip_tb.grid(row=5,column=1,padx=0)

space_label = Label(button_frame, text = '  \n\n  ')
space_label.grid(row=6,column=0)

button_invert = Button(button_frame, image = i_l, command = invert_image)
button_invert.grid(row=7,column=1,padx=0)

space_label = Label(button_frame, text = '  \n\n  ')
space_label.grid(row=8,column=0)

remove_button = Button(root, image = r_l, command = remove_image)
remove_button.grid(row=2,column=2)

brightness_slider = Scale(button_frame, from_=0.0, to=4.0, orient=HORIZONTAL, command=img_brightness, resolution=0.1)
brightness_slider.grid(row=10,column=1,padx=0)
brightness_slider.set(1.0)

bri_button = Button(button_frame, text="Apply Brightness", command=apply_bri, state=DISABLED)
bri_button.grid(row=10,column=2,padx=0)

contrast_slider = Scale(button_frame, from_=0.0, to=4.0, orient=HORIZONTAL, command=img_contrast, resolution=0.1)
contrast_slider.grid(row=11,column=1,padx=0)
contrast_slider.set(1.0)

con_button = Button(button_frame, text="Apply Contrast", command=apply_con, state=DISABLED)
con_button.grid(row=11,column=2,padx=0)

sharpness_slider = Scale(button_frame, from_=0.0, to=4.0, orient=HORIZONTAL, command=img_sharpness, resolution=0.1)
sharpness_slider.grid(row=12,column=1,padx=0)
sharpness_slider.set(1.0)

sha_button = Button(button_frame, text="Apply Sharpness", command=apply_sha, state=DISABLED)
sha_button.grid(row=12,column=2,padx=0)

saturation_slider = Scale(button_frame, from_=0.0, to=4.0, orient=HORIZONTAL, command=img_saturation, resolution=0.1)
saturation_slider.grid(row=13,column=1,padx=0)
saturation_slider.set(1.0)

sat_button = Button(button_frame, text="Apply Saturation", command=apply_sat, state=DISABLED)
sat_button.grid(row=13,column=2,padx=0)

#}

root.mainloop()