import sys
if len(sys.argv) == 2:
    if sys.argv[1] == "-c":
        def commandLine():
            def dostonix(s):
                l = []
                g = ""
                for i in range(len(s)):
                    l.append(s[i])
                    if l[i] == "\\":
                        l[i] = "/"
                    g += str(l[i])
                g = "\"{}\"".format(g)
                return g
            def nixtodos(s):
                l = []
                g = ""
                for i in range(len(s)):
                    l.append(s[i])
                    if l[i] == "/":
                        l[i] = "\\"
                    g += str(l[i])
                g = "\"{}\"".format(g)
                return g
            f = input("dos or nix: ")
            s = input("File path: ")
            if f == "dos":
                print("Formatted filepath:\t" + dostonix(s))
            elif f == "nix":
                print("Formatted filepath:\t" + nixtodos(s))
            else:
                print("ERROR: Unsupported filepath format.")
        commandLine()

else:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *

    class MainWindow(QMainWindow):
        def __init__(self, *args, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)
            self.setWindowTitle("Filepath Converter")
            self.setGeometry(100, 100, 800, 80)
            layout = QGridLayout()
            '''l1 = QLabel("Filepath:")
            layout.addWidget(l1, 0, 0)
            l2 = QLabel("Formatted Filepath:")
            layout.addWidget(l2, 0, 2)'''
            self.e1 = QLineEdit()
            self.e1.setPlaceholderText("Old Filepath")
            layout.addWidget(self.e1, 0, 0)
            self.e2 = QLineEdit()
            self.e2.setPlaceholderText("Formatted Filepath")
            layout.addWidget(self.e2, 0, 2)
            self.cb = QComboBox()
            self.cb.addItems(["dos", "unix"])
            layout.addWidget(self.cb, 0, 1)
            self.b1 = QPushButton("Format")
            #b1.toggle()
            self.b1.clicked.connect(lambda: self.format_filepath())
            layout.addWidget(self.b1, 0, 3)
            widg = QWidget()
            widg.setLayout(layout)
            self.setCentralWidget(widg)
        def format_filepath(self):
            fp = self.e1.text()
            osname = self.cb.currentIndex()
            l = []
            g = ""
            if osname == 0:
                for i in range(len(fp)):
                    l.append(fp[i])
                    if l[i] == "\\":
                        l[i] = "/"
                    g += str(l[i])
            elif osname == 1:
                for i in range(len(fp)):
                    l.append(fp[i])
                    if l[i] == "/":
                        l[i] = "\\"
                    g += str(l[i])
            g = "\"{}\"".format(g)
            self.e2.setText(g)
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
