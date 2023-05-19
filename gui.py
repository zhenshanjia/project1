from tkinter import *
import volume


class GUI:
    def __init__(self,window):
        self.window = window
        self.frame1 = Frame(window)
        self.welcome_label = Label(self.frame1, text = 'Please select an object to calculate the volume')
        self.welcome_label.pack()
        self.frame1.pack()


        self.frame2 = Frame(window)
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.sphere_button = Radiobutton(self.frame2, text="SPHERE", width=10, variable = self.radio_1, value = 1, command = self.shape)
        self.cube_button = Radiobutton(self.frame2, text="CUBE", width=10, variable = self.radio_1, value =2, command = self.shape)
        self.cone_button = Radiobutton(self.frame2, text="CONE", width=10, variable = self.radio_1, value =3, command= self.shape)
        self.frame2.pack()
        self.sphere_button.pack(side='left')
        self.cube_button.pack(side='left')
        self.cone_button.pack(side='left')


        self.frame3 = Frame(window)
        self.input = Label(self.frame3, text = 'Please input values ')
        self.input.pack()
        self.frame3.pack()

        # First number
        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first)
        self.entry_first = Entry(self.frame_first, width = 15, borderwidth = 1)
        self.label_first.pack(padx=20, side='left', )
        self.entry_first.pack(padx=20, side='left', )
        self.frame_first.pack(anchor='w', pady=10)
        self.entry_first.pack_forget()

        # Second number
        self.frame_second = Frame(self.window)
        self.label_second = Label(self.frame_second)
        self.entry_second = Entry(self.frame_second, width = 15, borderwidth = 1)
        self.label_second.pack(padx=20, side='left')
        self.entry_second.pack(padx=20, side='left')
        self.frame_second.pack(anchor='w', pady=10)
        self.entry_second.pack_forget()

        # Results label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Compute button
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='Calculate', command=self.compute)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def shape(self):
        self.entry_first.delete(0, END)
        self.entry_second.delete(0, END)
        self.label_result.config(text='')
        self.entry_first.pack()
        shape = self.radio_1.get()

        if shape == 1:
            self.label_first.config(text='Radius')
            self.label_second.config(text='')
            self.entry_second.pack_forget()
        elif shape == 2:
            self.label_first.config(text='Side')
            self.label_second.config(text='')
            self.entry_second.pack_forget()
        elif shape == 3:
            self.label_first.config(text='Radius')
            self.label_second.config(text='Height')
            self.entry_second.pack()


    def compute(self):
        try:
            first_num = self.entry_first.get()
            second_num = self.entry_second.get()
            shape = self.radio_1.get()

            if shape == 1:
                self.label_result.config(text=f'Sphere volume = {volume.sphere(first_num)}')
            elif shape == 2:
                self.label_result.config(text=f'Cube volume = {volume.cube(first_num)}')
            elif shape == 3:
                self.label_result.config(text=f'Cone volume = {volume.cone(first_num, second_num)}')
            else:
                self.label_result.config(text='No operation selected')
        except ValueError:
            self.label_result.config(text='Enter numeric values')
        except TypeError:
            self.label_result.config(text='Values must be positive')


def sphere_volume(self):
    label_sphere =  Label(window, text = 'Please input the radius:')
    sphere_radius = Entry(window, width = 15, borderwidth = 1)
    label_sphere.pack()
    sphere_radius.pack()

    label_sphere_calculated = Label(window, text = 'The volume of the sphere is:10')
    label_sphere_calculated.pack()
def cube_volume(self):
    label_cube = Label(window, text='Please input side:')
    cube_side = Entry(window, width=15, borderwidth = 1)
    label_cube.pack()
    cube_side.pack()
def cone_volume(self):
    label_cone_radius = Label(window, text='Please input radius:')
    label_cone_height = Label(window, text='Please input height:')
    cone_radius = Entry(window, width = 15, borderwidth = 1)
    cone_height = Entry(window, width = 15, borderwidth = 1)
    label_cone_radius.pack()
    label_cone_height.pack()
    cone_radius.pack()
    cone_height.pack()



if __name__ == '__main__':
    main()