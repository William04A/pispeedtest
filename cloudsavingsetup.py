import requests
from bs4 import BeautifulSoup
import sys

from utilities.sharedcode import currentversion
import datetime

import os
import shutil
from subprocess import DEVNULL, Popen

import time

currentversion.getfileversionnumber()
currentversionnumber = currentversion.getfileversionnumber.versionnumber
print("PiSpeedtest Update Checker 1.0")

print("PLEASE NOTE: This code is in BETA and only available in English at the moment.")
#Defining the main updating code:
def update():
    print("Okay, initializing update.")
    print("----------------------------------------------------------")
    print("DON´T WORRY, ALL YOUR DATA AND OLD VERSIONS WILL BE SAVED!")
    print("----------------------------------------------------------")
    print(str(datetime.datetime.now().ctime()) + ": " + "Starting update...")
    print(str(datetime.datetime.now().ctime()) + ": " + "Creating a new folder for the update...")
    directoryname = "PiSpeedtest_update_" + str(latestversionnumber)
    os.mkdir(directoryname)
    print(str(datetime.datetime.now().ctime()) + ": " + "Created directory \"" + directoryname + "\".")
    os.chdir(os.path.join(os.getcwd() + "\\") + directoryname)
    print(str(datetime.datetime.now().ctime()) + ": " + "Successfully changed directory to \"" + str(os.getcwd()) + "\"")
    print(str(datetime.datetime.now().ctime()) + ": " + "Downloading new update...")
    Popen("git clone https://github.com/William04A/pispeedtest.git", shell=True, stderr=DEVNULL, stdout=DEVNULL)
    print(str(datetime.datetime.now().ctime()) + ": " + "Downloaded update successfully.")
    print(str(datetime.datetime.now().ctime()) + ": " + "Waiting to make sure that git has finished copying ", end="",flush=True)
    # Code partly taken from "https://stackoverflow.com/questions/3160699/python-progress-bar", by ChristopheD.
    toolbar_width = 50
    # setup toolbar
    sys.stdout.write("%s" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    for i in range(10):
        sys.stdout.write(".")
        sys.stdout.flush()

        time.sleep(1)
    sys.stdout.write("\n")
    sys.stdout.flush()
    print(str(datetime.datetime.now().ctime()) + ": " + "Copying data from current PiSpeedtest version...")

    print(str(datetime.datetime.now().ctime()) + ": " + "Starting to copy speedtest results...")
    os.chdir(os.path.dirname(os.getcwd()))
    directorycontents_speedtestresults = os.listdir(os.path.join(os.getcwd() + "\\speedtestresults"))
    for a in range(len(directorycontents_speedtestresults)):
        shutil.copy(os.path.join(os.getcwd() + "\\speedtestresults\\" + directorycontents_speedtestresults[a]), os.path.join(os.getcwd() + "\\" + directoryname + "\\pispeedtest\\speedtestresults"))
        sys.stdout.write("\r" + str(datetime.datetime.now().ctime()) + ": " + "Moving file " + str(a + 1) + "/" + str(len(directorycontents_speedtestresults)) + " (speedtest results)")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")
    print(str(datetime.datetime.now().ctime()) + ": " + "Successfully copied speedtest results.")
    print(str(datetime.datetime.now().ctime()) + ": " + "Starting to copy speedtest reports...")
    directorycontents_speedtestreports = os.listdir(os.path.join(os.getcwd() + "\\speedtestreports"))
    for b in range(len(directorycontents_speedtestreports)):
        shutil.copy(os.path.join(os.getcwd() + "\\speedtestreports\\" + directorycontents_speedtestreports[b]), os.path.join(os.getcwd() + "\\" + directoryname + "\\pispeedtest\\speedtestreports"))
        sys.stdout.write("\r" + str(datetime.datetime.now().ctime()) + ": " + "Moving file " + str(b + 1) + "/" + str(
            len(directorycontents_speedtestreports)) + " (speedtest reports)")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")
    print(str(datetime.datetime.now().ctime()) + ": " + "Successfully copied speedtest reports.")
    print(str(datetime.datetime.now().ctime()) + ": " + "Copying language configuration...")
    with open(os.path.join(os.getcwd() + "\\configurationfiles\\languageconfiguration.txt"),"r") as languageconfigurationfile:
        currentlanguageconfiguration = languageconfigurationfile.read().splitlines()[1]
    with open(os.path.join(os.getcwd() + "\\" + directoryname + "\\pispeedtest\\configurationfiles\\languageconfiguration.txt"), "w") as languageconfigurationfile_new:
        languageconfigurationfile_new.truncate()
        languageconfigurationfile_new.write("This is the language configuration file for the application PiSpeedtest.")
        languageconfigurationfile_new.write(currentlanguageconfiguration)
    print(str(datetime.datetime.now().ctime()) + ": " + "Succefully copied language configuration file.")
    print(str(datetime.datetime.now().ctime()) + ": " + "Copying cloudsaving configuration files...")
    print(str(datetime.datetime.now().ctime()) + ": " + "Copying cloudsaving API key.")
    with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as pispeedtestcloudsavingapikeyfile:
        currentcloudsavingapikey = pispeedtestcloudsavingapikeyfile.read().splitlines()[1]

    with open(os.path.join(os.getcwd() + "\\" + directoryname + "\\pispeedtest\\" + "\\cloudsaving\\savedata\\apikey.txt"), "w") as pispeedtestcloudsavingapikeyfile_new:
        pispeedtestcloudsavingapikeyfile_new.truncate()
        pispeedtestcloudsavingapikeyfile_new.write("Please do not modify this file! It contains an API-key for cloud-saving speedtests made with the application PiSpeedtest. (Swedish: Modifiera inte denna fil, tack! Den innehåller din API-nyckel för att ladda upp resultat i molnet med PiSpeedtest):"+ "\n")
        pispeedtestcloudsavingapikeyfile_new.write(currentcloudsavingapikey)

        pispeedtestcloudsavingapikeyfile_new.write("\n")
    print(str(datetime.datetime.now().ctime()) + ": " + "Successfully copied PiSpeedtest cloudsaving API key.")
    print(str(datetime.datetime.now().ctime()) + ": " + "Copying cloudsaving status...")
    with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\status.txt"),"r") as pispeedtestcloudsavingstatusfile:
        currentcloudsavingstatus = pispeedtestcloudsavingstatusfile.read().splitlines()[0]
    with open(os.path.join(os.getcwd() + "\\" + directoryname + "\\pispeedtest\\cloudsaving\\savedata\\status.txt"),"w") as pispeedtestcloudsavingstatusfile_new:
        pispeedtestcloudsavingstatusfile_new.truncate()
        pispeedtestcloudsavingstatusfile_new.write(currentcloudsavingstatus + "\n")
    print(str(datetime.datetime.now().ctime()) + ": " + "The PiSpeedtest cliydsaving status has been successfully copied.")
    print(str(datetime.datetime.now().ctime()) + ": " + "NOTICE: Please note that the file \"config.txt\" has to be copied manually as you have to check that it is compatible with the PiSpeedtest version that you update to.")
    print(str(datetime.datetime.now().ctime()) + ": " + "Copying speedtest result images...")

    directorycontents_speedtestresultsimages = os.listdir(os.path.join(os.getcwd() + "\\images\\speedtestresultimages"))
    for c in range(len(directorycontents_speedtestresultsimages)):
        shutil.copy(os.path.join(os.getcwd() + "\\images\\speedtestresultimages\\" + directorycontents_speedtestresultsimages[c]), os.path.join(os.getcwd() + "\\" + directoryname + "\\pispeedtest\\images\\speedtestresultimage"))
        sys.stdout.write("\r" + str(datetime.datetime.now().ctime()) + ": " + "Moving file " + str(c + 1) + "/" + str(len(directorycontents_speedtestresultsimages)) + " (speedtest result images)")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")

    print(str(datetime.datetime.now().ctime()) + ": " + "Update finished!")
sys.stdout.write("Contacting update server... Initializing")

updatecheck = requests.get("https://pispeedtestfiles.000webhostapp.com/latestversion.html")
sys.stdout.write("\b" * 12 + "Getting latest version...")
sys.stdout.flush()
soup = BeautifulSoup(updatecheck.text, "html.parser")


latestversionnumber = str(soup.get_text()).replace("\n", "")
sys.stdout.write("\b" * 25 + "Retrieved latest version (4.0).")

sys.stdout.flush()

print("\n")
if float(latestversionnumber) == float(currentversionnumber):

    print("There isn´t an update available for PiSpeedtest right now.")

elif float(latestversionnumber) > float(currentversionnumber):
    print("Found an update for PiSpeedtest (" + str(latestversionnumber) + ")")
    updatequestion = input("Would you like to update PiSpeedtest? YES or NO: ")
    if updatequestion.capitalize() == "Yes":
       update()
    elif updatequestion.capitalize() == "No":
        print("Okay, an update will not be performed.")
    else:
        print("Could not understand your option.")
else:
    print("It seems like you are running a beta version of PiSpeedtest. There isn´t an update available. ")


    lateststableversioninput = input("To downgrade to the previous stable version of PiSpeedtest, type \"UPDATE\". Otherwise, just press enter to exit PiSpeedtest. ")
    if lateststableversioninput.capitalize() == "Update":

        print("Okay, initializing setup.")
        update()
    else:
        print("Okay, closing the PiSpeedtest update program in ten seconds.")

        time.sleep(10)
        exit()
