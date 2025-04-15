import gi,webbrowser as browser
gi.require_version("Gtk","3.0")
from gi.repository import GdkPixbuf,Gtk as gtk

class Origin(gtk.Window):

    def __init__(self):
        # call super() function
        super().__init__(title = "Origin GTK UI")
        self.set_border_width(10)
        #containing box
        box = gtk.Box(orientation = gtk.Orientation.VERTICAL, spacing = 10)
        #label wiget
        label = gtk.Label(label = "This your mans?")
        box.add(label)
        #image
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("diddy.jpg",300,200,True)
        diddy = gtk.Image.new_from_pixbuf(pixbuf)
        box.add(diddy)
        #button wideget
        button = gtk.Button(label = "Touch Me or I will Touch You")
        button.connect("clicked", self.buttonclick)
        box.add(button)
        self.add(box)

    def buttonclick(self,widget):
        browser.open("https://www.google.com/search?q=baby+oil")

window = Origin()
window.connect("destroy", gtk.main_quit)
window.show_all()
gtk.main()
