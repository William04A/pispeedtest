import os

import pip._internal

print("PiSpeedtest Automatic Setup 2.0 (released with PiSpeedtest 3.5)")


with open(os.path.join(os.getcwd() + "\\configurationfiles\\" + "languageconfiguration.txt"), "r+") as languageconfigurationsfile:
    languageconfigurationsfilecontent = languageconfigurationsfile.read().splitlines()
    languageconfiguration = languageconfigurationsfilecontent[1]


#Language configuarations

if languageconfiguration == "sv-se":
    notwindowsos = "Du har inte Windows som operativsystem. Installeraren är tyvärr endast kompatibel med Windows i nuläget."

    installcomplete = "PiSpeedtest har nu installerats. Röd text innebär att något inte fungerade under installationen. Om du inte fick någon röd text så innebär det med största sannolikhet att PiSpeedtest har installerats korrekt."
    pipupgradeinformationmessage = "\"pip\" (Python Pakethanterare) kommer att uppdateras. Vill du skippa det (rekommenderas ej)?  Nuvarande pip-version: "
    installquestionmessage = "Skriv \"YES\" för att fortsätta eller skriv någonting annat för att skippa \"pip\"-uppdateringen: "
elif languageconfiguration == "en-us":
    notwindowsos = "Your operating system is not Windows. The setup program is only compatible with Windows at the moment."

    installcomplete = "PiSpeedtest has now been installed. Any red text means that the installation failed. If you didn´t get any red text, it most likely means that PiSpeedtest´s requirements has been installed properly."
    pipupgradeinformationmessage = "Your \"pip\" (Python Package List) will be updated. Do you want to skip that (not recommended)?  Current pip version: "
    installquestionmessage = "Type \"YES\" to continue or type anything else to skip the pip update: "
else:
    notwindowsos = "The current language configuration is somehow invalid."

    installcomplete = "The current language configuration is somehow invalid."

    pipupgradeinformationmessage = "The current language conifguration is somehow invalid."

    installquestionmessage = "The current language configuration is somehow invalid."
print(pipupgradeinformationmessage + str(pip.__version__) + ".")
installquestion = input(installquestionmessage)

if installquestion == "yes" or installquestion == "YES":
    pip._internal.main(["install", "--upgrade", "pip"])
else:
    print("\n")
print("\n" + "Please wait... (0% installed)")
pip._internal.main(["install", "speedtest-cli"])
print("\n" + "Please wait... (33% installed)")
pip._internal.main(["install", "beautifulsoup4"])
print("\n" + "Please wait... (66% installed)")
pip._internal.main(["install", "requests"])
print("\n" + "Please wait... (100% installed)")

print(installcomplete)
