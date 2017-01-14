# WORK IN PROGRESS

import tkinter as tk
import sys
import NatGeo_PhotoOfTheDay as natgeo

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        toolbar = tk.Frame(self)
        toolbar.pack(side="top", fill="x")
        b1 = tk.Button(self, text="Get natgeo img", command=natgeo.main)
        b1.pack(in_=toolbar, side="left")
        b2 = tk.Button(self, text="quit", command=self.destroy)
        b2.pack(in_=toolbar, side="left")
        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)

        sys.stdout = TextRedirector(self.text)

class TextRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str)
        self.widget.configure(state="disabled")

    def flush(self):
        pass

app = ExampleApp()
app.mainloop()

