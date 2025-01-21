import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QGroupBox, QCheckBox, QSlider, QLabel, QComboBox, QGridLayout,
                             QPushButton, QStackedWidget, QFrame)
from PyQt5.QtGui import QColor, QIcon, QPixmap, QFont, QPainter, QLinearGradient
from PyQt5.QtCore import Qt, QSize, QTimer, QRect, QEvent


class ColorBar(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setFixedHeight(5)
        self.setStyleSheet(f"background-color: {color};")

class CustomSlider(QSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 8px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0e84b5, stop:1 #0e84b5);
                margin: 2px 0;
            }
            QSlider::handle:horizontal {
                background: #0e84b5;
                border: none;
                width: 16px;
                height: 16px;
                margin: -4px 0;
            }
        """)


class RainbowBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(5)
        self.offset = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_gradient)
        self.timer.start(50)  # Her 50 ms'de bir güncelle

    def update_gradient(self):
        self.offset = (self.offset + 1) % 360
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), 0)
        
        for i in range(7):
            color = QColor()
            color.setHsv((self.offset + i * 51) % 360, 255, 255)
            gradient.setColorAt(i / 6, color)
        
        painter.fillRect(self.rect(), gradient)

class ExhibitionTheme(QMainWindow):
    def __init__(self, size=(800, 600)):
        super().__init__()
        self.setGeometry(100, 100, size[0], size[1])
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.tabs = {}
        self.setup_ui()
        self.installEventFilter(self)
        self.hidden = False  # Yeni bir değişken ekleyin



    def setup_ui(self):
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #1e1e1e;
                color: white;
            }
            QGroupBox {
                border: 1px solid #3a3a3a;
                margin-top: 0.5em;
                font-weight: bold;
                font-size: 14px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px 0 3px;
            }
            QCheckBox {
                font-size: 12px;
            }
            QCheckBox::indicator {
                width: 13px;
                height: 13px;
            }
            QLabel {
                font-size: 12px;
            }
            QComboBox {
                background-color: #2a2a2a;
                border: 1px solid #3a3a3a;
                border-radius: 3px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
                font-size: 12px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: #3a3a3a;
                border-left-style: solid;
            }
            QPushButton {
                background-color: transparent;
                border: none;
                padding: 10px;
                icon-size: 48px;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Add rainbow bar at the top
        rainbow_bar = RainbowBar()
        main_layout.addWidget(rainbow_bar)

        # Add a horizontal line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: #3a3a3a;")
        main_layout.addWidget(line)

        content_layout = QHBoxLayout()
        # Left sidebar with buttons
        self.sidebar = QVBoxLayout()
        self.stacked_widget = QStackedWidget()
        content_layout.addLayout(self.sidebar, 1)
        content_layout.addWidget(self.stacked_widget, 4)

        main_layout.addLayout(content_layout)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Insert:
                if self.isVisible():
                    self.hide()
                else:
                    self.show()
                return True
            elif event.key() == Qt.Key_End:
                QApplication.quit()
                return True
        return super().eventFilter(obj, event)




    def add_tab(self, name, icon_path=None):
        button = QPushButton()
        if icon_path:
            icon = QIcon(icon_path)
            button.setIcon(icon)
            button.setIconSize(QSize(48, 48))
        self.sidebar.addWidget(button)
        
        content = QWidget()
        content_layout = QGridLayout(content)
        self.stacked_widget.addWidget(content)
        
        button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(content))
        
        self.tabs[name] = content_layout  # Store the tab layout reference
        return content_layout
    def create_group_box(self, title, checkboxes, sliders=None):
        group_box = QGroupBox(title)
        layout = QGridLayout()

        for i, checkbox_text in enumerate(checkboxes):
            checkbox = QCheckBox(checkbox_text)
            checkbox.setFont(QFont("Segoe UI", 10))
            layout.addWidget(checkbox, i, 0)

        if sliders:
            for i, (slider_text, values) in enumerate(sliders.items()):
                label = QLabel(slider_text)
                label.setFont(QFont("Segoe UI", 10))
                layout.addWidget(label, i, 1)
                if isinstance(values[0], (int, float)):
                    slider = CustomSlider(Qt.Horizontal)
                    min_value, max_value = values[1], values[2]
                    initial_value = values[0]
                    slider.setRange(min_value, max_value)
                    slider.setValue(int(initial_value))
                    layout.addWidget(slider, i, 2)
                    value_label = QLabel(str(initial_value))
                    value_label.setFont(QFont("Segoe UI", 10))
                    value_label.setStyleSheet("color: #0e84b5;")
                    layout.addWidget(value_label, i, 3)
                    
                    # Create a blue bar to represent the slider value
                    blue_bar = QWidget()
                    blue_bar.setStyleSheet("background-color: #0e84b5;")
                    blue_bar.setFixedHeight(5)
                    layout.addWidget(blue_bar, i, 2)
                    
                    # Update the blue bar width and label when the slider value changes
                    def update_blue_bar(value, bar=blue_bar, slider=slider, label=value_label):
                        bar_width = int((value - slider.minimum()) / (slider.maximum() - slider.minimum()) * slider.width())
                        bar.setFixedWidth(bar_width)
                        label.setText(str(value))
                    
                    slider.valueChanged.connect(update_blue_bar)
                    # Initial update of the blue bar
                    update_blue_bar(initial_value)
                else:
                    combo = QComboBox()
                    combo.addItems(values)
                    combo.setFont(QFont("Segoe UI", 10))
                    layout.addWidget(combo, i, 2, 1, 2)

        group_box.setLayout(layout)
        return group_box



# Yeni bir fonksiyon ekleyelim
def setup_tabs(window):
    # Combat tab
    tab1 = window.add_tab("", "C:\\Users\\engin\\Downloads\\pythongui\\com.png")
    tab1.addWidget(window.create_group_box("Criticals", ["Enable", "Hurttime"], {"Mode": ["Packet"]}), 0, 0)
    tab1.addWidget(window.create_group_box("AutoClicker", ["Enable", "Random", "On-mouse"], {"Delay": [100, 50, 500], "Maxrand": [50, 0, 100]}), 0, 1)
    tab1.addWidget(window.create_group_box("AimAssist", ["Enable"], {
        "Weapon": ["Bow"],
        "Fovpitch": [25, 0, 180],
        "Fovyaw": [15, 0, 180],
        "Randomize": [6, 0, 20],
        "Randomyaw": [6, 0, 20],
        "Range": [5, 1, 10],
        "Speed-h": [10, 1, 20],
        "Speed-v": [10, 1, 20]
    }), 1, 0)
    
    tab1.addWidget(window.create_group_box("AutoSoup", ["Enable", "Drop"], {"Delay": [350, 100, 1000], "Health": [3, 1, 10]}), 1, 1)
    tab1.addWidget(window.create_group_box("AntiVelocity", ["Enable", "Horizontal", "Vertical"], {"Horizontal": [0, 0, 100], "Vertical": [0, 0, 100]}), 2, 0)
    tab1.addWidget(window.create_group_box("KillAura", ["Enable", "Armor", "Players", "Teams", "Invisibles", "Death", "Others"], {
        "Fov": [180, 0, 360],
        "Range": [45, 10, 100],
        "Speed": [10, 1, 20],
        "Mode": ["Switch"],
        "Priority": ["Angle"]
    }), 2, 1)
    
    tab1.addWidget(window.create_group_box("AutoPot", ["Enable", "Predict", "Regen", "Overpot"], {"Delay": [350, 100, 1000], "Health": [5, 1, 20]}), 3, 0)
    tab1.addWidget(window.create_group_box("BowAimbot", ["Enable"], {}), 3, 1)
    tab1.addWidget(window.create_group_box("AutoSword", ["Enable"], {}), 3, 2)
    
    # Movement tab
    tab2 = window.add_tab("", "C:\\Users\\engin\\Downloads\\pythongui\\mov.png")
    tab2.addWidget(window.create_group_box("Speed", ["Enable"], {"Mode": ["Ground", "Jump"]}), 0, 0)
    tab2.addWidget(window.create_group_box("Flight", ["Enable"], {"Mode": ["Vanilla", "Glide"]}), 0, 1)
    tab2.addWidget(window.create_group_box("LongJump", ["Enable"], {"Boost": [10, 1, 50]}), 1, 0)
    tab2.addWidget(window.create_group_box("NoFall", ["Enable"], {"Mode": ["Packet", "Ground"]}), 1, 1)

    # Player tab
    tab3 = window.add_tab("", "C:\\Users\\engin\\Downloads\\pythongui\\player.png")
    tab3.addWidget(window.create_group_box("AutoArmor", ["Enable", "OpenInv"], {"Delay": [100, 0, 500]}), 0, 0)
    tab3.addWidget(window.create_group_box("ChestStealer", ["Enable"], {"Delay": [50, 0, 300]}), 0, 1)
    tab3.addWidget(window.create_group_box("InventoryManager", ["Enable"], {"CleanDelay": [100, 0, 500]}), 1, 0)

    # Render tab
    tab4 = window.add_tab("", "C:\\Users\\engin\\Downloads\\pythongui\\render.png")
    tab4.addWidget(window.create_group_box("ESP", ["Enable", "Box", "Tracers", "Nametags"], {"Color": ["Rainbow", "Static"]}), 0, 0)
    tab4.addWidget(window.create_group_box("Chams", ["Enable", "Visible", "Invisible"], {"Color": ["Rainbow", "Static"]}), 0, 1)
    tab4.addWidget(window.create_group_box("FullBright", ["Enable"], {}), 1, 0)

    # Misc tab
    tab5 = window.add_tab("", "C:\\Users\\engin\\Downloads\\pythongui\\misc.png")
    tab5.addWidget(window.create_group_box("AntiBot", ["Enable"], {"Mode": ["Hypixel", "Mineplex"]}), 0, 0)
    tab5.addWidget(window.create_group_box("Disabler", ["Enable"], {"Mode": ["Hypixel", "NCP"]}), 0, 1)
    tab5.addWidget(window.create_group_box("Spammer", ["Enable"], {"Delay": [1000, 100, 5000]}), 1, 0)
    

def create_exhibition_theme(size=(800, 600)):
    app = QApplication(sys.argv)
    window = ExhibitionTheme(size)
    return window, app





    

# Örnek kullanım
if __name__ == '__main__':
    window, app = create_exhibition_theme()
    setup_tabs(window)
    window.show()
    sys.exit(app.exec_())