import speedtest

import time

import datetime
import requests


downloadlist = []
uploadlist = []
pinglist = []
filename = "speedtestdata_date:" + str(datetime.datetime.now().day) + ".txt"

smallestkbitsup = 1000
largestkbitsup = 0
smallestkbitsdown = 1000
largestkbitsdown = 0
noconnection = 0
approved_languages = ["sv-se", "en-us"]
with open("languageconfiguration.txt", "r+") as languagecofigurationfile:
    languageconfig = languagecofigurationfile.read().splitlines()
if languageconfig[1] not in approved_languages:
    print("The current language configuration is not valid. Please check the file languageconfiguration.txt. Valid languages are:")
    for i in range(len(approved_languages)):
        print(approved_languages[i])
    languageconfiguration = "sv-se"
    print("For this time, the language has been set to sv-se, Swedish.")
else:
    print("Language configuration " + str(languageconfig[1]) + " found.")
    languageconfiguration = languageconfig[1]
def processpeedtest(backupmode, filename):
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    results = s.results.dict()
    resultlist = list(results.values())
    download = str(round(resultlist[0]/1000000)) + " mbit/s"
    upload = str(round(resultlist[1]/1000000)) + " mbit/s"
    ping = str(resultlist[2]) + "ms"
    downloadlist.append(download)
    uploadlist.append(upload)
    pinglist.append(ping)
    fullresults = "Results: " + " Download: " + download + " Upload: " + upload + " Ping: " + ping + "."
    print(fullresults)
    if backupmode == False:
        with open(filename, "w") as file:
            file.close()
        with open(filename, "a+") as file:
            file.write(fullresults + "\n")
    elif backupmode == True:
        with open("speedtestbackup.txt") as backupfile:
            backupfile.write(fullresults + "\n")
if languageconfiguration == "sv-se":
    try:
        request = requests.get("https://www.google.com")
        print("Pre-test-resultat: " + " Ping till https://www.google.com. Resultat: " + str(request.elapsed.total_seconds()) + " sekunder.")
    except requests.exceptions.ConnectionError:
        print("En aktiv internetuppkoppling kunde ej hittas.")

        noconnection = 1

    print("För att få programmet att fungera optimalt så körs ett \"speedtest\" för att mäta tid m.m. Vänligen vänta.")
    timeone = time.time()
    if noconnection == 0:
        processpeedtest(0, filename="initialspeedtests.txt")
    elif noconnection == 1:
        print("En aktiv internetuppkoppling kunde ej hittas.")
    speedtesttime = round(time.time() - timeone)
    print("Ett speedtest har nu körts. Det tog: " + str(speedtesttime) + " sekunder.")

    print("Programlägen:")
    print("BETA MODE - Betafunktioner som kan innehålla buggar.")
    print("STABLE - Kör de stabila funktionerna i PiSpeedtest.")
    print("COMPATIBLE - Välj detta lägeför kompatibilitet med Mac, vissa Linuxsystem eller andra system än Windows.")
    mode = input("Vänligen välj ett läge genom att skriva dess namn och trycka på enter: ")
    if mode == "BETA MODE":
        import ctypes
        times = int(input("Hur länge vill du köra programmet? (I sekunder) 12 timmar = 43 200 sekunder: "))
        interval = int(input("Hur ofta vill du köra programmet (i sekunder)? Ett \"speedtest\" tar cirka " + str(speedtesttime) + "sekunder. "))
        inputfilename = str(input("Vilket namn vill du ha på speedtestfilen? Lägg till \".txt\"! Använd inte filnamn du redan använt! "))
        repeat = round(times/(interval-speedtesttime))
        ctypes.windll.user32.MessageBoxW(None, "Ett speedtest startas.", "PiSpeedtest", 0)
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:
                    print("Startar test.")
                    processpeedtest(0, filename=inputfilename)
                    print("Test utfört.")
                    time.sleep(interval-speedtesttime)
                except:
                    ctypes.windll.user32.MessageBoxW(None, "Ett fel inträffade när ett speedtest skulle köras.", "PiSpeedtest", 0)

                    print("Ett fel inträffade.")

                    #This is being added in a later release:
                    #box = ctypes.windll.user32.MessageBoxW(None, "An error occured while running a speedtest. Would you like to try again? Everything will restart. The file with new speedtest data will be namned \"speedtestbackup.txt\".", "PiSpeedtest", 5)
                    #if box == 1:
                        #print("Kör speedtest igen.")
                        #for speedtestindex in range(repeat):

                            #print("A speedtest is being started.")
                            #processpeedtest(0, filename="speedtestbackup.txt")
                            #print("A speedtest has been completed.")
                            #time.sleep(interval)
                    #elif box == 2:
                        #print("Quitting PiSpeedtest because of an error.")
                    #else:
                        #print("Quitting PiSpeedtest because of an error.")
        else:
            print("En aktiv internetuppkoppling kunde ej hittas.")
    elif mode == "STABLE":
        import ctypes
        times = int(input("Hur länge vill du köra programmet? (I sekunder) 12 timmar = 43 200 sekunder: "))
        interval = int(input("Hur länge vill du vänta mellan varje speedtest (i sekunder)? "))
        inputfilename = str(input("Vilket namn vill du ha på speedtestfilen? Lägg till \".txt\"! Använd inte filnamn du redan använt! "))
        repeat = round(times)
        ctypes.windll.user32.MessageBoxW(None, "Ett speedtest har nu startats.", "PiSpeedtest", 0)
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:
                    print("Startar test.")
                    processpeedtest(0, filename=inputfilename)
                    print("Test utfört.")
                    time.sleep(interval)
                except:
                    print("Ett fel inträffade.")
                    ctypes.windll.user32.MessageBoxW(None, "Ett fel inträffade när ett speedtest skulle köras.", "PiSpeedtest", 0)

        else:
            print("En aktiv internetuppkoppling kunde ej hittas.")
    elif mode == "COMPATIBLE":
        times = int(input("Hur länge vill du köra programmet? (I sekunder) 12 timmar = 43 200 sekunder: "))
        interval = int(input("Hur länge vill du vänta mellan varje speedtest (i sekunder)? "))
        inputfilename = str(input("Vilket namn vill du ha på speedtestfilen? Lägg till \".txt\"!"))
        repeat = round(times)
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:
                    print("Startar test.")
                    processpeedtest(0 , inputfilename)
                    print("Test utfört.")
                    time.sleep(interval)
                except:
                    print("Ett fel inträffade.")
        else:
            print("En aktiv internetuppkoppling kunde ej hittas.")

