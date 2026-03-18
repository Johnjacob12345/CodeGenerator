import customtkinter as ctk

# Create TabList
shooterTabs = []
climberTabs = []

# Initialize the CustomTkinter theme
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Create the main application window
app = ctk.CTk()
app.title("FRC Code Generator")
app.geometry("800x700")

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
settings_label = ctk.CTkLabel(
    tabview.tab("Settings"), text="Adjust your settings here."
)
settings_label.pack(pady=10)

# Add widgets to the "About" tab
about_label = ctk.CTkLabel(
    tabview.tab("About"),
    text="Made by Banyan for the 2026 FRC season to help teams generate code in java for their robots.",
)
about_label.pack(pady=10)






def newShooterTab():
    shooterTabs.append("Shooter" + str(len(shooterTabs)))
    tabview.add("Shooter" + str(len(shooterTabs)))
    motorTypeEntry("Shooter" + str(len(shooterTabs)))
    portEntry("Shooter" + str(len(shooterTabs)))
    SpeedEntry("Shooter" + str(len(shooterTabs)))
    new_tab_label = ctk.CTkLabel(
        tabview.tab("Shooter" + str(len(shooterTabs))), text="Shooter Tab Content"
    )
    new_tab_label.pack(pady=10)


def newClimberTab():
    climberTabs.append("Climber" + str(len(climberTabs)))
    tabview.add("Climber" + str(len(climberTabs)))
    motorTypeEntry("Climber" + str(len(climberTabs)))
    portEntry("Climber" + str(len(climberTabs)))
    climberTopEntry(len(climberTabs))
    climberBottomEntry(len(climberTabs))
    new_tab_label = ctk.CTkLabel(tabview.tab("Climber" + str(len(climberTabs))), text="Climber Tab Content")
    new_tab_label.pack(pady=10)


def newDriveTab():
    tabview.add("Drive")
    new_tab_label = ctk.CTkLabel(tabview.tab("Drive"), text="Drive Tab Content")
    new_tab_label.pack(pady=10)

def newVisionTab():
    tabview.add("Vision")
    new_tab_label = ctk.CTkLabel(tabview.tab("Vision"), text="Vision Tab Content")
    new_tab_label.pack(pady=10)

def newIntakeTab():
    tabview.add("Intake")
    new_tab_label = ctk.CTkLabel(tabview.tab("Intake"), text="Intake Tab Content")
    new_tab_label.pack(pady=10)

def newAgitatorTab():
    tabview.add("Agitator")
    new_tab_label = ctk.CTkLabel(tabview.tab("Agitator"), text="Agitator Tab Content")
    new_tab_label.pack(pady=10)


def gererateCode():
    print("Generating code...")


def climberTopEntry(climberNum):
    entry = ctk.CTkEntry(
        tabview.tab("Climber" + str(climberNum)), placeholder_text="Top Position"
    )
    entry.pack(pady=10)


def climberBottomEntry(climberNum):
    entry = ctk.CTkEntry(
        tabview.tab("Climber" + str(climberNum)), placeholder_text="Bottom Position"
    )
    entry.pack(pady=10)


def portEntry(tabName):
    entry = ctk.CTkEntry(tabview.tab(tabName), placeholder_text="Port Number")
    entry.pack(pady=10)


def motorTypeEntry(tabName):
    # Create a ComboBox
    combo_values = ["Kraken", "Neo", "Sim"]

    combobox = ctk.CTkComboBox(
        master=tabview.tab(tabName),  # Place it on the specified tab
        values=combo_values,
        width=200,
    )
    combobox.pack(pady=20)

    # Set default value
    combobox.set("Neo")

    # Function to handle selection
    def on_select(choice):
        print(f"Selected: {choice}")

    # Bind selection event
    combobox.bind("<<ComboboxSelected>>", lambda event: on_select(combobox.get()))

def SpeedEntry(tabName):
    entry = ctk.CTkEntry(tabview.tab(tabName), placeholder_text="Speed(RPM)")
    entry.pack(pady=10)



# Create a button on home tab
button_NewShooter = ctk.CTkButton(
    master=tabview.tab("Home"),  # Parent is the Home frame
    text="New Shooter",
    command=newShooterTab,
)
button_NewShooter.pack(pady=20)

button_NewClimber = ctk.CTkButton(
    master=tabview.tab("Home"), text="New Climber", command=newClimberTab
)
button_NewClimber.pack(pady=20)

button_NewDrive = ctk.CTkButton(
    master=tabview.tab("Home"), text="New Drive", command=newDriveTab
)
button_NewDrive.pack(pady=20)

button_NewVision = ctk.CTkButton(
    master=tabview.tab("Home"), text="New Vision", command=newVisionTab
)
button_NewVision.pack(pady=20)

button_NewIntake = ctk.CTkButton(
    master=tabview.tab("Home"), text="New Intake", command=newIntakeTab
)
button_NewIntake.pack(pady=20)

button_NewAgitator = ctk.CTkButton(
    master=tabview.tab("Home"), text="New Agitator", command=newAgitatorTab
)
button_NewAgitator.pack(pady=20)

button_Generate = ctk.CTkButton(
    master=tabview.tab("Home"), text="Generate Code", command=gererateCode
)
button_Generate.pack(pady=20)


# Run the application
app.mainloop()
