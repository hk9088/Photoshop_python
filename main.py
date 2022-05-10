from tkinter import *
from  tkinter import  filedialog
from PIL import  Image, ImageTk , ImageEnhance
import  os


def btn_browse_clicked():
    try:
        btn_browse_clicked.fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                     filetypes=(("ALL Files", "*.*"),("JPG File", "*.jpg"), ("PNG", "*.png")))
        btn_browse_clicked.s = 1
        btn_browse_clicked.color = 1
        btn_browse_clicked.bri = 1
        btn_browse_clicked.con = 1
        btn_browse_clicked.img = Image.open(btn_browse_clicked.fln)
        load_image(btn_browse_clicked.img)
    except:
        pass


def load_image(img):
    try:


        w, h = img.size
        w_var.set(str(w))
        h_var.set(str(h))

        img = img.resize((774, 650), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        canvas2 = Canvas(
            window,
            bg="#ffffff",
            height=650,
            width=774,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas2.place(x=253, y=0)
        btn_browse_clicked.lb1 = Label(canvas2)
        btn_browse_clicked.lb1.configure(image=img)
        btn_browse_clicked.lb1.anchor = "nw"
        btn_browse_clicked.lb1.image = img
        btn_browse_clicked.lb1.place(x=0, y=0)


    except:
        pass

def btn_show_clicked():
    try:
        img = Image.open(btn_browse_clicked.fln)
        img.show()

    except:
        pass



def btn_jpg_clicked():
    try:
        filename, extension = os.path.splitext(btn_browse_clicked.fln)
        filename = filename + "_0"
        extension = '.jpg'
        f = filename + extension
        w_var = entry0.get()
        h_var = entry1.get()
        btn_browse_clicked.img.thumbnail((int(w_var), int(h_var)))
        btn_browse_clicked.img.save(f)


    except:
        pass

def btn_png_clicked():
    try:
        filename, extension = os.path.splitext(btn_browse_clicked.fln)
        filename = filename + "_0"
        extension = '.png'
        f = filename + extension
        w_var = entry0.get()
        h_var = entry1.get()
        btn_browse_clicked.img.thumbnail((int(w_var), int(h_var)))
        btn_browse_clicked.img.save(f)
    except:
        pass

def btn_pdf_clicked():
    try:

        filename, extension = os.path.splitext(btn_browse_clicked.fln)
        filename = filename + "_0"
        extension = '.pdf'
        f = filename + extension
        w_var = entry0.get()
        h_var = entry1.get()
        btn_browse_clicked.img.thumbnail((int(w_var), int(h_var)))
        btn_browse_clicked.img.save(f)
    except:
        pass



def btn_sharpness_plus_clicked():
    try:

        btn_browse_clicked.s = btn_browse_clicked.s + 0.1
        enhancer = ImageEnhance.Sharpness(btn_browse_clicked.img)
        btn_browse_clicked.img  = enhancer.enhance(btn_browse_clicked.s)

        load_image(btn_browse_clicked.img)

    except:
        pass

def btn_sharpness_minus_clicked():
    try:

        btn_browse_clicked.s = btn_browse_clicked.s - 0.1
        enhancer = ImageEnhance.Sharpness(btn_browse_clicked.img)
        btn_browse_clicked.img = enhancer.enhance(btn_browse_clicked.s)

        load_image(btn_browse_clicked.img)

    except:
        pass

def btn_color_minus_clicked():
    try:

        btn_browse_clicked.color = btn_browse_clicked.color - 0.1
        enhancer = ImageEnhance.Color(btn_browse_clicked.img)
        btn_browse_clicked.img = enhancer.enhance(btn_browse_clicked.color)

        load_image(btn_browse_clicked.img)

    except:
        pass

def btn_color_plus_clicked():
    try:
        if (btn_browse_clicked.color <= 0):
            btn_browse_clicked.color = 1
        btn_browse_clicked.color = btn_browse_clicked.color + 0.1
        enhancer = ImageEnhance.Color(btn_browse_clicked.img)
        btn_browse_clicked.img = enhancer.enhance(btn_browse_clicked.color)

        load_image(btn_browse_clicked.img)

    except:
        pass


def btn_brightness_minus_clicked():
    try:

        btn_browse_clicked.bri = btn_browse_clicked.bri - 0.1
        enhancer = ImageEnhance.Brightness(btn_browse_clicked.img)
        btn_browse_clicked.img = enhancer.enhance(btn_browse_clicked.bri)

        load_image(btn_browse_clicked.img)

    except:
        pass
def btn_brightness_plus_clicked():
    try:

        btn_browse_clicked.bri = btn_browse_clicked.bri + 0.1
        enhancer = ImageEnhance.Brightness(btn_browse_clicked.img)
        btn_browse_clicked.img = enhancer.enhance(btn_browse_clicked.bri)

        load_image(btn_browse_clicked.img)

    except:
        pass


def btn_contrast_minus_clicked():
    try:

        btn_browse_clicked.con = btn_browse_clicked.con - 0.1
        enhancer = ImageEnhance.Contrast(btn_browse_clicked.img)
        btn_browse_clicked.img = enhancer.enhance(btn_browse_clicked.con)

        load_image(btn_browse_clicked.img)

    except:
        pass
def btn_contrast_plus_clicked():
    try:

        btn_browse_clicked.con = btn_browse_clicked.con + 0.1
        enhancer = ImageEnhance.Contrast(btn_browse_clicked.img)
        btn_browse_clicked.img = enhancer.enhance(btn_browse_clicked.con)

        load_image(btn_browse_clicked.img)

    except:
        pass




window = Tk()
window.title("Photoshop")
window.geometry("1024x768")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    512.0, 384.0,
    image=background_img)


browse_img = PhotoImage(file = f"browse_img.png")
browse = Button(
    image = browse_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_browse_clicked,
    relief = "flat")

browse.place(
    x = 342, y = 701,
    width = 170,
    height = 51)

show_img = PhotoImage(file = f"show_img.png")
show = Button(
    image = show_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_show_clicked,
    relief = "flat")

show.place(
    x = 803, y = 701,
    width = 170,
    height = 51)

jpg_img = PhotoImage(file = f"jpg_img.png")
jpg = Button(
    image = jpg_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_jpg_clicked,
    relief = "flat")

jpg.place(
    x = 20, y = 697,
    width = 66,
    height = 34)

png_img = PhotoImage(file = f"png_img.png")
png = Button(
    image = png_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_png_clicked,
    relief = "flat")

png.place(
    x = 93, y = 697,
    width = 66,
    height = 34)

pdf_img = PhotoImage(file = f"pdf_img.png")
pdf = Button(
    image = pdf_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_pdf_clicked,
    relief = "flat")

pdf.place(
    x = 162, y = 697,
    width = 66,
    height = 34)

sharpness_plus_img = PhotoImage(file = f"plus_img.png")
sharpness_plus_button = Button(
    image = sharpness_plus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_sharpness_plus_clicked,
    relief = "flat")

sharpness_plus_button.place(
    x = 58, y = 276,
    width = 26,
    height = 26)

sharpness_minus_img = PhotoImage(file = f"minus_img.png")
sharpness_minus_button = Button(
    image = sharpness_minus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_sharpness_minus_clicked,
    relief = "flat")

sharpness_minus_button.place(
    x = 152, y = 276,
    width = 26,
    height = 26)

color_minus_img = PhotoImage(file = f"minus_img.png")
color_minus_button = Button(
    image = color_minus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_color_minus_clicked,
    relief = "flat")

color_minus_button.place(
    x = 152, y = 354,
    width = 26,
    height = 26)

color_plus_img = PhotoImage(file = f"plus_img.png")
color_plus_button = Button(
    image = color_plus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_color_plus_clicked,
    relief = "flat")

color_plus_button.place(
    x = 58, y = 354,
    width = 26,
    height = 26)

brightness_minus_img = PhotoImage(file = f"minus_img.png")
brightness_minus_button = Button(
    image = brightness_minus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_brightness_minus_clicked,
    relief = "flat")

brightness_minus_button.place(
    x = 152, y = 450,
    width = 26,
    height = 26)

brightness_plus_img = PhotoImage(file = f"plus_img.png")
brightness_plus_button = Button(
    image = brightness_plus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_brightness_plus_clicked,
    relief = "flat")

brightness_plus_button.place(
    x = 58, y = 450,
    width = 26,
    height = 26)

contrast_minus_img = PhotoImage(file = f"minus_img.png")
contrast_minus_button = Button(
    image = contrast_minus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_contrast_minus_clicked,
    relief = "flat")

contrast_minus_button.place(
    x = 152, y = 528,
    width = 26,
    height = 26)

contrast_plus_img = PhotoImage(file = f"plus_img.png")
contrast_plus_button = Button(
    image = contrast_plus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_contrast_plus_clicked,
    relief = "flat")

contrast_plus_button.place(
    x = 58, y = 528,
    width = 26,
    height = 26)


h_var = StringVar()
w_var = StringVar()
entry0 = Entry(
    textvariable = w_var,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry0.place(
    x=57, y=187,
    width=33.0,
    height=23)

entry1 = Entry(
    textvariable = h_var,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry1.place(
    x=150, y=187,
    width=33.0,
    height=23)






window.resizable(False, False)
window.mainloop()