elif languageconfiguration == "en-us":
    try:
        request = requests.get("https://www.google.com")
        print("Pre-test-results: " + " Ping to https://www.google.com. Result: " + str(
            request.elapsed.total_seconds()) + " seconds.")
    except requests.exceptions.ConnectionError:
        print("An active internet connection could not be found.")

        noconnection = 1

    print("In order to make the program work properly, a \"speedtest\" has been started to measure time and more. Please wait.")
    timeone = time.time()
    if noconnection == 0:
        processpeedtest(0, filename="initialspeedtests.txt")
    elif noconnection == 1:
        print("An active internet connection could not be established.")
    speedtesttime = round(time.time() - timeone)
    print("A speedtest has now been run. It took " + str(speedtesttime) + " seconds.")

    print("Options:")
    print("BETA MODE - Functions in beta that might not work properly.")
    print("STABLE - Run the stable and tested functions in PiSpeedtest.")
    print("COMPATIBLE - Select this mode for compatibility with more operating systems than Windows, including Mac, some Linux OSes and other operating systems. A stable releasy is being run, not a beta release.")
    mode = input("Please select a mode by typing its name and then pressing enter on your keyboard: ")
    if mode == "BETA MODE":
        import ctypes
        times = int(input("For how long do you want to run the program? (In seconds) 12 hours = 43 200 seconds: "))
        interval = int(input("How long do you want to wait between each speedtest (in seconds)? "))
        inputfilename = str(input("What name would you like to have on the results file? Add \".txt\" at the end of the name and do not reuse old file names! "))
        repeat = round(times / (interval - speedtesttime))
        ctypes.windll.user32.MessageBoxW(None, "A speedtest is being started.", "PiSpeedtest", 0)
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:
                    print("Starting test.")
                    processpeedtest(0, filename=inputfilename)
                    print("A speedtest has been run.")
                    time.sleep(interval - speedtesttime)
                except:
                    ctypes.windll.user32.MessageBoxW(None, "An error occured while running a speedtest.", "PiSpeedtest", 0)

                    print("An error occoured.")

                    # This is being added in a later release:
                    # box = ctypes.windll.user32.MessageBoxW(None, "Ett fel inträffade när ett speedtest skulle köras. Vill du försöka igen? Allt kommer då att börja om från början. Filen med ny speedtestdata kommer att heta \"speedtestbackup.txt\".", "PiSpeedtest", 5)
                    # if box == 1:
                    # print("Kör speedtest igen.")
                    # for speedtestindex in range(repeat):

                    # print("Startar test.")
                    # processpeedtest(0, filename="speedtestbackup.txt")
                    # print("Test utfört.")
                    # time.sleep(interval)
                    # elif box == 2:
                    # print("Avslutar PiSpeedtest eftersom att ett fel inträffade.")
                    # else:
                    # print("Avslutar PiSpeedtest eftersom att ett fel inträffade.")
        else:
            print("An active internet connection could not be established.")
    elif mode == "STABLE":
        import ctypes
        times = int(input("For how long do you want to run the program? (In seconds) 12 hours = 43 200 seconds: "))
        interval = int(input("How long do you want to wait between each speedtest (in seconds)? "))
        inputfilename = str(input("What name would you like to have on the results file? Add \".txt\" at the end of the name and do not reuse old file names! "))
        repeat = round(times)
        ctypes.windll.user32.MessageBoxW(None, "A speedtest has now started.", "PiSpeedtest", 0)
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:
                    print("Starting test.")
                    processpeedtest(0, inputfilename)
                    print("A test has been run.")
                    time.sleep(interval)
                except:
                    print("There was an unexpected error.")
        else:
            print("An active internet connection could not be establised.")
    elif mode == "COMPATIBLE":
        times = int(input("For how long do you want to run the program? (In seconds) 12 hours = 43 200 seconds: "))
        interval = int(input("How long do you want to wait between each speedtest (in seconds)? "))
        inputfilename = str(input("What name would you like to have on the results file? Add \".txt\" at the end of the name and do not reuse old file names! "))
        repeat = round(times)
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:
                    print("Starting test.")
                    processpeedtest(0, inputfilename)
                    print("A test has been run.")
                    time.sleep(interval)
                except:
                    print("There was an unexpected error.")
        else:
            print("An active internet connection could not be establised.")
