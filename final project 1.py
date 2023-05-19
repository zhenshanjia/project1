from gui import *

def main():
    window = Tk()
    window.title('volume calculation')
    window.geometry('300x300')
    window.resizable(False, False)

    GUI(window)

    window.mainloop()
if __name__ == '__main__':
    main()