import os

import subprocess

print("PiSpeedtest Automatic Setup 1.0 (released with PiSpeedtest 2.0)")


with open("languageconfiguration.txt") as languageconfigurationsfile:
    languageconfigurationsfilecontent = languageconfigurationsfile.read().splitlines()
    languageconfiguration = languageconfigurationsfilecontent[1]


#Language configuarations
if languageconfiguration == "sv-se":
    notwindowsos = "Du har inte Windows som operativsystem. Installeraren är tyvärr endast kompatibel med Windows i nuläget."

    installcomplete = "PiSpeedtest har nu installerats. Röd text innebär att något inte fungerade under installationen. Om du inte fick någon röd text så innebär det med största sannolikhet att PiSpeedtest har installerats korrekt."
elif languageconfiguration == "en-us":
    notwindowsos = "Your operating system is not Windows. The setup program is only compatible with Windows at the moment."

    installcomplete = "PiSpeedtest has now been installed. Any red text means that the installation failed. If you didn´t get any red text, it most likely means that PiSpeedtest´s requirements has been installed properly."
else:
    notwindowsos = "The current language configuration is somehow invalid."

    installcomplete = "The current language configuration is somehow invalid."
if os.name == "nt":
    updatepipcode = subprocess.Popen(["python -m pip"], shell=True)
    installcode1 = subprocess.Popen(["pip install speedtest-cli"], shell=True)
    installcode2 = subprocess.call(["pip install beautifulsoup4"], shell=True)

    print(installcomplete)
else:
    print(notwindowsos)
