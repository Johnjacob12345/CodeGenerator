import customtkinter as ctk

#Create TabList
shooterTabs = []
climberTabs = []

# Initialize the CustomTkinter theme
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Create the main application window
app = ctk.CTk()
app.title("CustomTkinter Tabs Example")
app.geometry("1000x600")

# Create a Tabview widget
tabview = ctk.CTkTabview(app, width=480, height=250, corner_radius=10)
tabview.pack(padx=20, pady=20, fill="both", expand=True)

# Add tabs
tabview.add("Home")
tabview.add("Settings")
tabview.add("About")

# Optionally set the default selected tab
tabview.set("Home")

# Add widgets to the "Home" tab
home_label = ctk.CTkLabel(tabview.tab("Home"), text="Welcome!")
home_label.pack(pady=10)

# Add widgets to the "Settings" tab
settings_label = ctk.CTkLabel(tabview.tab("Settings"), text="Adjust your settings here.")
settings_label.pack(pady=10)

# Add widgets to the "About" tab
about_label = ctk.CTkLabel(tabview.tab("About"), text="This is a CustomTkinter Tabview example.")
about_label.pack(pady=10)



def newShooterTab():
    shooterTabs.append("Shooter" + str(len(shooterTabs)))
    tabview.add("Shooter" + str(len(shooterTabs)))
    new_tab_label = ctk.CTkLabel(tabview.tab("Shooter"), text="Shooter Tab Content")
    new_tab_label.pack(pady=10)

def newClimberTab():
    climberTabs.append("Climber" + str(len(climberTabs)))
    tabview.add("Climber" + str(len(climberTabs)))
    new_tab_label = ctk.CTkLabel(tabview.tab("Climber"), text="Climber Tab Content")
    new_tab_label.pack(pady=10)

def newDriveTab():
    tabview.add("Drive")
    new_tab_label = ctk.CTkLabel(tabview.tab("Drive"), text="Drive Tab Content")
    new_tab_label.pack(pady=10)

def gererateCode():
    print("Generating code...")




# Create a button on home tab
button_NewShooter = ctk.CTkButton(
    master=tabview.tab("Home"),  # Parent is the Home frame
    text="New Shooter",
    command=newShooterTab
)
button_NewShooter.pack(pady=20)

button_NewClimber = ctk.CTkButton(
    master=tabview.tab("Home"),
    text="New Climber",
    command=newClimberTab
)
button_NewClimber.pack(pady=20)

button_NewDrive = ctk.CTkButton(
    master=tabview.tab("Home"),
    text="New Drive",
    command=newDriveTab
)
button_NewDrive.pack(pady=20)

button_Generate = ctk.CTkButton(
    master=tabview.tab("Home"),
    text="Generate Code",
    command=gererateCode
)
button_Generate.pack(pady=20)

# Run the application
app.mainloop()
