import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QLabel, qApp
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
# import Image




class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        # Allowing usage of image in other functions
        self.use_image = QLabel()

        # Placing image in main window
        self.setCentralWidget(self.use_image)

        self.init_ui()

    def init_ui(self):

        # Create Menu Bar
        bar = self.menuBar()

        # Create Root Menus
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # Create Actions for menus
        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction('Save as', self)
        save_action.setShortcut('Ctrl+S')

        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('Ctrl+Q')

        blur_action = QAction('Blur', self)

        noise_action = QAction('Noise', self)

        zoomin_action = QAction('Zoom in', self)
        zoomin_action.setShortcut('Ctrl+=')

        zoomout_action = QAction('Zoom out', self)
        zoomout_action.setShortcut('Ctrl+-')

        # Add actions to Menus
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(quit_action)


        filters_menu = edit.addMenu('Filters')
        filters_menu.addAction(blur_action)
        filters_menu.addAction(noise_action)

        zoom_menu = edit.addMenu('Zoom (Use only if necessary)')
        zoom_menu.addAction(zoomin_action)
        zoom_menu.addAction(zoomout_action)

        # Events
        new_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.selected)

        zoomout_action.triggered.connect(self.zoom_out)
        zoomin_action.triggered.connect(self.zoom_in)


        self.setWindowTitle("Image Processor")
        self.resize(900, 600)

        self.show()
        self.use_image.show()


    def quit_trigger(self):
        qApp.quit()


    def selected(self, q):
        print(q.text() + ' selected')


    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        pixmap = QPixmap(filename)
        width = pixmap.width()
        height = pixmap.height()
        if width > 900 or height > 600:
        	self.use_image.setPixmap(pixmap.scaled(1800, 1200, Qt.KeepAspectRatio, Qt.FastTransformation))
        else:
        	self.use_image.setPixmap(pixmap)
        print("File opened")


    def save_file(self):
        img, _ = QFileDialog.getSaveFileName(self,"Save File", filter="PNG(*.png);; JPEG(*.jpg)")
        if img[-3:] == "png":
            p = self.use_image.grab()
            p.save(img, "png")
        elif img[-3:] == "jpg":
            p = self.use_image.grab()
            p.save(img, "jpg")
        print("File saved")


    # Might need some improvement
    def zoom_out(self):
    	width = self.use_image.width()
    	height = self.use_image.height()
    	p = self.use_image.grab()
    	self.use_image.setPixmap(p.scaled((width - 0.1*width), (height - 0.1*height), Qt.KeepAspectRatio, Qt.SmoothTransformation))


    # Might need some improvement
    def zoom_in(self):
    	width = self.use_image.width()
    	height = self.use_image.height()
    	p = self.use_image.grab()
    	self.use_image.setPixmap(p.scaled((width + 0.1*width), (height + 0.1*height), Qt.KeepAspectRatio, Qt.SmoothTransformation))


app = QApplication(sys.argv)
image_processor = Window()
sys.exit(app.exec_())