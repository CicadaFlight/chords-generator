from tkinter import *
import MusicScript


# UI

root = Tk()
root.title("Chord Progression Generator")
root.geometry("550x270")
root.iconbitmap("./icon.ico")

# input fields
header = LabelFrame(root, text="Generate a chord progression", padx=10, pady=10)
header.pack(fill="x", padx=10, pady=10)

input_wrap = Frame(header)

# major or minor?
options = ["Major", "Minor"]
value_inside = StringVar(root)
value_inside.set(options[0])
dropdown = OptionMenu(input_wrap, value_inside, *options)
dropdown.pack(side=LEFT)

# number of chords
num_chords = Entry(input_wrap, width=6)
num_chords.insert(END, "4")
num_chords.pack(side=LEFT, padx=40)

# prob of 7ths
slider = Scale(input_wrap, from_=0, to=100, orient=HORIZONTAL)
slider.pack(side=LEFT)

# include diminished
include_dim = IntVar()
check = Checkbutton(input_wrap, variable=include_dim)
check.pack(side=LEFT, padx=40)

input_wrap.pack()



# labels
label_wrapper = Frame(header)
l_root = Label(label_wrapper, text="Root chord").pack(side=LEFT)
l_amt = Label(label_wrapper, text="Amount").pack(side=LEFT, padx=40)
l_prob = Label(label_wrapper, text="Jazziness").pack(side=LEFT)
l_dim = Label(label_wrapper, text="Include dim").pack(side=LEFT, padx=40)
label_wrapper.pack()


# result field must be declared before the logic
res_field_text = StringVar()
res_field = Label(root, textvariable = res_field_text)
#res_field.config(state="disabled")

# message field
msg_text = StringVar()
msg_field = Label(root, textvariable=msg_text, fg="red4")


# when button is pushed
def try_generate():
    try:
        _root = value_inside.get()
        _amt = int(num_chords.get())
        if _amt > 16:
            msg_text.set("Amount of chords to generate can be 16 at most")
            return
        elif _amt < 1:
            msg_text.set("Amount of chords to generate must be at least 1")
            return
        _prob = (int(slider.get()) / 100) # method takes value between 0 and 1
        _dim = bool(include_dim.get())
        prog = MusicScript.generate_chord_progression(_root, _amt, _prob, _dim)
        res_field_text.set("    ".join(prog))
        msg_text.set("")
    except:
        msg_text.set("One or more fields contain illegal values")

# generate button
gen_btn = Button(root, text="Generate", width=30, command=try_generate)
gen_btn.pack()


# result field
res_field.pack(padx=50, pady=20)

# message field
msg_field.pack(padx=50, pady=20)


root.mainloop()