from tnter import*
from PIL import ImageTk, Image
root=Tk()
root.minsize(650,650)
root.maxsize(1000,1000)
open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))
root.configure("lilac")
l=Label(root,text="file name")
l.place(relx=0.28,rely=0.03,anchor=CENTER)
e=Entry(root)
e.place(relx=0.48,rely=0.03,anchor=CENTER)
mt=Text(root,height=35,width=80)
mt.place(relx=.5,rely=0.55,anchor=CENTER)
root.mainloop()

