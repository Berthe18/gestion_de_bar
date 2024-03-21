import tkinter as tk
from modernbutton import MenuButton
import customtkinter as ctk
from tkinter import ttk
import ttkthemes
import ctypes

class Admin(tk.Tk):
    def __init__(self):
        super().__init__()

        self.config = {
            "host" :"localhost",
            "port" : 3306,
            "user" : "root",
            "password" : "",
            "database" : "barpro"

        }

        self.geometry("1200x800")

        self.img = {
                    "acceuil" : tk.PhotoImage(file="images/icons8-accueil-64 (1).png"),
                    "produits" : tk.PhotoImage(file="images/rotation (1).png"),
                    "facture" : tk.PhotoImage(file="images/facture-dachat (1) (1).png"),
                    "personnel" : tk.PhotoImage(file="images/employees (1).png")
            }

        self.dummy_window = tk.Toplevel(self, width=10, height=10)
        self.dummy_window.bind("<FocusIn>", lambda ev : self.focus_set())
        self.dummy_window.bind("<Destroy>", lambda ev : self.destroy())
        self.dummy_window.attributes('-alpha',0.0 )
        self.grab_set()
        
        self.overrideredirect(True)

        self.x = 0
        self.y = 0

        self.main_frame = tk.Frame(self, width=300, height=200, bg="white", relief="solid", bd=1, highlightbackground="#0087d2", highlightthickness=2)
        self.main_frame.pack(fill=tk.BOTH, expand=True)


        self.title_frame = tk.Frame(self.main_frame, width=300, height=30, bg="#333333", relief="flat")
        self.title_frame.grid_anchor("e")

        self.quit_button = ctk.CTkButton(self.title_frame, text = "×", fg_color="transparent", text_color="white", width= 40, font = ("Arial", 20), hover_color="red", corner_radius=0, command=self.destroy)
        self.quit_button.grid(column=5, row=0, sticky="ns")

        self.title_frame.pack(fill=tk.X)

        self.title_frame.bind("<Button-1>", self.on_click)
        self.title_frame.bind("<B1-Motion>", self.on_motion)

        self.dummy_window.title("Admin BarPro")

        self.style()

        self.objects()

    def on_click(self, event):
        self.x = event.x
        self.y = event.y

    def destroy(self):
        return self.event_generate("<Destroy>")

    def on_motion(self, event):
        delta_x = event.x - self.x
        delta_y = event.y - self.y
        new_x = self.winfo_x() + delta_x
        new_y = self.winfo_y() + delta_y
        self.geometry(f"+{new_x}+{new_y}")
    
    def objects(self):
        self.left_menu = tk.PanedWindow(self.main_frame, orient="vertical", width="300", bg="#292929", relief="flat" ,bd=0)
        
        self.left_menu.pack_propagate(0)
        
        self.label = tk.Label(self.left_menu, text= "BarPro")
        
        self.menu_var = tk.IntVar()
        self.menu_var.set(0)

        self.accbtn = MenuButton(self.left_menu, text="Acceuil", bg_color="#292929", text_color="white", image=self.img["acceuil"],  command= self.cmd1, active_color="#1e1e1e")
        self.accbtn.pack(pady=(100, 0), fill="x")
        self.accbtn.set_active()
        self.probtn = MenuButton(self.left_menu, text="Stocks", bg_color="#292929", text_color="white", image=self.img["produits"],  command= self.cmd2, active_color="#1e1e1e")
        self.probtn.pack(fill="x")
        self.facbtn = MenuButton(self.left_menu, text="Facture", bg_color="#292929", text_color="white", image=self.img["facture"],  command= self.cmd3, active_color="#1e1e1e")
        self.facbtn.pack(fill="x")
        self.regbtn = MenuButton(self.left_menu, text="Personnel", bg_color="#292929", text_color="white", image=self.img["personnel"],  command= self.cmd4, active_color="#1e1e1e")
        self.regbtn.pack(fill="x")

        self.menu_btns = (self.accbtn, self.probtn, self.facbtn, self.regbtn)

        self.menu_var.trace_add("write", self.menu_change)

        tk.Label(self.left_menu, text="@UPMSC Devs 2023\nQuincalPro\nversion : 1.0", fg="white", bg="#292929", font=("", 14)).pack(side= "bottom", pady=(0, 40))

        self.left_menu.pack(side="left", fill="y", anchor="nw")

        self.tabs_frame = tk.Frame(self.main_frame, bg="#1e1e1e")
        self.tabs_frame.grid_anchor('center')
        

        ####ACCEUIL

        self.home_frame = tk.Frame(self.tabs_frame, bg="#1e1e1e")
        self.home_frame.grid_anchor("center")

        self.stats1 = ctk.CTkFrame(self.home_frame, width= 410,height= 350, fg_color="#292929")

        self.stats1.grid(column = 0, row =0, padx= 10, pady =(10, 20))

        self.stats2 = ctk.CTkFrame(self.home_frame, width= 410,height= 350, fg_color="#292929", )
        self.stats2.grid(column = 1, row =0, padx= 10, pady =(10, 20))

        self.stats3 = ctk.CTkFrame(self.home_frame, width= 840,height= 350, fg_color="#292929", )
        self.stats3.grid(column = 0, row =1, columnspan= 2)

        self.home_frame.grid(column=0,row=0, sticky="nswe")
        

        ####PRODUITS

        self.stock_frame = tk.Frame(self.tabs_frame, bg="#1e1e1e")
        self.stock_frame.grid_anchor("center")

        self.list_stock = tk.Frame(self.stock_frame, bg="#1e1e1e")

        self.search_pro = ctk.CTkEntry(self.list_stock , width=300, font=('Times new roman', 17), fg_color='white', text_color='black', placeholder_text='Rechercher' , placeholder_text_color='grey', border_color='royalblue')
        self.search_pro.grid(column=0, row=0, pady=(0, 20),sticky='w', padx =20)

        self.product_list_scroll = ctk.CTkScrollbar(self.list_stock)

        self.product_list = ttk.Treeview(self.list_stock, columns=(1, 2, 3), yscrollcommand=self.product_list_scroll.set, height=15)

        self.product_list_scroll.configure(command=self.product_list.yview)

        self.product_list.heading('#0', text='ID')
        self.product_list.column('#0', width=50)

        self.product_list.heading(1, text='Article')
        self.product_list.column(1, width=300)

        self.product_list.heading(2, text='Categorie')
        self.product_list.column(2, width=200)

        self.product_list.heading(3, text='Prix (francs Cfa)')
        self.product_list.column(3, width=250, anchor='center')     

        self.product_list.grid(column=0, row=1)


        self.list_stock.grid(column=0, row=0, sticky="nwse")
        self.stock_frame.grid(column =0, row=0, sticky="nswe")
        


        ####FACTURE

        self.frame3 = tk.Frame(self.tabs_frame, bg="#1e1e1e")


        self.frame3.grid(row=0,column=0, sticky="nswe")

        ####OPTIONS

        self.frame4 = tk.Frame(self.tabs_frame, bg="#1e1e1e")
    
        self.frame4.grid(column =0, row=0, sticky="nswe")
        
        self.parts = [self.home_frame, self.stock_frame, self.frame3, self.frame4]
        
        self.subtab(self.parts[0])

        self.tabs_frame.pack(side="top", expand= True, fill="both", padx=0)

        self.main_frame.pack(expand= True, fill="both")

    
            
    def cmd1(self):
        if self.menu_var.get() != 0:
            self.menu_var.set(0)
            self.subtab(self.parts[0])
            
    def cmd2(self):
        if self.menu_var.get() != 1:
            self.menu_var.set(1)
            self.subtab(self.parts[1])
    
    def cmd3(self):
        if self.menu_var.get() != 2:
            self.menu_var.set(2)
            self.subtab(self.parts[2])

    def cmd4(self):
        if self.menu_var.get() != 3:
            self.menu_var.set(3)
            self.subtab(self.parts[3])

    def menu_change(self, *args):
        pos = self.menu_var.get()
        for btn in self.menu_btns:
            if self.menu_btns.index(btn) == pos:
                btn.set_active()
            else:
                btn.set_disable()

    def subtab(self, part=tk.Frame):
        part.update()
        part.update_idletasks()
        part.tkraise()

    def style(self):
        #ctypes.windll.uxtheme.SetPreferredAppMode(1)
        self.mystyle  = ttkthemes.ThemedStyle(self, theme="equilux")
        self.mystyle.configure("Treeview", background= "#292929")
        self.mystyle.configure("Treeview.Heading", background = "#292929", fieldbackground= "#292929", foreground= "white")
       
if __name__ == "__main__":
    window = Admin()
    window.mainloop()