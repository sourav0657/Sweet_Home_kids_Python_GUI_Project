import tkinter as tk
import webbrowser

class SweetHome:
    def __init__(self, root):
        self.f = tk.Canvas(
            root,
            bg='#FFD6A5',
            width=root.winfo_screenwidth(),
            height=root.winfo_screenheight()
        )
        self.f.pack(fill="both", expand=True)

        # draw when canvas size is ready / changes
        self.f.bind("<Configure>", self.draw_home)
        self.is_sun = True

    def draw_home(self, event):
        self.f.delete("all")

        # create rectangle
        margin = 250
        self.house_width = self.f.winfo_width() * 0.20
        self.house_height = self.f.winfo_height() * 0.20
        self.w1 = self.f.winfo_width() - self.house_width - margin
        self.w2 = self.house_width + self.w1
        self.h1 = ((self.f.winfo_height() - self.house_height) / 2 + 50)
        self.h2 = self.house_height + self.h1 + 50

        # house
        self.f.create_rectangle(
            self.w1, self.h1, self.w2, self.h2,
            fill="#FFF1C1", outline="black", width=1
        )

        self.home_door_rect()
        self.home_window_rect()
        self.home_roof()
        self.home_roof_window_rect()
        self.home_sun_moon()
        self.home_road()
        self.home_bushes()
        self.home_pond()

    def home_door_rect(self):
        # Door size (relative to house)
        self.door_width = self.house_width * 0.25
        self.door_height = self.house_height * 0.60

        # Center door horizontally
        self.dw1 = self.w1 + (self.house_width - self.door_width) / 2
        self.dw2 = self.dw1 + self.door_width

        # Place door at bottom of house
        self.dh2 = self.h2
        self.dh1 = self.dh2 - self.door_height
        self.home_door =  self.f.create_rectangle(self.dw1, self.dh1, self.dw2, self.dh2,fill="#8B5A2B", outline="black", width=1)
        self.home_door_text = self.f.create_text((self.dw1 + self.dw2) / 2,(self.dh1 + self.dh2) / 2,text="Learn ABCD",
                                                 fill="white",font=("Arial", 9, "bold"))
        self.f.tag_bind(self.home_door,"<Button-1>", self.home_door_click)
        self.f.tag_bind(self.home_door, "<Button-3>", self.home_door_click)
        self.f.tag_bind(self.home_door_text, "<Button-1>", self.home_door_click)
        self.f.tag_bind(self.home_door_text, "<Button-3>", self.home_door_click)

    def home_door_click(self, event):
        self.f.itemconfig(self.home_door, fill="#5A3A1B")  # darker (pressed look)
        webbrowser.open("https://www.youtube.com/watch?v=hq3yfQnllfQ")

    def home_window_rect(self):
        # windows
        self.window_width = self.house_width * 0.15
        self.window_height = self.house_height * 0.20
        self.wy1 = self.h1 + self.house_height * 0.20
        self.wy2 = self.wy1 + self.window_height
        # Left window
        self.lw1 = self.w1 + self.house_width * 0.15
        self.lw2 = self.lw1 + self.window_width
        self.f.create_rectangle(self.lw1, self.wy1, self.lw2, self.wy2, fill="#D9A441", outline="black", width=1)  # Soft Amber Glass

        # Right window
        self.rw2 = self.w2 - self.house_width * 0.10
        self.rw1 = self.rw2 - self.window_width
        self.f.create_rectangle(self.rw1, self.wy1, self.rw2, self.wy2, fill="#D9A441", outline="black", width=1)  # Soft Amber Glass

    def home_roof(self):
        #rooftop
        self.roof_peak_x = (self.w1 + self.w2) / 2
        self.roof_height = self.house_height * 0.85  # adjust for steepness
        self.roof_peak_y = self.h1 - self.roof_height
        self.f.create_polygon(self.w1,self.h1,self.w2,self.h1,self.roof_peak_x,self.roof_peak_y,fill= "#424242", outline="black",width=1) #charcoal grey

    def home_roof_window_rect(self):
        # Rooftop window size (relative)
        self.roof_window_width = self.house_width * 0.20
        self.roof_window_height = self.roof_height * 0.25

        # Center window horizontally on roof
        self.rf1 = self.roof_peak_x - self.roof_window_width / 2
        self.rf2 = self.roof_peak_x + self.roof_window_width / 2

        # Place window slightly below the roof peak
        self.rh1 = self.roof_peak_y + self.roof_height * 0.55
        self.rh2 = self.rh1 + self.roof_window_height
        self.f.create_rectangle(self.rf1, self.rh1, self.rf2, self.rh2,fill="#6FAFC8", outline="black", width=1) #Smoky Sky Blue

    def home_sun_moon(self):
        #Create Sun/moon
        self.oval_width = self.f.winfo_width() * 0.08
        self.oval_height = self.f.winfo_height() * 0.14
        self.margin1 = 126.4
        self.margin2 = 116.4
        self.sun_moon_w1 = self.oval_width
        self.sun_moon_h1 = self.oval_height
        self.sun_moon_w2 = self.oval_width + self.margin1
        self.sun_moon_h2 = self.oval_height + self.margin2
        self.moon_button = self.f.create_oval(self.sun_moon_w1,self.sun_moon_h1,self.sun_moon_w2,self.sun_moon_h2,
                           fill="#FFD84D",outline="black",width=1) #Warm Golden Sun
        self.f.sun_text =self.f.create_text((self.sun_moon_w1 + self.sun_moon_w2)/2,
                                            (self.sun_moon_h1 + self.sun_moon_h2)/2,text= "Sun",fill="Black",
                                            font=("Arial", 15, "bold"),state="normal")
        self.f.moon_text = self.f.create_text((self.sun_moon_w1 + self.sun_moon_w2)/2,
                                            (self.sun_moon_h1 + self.sun_moon_h2)/2,text= "Moon",fill="Black",
                                            font=("Arial", 15, "bold"),state="hidden")
        self.f.tag_bind(self.moon_button, "<Button-1>", self.on_sun_moon_click)
        self.f.tag_bind(self.moon_button, "<Button-3>", self.on_sun_moon_click)
        self.f.tag_bind(self.f.sun_text, "<Button-1>", self.on_sun_moon_click)
        self.f.tag_bind(self.f.sun_text, "<Button-3>", self.on_sun_moon_click)
        self.f.tag_bind(self.f.moon_text, "<Button-1>", self.on_sun_moon_click)
        self.f.tag_bind(self.f.moon_text, "<Button-3>", self.on_sun_moon_click)

    def on_sun_moon_click(self, event):
        if self.is_sun:
            # Switch to night (Moon)
            self.f.itemconfig(self.moon_button, fill="#DDE6F0")
            self.f.config(bg="#0B1D3A")
            self.f.itemconfig(self.f.sun_text, state="hidden")
            self.f.itemconfig(self.f.moon_text, state="normal")
            self.f.itemconfig(self.home_pond_color, fill="#1F5F6E")
            webbrowser.open("https://www.youtube.com/watch?v=i_jiQzoQF5M")

        else:
            # Switch to day (Sun)
            self.f.itemconfig(self.moon_button, fill="#FFD84D")
            self.f.config(bg="#FFD6A5")
            self.f.itemconfig(self.f.sun_text, state="normal")
            self.f.itemconfig(self.f.moon_text, state="hidden")
            webbrowser.open("https://www.youtube.com/watch?v=B-b4XvuQo1Y")
            self.f.itemconfig(self.home_pond_color, fill="lightblue")
        self.is_sun = not self.is_sun

    def home_road(self):
        # Road
        self.tilt = 150 # for slant
        self.door_center_x = (self.dw1 + self.dw2) / 2
        self.road_width = 120
        self.road_w1 = self.dw1 - 150
        self.road_h1 = self.dh2
        self.road_w2 = self.dw2 - 150
        self.road_h2 = self.f.winfo_height() - 150
        self.f.create_polygon(self.road_w1 + self.tilt, self.road_h1,self.road_w2 + self.tilt,
                              self.road_h1,self.road_w2, self.road_h2,self.road_w1, self.road_h2,fill="#8D6E63",
                              outline="black",width=1) #warm stone brown

    def home_bushes(self):
        #making bushes
        self.canvas_bush_w = self.f.winfo_width()
        self.canvas_bush_h = self.f.winfo_height()
        self.bush_width = self.canvas_bush_w * 1
        self.bush_height = self.canvas_bush_h * 1
        self.bush_w1 = self.canvas_bush_w - self.bush_width
        self.bush_h1 = self.canvas_bush_h -100
        self.bush_w2 =  self.canvas_bush_w - self.bush_width + 150 #bush_width
        self.bush_h2 =  self.h2 - 140
        #for i in range(3):
        for i in range(6):
            self.f.create_arc(self.bush_w1, self.bush_h1 - 50, self.bush_w2, self.bush_h2 + 50, start=0, extent=180, fill='#2E7D32') #Natural Garden Green
            self.bush_w1 = self.bush_w1 + 150
            self.bush_w2 = self.bush_w2 + 150
        self.bush_w1_half = (self.canvas_bush_w - self.bush_width) + 900
        self.bush_w2_half  = (self.canvas_bush_w - self.bush_width + 150) + 910  # bush_width
        self.f.create_arc(self.bush_w1_half, self.bush_h1 - 50, self.bush_w2_half, self.bush_h2 + 50, start=180, extent=-90, fill='#2E7D32') #Natural Garden Green
        self.bush_w1_right_half = (self.canvas_bush_w - self.bush_width) + 1215
        self.bush_w2_right_half = (self.canvas_bush_w - self.bush_width + 150) + 1215  # bush_width
        self.f.create_arc(self.bush_w1_right_half, self.bush_h1- 50, self.bush_w2_right_half, self.bush_h2 + 50, start=0, extent=90, fill='#2E7D32') #Natural Garden Green
        self.bush_w1_right_half1 = self.bush_w1_right_half + 150
        self.bush_w2_right_half1 = self.bush_w2_right_half + 150
        for i in range(2):
            self.f.create_arc(self.bush_w1_right_half1, self.bush_h1- 50, self.bush_w2_right_half1, self.bush_h2 + 50, start=0, extent=180, fill='#2E7D32') #Natural Garden Green
            self.bush_w1_right_half1 = self.bush_w1_right_half1 + 150
            self.bush_w2_right_half1 = self.bush_w2_right_half1 + 150

    def home_pond(self):
        #making pond
        self.canvas_pond_w = self.f.winfo_width()
        self.canvas_pond_h = self.f.winfo_height()
        self.pond_width = self.canvas_pond_w * 1
        self.pond_height = self.canvas_pond_h * 1
        self.pond_w1 = self.canvas_pond_w - self.pond_width + 250
        self.pond_h1 = self.canvas_pond_h - self.pond_height + 650
        self.pond_w2 = self.canvas_pond_w - self.pond_width + 600
        self.pond_h2 = self.f.winfo_height() - 80
        self.home_pond_color = self.f.create_oval(self.pond_w1,self.pond_h1,self.pond_w2,
                                                  self.pond_h2,fill='lightblue',outline="black",width=1)
        self.f.pond_text = self.f.create_text((self.pond_w1 + self.pond_w2) / 2, (self.pond_h1 + self.pond_h2) / 2,
                                              text="Pond", fill="Black",
                                              font=("Arial", 15, "bold"))
        self.f.tag_bind(self.home_pond_color, "<Button-1>", self.on_pond_click)
        self.f.tag_bind(self.home_pond_color, "<Button-3>", self.on_pond_click)
        self.f.tag_bind(self.f.pond_text, "<Button-1>", self.on_pond_click)
        self.f.tag_bind(self.f.pond_text, "<Button-3>", self.on_pond_click)

    def on_pond_click(self, event):
        webbrowser.open("https://www.youtube.com/watch?v=wT538Nn5HKA")
root = tk.Tk()
mb = SweetHome(root)
root.mainloop()
