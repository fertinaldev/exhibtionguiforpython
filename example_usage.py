from exhibition_theme import create_exhibition_theme

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

if __name__ == '__main__':
    window, app = create_exhibition_theme()
    setup_tabs(window)
    window.show()
    app.exec_()