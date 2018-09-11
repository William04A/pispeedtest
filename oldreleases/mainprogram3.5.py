try:
    import speedtest

    import time


    import os


    # Defining errors - These are not implemented that much yet.
    def __main__():
        pass
    class PiSpeedtestErrors(Exception):
        pass


    class NoModeDefinded(PiSpeedtestErrors):
        pass


    class FileError(PiSpeedtestErrors):
        pass

    class NoInternetConnection(PiSpeedtestErrors):
        pass

    class UpdatecheckServerError(NoInternetConnection):
        pass


    downloadlist = []
    uploadlist = []
    pinglist = []

    smallestkbitsup = 1000
    largestkbitsup = 0
    smallestkbitsdown = 1000
    largestkbitsdown = 0
    noconnection = 0
    fileversionnumber = "3.5"
    allowedmodes = ["BETA MODE", "STABLE", "COMPATIBLE"]
    loadconfig = [0, 0, 0, 0, 0]

    allowedtextlayouts = ["Text", "Plain", "Lists", "Detailed-text", "With-units"]

    fontfilename = "Roboto-Bold.ttf" #Add a custom font filename here if you want a custom font for the images. Don´t forget the file extension! Only .ttf-files supported.
    print("PiSpeedtest " + fileversionnumber + ".")
    # Language settings:
    approved_languages = ["sv-se", "en-us"]  # To add a language that´s not in the list, make sure to add its name here.
    languageconfigpath = os.path.join(os.getcwd() + "/configurationfiles/languageconfiguration.txt")
    try:
        with open(languageconfigpath, "r+") as languagecofigurationfile:
            languageconfig = languagecofigurationfile.read().splitlines()
    except:
        print("Could not find language configuration. Please make sure that \"languageconfiguration.txt\" is in the directory /configurationfiles.")
        languageconfig = ["Configuration not found." + "ConfigurationNotFound"]
    if languageconfig[1] not in approved_languages:
        print("The current language configuration is not valid. Please check the file languageconfiguration.txt. Valid languages are:")
        for i in range(len(approved_languages)):
            print(approved_languages[i])
        languageconfiguration = "sv-se"
        print("For this time, the language has been set to sv-se, Swedish.")
    else:
        print("Language configuration " + str(languageconfig[1]) + " found.")
        languageconfiguration = languageconfig[1]
    print("\n")
    # Language configuration - feel free to add your own languages here!
    if languageconfiguration == "sv-se":
        pretestresults = "Pre-test-resultat: Ping till https://www.google.com. Resultat: "
        pretestresults2 = " sekunder."
        nointernetconnectionmessage = "En aktiv internetuppkopppling kunde inte hittas."
        lookingforupdatesmessage = "Letar efter uppdateringar..."
        latestversionmessage = "Senaste versionen av PiSpeedtest är: "
        youhavethelatestversionmessage = "Du har den senaste versionen av PiSpeedtest."
        initialspeedtestinformation = "För att få programmet att fungera optimalt så körs ett \"speedtest\" för att mäta tid m.m. Vänligen vänta."
        speedtestran = "Ett speedtest har nu körts. Det tog: "
        speedtestseconds = " sekunder."
        programmodes = "Programlägen:"
        stablemode = "STABLE - Kör de stabila funktionerna i PiSpeedtest."
        betamode = "BETA MODE - Betafunktioner som kan innehålla buggar."
        compatiblemode = "COMPATIBLE - Välj detta läge för kompatibilitet med Mac, vissa Linuxsystem eller andra system än Windows. En stabil version kommer att köras, inte en betaversion."
        pleaseselectaspeedtestmodemessage = "Vänligen välj ett PiSpeedtest-läge genom att skriva dess namn och trycka på enter: "
        programdurationseconds = "Hur länge vill du köra programmet (i sekunder)? 12 timmar = 43 200 sekunder: "

        programdurationminutes = "Hur länge vill du köra programmet (i minuter)? 12 timmar = 720 minuter: "
        howofteninput = "Hur ofta vill du köra programmet (i sekunder) tar cirka "
        seconds = " sekunder. "
        speedtestfilenameinput = "Vilket namn vill du ha på speedtestfilen? Använd inte punkter eller .txt, det läggs till automatiskt. "
        errormessage = "Ett fel inträffade när ett speedtest skulle köras."
        startingspeedtestmessage = "Startar test."
        speedtestcompletedmessage = "Test utfört."
        programdurationmodemessage = "Vill du ange hur länge du vill köra programmet i sekunder eller minuter? (Skriv \"SECONDS\" eller \"MINUTES\" för att välja.)"
        programdurationmodeerror = "Ett fel inträffade. Skrev du rätt när du valde läge? Läget \"MINUTES\" kommer att väljas automatiskt."
        newversionmessage = "Version: "
        newversionmessage2 = " av PiSpeedtest finns tillgänglig. Du har version: "
        newversionmessage3 = " installerad."
        lookingforupdateserror = "Ett fel inträffade när PiSpeedtest sökte efter nya uppdateringar."

        skipdetected = "SKIP DETEKTERAT"
        speedtestconfignotfound = "Kunde inte hitta konfigurationsfilen."
        loadingconfigurationmessage = "Laddar konfiguration..."
        configuredmodemessage = "Det konfiguerade läget är: "
        minutes = " minuter."
        configuredspeedtestdurationmessage = "Konfiguerad speedtest-tid: "
        invalidmode = "Konfigurationsfilen innehåller ett felaktigt läge."
        invalidduration = "Konfigurationsfilen innehåller en ogiltig spedtest-tid."
        configuredruneverysecondmessage = "Konfiguerad \"kör var ___ sekund\": "
        runeverysecondinvalid = "\"Kör var ___ sekund\"-konfigurationen är felaktig."
        invalidmodeselected = "Du valde inte ett giltigt program-läge. Vänligen starta om PiSpeedtest."
        waiterror = "Ett fel inträffad när speedtest-tider skulle beräknas. \"Kör programmet var ___ - sekund måste vara större än: "
        betaversionmessage = "Det verkar som att du använder en betaversion av PiSpeedtest "
        maybenotstable = "Betaversioner kan innehålla buggar och vara ostadiga."
        erroroccurred = "Ett fel inträffade när PiSpeedtest kördes. Fel: "

        normalmodedescription = "NORMAL - Endast ett speedtest kommer att köras för att mäta tid m.m."
        accuratemodedescription = "ACCURATE - Tre stycken speedtests kommer att köras för att mäta tid m.m, vilket betyder bättre nogrannhet. Detta tar cirka en minut."
        fastmodedescription = "FAST - Detta läge testar bara uppladdningshastigheten och multiplicerar den med två för att få tidsdata. Resultaten är inte nogranna, men programmet initieras snabbare."
        superbmodedescription = "SUPERB - Fem speedtests kommer att köras, vilket bara rekommenderas när du behöver en exakt tidsavläsning. Detta läge avrundar tidsdata till en decimal, vilket är mer exakt än andra lägen. Detta läge kommer dock att ta två minuter att köra."
        mode_error = "Ett fel inträffade när du skulle välja läge. Starta om PiSpeedtest och se till att läget är korrekt skrivet."
        fastspeedtest = "Detta speedtest testade bara uppladdningshastigheten."
        fastspeedtestnotice = "FÖR ATT FÅ PROGRAMMET ATT VARA SÅ NOGRANNT SOM MÖJLIGT REKOMMENDERAS DETTA LÄGE (\"FAST\") EJ!"
        speedtestmodeselection = "Skriv lägets namn och tryck sedan enter för att välja det: "
        programoptionsmessage = "Det finns olika alternativ för hur resultaten ska formatteras/skrivas ut. Här är en lista: "
        textoptionmessage = "Text - Resultaten är formatterade med hjälp av enkla ord och resultaten.(PiSpeedtest´s standard-layout)"
        plainoptionmessage = "Plain - Visar endast resultaten i siffror (Nedladdning, uppladdning och pinghastigheter). Ingen text. Resultaten är separerade med hjälp av mellanrum."
        listsoptionmessage = "Lists - Visar alla resultat från varje speedtest som körs sedan programet startades. (rekommenderas endast för debugging etc.)"
        detailedtextoptionsmessage = "Detailed-text - Perfekt för att presentera datan till allmänheten eftersom enheter, kommentarer och tidsstämplar är inkluderade."
        withunitsoptionsmessage = "With-units - Samma som \"Text\"-alternativet, men med enheter utskrivna."
        textlayoutconfigurationmessage = "Välj ett läge genom att skriva dess namn (t.ex. \"Text\") och sedan trycka på enter: "
        invalidtextlayout = "Du valde ett felaktigt läge. Standardläget, \"Text\" kommer att väljas istället."
        imagegenerationerror = "Ett fel inträffade när en resultat-bild skulle genereras."

        speedteststartpopupmessage = "Ett popupfönster kommer nu att visas. Kom ihåg att trycka på \"Ok\". Om du inte gör det så kommer ett speedtest inte att startas."

        releasemessageinformation = "Det finns ett meddelade angående den senaste versionen, vilket är: "
        speedtestaccuracymodefoundmessage = " har valts som speedtest-nogrannhets-läge."

        cloudsavingturnedoff = "Din molnlagring för PiSpeedtest är avstängd."
        cloudsavingenabled = "Din molnlagring för PiSpeedtest är aktiverad."
        cloudsavingnotconfigured = "Du har inte konfigurerat molnlagring för PiSpeedtest."
        configurecloudsavingmessage = "Skriv \"ENABLE\" och tryck enter för att aktivera molnlagring eller skriv \"NO\" för att gå vidare utan att konfiguera molnlagring. "
        skipingcloudsavingsetupmessage = "Okej, skippar setup-programmet."
        maxdownloadspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (nedladdningshastighet)?: "
        maxuploadspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (uppladdningshastighet)?: "
        maxpingspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (pinghastighet)?: "
        connectiontypeinputmessage = "Vilken uppkopplingstyp har du?? WIFI, CABLE eller CELLULAR: "

        speedtestimagesaved = "En speedtest-resultatsbild har nu sparats i mappen \"images\"."
        cloudsavingerror = "Ett fel inträffade när PiSpeedtest-resultaten skulle laddas upp till molnet."
        invalidapikey = "Din nuvarande API-nycjek för molnlagring är felaktig."
        foundapikeyfile = "Filen \"apikey.txt\" hittades. Letar efter API-nyckel."
        foundapikey = "En gilltig API-nyckel för molnlagring hittades."
        pingspeednotputintoconsiderationmessage = " Ping-hastighet är ej med i beräkningen."
        pressenterkeymessage = "Tryck på enter-knappen för att stänga PiSpeedtest."
    elif languageconfiguration == "en-us":
        pretestresults = "Pre-test-result: Ping to https://www.google.com. Result: "
        pretestresults2 = " seconds."
        nointernetconnectionmessage = "An active internet connection could not be established."
        lookingforupdatesmessage = "Looking for updates..."
        latestversionmessage = "The latest version of PiSpeedtest is: "
        youhavethelatestversionmessage = "You have the latest version of PiSpeedtest."
        initialspeedtestinformation = "To make the program work better, a \"speedtest\" is being run in the beginning of the program. You can choose between three different modes:"
        speedtestran = "A speedtest has now been run. It took: "
        speedtestseconds = " seconds."
        programmodes = "Program-modes:"
        stablemode = "STABLE - Run the stable and tested functions in PiSpeedtest."
        betamode = "BETA MODE - Functions in beta that might not work properly."
        compatiblemode = "COMPATIBLE - Select this mode for compatibility with more operating systems than Windows, including Mac, some Linux OSes and other operating systems. A stable release is being run, not a beta release."
        pleaseselectaspeedtestmodemessage = "Please select a PiSpeedtest-mode by typing its name and then pressing enter on your keyboard: "
        programdurationseconds = "For how long do you want to run the program (in seconds)? 12 hours = 43 200 seconds: "

        programdurationminutes = "For how long do you want to run the program (in minutes)? 12 hours = 720 minutes: "
        howofteninput = "How often do you want to run the program (in seconds)? A speedtest takes about "
        seconds = " seconds. "
        speedtestfilenameinput = "What name would you like the speedtestfile to have? Do not use any dots or .txt, it will be added automatically. "
        errormessage = "An error occured during the speedtest."
        startingspeedtestmessage = "Starting speedtest."
        speedtestcompletedmessage = "A speedtest has been run."
        programdurationmodemessage = "Do you want to enter how long you want to run the program in seconds or minutes? (Write \"SECONDS\" or \"MINUTES\" to select.) "
        programdurationmodeerror = "An error occured. Did you type everything in correctly when you choosed an option? The option \"MINUTES\" will be selected automatically. "
        newversionmessage = "Version: "
        newversionmessage2 = " of PiSpeedtest is available. You have version: "
        newversionmessage3 = " installed."
        lookingforupdateserror = "An error occured while looking for updates."
        skipdetected = "SKIP DETECTED"
        speedtestconfignotfound = "Could not find the configuration file."
        loadingconfigurationmessage = "Loading configuration..."
        languageconfigurationnotfound = "Could not find the language configuration file."
        configuredmodemessage = "The configured mode is: "
        minutes = " minutes."
        configuredspeedtestdurationmessage = "Configured speedtest duration: "
        invalidmode = "The speedtest file contains an invalid mode."
        invalidduration = "The speedtest file contains an invalid speedtest duration."
        configuredruneverysecondmessage = "Configured \"run every ___ seconds\": "
        runeverysecondinvalid = "The \"run every ___ seconds\" configuration is invalid."
        invalidmodeselected = "You didn´t select a valid mode. Please restart PiSpeedtest."
        waiterror = "An error occured when calculating speedtest wait times. Make sure that it is bigger than: "
        betaversionmessage = "It looks like you are running a beta version of PiSpeedtest "
        maybenotstable = "Beta versions may contain bugs and be unstable."

        erroroccurred = "An error occured while running PiSpeedtest. Error: "
        normalmodedescription = "NORMAL - Only one speedtest will be run to measure time."
        accuratemodedescription = "ACCURATE - Three speedtests will be run to measure time, which means increased accuracy. This takes about one minute."
        fastmodedescription = "FAST - This mode only tests the upload speed and then multiplies it by two to get time data. The results are not accurate, but the program loads faster."
        superbmodedescription = "SUPERB - Five speedtests will be run to measure time, which is only recommended for times when you need a perfect time measurement. This mode rounds the time to one decimal, which is more accurate than other modes. You have to wait about two minutes, though."
        speedtestaccuracymodefoundmessage = " has been chosen as speedtest accuracy mode."
        mode_error = "An error occurent when you selected a mode. Restart PiSpeedtest and make surte to enter the mode correctly."
        fastspeedtest = "This speedtest only tested the upload speed."
        fastspeedtestnotice = "TO MAKE THE PROGRAM ACCURATE ENOUGH, THIS MODE (\"FAST\") IS NOT RECOMMENDED!"
        speedtestmodeselection = "Type the mode´s name and then press enter to select it: "
        programoptionsmessage = "There are different types of options for how to format the results. Here is a list: "
        textoptionmessage = "Text - The results are formatted using simple words and the results. (the standard PiSpeedtest layout)"
        plainoptionmessage = "Plain - Only get the result values (Download, upload and ping speeds). No text. The values are separated using spaces."
        listsoptionmessage = "Lists - Shows all the results from every speedtest done since running the program. (this is only recommended for debugging etc.)"
        detailedtextoptionsmessage = "Detailed-text - Perfect for copy-pasting the data and presenting to the public as units, comments and timestamps are included."
        withunitsoptionsmessage = "With-units - The same as the \"Text\"-option, but with units."
        textlayoutconfigurationmessage = "Choose a mode by typing its name (e.g \"Text\") and the pressing enter: "
        invalidtextlayout = "You selected an invalid text layout. The standard text formatting mode, \"Text\" will be selected instead."
        imagegenerationerror = "An error occured while generating a results image."
        speedteststartpopupmessage = "A popup window will now be shown. Be sure to tap \"Ok\". If you don´t do that, the speedtests won´t start."

        releasemessageinformation = "There is a message about this release, which is: "
        speedtestaccuracymodemfoundessage = " has been selected as the speedtest accuracy mode."
        cloudsavingturnedoff = "Your cloudsaving for PiSpeedtest is currently turned off."
        cloudsavingenabled = "You have PiSpeedtest cloudsaving enabled."
        cloudsavingnotconfigured = "You haven´t configured cloudsaving for PiSpeedtest."


        configurecloudsavingmessage = "Type \"ENABLE\" and press enter to enable cloudsaving or type \"NO\" to skip. "

        skipingcloudsavingsetupmessage = "Okay, skipping setup."
        maxdownloadspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using (download speed)? "

        maxuploadspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using? (upload speed)?: "
        maxpingspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using (ping speed)? "

        connectiontypeinputmessage = "What connection type are you using? WIFI, CABLE or CELLULAR: "
        speedtestimagesaved = "A result image has been generated and saved in the directory \"images\"."

        generatingspeedtestreportmessage = "Generating speedtest report..."
        savedspeedtestreportmessage = "A speedtest report has been saved."
        cloudserverreponsemessage = "Cloudsaving server response: "
        viewresultslinkmessage = "View your speedtest results here: "
        downloadresultslinkmessage = "Additionally, the speedtest results can be downloaded here: "


        cloudsavingerror = "An error occured while cloudsaving PiSpeedtest results. "
        invalidapikey = "Your current cloudsaving API key is invalid."
        foundapikeyfile = "The file \"apikey.txt\" was found. Looking for API-key."

        pressenterkeymessage = "Press the enter key to close PiSpeedtest."
        foundapikey = "A valid cloudsaving API keywas found."
        pingspeednotputintoconsiderationmessage = " Ping speed is not put into consideration."
        pressenterkeymessage = "Press the enter key to close PiSpeedtest."
    else:
        pretestresults = "The current language configuration is somehow invalid."
        pretestresults2 = "The current language configuration is somehow invalid."
        nointernetconnectionmessage = "The current language configuration is somehow invalid."
        lookingforupdatesmessage = "The current language configuration is somehow invalid."
        latestversionmessage = "The current language configuration is somehow invalid."
        youhavethelatestversionmessage = "The current language configuration is somehow invalid."
        initialspeedtestinformation = "The current language configuration is somehow invalid."
        speedtestran = "The current language configuration is somehow invalid."
        speedtestseconds = "The current language configuration is somehow invalid."
        programmodes = "The current language configuration is somehow invalid."
        stablemode = "The current language configuration is somehow invalid."
        betamode = "The current language configuration is somehow invalid."
        compatiblemode = "The current language configuration is somehow invalid."
        pleaseselectaspeedtestmodemessage = "The current language configuration is somehow invalid."
        programdurationseconds = "The current language configuration is somehow invalid."

        programdurationminutes = "The current language configuration is somehow invalid."
        howofteninput = "The current language configuration is somehow invalid."
        seconds = "The current language configuration is somehow invalid."
        speedtestfilenameinput = "The current language configuration is somehow invalid."
        errormessage = "The current language configuration is somehow invalid."
        startingspeedtestmessage = "The current language configuration is somehow invalid."
        speedtestcompletedmessage = "The current language configuration is somehow invalid."
        programdurationmodemessage = "The current language configuration is somehow invalid."
        programdurationmodeerror = "The current language configuration is somehow invalid."
        newversionmessage = "The current language configuration is somehow invalid."
        newversionmessage2 = "The current language configuration is somehow invalid."
        newversionmessage3 = "The current language configuration is somehow invalid."

        lookingforupdateserror = "The current language configuration is somehow invalid."
        skipdetected = "The current language configuration is somehow invalid."
        speedtestconfignotfound = "The current language configuration is somehow invalid."
        loadingconfigurationmessage = "The current language configuration is somehow invalid."
        configuredmodemessage = "The current language configuration is somehow invalid."

        minutes = "The current language configuration is somehow invalid."
        configuredspeedtestdurationmessage = "The current language configuration is somehow invalid."
        invalidmode = "The current language configuration is somehow invalid."
        invalidduration = "The current language configuration is somehow invalid."
        configuredruneverysecondmessage = "The current language configuration is somehow invalid."
        runeverysecondinvalid = "The current language configuration is somehow invalid."
        invalidmodeselected = "The current language configuration is somehow invalid."
        waiterror = "The current language configuration is somehow invalid."
        betaversionmessage = "The current language configuration is somehow invalid."
        maybenotstable =  "The current language configuration is somehow invalid."
        erroroccurred = "The current language configuration is somehow invalid."
        normalmodedescription = "The current language configuration is somehow invalid."
        accuratemodedescription = "The current language configuration is somehow invalid."
        superbmodedescription = "The current language configuration is somehow invalid."
        mode_error = "The current language configuration is somehow invalid."
        fastspeedtest = "The current language configuration is somehow invalid."
        fastspeedtestnotice = "The current language configuration is somehow invalid."
        speedtestmodeselection = "The current language configuration is somehow invalid."
        programoptionsmessage = "The current language configuration is somehow invalid."
        textoptionmessage = "The current language configuration is somehow invalid."
        plainoptionmessage = "The current language configuration is somehow invalid."
        listsoptionmessage = "The current language configuration is somehow invalid."
        detailedtextoptionsmessage = "The current language configuration is somehow invalid."
        withunitsoptionsmessage = "The current language configuration is somehow invalid."
        invalidtextlayout = "The current language configuration is somehow invalid."
        imagegenerationerror = "The current language configuration is somehow invalid."
        speedteststartpopupmessage = "The current language configuration is somehow invalid."
        releasemessageinformation = "The current language configuration is somehow invalid."
        speedtestaccuracymodefoundmessage = "The current language configuration is somehow invalid."
        cloudsavingturnedoff = "The current language configuration is somehow invalid."
        cloudsavingenabled = "The current language configuration is somehow invalid."
        cloudsavingnotconfigured = "The current language configuration is somehow invalid."
        configurecloudsavingmessage = "The current language configuration is somehow invalid."
        skipingcloudsavingsetupmessage = "The current language configuration is somehow invalid."
        maxdownloadspeedinputmessage = "The current language configuration is somehow invalid."
        maxuploadspeedinputmessage = "The current language configuration is somehow invalid."
        maxpingspeedinputmessage = "The current language configuration is somehow invalid."
        connectiontypeinputmessage = "The current language configuration is somehow invalid."
        speedtestimagesaved = "The current language configuration is somehow invalid."
        generatingspeedtestreportmessage = "The current language configuration is somehow invalid."
        savedspeedtestreportmessage = "The current language configuration is somehow invalid."
        cloudserverreponsemessage = "The current language configuration is somehow invalid."
        viewresultslinkmessage = "The current language configuration is somehow invalid."
        downloadresultslinkmessage = "The current language configuration is somehow invalid."


        cloudsavingerror = "The current language configuration is somehow invalid."
        invalidapikey = "The current language configuration is somehow invalid."

        foundapikeyfile = "The current language configuration is somehow invalid."
        foundapikey = "The current language configuration is somehow invalid."
        pingspeednotputintoconsiderationmessage = "The current language configuration is somehow invalid."
        pressenterkeymessage = "The current language configuration is somehow invalid."


    # Main speedtest code:
    def processpeedtest(backupmode, filename, textlayout):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        results = s.results.dict()
        resultlist = list(results.values())
        download = str(round(resultlist[0] / 1000000)) + " mbit/s"
        upload = str(round(resultlist[1] / 1000000)) + " mbit/s"
        ping = str(resultlist[2]) + "ms"
        downloadlist.append(str(round(resultlist[0] / 1000000)))
        uploadlist.append(str(round(resultlist[1] / 1000000)))
        pinglist.append(str(round(resultlist[2])))
        if textlayout == "Text":
            fullresults = "Results: " + " Download: " + download + " Upload: " + upload + " Ping: " + ping + "."
        elif textlayout == "Plain":
            fullresults = download  + " " + upload + " " + ping
        elif textlayout == "Lists":
            fullresults = str(downloadlist) + ", " + str(uploadlist) + ", " + str(downloadlist) + "."
        elif textlayout == "Detailed-text":
            fullresults = "A test at " + str(time.ctime()) + " has been run. " + "The results was " + " Download speed (mbit/s): " + download + " Upload speed (mbit/s): " + upload + " Ping (milliseconds): " + ping + "."
        elif textlayout == "With-units":
            fullresults = "Results: " + " Download: " + download + " mbit/s " + " Upload: " + upload + " mbit/s "+ " Ping: " + ping + " milliseconds" + "."
        print(fullresults)
        if backupmode == False:

            with open(filename, "a+") as file:
                file.write(fullresults + "\n")
        elif backupmode == True:
            with open("speedtestbackup.txt", "a+") as backupfile:
                backupfile.write(fullresults + "\n")


    #(end of main speedtest code.)
    def processspeedtest_onlyupload(filename):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.upload()
        results = round(int(s.results.upload) / 1000000)
        with open(filename, "a+") as file:
            file.write("Upload: " + str(results) + " (only upload test)")




    try:
        import requests
        request = requests.get("https://www.google.com")
        print(pretestresults + str(request.elapsed.total_seconds()) + pretestresults2)
    except requests.exceptions.ConnectionError:
        print(nointernetconnectionmessage)
        noconnection = 1
        raise NoInternetConnection(nointernetconnectionmessage)
    print(lookingforupdatesmessage)
    print("\n")
    try:
        import requests
        from bs4 import BeautifulSoup

        updatecheck = requests.get("https://pispeedtestfiles.000webhostapp.com/latestversion.html")
        soup = BeautifulSoup(updatecheck.text, "html.parser")

        latestversionnumber = str(soup.get_text()).replace("\n", "")
        print(latestversionmessage + latestversionnumber + ".")
        if latestversionnumber == fileversionnumber:
            print(youhavethelatestversionmessage)
        elif float(latestversionnumber) < float(fileversionnumber):
            print(betaversionmessage + "( "+ fileversionnumber + ") . " + maybenotstable)
        else:
            releasemessage = requests.get("https://pispeedtestfiles.000webhostapp.com/releasemessage.html")
            releasemessageversion = requests.get("https://pispeedtestfiles.000webhostapp.com/releasemessageversion.html")
            soup = BeautifulSoup(releasemessageversion.text, "html.parser")
            releasemessageversionnumber = str(soup.get_text()).replace("\n", "")
            try:
                if float(releasemessageversionnumber) == float(latestversionnumber):
                    soup = BeautifulSoup(releasemessage.text, "html.parser")
                    messagefornewrelease = str(soup.get_text())
                    print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
                    print(releasemessageinformation + "\n" +  messagefornewrelease)
                else:
                    print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
            except:
                print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
    except Exception as e:
        print(lookingforupdateserror + " (" + str(e) + ").")
    print("\n")
    with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\status.txt"), "r") as cloudsavingstatustextfile:
        filecontents = cloudsavingstatustextfile.read().splitlines()
    if filecontents[0] == "ENABLED":
        print(cloudsavingenabled)
    elif filecontents[0] == "OFF":
        print(cloudsavingturnedoff)
    elif filecontents[0] == "NOT CONFIGURED":
        print(cloudsavingnotconfigured)
        confirm = input(configurecloudsavingmessage)
        if confirm == "ENABLE":
            import cloudsavingsetup
            cloudsavesetup.setup()
        else:

            print(skipingcloudsavingsetupmessage)

    print("\n")
    print(initialspeedtestinformation)
    print(normalmodedescription)
    print(accuratemodedescription)
    print(fastmodedescription)
    print(superbmodedescription)
    speedtestaccuracymode = input(speedtestmodeselection)
    initialspeedtestsfile = os.path.join(os.getcwd() + "/speedtestresults/" + "intialspeedtests.txt")
    #Message when a speedtest accuracy mode is found:
    def speedtestaccuracymodefound():
        print(speedtestaccuracymode + speedtestaccuracymodefoundmessage)
    if speedtestaccuracymode == "NORMAL" or speedtestaccuracymode.lower() == "normal":
        speedtestaccuracymodefound()
        timeone = time.time()
        if noconnection == 0:

            processpeedtest(0, filename=initialspeedtestsfile, textlayout="Text")
            speedtesttime = round(time.time() - timeone)
            print(speedtestran + str(speedtesttime) + speedtestseconds)
        elif noconnection == 1:
            print(nointernetconnectionmessage)

    elif speedtestaccuracymode == "ACCURATE" or speedtestaccuracymode.lower() == "accurate":
        timelist = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            for i in range(3):
                time1 = time.time()
                processpeedtest(False, "initialspeedtest.txt", textlayout="Text")
                timelist.append(str(round(time.time()-time1)))
                print(speedtestran + str(timelist[i]) + speedtestseconds)
            speedtesttime = round(eval("+".join(timelist)))
        elif noconnection == 1:
            print(nointernetconnectionmessage)
    elif speedtestaccuracymode == "FAST" or speedtestaccuracymode.lower() == "fast":
        timelist3 = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            timeone1 = time.time()
            processspeedtest_onlyupload("initialspeedtests.txt")
            speedtesttime = str(round((time.time() - timeone1)*2))
            print(speedtestran + str(round(int(speedtesttime)/2)) + speedtestseconds + " " + fastspeedtest)

    elif speedtestaccuracymode == "SUPERB" or speedtestaccuracymode.lower() == "superb":
        timelist2 = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            for i in range(5):
                timenumberone = time.time()
                processpeedtest(False, "initialspeedtest.txt", textlayout="Text")
                timelist2.append(str(round(time.time() - timenumberone, 1)))
                print(speedtestran + timelist2[i] + speedtestseconds)
            times = "+".join(timelist2)
            speedtesttime = round(eval(times)/5, 1)


        elif noconnection == 1:
            print(nointernetconnectionmessage)
    else:
        print(mode_error)

        exit()
    print("\n")

    try:
        configurationfile = os.path.join(os.getcwd() + "/configurationfiles/config.txt")

        with open(configurationfile, "r+") as configurationsfile:
            print(loadingconfigurationmessage)
            configurationfilecontent = configurationsfile.read().splitlines()
            if configurationfilecontent[9] in allowedmodes:
                configuredmode = configurationfilecontent[9]
                print(configuredmodemessage + configuredmode + ".")
                loadconfig[0] = 1
            elif configurationfilecontent[9] == "-SKIP-":
                print(skipdetected)
                loadconfig[0] = 0
            else:
                print(invalidmode)

                loadconfig[0] = 0
            try:
                configuredspeedtestduration1 = int(configurationfilecontent[10])
                configuredspeedtestduration = int(configuredspeedtestduration1 * 60)
                print(configuredspeedtestdurationmessage + str(configuredspeedtestduration / 60) + minutes)
                loadconfig[1] = 1
            except:
                if configurationfilecontent[10] == "-SKIP-":
                    print(skipdetected)
                    loadconfig[1] = 0
                else:
                    print(invalidduration)
                    loadconfig[1] = 0
            try:
                configuredruneverysecond = int(configurationfilecontent[11])
                print(configuredruneverysecondmessage + str(configuredruneverysecond) + seconds)
                loadconfig[2] = 1
            except:
                if configurationfilecontent[11] == "-SKIP-":
                    print(skipdetected)
                    loadconfig[2] = 0
                else:
                    print(runeverysecondinvalid)
                    loadconfig[2] = 0
        print("\n")
    except:
        print(speedtestconfignotfound)
        loadconfig[0] = 0
        loadconfig[1] = 0
        loadconfig[2] = 0
    if loadconfig[0] == 0:
        print("\n")
        print(programmodes)
        print(betamode)
        print(stablemode)
        print(compatiblemode)
        mode = input(pleaseselectaspeedtestmodemessage)
    elif loadconfig[0] == 1:
        mode = configuredmode
    else:
        print("\n")
        print(programmodes)
        print(betamode)
        print(stablemode)
        print(compatiblemode)
        mode = input(pleaseselectaspeedtestmodemessage)

    if mode == "BETA MODE" or mode.lower() == "beta mode":
        import ctypes

        print("\n")


        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        #inputmaxpingspeed = int(input(maxpingspeedinputmessage)) (not used for the connection score algorithm yet.)
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        print(speedteststartpopupmessage)
        ctypes.windll.user32.MessageBoxW(None, startingspeedtestmessage, "PiSpeedtest", 0)
        steps = int(times)


        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:
                    ctypes.windll.user32.MessageBoxW(None, errormessage, "PiSpeedtest", 0)

                    print(errormessage + "(" + str(e) + ").")

                    # This is being added in a later release:
                    # box = ctypes.windll.user32.MessageBoxW(None, "An error occured while running a speedtest. Would you like to try again? Everything will restart. The file with new speedtest data will be namned \"speedtestbackup.txt\".", "PiSpeedtest", 5)
                    # if box == 1:
                    # print(Running speedtest once more.")
                    # for speedtestindex in range(repeat):

                    # print("A speedtest is being started.")
                    # processpeedtest(0, filename="speedtestbackup.txt")
                    # print("A speedtest has been completed.")
                    # time.sleep(interval)
                    # elif box == 2:
                    # print("Quitting PiSpeedtest because of an error.")
                    # else:
                    # print("Quitting PiSpeedtest because of an error.")
            print("\n")
            try:
                from PIL import Image, ImageDraw, ImageFont


                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount)/len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount)/(len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount)/len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed/ 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")


                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"),"w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " +  "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)

    elif mode == "STABLE" or mode.lower() == "stable":
        import ctypes

        print("\n")

        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        print(speedteststartpopupmessage)
        ctypes.windll.user32.MessageBoxW(None, startingspeedtestmessage, "PiSpeedtest", 0)
        steps = int(times)

        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:
                    ctypes.windll.user32.MessageBoxW(None, errormessage, "PiSpeedtest", 0)

                    print(errormessage + "(" + str(e) + ").")
            print("\n")


            try:
                from PIL import Image, ImageDraw, ImageFont

                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount) / len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount) / (len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount) / len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(
                    mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(
                    os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")

                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace(
                                "A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"),"w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)
    elif mode == "COMPATIBLE" or mode.lower() == "compatible":
        print("\n")

        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        steps = int(times)

        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:

                    print(errormessage + "(" + str(e) + ").")
            print("\n")

            try:
                from PIL import Image, ImageDraw, ImageFont

                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount) / len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount) / (len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount) / len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(
                    mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(
                    os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")

                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"), "w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)
    else:
        print(invalidmodeselected)
        raise NoModeDefinded("\"" + mode + "\"" + " is not a valid mode.")

except Exception as e:

    print(erroroccurred + " (" + str(e) + ").")

finally:




    print("\n")
    input(pressenterkeymessage)
try:
    import speedtest

    import time


    import os


    # Defining errors - These are not implemented that much yet.
    def __main__():
        pass
    class PiSpeedtestErrors(Exception):
        pass


    class NoModeDefinded(PiSpeedtestErrors):
        pass


    class FileError(PiSpeedtestErrors):
        pass

    class NoInternetConnection(PiSpeedtestErrors):
        pass

    class UpdatecheckServerError(NoInternetConnection):
        pass


    downloadlist = []
    uploadlist = []
    pinglist = []

    smallestkbitsup = 1000
    largestkbitsup = 0
    smallestkbitsdown = 1000
    largestkbitsdown = 0
    noconnection = 0
    fileversionnumber = "3.5"
    allowedmodes = ["BETA MODE", "STABLE", "COMPATIBLE"]
    loadconfig = [0, 0, 0, 0, 0]

    allowedtextlayouts = ["Text", "Plain", "Lists", "Detailed-text", "With-units"]

    fontfilename = "Roboto-Bold.ttf" #Add a custom font filename here if you want a custom font for the images. Don´t forget the file extension! Only .ttf-files supported.
    print("PiSpeedtest " + fileversionnumber + ".")
    # Language settings:
    approved_languages = ["sv-se", "en-us"]  # To add a language that´s not in the list, make sure to add its name here.
    languageconfigpath = os.path.join(os.getcwd() + "/configurationfiles/languageconfiguration.txt")
    try:
        with open(languageconfigpath, "r+") as languagecofigurationfile:
            languageconfig = languagecofigurationfile.read().splitlines()
    except:
        print("Could not find language configuration. Please make sure that \"languageconfiguration.txt\" is in the directory /configurationfiles.")
        languageconfig = ["Configuration not found." + "ConfigurationNotFound"]
    if languageconfig[1] not in approved_languages:
        print("The current language configuration is not valid. Please check the file languageconfiguration.txt. Valid languages are:")
        for i in range(len(approved_languages)):
            print(approved_languages[i])
        languageconfiguration = "sv-se"
        print("For this time, the language has been set to sv-se, Swedish.")
    else:
        print("Language configuration " + str(languageconfig[1]) + " found.")
        languageconfiguration = languageconfig[1]
    print("\n")
    # Language configuration - feel free to add your own languages here!
    if languageconfiguration == "sv-se":
        pretestresults = "Pre-test-resultat: Ping till https://www.google.com. Resultat: "
        pretestresults2 = " sekunder."
        nointernetconnectionmessage = "En aktiv internetuppkopppling kunde inte hittas."
        lookingforupdatesmessage = "Letar efter uppdateringar..."
        latestversionmessage = "Senaste versionen av PiSpeedtest är: "
        youhavethelatestversionmessage = "Du har den senaste versionen av PiSpeedtest."
        initialspeedtestinformation = "För att få programmet att fungera optimalt så körs ett \"speedtest\" för att mäta tid m.m. Vänligen vänta."
        speedtestran = "Ett speedtest har nu körts. Det tog: "
        speedtestseconds = " sekunder."
        programmodes = "Programlägen:"
        stablemode = "STABLE - Kör de stabila funktionerna i PiSpeedtest."
        betamode = "BETA MODE - Betafunktioner som kan innehålla buggar."
        compatiblemode = "COMPATIBLE - Välj detta läge för kompatibilitet med Mac, vissa Linuxsystem eller andra system än Windows. En stabil version kommer att köras, inte en betaversion."
        pleaseselectaspeedtestmodemessage = "Vänligen välj ett PiSpeedtest-läge genom att skriva dess namn och trycka på enter: "
        programdurationseconds = "Hur länge vill du köra programmet (i sekunder)? 12 timmar = 43 200 sekunder: "

        programdurationminutes = "Hur länge vill du köra programmet (i minuter)? 12 timmar = 720 minuter: "
        howofteninput = "Hur ofta vill du köra programmet (i sekunder) tar cirka "
        seconds = " sekunder. "
        speedtestfilenameinput = "Vilket namn vill du ha på speedtestfilen? Använd inte punkter eller .txt, det läggs till automatiskt. "
        errormessage = "Ett fel inträffade när ett speedtest skulle köras."
        startingspeedtestmessage = "Startar test."
        speedtestcompletedmessage = "Test utfört."
        programdurationmodemessage = "Vill du ange hur länge du vill köra programmet i sekunder eller minuter? (Skriv \"SECONDS\" eller \"MINUTES\" för att välja.)"
        programdurationmodeerror = "Ett fel inträffade. Skrev du rätt när du valde läge? Läget \"MINUTES\" kommer att väljas automatiskt."
        newversionmessage = "Version: "
        newversionmessage2 = " av PiSpeedtest finns tillgänglig. Du har version: "
        newversionmessage3 = " installerad."
        lookingforupdateserror = "Ett fel inträffade när PiSpeedtest sökte efter nya uppdateringar."

        skipdetected = "SKIP DETEKTERAT"
        speedtestconfignotfound = "Kunde inte hitta konfigurationsfilen."
        loadingconfigurationmessage = "Laddar konfiguration..."
        configuredmodemessage = "Det konfiguerade läget är: "
        minutes = " minuter."
        configuredspeedtestdurationmessage = "Konfiguerad speedtest-tid: "
        invalidmode = "Konfigurationsfilen innehåller ett felaktigt läge."
        invalidduration = "Konfigurationsfilen innehåller en ogiltig spedtest-tid."
        configuredruneverysecondmessage = "Konfiguerad \"kör var ___ sekund\": "
        runeverysecondinvalid = "\"Kör var ___ sekund\"-konfigurationen är felaktig."
        invalidmodeselected = "Du valde inte ett giltigt program-läge. Vänligen starta om PiSpeedtest."
        waiterror = "Ett fel inträffad när speedtest-tider skulle beräknas. \"Kör programmet var ___ - sekund måste vara större än: "
        betaversionmessage = "Det verkar som att du använder en betaversion av PiSpeedtest "
        maybenotstable = "Betaversioner kan innehålla buggar och vara ostadiga."
        erroroccurred = "Ett fel inträffade när PiSpeedtest kördes. Fel: "

        normalmodedescription = "NORMAL - Endast ett speedtest kommer att köras för att mäta tid m.m."
        accuratemodedescription = "ACCURATE - Tre stycken speedtests kommer att köras för att mäta tid m.m, vilket betyder bättre nogrannhet. Detta tar cirka en minut."
        fastmodedescription = "FAST - Detta läge testar bara uppladdningshastigheten och multiplicerar den med två för att få tidsdata. Resultaten är inte nogranna, men programmet initieras snabbare."
        superbmodedescription = "SUPERB - Fem speedtests kommer att köras, vilket bara rekommenderas när du behöver en exakt tidsavläsning. Detta läge avrundar tidsdata till en decimal, vilket är mer exakt än andra lägen. Detta läge kommer dock att ta två minuter att köra."
        mode_error = "Ett fel inträffade när du skulle välja läge. Starta om PiSpeedtest och se till att läget är korrekt skrivet."
        fastspeedtest = "Detta speedtest testade bara uppladdningshastigheten."
        fastspeedtestnotice = "FÖR ATT FÅ PROGRAMMET ATT VARA SÅ NOGRANNT SOM MÖJLIGT REKOMMENDERAS DETTA LÄGE (\"FAST\") EJ!"
        speedtestmodeselection = "Skriv lägets namn och tryck sedan enter för att välja det: "
        programoptionsmessage = "Det finns olika alternativ för hur resultaten ska formatteras/skrivas ut. Här är en lista: "
        textoptionmessage = "Text - Resultaten är formatterade med hjälp av enkla ord och resultaten.(PiSpeedtest´s standard-layout)"
        plainoptionmessage = "Plain - Visar endast resultaten i siffror (Nedladdning, uppladdning och pinghastigheter). Ingen text. Resultaten är separerade med hjälp av mellanrum."
        listsoptionmessage = "Lists - Visar alla resultat från varje speedtest som körs sedan programet startades. (rekommenderas endast för debugging etc.)"
        detailedtextoptionsmessage = "Detailed-text - Perfekt för att presentera datan till allmänheten eftersom enheter, kommentarer och tidsstämplar är inkluderade."
        withunitsoptionsmessage = "With-units - Samma som \"Text\"-alternativet, men med enheter utskrivna."
        textlayoutconfigurationmessage = "Välj ett läge genom att skriva dess namn (t.ex. \"Text\") och sedan trycka på enter: "
        invalidtextlayout = "Du valde ett felaktigt läge. Standardläget, \"Text\" kommer att väljas istället."
        imagegenerationerror = "Ett fel inträffade när en resultat-bild skulle genereras."

        speedteststartpopupmessage = "Ett popupfönster kommer nu att visas. Kom ihåg att trycka på \"Ok\". Om du inte gör det så kommer ett speedtest inte att startas."

        releasemessageinformation = "Det finns ett meddelade angående den senaste versionen, vilket är: "
        speedtestaccuracymodefoundmessage = " har valts som speedtest-nogrannhets-läge."

        cloudsavingturnedoff = "Din molnlagring för PiSpeedtest är avstängd."
        cloudsavingenabled = "Din molnlagring för PiSpeedtest är aktiverad."
        cloudsavingnotconfigured = "Du har inte konfigurerat molnlagring för PiSpeedtest."
        configurecloudsavingmessage = "Skriv \"ENABLE\" och tryck enter för att aktivera molnlagring eller skriv \"NO\" för att gå vidare utan att konfiguera molnlagring. "
        skipingcloudsavingsetupmessage = "Okej, skippar setup-programmet."
        maxdownloadspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (nedladdningshastighet)?: "
        maxuploadspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (uppladdningshastighet)?: "
        maxpingspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (pinghastighet)?: "
        connectiontypeinputmessage = "Vilken uppkopplingstyp har du?? WIFI, CABLE eller CELLULAR: "

        speedtestimagesaved = "En speedtest-resultatsbild har nu sparats i mappen \"images\"."
        cloudsavingerror = "Ett fel inträffade när PiSpeedtest-resultaten skulle laddas upp till molnet."
        invalidapikey = "Din nuvarande API-nycjek för molnlagring är felaktig."
        foundapikeyfile = "Filen \"apikey.txt\" hittades. Letar efter API-nyckel."
        foundapikey = "En gilltig API-nyckel för molnlagring hittades."
        pingspeednotputintoconsiderationmessage = " Ping-hastighet är ej med i beräkningen."
        pressenterkeymessage = "Tryck på enter-knappen för att stänga PiSpeedtest."
    elif languageconfiguration == "en-us":
        pretestresults = "Pre-test-result: Ping to https://www.google.com. Result: "
        pretestresults2 = " seconds."
        nointernetconnectionmessage = "An active internet connection could not be established."
        lookingforupdatesmessage = "Looking for updates..."
        latestversionmessage = "The latest version of PiSpeedtest is: "
        youhavethelatestversionmessage = "You have the latest version of PiSpeedtest."
        initialspeedtestinformation = "To make the program work better, a \"speedtest\" is being run in the beginning of the program. You can choose between three different modes:"
        speedtestran = "A speedtest has now been run. It took: "
        speedtestseconds = " seconds."
        programmodes = "Program-modes:"
        stablemode = "STABLE - Run the stable and tested functions in PiSpeedtest."
        betamode = "BETA MODE - Functions in beta that might not work properly."
        compatiblemode = "COMPATIBLE - Select this mode for compatibility with more operating systems than Windows, including Mac, some Linux OSes and other operating systems. A stable release is being run, not a beta release."
        pleaseselectaspeedtestmodemessage = "Please select a PiSpeedtest-mode by typing its name and then pressing enter on your keyboard: "
        programdurationseconds = "For how long do you want to run the program (in seconds)? 12 hours = 43 200 seconds: "

        programdurationminutes = "For how long do you want to run the program (in minutes)? 12 hours = 720 minutes: "
        howofteninput = "How often do you want to run the program (in seconds)? A speedtest takes about "
        seconds = " seconds. "
        speedtestfilenameinput = "What name would you like the speedtestfile to have? Do not use any dots or .txt, it will be added automatically. "
        errormessage = "An error occured during the speedtest."
        startingspeedtestmessage = "Starting speedtest."
        speedtestcompletedmessage = "A speedtest has been run."
        programdurationmodemessage = "Do you want to enter how long you want to run the program in seconds or minutes? (Write \"SECONDS\" or \"MINUTES\" to select.) "
        programdurationmodeerror = "An error occured. Did you type everything in correctly when you choosed an option? The option \"MINUTES\" will be selected automatically. "
        newversionmessage = "Version: "
        newversionmessage2 = " of PiSpeedtest is available. You have version: "
        newversionmessage3 = " installed."
        lookingforupdateserror = "An error occured while looking for updates."
        skipdetected = "SKIP DETECTED"
        speedtestconfignotfound = "Could not find the configuration file."
        loadingconfigurationmessage = "Loading configuration..."
        languageconfigurationnotfound = "Could not find the language configuration file."
        configuredmodemessage = "The configured mode is: "
        minutes = " minutes."
        configuredspeedtestdurationmessage = "Configured speedtest duration: "
        invalidmode = "The speedtest file contains an invalid mode."
        invalidduration = "The speedtest file contains an invalid speedtest duration."
        configuredruneverysecondmessage = "Configured \"run every ___ seconds\": "
        runeverysecondinvalid = "The \"run every ___ seconds\" configuration is invalid."
        invalidmodeselected = "You didn´t select a valid mode. Please restart PiSpeedtest."
        waiterror = "An error occured when calculating speedtest wait times. Make sure that it is bigger than: "
        betaversionmessage = "It looks like you are running a beta version of PiSpeedtest "
        maybenotstable = "Beta versions may contain bugs and be unstable."

        erroroccurred = "An error occured while running PiSpeedtest. Error: "
        normalmodedescription = "NORMAL - Only one speedtest will be run to measure time."
        accuratemodedescription = "ACCURATE - Three speedtests will be run to measure time, which means increased accuracy. This takes about one minute."
        fastmodedescription = "FAST - This mode only tests the upload speed and then multiplies it by two to get time data. The results are not accurate, but the program loads faster."
        superbmodedescription = "SUPERB - Five speedtests will be run to measure time, which is only recommended for times when you need a perfect time measurement. This mode rounds the time to one decimal, which is more accurate than other modes. You have to wait about two minutes, though."
        speedtestaccuracymodefoundmessage = " has been chosen as speedtest accuracy mode."
        mode_error = "An error occurent when you selected a mode. Restart PiSpeedtest and make surte to enter the mode correctly."
        fastspeedtest = "This speedtest only tested the upload speed."
        fastspeedtestnotice = "TO MAKE THE PROGRAM ACCURATE ENOUGH, THIS MODE (\"FAST\") IS NOT RECOMMENDED!"
        speedtestmodeselection = "Type the mode´s name and then press enter to select it: "
        programoptionsmessage = "There are different types of options for how to format the results. Here is a list: "
        textoptionmessage = "Text - The results are formatted using simple words and the results. (the standard PiSpeedtest layout)"
        plainoptionmessage = "Plain - Only get the result values (Download, upload and ping speeds). No text. The values are separated using spaces."
        listsoptionmessage = "Lists - Shows all the results from every speedtest done since running the program. (this is only recommended for debugging etc.)"
        detailedtextoptionsmessage = "Detailed-text - Perfect for copy-pasting the data and presenting to the public as units, comments and timestamps are included."
        withunitsoptionsmessage = "With-units - The same as the \"Text\"-option, but with units."
        textlayoutconfigurationmessage = "Choose a mode by typing its name (e.g \"Text\") and the pressing enter: "
        invalidtextlayout = "You selected an invalid text layout. The standard text formatting mode, \"Text\" will be selected instead."
        imagegenerationerror = "An error occured while generating a results image."
        speedteststartpopupmessage = "A popup window will now be shown. Be sure to tap \"Ok\". If you don´t do that, the speedtests won´t start."

        releasemessageinformation = "There is a message about this release, which is: "
        speedtestaccuracymodemfoundessage = " has been selected as the speedtest accuracy mode."
        cloudsavingturnedoff = "Your cloudsaving for PiSpeedtest is currently turned off."
        cloudsavingenabled = "You have PiSpeedtest cloudsaving enabled."
        cloudsavingnotconfigured = "You haven´t configured cloudsaving for PiSpeedtest."


        configurecloudsavingmessage = "Type \"ENABLE\" and press enter to enable cloudsaving or type \"NO\" to skip. "

        skipingcloudsavingsetupmessage = "Okay, skipping setup."
        maxdownloadspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using (download speed)? "

        maxuploadspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using? (upload speed)?: "
        maxpingspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using (ping speed)? "

        connectiontypeinputmessage = "What connection type are you using? WIFI, CABLE or CELLULAR: "
        speedtestimagesaved = "A result image has been generated and saved in the directory \"images\"."

        generatingspeedtestreportmessage = "Generating speedtest report..."
        savedspeedtestreportmessage = "A speedtest report has been saved."
        cloudserverreponsemessage = "Cloudsaving server response: "
        viewresultslinkmessage = "View your speedtest results here: "
        downloadresultslinkmessage = "Additionally, the speedtest results can be downloaded here: "


        cloudsavingerror = "An error occured while cloudsaving PiSpeedtest results. "
        invalidapikey = "Your current cloudsaving API key is invalid."
        foundapikeyfile = "The file \"apikey.txt\" was found. Looking for API-key."

        pressenterkeymessage = "Press the enter key to close PiSpeedtest."
        foundapikey = "A valid cloudsaving API keywas found."
        pingspeednotputintoconsiderationmessage = " Ping speed is not put into consideration."
        pressenterkeymessage = "Press the enter key to close PiSpeedtest."
    else:
        pretestresults = "The current language configuration is somehow invalid."
        pretestresults2 = "The current language configuration is somehow invalid."
        nointernetconnectionmessage = "The current language configuration is somehow invalid."
        lookingforupdatesmessage = "The current language configuration is somehow invalid."
        latestversionmessage = "The current language configuration is somehow invalid."
        youhavethelatestversionmessage = "The current language configuration is somehow invalid."
        initialspeedtestinformation = "The current language configuration is somehow invalid."
        speedtestran = "The current language configuration is somehow invalid."
        speedtestseconds = "The current language configuration is somehow invalid."
        programmodes = "The current language configuration is somehow invalid."
        stablemode = "The current language configuration is somehow invalid."
        betamode = "The current language configuration is somehow invalid."
        compatiblemode = "The current language configuration is somehow invalid."
        pleaseselectaspeedtestmodemessage = "The current language configuration is somehow invalid."
        programdurationseconds = "The current language configuration is somehow invalid."

        programdurationminutes = "The current language configuration is somehow invalid."
        howofteninput = "The current language configuration is somehow invalid."
        seconds = "The current language configuration is somehow invalid."
        speedtestfilenameinput = "The current language configuration is somehow invalid."
        errormessage = "The current language configuration is somehow invalid."
        startingspeedtestmessage = "The current language configuration is somehow invalid."
        speedtestcompletedmessage = "The current language configuration is somehow invalid."
        programdurationmodemessage = "The current language configuration is somehow invalid."
        programdurationmodeerror = "The current language configuration is somehow invalid."
        newversionmessage = "The current language configuration is somehow invalid."
        newversionmessage2 = "The current language configuration is somehow invalid."
        newversionmessage3 = "The current language configuration is somehow invalid."

        lookingforupdateserror = "The current language configuration is somehow invalid."
        skipdetected = "The current language configuration is somehow invalid."
        speedtestconfignotfound = "The current language configuration is somehow invalid."
        loadingconfigurationmessage = "The current language configuration is somehow invalid."
        configuredmodemessage = "The current language configuration is somehow invalid."

        minutes = "The current language configuration is somehow invalid."
        configuredspeedtestdurationmessage = "The current language configuration is somehow invalid."
        invalidmode = "The current language configuration is somehow invalid."
        invalidduration = "The current language configuration is somehow invalid."
        configuredruneverysecondmessage = "The current language configuration is somehow invalid."
        runeverysecondinvalid = "The current language configuration is somehow invalid."
        invalidmodeselected = "The current language configuration is somehow invalid."
        waiterror = "The current language configuration is somehow invalid."
        betaversionmessage = "The current language configuration is somehow invalid."
        maybenotstable =  "The current language configuration is somehow invalid."
        erroroccurred = "The current language configuration is somehow invalid."
        normalmodedescription = "The current language configuration is somehow invalid."
        accuratemodedescription = "The current language configuration is somehow invalid."
        superbmodedescription = "The current language configuration is somehow invalid."
        mode_error = "The current language configuration is somehow invalid."
        fastspeedtest = "The current language configuration is somehow invalid."
        fastspeedtestnotice = "The current language configuration is somehow invalid."
        speedtestmodeselection = "The current language configuration is somehow invalid."
        programoptionsmessage = "The current language configuration is somehow invalid."
        textoptionmessage = "The current language configuration is somehow invalid."
        plainoptionmessage = "The current language configuration is somehow invalid."
        listsoptionmessage = "The current language configuration is somehow invalid."
        detailedtextoptionsmessage = "The current language configuration is somehow invalid."
        withunitsoptionsmessage = "The current language configuration is somehow invalid."
        invalidtextlayout = "The current language configuration is somehow invalid."
        imagegenerationerror = "The current language configuration is somehow invalid."
        speedteststartpopupmessage = "The current language configuration is somehow invalid."
        releasemessageinformation = "The current language configuration is somehow invalid."
        speedtestaccuracymodefoundmessage = "The current language configuration is somehow invalid."
        cloudsavingturnedoff = "The current language configuration is somehow invalid."
        cloudsavingenabled = "The current language configuration is somehow invalid."
        cloudsavingnotconfigured = "The current language configuration is somehow invalid."
        configurecloudsavingmessage = "The current language configuration is somehow invalid."
        skipingcloudsavingsetupmessage = "The current language configuration is somehow invalid."
        maxdownloadspeedinputmessage = "The current language configuration is somehow invalid."
        maxuploadspeedinputmessage = "The current language configuration is somehow invalid."
        maxpingspeedinputmessage = "The current language configuration is somehow invalid."
        connectiontypeinputmessage = "The current language configuration is somehow invalid."
        speedtestimagesaved = "The current language configuration is somehow invalid."
        generatingspeedtestreportmessage = "The current language configuration is somehow invalid."
        savedspeedtestreportmessage = "The current language configuration is somehow invalid."
        cloudserverreponsemessage = "The current language configuration is somehow invalid."
        viewresultslinkmessage = "The current language configuration is somehow invalid."
        downloadresultslinkmessage = "The current language configuration is somehow invalid."


        cloudsavingerror = "The current language configuration is somehow invalid."
        invalidapikey = "The current language configuration is somehow invalid."

        foundapikeyfile = "The current language configuration is somehow invalid."
        foundapikey = "The current language configuration is somehow invalid."
        pingspeednotputintoconsiderationmessage = "The current language configuration is somehow invalid."
        pressenterkeymessage = "The current language configuration is somehow invalid."


    # Main speedtest code:
    def processpeedtest(backupmode, filename, textlayout):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        results = s.results.dict()
        resultlist = list(results.values())
        download = str(round(resultlist[0] / 1000000)) + " mbit/s"
        upload = str(round(resultlist[1] / 1000000)) + " mbit/s"
        ping = str(resultlist[2]) + "ms"
        downloadlist.append(str(round(resultlist[0] / 1000000)))
        uploadlist.append(str(round(resultlist[1] / 1000000)))
        pinglist.append(str(round(resultlist[2])))
        if textlayout == "Text":
            fullresults = "Results: " + " Download: " + download + " Upload: " + upload + " Ping: " + ping + "."
        elif textlayout == "Plain":
            fullresults = download  + " " + upload + " " + ping
        elif textlayout == "Lists":
            fullresults = str(downloadlist) + ", " + str(uploadlist) + ", " + str(downloadlist) + "."
        elif textlayout == "Detailed-text":
            fullresults = "A test at " + str(time.ctime()) + " has been run. " + "The results was " + " Download speed (mbit/s): " + download + " Upload speed (mbit/s): " + upload + " Ping (milliseconds): " + ping + "."
        elif textlayout == "With-units":
            fullresults = "Results: " + " Download: " + download + " mbit/s " + " Upload: " + upload + " mbit/s "+ " Ping: " + ping + " milliseconds" + "."
        print(fullresults)
        if backupmode == False:

            with open(filename, "a+") as file:
                file.write(fullresults + "\n")
        elif backupmode == True:
            with open("speedtestbackup.txt", "a+") as backupfile:
                backupfile.write(fullresults + "\n")


    #(end of main speedtest code.)
    def processspeedtest_onlyupload(filename):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.upload()
        results = round(int(s.results.upload) / 1000000)
        with open(filename, "a+") as file:
            file.write("Upload: " + str(results) + " (only upload test)")




    try:
        import requests
        request = requests.get("https://www.google.com")
        print(pretestresults + str(request.elapsed.total_seconds()) + pretestresults2)
    except requests.exceptions.ConnectionError:
        print(nointernetconnectionmessage)
        noconnection = 1
        raise NoInternetConnection(nointernetconnectionmessage)
    print(lookingforupdatesmessage)
    print("\n")
    try:
        import requests
        from bs4 import BeautifulSoup

        updatecheck = requests.get("https://pispeedtestfiles.000webhostapp.com/latestversion.html")
        soup = BeautifulSoup(updatecheck.text, "html.parser")

        latestversionnumber = str(soup.get_text()).replace("\n", "")
        print(latestversionmessage + latestversionnumber + ".")
        if latestversionnumber == fileversionnumber:
            print(youhavethelatestversionmessage)
        elif float(latestversionnumber) < float(fileversionnumber):
            print(betaversionmessage + "( "+ fileversionnumber + ") . " + maybenotstable)
        else:
            releasemessage = requests.get("https://pispeedtestfiles.000webhostapp.com/releasemessage.html")
            releasemessageversion = requests.get("https://pispeedtestfiles.000webhostapp.com/releasemessageversion.html")
            soup = BeautifulSoup(releasemessageversion.text, "html.parser")
            releasemessageversionnumber = str(soup.get_text()).replace("\n", "")
            try:
                if float(releasemessageversionnumber) == float(latestversionnumber):
                    soup = BeautifulSoup(releasemessage.text, "html.parser")
                    messagefornewrelease = str(soup.get_text())
                    print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
                    print(releasemessageinformation + "\n" +  messagefornewrelease)
                else:
                    print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
            except:
                print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
    except Exception as e:
        print(lookingforupdateserror + " (" + str(e) + ").")
    print("\n")
    with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\status.txt"), "r") as cloudsavingstatustextfile:
        filecontents = cloudsavingstatustextfile.read().splitlines()
    if filecontents[0] == "ENABLED":
        print(cloudsavingenabled)
    elif filecontents[0] == "OFF":
        print(cloudsavingturnedoff)
    elif filecontents[0] == "NOT CONFIGURED":
        print(cloudsavingnotconfigured)
        confirm = input(configurecloudsavingmessage)
        if confirm == "ENABLE":
            import cloudsavingsetup
            cloudsavesetup.setup()
        else:

            print(skipingcloudsavingsetupmessage)

    print("\n")
    print(initialspeedtestinformation)
    print(normalmodedescription)
    print(accuratemodedescription)
    print(fastmodedescription)
    print(superbmodedescription)
    speedtestaccuracymode = input(speedtestmodeselection)
    initialspeedtestsfile = os.path.join(os.getcwd() + "/speedtestresults/" + "intialspeedtests.txt")
    #Message when a speedtest accuracy mode is found:
    def speedtestaccuracymodefound():
        print(speedtestaccuracymode + speedtestaccuracymodefoundmessage)
    if speedtestaccuracymode == "NORMAL" or speedtestaccuracymode.lower() == "normal":
        speedtestaccuracymodefound()
        timeone = time.time()
        if noconnection == 0:

            processpeedtest(0, filename=initialspeedtestsfile, textlayout="Text")
            speedtesttime = round(time.time() - timeone)
            print(speedtestran + str(speedtesttime) + speedtestseconds)
        elif noconnection == 1:
            print(nointernetconnectionmessage)

    elif speedtestaccuracymode == "ACCURATE" or speedtestaccuracymode.lower() == "accurate":
        timelist = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            for i in range(3):
                time1 = time.time()
                processpeedtest(False, "initialspeedtest.txt", textlayout="Text")
                timelist.append(str(round(time.time()-time1)))
                print(speedtestran + str(timelist[i]) + speedtestseconds)
            speedtesttime = round(eval("+".join(timelist)))
        elif noconnection == 1:
            print(nointernetconnectionmessage)
    elif speedtestaccuracymode == "FAST" or speedtestaccuracymode.lower() == "fast":
        timelist3 = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            timeone1 = time.time()
            processspeedtest_onlyupload("initialspeedtests.txt")
            speedtesttime = str(round((time.time() - timeone1)*2))
            print(speedtestran + str(round(int(speedtesttime)/2)) + speedtestseconds + " " + fastspeedtest)

    elif speedtestaccuracymode == "SUPERB" or speedtestaccuracymode.lower() == "superb":
        timelist2 = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            for i in range(5):
                timenumberone = time.time()
                processpeedtest(False, "initialspeedtest.txt", textlayout="Text")
                timelist2.append(str(round(time.time() - timenumberone, 1)))
                print(speedtestran + timelist2[i] + speedtestseconds)
            times = "+".join(timelist2)
            speedtesttime = round(eval(times)/5, 1)


        elif noconnection == 1:
            print(nointernetconnectionmessage)
    else:
        print(mode_error)

        exit()
    print("\n")

    try:
        configurationfile = os.path.join(os.getcwd() + "/configurationfiles/config.txt")

        with open(configurationfile, "r+") as configurationsfile:
            print(loadingconfigurationmessage)
            configurationfilecontent = configurationsfile.read().splitlines()
            if configurationfilecontent[9] in allowedmodes:
                configuredmode = configurationfilecontent[9]
                print(configuredmodemessage + configuredmode + ".")
                loadconfig[0] = 1
            elif configurationfilecontent[9] == "-SKIP-":
                print(skipdetected)
                loadconfig[0] = 0
            else:
                print(invalidmode)

                loadconfig[0] = 0
            try:
                configuredspeedtestduration1 = int(configurationfilecontent[10])
                configuredspeedtestduration = int(configuredspeedtestduration1 * 60)
                print(configuredspeedtestdurationmessage + str(configuredspeedtestduration / 60) + minutes)
                loadconfig[1] = 1
            except:
                if configurationfilecontent[10] == "-SKIP-":
                    print(skipdetected)
                    loadconfig[1] = 0
                else:
                    print(invalidduration)
                    loadconfig[1] = 0
            try:
                configuredruneverysecond = int(configurationfilecontent[11])
                print(configuredruneverysecondmessage + str(configuredruneverysecond) + seconds)
                loadconfig[2] = 1
            except:
                if configurationfilecontent[11] == "-SKIP-":
                    print(skipdetected)
                    loadconfig[2] = 0
                else:
                    print(runeverysecondinvalid)
                    loadconfig[2] = 0
        print("\n")
    except:
        print(speedtestconfignotfound)
        loadconfig[0] = 0
        loadconfig[1] = 0
        loadconfig[2] = 0
    if loadconfig[0] == 0:
        print("\n")
        print(programmodes)
        print(betamode)
        print(stablemode)
        print(compatiblemode)
        mode = input(pleaseselectaspeedtestmodemessage)
    elif loadconfig[0] == 1:
        mode = configuredmode
    else:
        print("\n")
        print(programmodes)
        print(betamode)
        print(stablemode)
        print(compatiblemode)
        mode = input(pleaseselectaspeedtestmodemessage)

    if mode == "BETA MODE" or mode.lower() == "beta mode":
        import ctypes

        print("\n")


        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        #inputmaxpingspeed = int(input(maxpingspeedinputmessage)) (not used for the connection score algorithm yet.)
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        print(speedteststartpopupmessage)
        ctypes.windll.user32.MessageBoxW(None, startingspeedtestmessage, "PiSpeedtest", 0)
        steps = int(times)


        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:
                    ctypes.windll.user32.MessageBoxW(None, errormessage, "PiSpeedtest", 0)

                    print(errormessage + "(" + str(e) + ").")

                    # This is being added in a later release:
                    # box = ctypes.windll.user32.MessageBoxW(None, "An error occured while running a speedtest. Would you like to try again? Everything will restart. The file with new speedtest data will be namned \"speedtestbackup.txt\".", "PiSpeedtest", 5)
                    # if box == 1:
                    # print(Running speedtest once more.")
                    # for speedtestindex in range(repeat):

                    # print("A speedtest is being started.")
                    # processpeedtest(0, filename="speedtestbackup.txt")
                    # print("A speedtest has been completed.")
                    # time.sleep(interval)
                    # elif box == 2:
                    # print("Quitting PiSpeedtest because of an error.")
                    # else:
                    # print("Quitting PiSpeedtest because of an error.")
            print("\n")
            try:
                from PIL import Image, ImageDraw, ImageFont


                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount)/len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount)/(len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount)/len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed/ 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")


                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"),"w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " +  "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)

    elif mode == "STABLE" or mode.lower() == "stable":
        import ctypes

        print("\n")

        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        print(speedteststartpopupmessage)
        ctypes.windll.user32.MessageBoxW(None, startingspeedtestmessage, "PiSpeedtest", 0)
        steps = int(times)

        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:
                    ctypes.windll.user32.MessageBoxW(None, errormessage, "PiSpeedtest", 0)

                    print(errormessage + "(" + str(e) + ").")
            print("\n")


            try:
                from PIL import Image, ImageDraw, ImageFont

                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount) / len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount) / (len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount) / len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(
                    mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(
                    os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")

                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace(
                                "A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"),"w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)
    elif mode == "COMPATIBLE" or mode.lower() == "compatible":
        print("\n")

        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        steps = int(times)

        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:

                    print(errormessage + "(" + str(e) + ").")
            print("\n")

            try:
                from PIL import Image, ImageDraw, ImageFont

                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount) / len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount) / (len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount) / len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(
                    mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(
                    os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")

                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"), "w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)
    else:
        print(invalidmodeselected)
        raise NoModeDefinded("\"" + mode + "\"" + " is not a valid mode.")

except Exception as e:

    print(erroroccurred + " (" + str(e) + ").")

finally:




    print("\n")
    input(pressenterkeymessage)
try:
    import speedtest

    import time


    import os


    # Defining errors - These are not implemented that much yet.
    def __main__():
        pass
    class PiSpeedtestErrors(Exception):
        pass


    class NoModeDefinded(PiSpeedtestErrors):
        pass


    class FileError(PiSpeedtestErrors):
        pass

    class NoInternetConnection(PiSpeedtestErrors):
        pass

    class UpdatecheckServerError(NoInternetConnection):
        pass


    downloadlist = []
    uploadlist = []
    pinglist = []

    smallestkbitsup = 1000
    largestkbitsup = 0
    smallestkbitsdown = 1000
    largestkbitsdown = 0
    noconnection = 0
    fileversionnumber = "3.5"
    allowedmodes = ["BETA MODE", "STABLE", "COMPATIBLE"]
    loadconfig = [0, 0, 0, 0, 0]

    allowedtextlayouts = ["Text", "Plain", "Lists", "Detailed-text", "With-units"]

    fontfilename = "Roboto-Bold.ttf" #Add a custom font filename here if you want a custom font for the images. Don´t forget the file extension! Only .ttf-files supported.
    print("PiSpeedtest " + fileversionnumber + ".")
    # Language settings:
    approved_languages = ["sv-se", "en-us"]  # To add a language that´s not in the list, make sure to add its name here.
    languageconfigpath = os.path.join(os.getcwd() + "/configurationfiles/languageconfiguration.txt")
    try:
        with open(languageconfigpath, "r+") as languagecofigurationfile:
            languageconfig = languagecofigurationfile.read().splitlines()
    except:
        print("Could not find language configuration. Please make sure that \"languageconfiguration.txt\" is in the directory /configurationfiles.")
        languageconfig = ["Configuration not found." + "ConfigurationNotFound"]
    if languageconfig[1] not in approved_languages:
        print("The current language configuration is not valid. Please check the file languageconfiguration.txt. Valid languages are:")
        for i in range(len(approved_languages)):
            print(approved_languages[i])
        languageconfiguration = "sv-se"
        print("For this time, the language has been set to sv-se, Swedish.")
    else:
        print("Language configuration " + str(languageconfig[1]) + " found.")
        languageconfiguration = languageconfig[1]
    print("\n")
    # Language configuration - feel free to add your own languages here!
    if languageconfiguration == "sv-se":
        pretestresults = "Pre-test-resultat: Ping till https://www.google.com. Resultat: "
        pretestresults2 = " sekunder."
        nointernetconnectionmessage = "En aktiv internetuppkopppling kunde inte hittas."
        lookingforupdatesmessage = "Letar efter uppdateringar..."
        latestversionmessage = "Senaste versionen av PiSpeedtest är: "
        youhavethelatestversionmessage = "Du har den senaste versionen av PiSpeedtest."
        initialspeedtestinformation = "För att få programmet att fungera optimalt så körs ett \"speedtest\" för att mäta tid m.m. Vänligen vänta."
        speedtestran = "Ett speedtest har nu körts. Det tog: "
        speedtestseconds = " sekunder."
        programmodes = "Programlägen:"
        stablemode = "STABLE - Kör de stabila funktionerna i PiSpeedtest."
        betamode = "BETA MODE - Betafunktioner som kan innehålla buggar."
        compatiblemode = "COMPATIBLE - Välj detta läge för kompatibilitet med Mac, vissa Linuxsystem eller andra system än Windows. En stabil version kommer att köras, inte en betaversion."
        pleaseselectaspeedtestmodemessage = "Vänligen välj ett PiSpeedtest-läge genom att skriva dess namn och trycka på enter: "
        programdurationseconds = "Hur länge vill du köra programmet (i sekunder)? 12 timmar = 43 200 sekunder: "

        programdurationminutes = "Hur länge vill du köra programmet (i minuter)? 12 timmar = 720 minuter: "
        howofteninput = "Hur ofta vill du köra programmet (i sekunder) tar cirka "
        seconds = " sekunder. "
        speedtestfilenameinput = "Vilket namn vill du ha på speedtestfilen? Använd inte punkter eller .txt, det läggs till automatiskt. "
        errormessage = "Ett fel inträffade när ett speedtest skulle köras."
        startingspeedtestmessage = "Startar test."
        speedtestcompletedmessage = "Test utfört."
        programdurationmodemessage = "Vill du ange hur länge du vill köra programmet i sekunder eller minuter? (Skriv \"SECONDS\" eller \"MINUTES\" för att välja.)"
        programdurationmodeerror = "Ett fel inträffade. Skrev du rätt när du valde läge? Läget \"MINUTES\" kommer att väljas automatiskt."
        newversionmessage = "Version: "
        newversionmessage2 = " av PiSpeedtest finns tillgänglig. Du har version: "
        newversionmessage3 = " installerad."
        lookingforupdateserror = "Ett fel inträffade när PiSpeedtest sökte efter nya uppdateringar."

        skipdetected = "SKIP DETEKTERAT"
        speedtestconfignotfound = "Kunde inte hitta konfigurationsfilen."
        loadingconfigurationmessage = "Laddar konfiguration..."
        configuredmodemessage = "Det konfiguerade läget är: "
        minutes = " minuter."
        configuredspeedtestdurationmessage = "Konfiguerad speedtest-tid: "
        invalidmode = "Konfigurationsfilen innehåller ett felaktigt läge."
        invalidduration = "Konfigurationsfilen innehåller en ogiltig spedtest-tid."
        configuredruneverysecondmessage = "Konfiguerad \"kör var ___ sekund\": "
        runeverysecondinvalid = "\"Kör var ___ sekund\"-konfigurationen är felaktig."
        invalidmodeselected = "Du valde inte ett giltigt program-läge. Vänligen starta om PiSpeedtest."
        waiterror = "Ett fel inträffad när speedtest-tider skulle beräknas. \"Kör programmet var ___ - sekund måste vara större än: "
        betaversionmessage = "Det verkar som att du använder en betaversion av PiSpeedtest "
        maybenotstable = "Betaversioner kan innehålla buggar och vara ostadiga."
        erroroccurred = "Ett fel inträffade när PiSpeedtest kördes. Fel: "

        normalmodedescription = "NORMAL - Endast ett speedtest kommer att köras för att mäta tid m.m."
        accuratemodedescription = "ACCURATE - Tre stycken speedtests kommer att köras för att mäta tid m.m, vilket betyder bättre nogrannhet. Detta tar cirka en minut."
        fastmodedescription = "FAST - Detta läge testar bara uppladdningshastigheten och multiplicerar den med två för att få tidsdata. Resultaten är inte nogranna, men programmet initieras snabbare."
        superbmodedescription = "SUPERB - Fem speedtests kommer att köras, vilket bara rekommenderas när du behöver en exakt tidsavläsning. Detta läge avrundar tidsdata till en decimal, vilket är mer exakt än andra lägen. Detta läge kommer dock att ta två minuter att köra."
        mode_error = "Ett fel inträffade när du skulle välja läge. Starta om PiSpeedtest och se till att läget är korrekt skrivet."
        fastspeedtest = "Detta speedtest testade bara uppladdningshastigheten."
        fastspeedtestnotice = "FÖR ATT FÅ PROGRAMMET ATT VARA SÅ NOGRANNT SOM MÖJLIGT REKOMMENDERAS DETTA LÄGE (\"FAST\") EJ!"
        speedtestmodeselection = "Skriv lägets namn och tryck sedan enter för att välja det: "
        programoptionsmessage = "Det finns olika alternativ för hur resultaten ska formatteras/skrivas ut. Här är en lista: "
        textoptionmessage = "Text - Resultaten är formatterade med hjälp av enkla ord och resultaten.(PiSpeedtest´s standard-layout)"
        plainoptionmessage = "Plain - Visar endast resultaten i siffror (Nedladdning, uppladdning och pinghastigheter). Ingen text. Resultaten är separerade med hjälp av mellanrum."
        listsoptionmessage = "Lists - Visar alla resultat från varje speedtest som körs sedan programet startades. (rekommenderas endast för debugging etc.)"
        detailedtextoptionsmessage = "Detailed-text - Perfekt för att presentera datan till allmänheten eftersom enheter, kommentarer och tidsstämplar är inkluderade."
        withunitsoptionsmessage = "With-units - Samma som \"Text\"-alternativet, men med enheter utskrivna."
        textlayoutconfigurationmessage = "Välj ett läge genom att skriva dess namn (t.ex. \"Text\") och sedan trycka på enter: "
        invalidtextlayout = "Du valde ett felaktigt läge. Standardläget, \"Text\" kommer att väljas istället."
        imagegenerationerror = "Ett fel inträffade när en resultat-bild skulle genereras."

        speedteststartpopupmessage = "Ett popupfönster kommer nu att visas. Kom ihåg att trycka på \"Ok\". Om du inte gör det så kommer ett speedtest inte att startas."

        releasemessageinformation = "Det finns ett meddelade angående den senaste versionen, vilket är: "
        speedtestaccuracymodefoundmessage = " har valts som speedtest-nogrannhets-läge."

        cloudsavingturnedoff = "Din molnlagring för PiSpeedtest är avstängd."
        cloudsavingenabled = "Din molnlagring för PiSpeedtest är aktiverad."
        cloudsavingnotconfigured = "Du har inte konfigurerat molnlagring för PiSpeedtest."
        configurecloudsavingmessage = "Skriv \"ENABLE\" och tryck enter för att aktivera molnlagring eller skriv \"NO\" för att gå vidare utan att konfiguera molnlagring. "
        skipingcloudsavingsetupmessage = "Okej, skippar setup-programmet."
        maxdownloadspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (nedladdningshastighet)?: "
        maxuploadspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (uppladdningshastighet)?: "
        maxpingspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (pinghastighet)?: "
        connectiontypeinputmessage = "Vilken uppkopplingstyp har du?? WIFI, CABLE eller CELLULAR: "

        speedtestimagesaved = "En speedtest-resultatsbild har nu sparats i mappen \"images\"."
        cloudsavingerror = "Ett fel inträffade när PiSpeedtest-resultaten skulle laddas upp till molnet."
        invalidapikey = "Din nuvarande API-nycjek för molnlagring är felaktig."
        foundapikeyfile = "Filen \"apikey.txt\" hittades. Letar efter API-nyckel."
        foundapikey = "En gilltig API-nyckel för molnlagring hittades."
        pingspeednotputintoconsiderationmessage = " Ping-hastighet är ej med i beräkningen."
        pressenterkeymessage = "Tryck på enter-knappen för att stänga PiSpeedtest."
    elif languageconfiguration == "en-us":
        pretestresults = "Pre-test-result: Ping to https://www.google.com. Result: "
        pretestresults2 = " seconds."
        nointernetconnectionmessage = "An active internet connection could not be established."
        lookingforupdatesmessage = "Looking for updates..."
        latestversionmessage = "The latest version of PiSpeedtest is: "
        youhavethelatestversionmessage = "You have the latest version of PiSpeedtest."
        initialspeedtestinformation = "To make the program work better, a \"speedtest\" is being run in the beginning of the program. You can choose between three different modes:"
        speedtestran = "A speedtest has now been run. It took: "
        speedtestseconds = " seconds."
        programmodes = "Program-modes:"
        stablemode = "STABLE - Run the stable and tested functions in PiSpeedtest."
        betamode = "BETA MODE - Functions in beta that might not work properly."
        compatiblemode = "COMPATIBLE - Select this mode for compatibility with more operating systems than Windows, including Mac, some Linux OSes and other operating systems. A stable release is being run, not a beta release."
        pleaseselectaspeedtestmodemessage = "Please select a PiSpeedtest-mode by typing its name and then pressing enter on your keyboard: "
        programdurationseconds = "For how long do you want to run the program (in seconds)? 12 hours = 43 200 seconds: "

        programdurationminutes = "For how long do you want to run the program (in minutes)? 12 hours = 720 minutes: "
        howofteninput = "How often do you want to run the program (in seconds)? A speedtest takes about "
        seconds = " seconds. "
        speedtestfilenameinput = "What name would you like the speedtestfile to have? Do not use any dots or .txt, it will be added automatically. "
        errormessage = "An error occured during the speedtest."
        startingspeedtestmessage = "Starting speedtest."
        speedtestcompletedmessage = "A speedtest has been run."
        programdurationmodemessage = "Do you want to enter how long you want to run the program in seconds or minutes? (Write \"SECONDS\" or \"MINUTES\" to select.) "
        programdurationmodeerror = "An error occured. Did you type everything in correctly when you choosed an option? The option \"MINUTES\" will be selected automatically. "
        newversionmessage = "Version: "
        newversionmessage2 = " of PiSpeedtest is available. You have version: "
        newversionmessage3 = " installed."
        lookingforupdateserror = "An error occured while looking for updates."
        skipdetected = "SKIP DETECTED"
        speedtestconfignotfound = "Could not find the configuration file."
        loadingconfigurationmessage = "Loading configuration..."
        languageconfigurationnotfound = "Could not find the language configuration file."
        configuredmodemessage = "The configured mode is: "
        minutes = " minutes."
        configuredspeedtestdurationmessage = "Configured speedtest duration: "
        invalidmode = "The speedtest file contains an invalid mode."
        invalidduration = "The speedtest file contains an invalid speedtest duration."
        configuredruneverysecondmessage = "Configured \"run every ___ seconds\": "
        runeverysecondinvalid = "The \"run every ___ seconds\" configuration is invalid."
        invalidmodeselected = "You didn´t select a valid mode. Please restart PiSpeedtest."
        waiterror = "An error occured when calculating speedtest wait times. Make sure that it is bigger than: "
        betaversionmessage = "It looks like you are running a beta version of PiSpeedtest "
        maybenotstable = "Beta versions may contain bugs and be unstable."

        erroroccurred = "An error occured while running PiSpeedtest. Error: "
        normalmodedescription = "NORMAL - Only one speedtest will be run to measure time."
        accuratemodedescription = "ACCURATE - Three speedtests will be run to measure time, which means increased accuracy. This takes about one minute."
        fastmodedescription = "FAST - This mode only tests the upload speed and then multiplies it by two to get time data. The results are not accurate, but the program loads faster."
        superbmodedescription = "SUPERB - Five speedtests will be run to measure time, which is only recommended for times when you need a perfect time measurement. This mode rounds the time to one decimal, which is more accurate than other modes. You have to wait about two minutes, though."
        speedtestaccuracymodefoundmessage = " has been chosen as speedtest accuracy mode."
        mode_error = "An error occurent when you selected a mode. Restart PiSpeedtest and make surte to enter the mode correctly."
        fastspeedtest = "This speedtest only tested the upload speed."
        fastspeedtestnotice = "TO MAKE THE PROGRAM ACCURATE ENOUGH, THIS MODE (\"FAST\") IS NOT RECOMMENDED!"
        speedtestmodeselection = "Type the mode´s name and then press enter to select it: "
        programoptionsmessage = "There are different types of options for how to format the results. Here is a list: "
        textoptionmessage = "Text - The results are formatted using simple words and the results. (the standard PiSpeedtest layout)"
        plainoptionmessage = "Plain - Only get the result values (Download, upload and ping speeds). No text. The values are separated using spaces."
        listsoptionmessage = "Lists - Shows all the results from every speedtest done since running the program. (this is only recommended for debugging etc.)"
        detailedtextoptionsmessage = "Detailed-text - Perfect for copy-pasting the data and presenting to the public as units, comments and timestamps are included."
        withunitsoptionsmessage = "With-units - The same as the \"Text\"-option, but with units."
        textlayoutconfigurationmessage = "Choose a mode by typing its name (e.g \"Text\") and the pressing enter: "
        invalidtextlayout = "You selected an invalid text layout. The standard text formatting mode, \"Text\" will be selected instead."
        imagegenerationerror = "An error occured while generating a results image."
        speedteststartpopupmessage = "A popup window will now be shown. Be sure to tap \"Ok\". If you don´t do that, the speedtests won´t start."

        releasemessageinformation = "There is a message about this release, which is: "
        speedtestaccuracymodemfoundessage = " has been selected as the speedtest accuracy mode."
        cloudsavingturnedoff = "Your cloudsaving for PiSpeedtest is currently turned off."
        cloudsavingenabled = "You have PiSpeedtest cloudsaving enabled."
        cloudsavingnotconfigured = "You haven´t configured cloudsaving for PiSpeedtest."


        configurecloudsavingmessage = "Type \"ENABLE\" and press enter to enable cloudsaving or type \"NO\" to skip. "

        skipingcloudsavingsetupmessage = "Okay, skipping setup."
        maxdownloadspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using (download speed)? "

        maxuploadspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using? (upload speed)?: "
        maxpingspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using (ping speed)? "

        connectiontypeinputmessage = "What connection type are you using? WIFI, CABLE or CELLULAR: "
        speedtestimagesaved = "A result image has been generated and saved in the directory \"images\"."

        generatingspeedtestreportmessage = "Generating speedtest report..."
        savedspeedtestreportmessage = "A speedtest report has been saved."
        cloudserverreponsemessage = "Cloudsaving server response: "
        viewresultslinkmessage = "View your speedtest results here: "
        downloadresultslinkmessage = "Additionally, the speedtest results can be downloaded here: "


        cloudsavingerror = "An error occured while cloudsaving PiSpeedtest results. "
        invalidapikey = "Your current cloudsaving API key is invalid."
        foundapikeyfile = "The file \"apikey.txt\" was found. Looking for API-key."

        pressenterkeymessage = "Press the enter key to close PiSpeedtest."
        foundapikey = "A valid cloudsaving API keywas found."
        pingspeednotputintoconsiderationmessage = " Ping speed is not put into consideration."
        pressenterkeymessage = "Press the enter key to close PiSpeedtest."
    else:
        pretestresults = "The current language configuration is somehow invalid."
        pretestresults2 = "The current language configuration is somehow invalid."
        nointernetconnectionmessage = "The current language configuration is somehow invalid."
        lookingforupdatesmessage = "The current language configuration is somehow invalid."
        latestversionmessage = "The current language configuration is somehow invalid."
        youhavethelatestversionmessage = "The current language configuration is somehow invalid."
        initialspeedtestinformation = "The current language configuration is somehow invalid."
        speedtestran = "The current language configuration is somehow invalid."
        speedtestseconds = "The current language configuration is somehow invalid."
        programmodes = "The current language configuration is somehow invalid."
        stablemode = "The current language configuration is somehow invalid."
        betamode = "The current language configuration is somehow invalid."
        compatiblemode = "The current language configuration is somehow invalid."
        pleaseselectaspeedtestmodemessage = "The current language configuration is somehow invalid."
        programdurationseconds = "The current language configuration is somehow invalid."

        programdurationminutes = "The current language configuration is somehow invalid."
        howofteninput = "The current language configuration is somehow invalid."
        seconds = "The current language configuration is somehow invalid."
        speedtestfilenameinput = "The current language configuration is somehow invalid."
        errormessage = "The current language configuration is somehow invalid."
        startingspeedtestmessage = "The current language configuration is somehow invalid."
        speedtestcompletedmessage = "The current language configuration is somehow invalid."
        programdurationmodemessage = "The current language configuration is somehow invalid."
        programdurationmodeerror = "The current language configuration is somehow invalid."
        newversionmessage = "The current language configuration is somehow invalid."
        newversionmessage2 = "The current language configuration is somehow invalid."
        newversionmessage3 = "The current language configuration is somehow invalid."

        lookingforupdateserror = "The current language configuration is somehow invalid."
        skipdetected = "The current language configuration is somehow invalid."
        speedtestconfignotfound = "The current language configuration is somehow invalid."
        loadingconfigurationmessage = "The current language configuration is somehow invalid."
        configuredmodemessage = "The current language configuration is somehow invalid."

        minutes = "The current language configuration is somehow invalid."
        configuredspeedtestdurationmessage = "The current language configuration is somehow invalid."
        invalidmode = "The current language configuration is somehow invalid."
        invalidduration = "The current language configuration is somehow invalid."
        configuredruneverysecondmessage = "The current language configuration is somehow invalid."
        runeverysecondinvalid = "The current language configuration is somehow invalid."
        invalidmodeselected = "The current language configuration is somehow invalid."
        waiterror = "The current language configuration is somehow invalid."
        betaversionmessage = "The current language configuration is somehow invalid."
        maybenotstable =  "The current language configuration is somehow invalid."
        erroroccurred = "The current language configuration is somehow invalid."
        normalmodedescription = "The current language configuration is somehow invalid."
        accuratemodedescription = "The current language configuration is somehow invalid."
        superbmodedescription = "The current language configuration is somehow invalid."
        mode_error = "The current language configuration is somehow invalid."
        fastspeedtest = "The current language configuration is somehow invalid."
        fastspeedtestnotice = "The current language configuration is somehow invalid."
        speedtestmodeselection = "The current language configuration is somehow invalid."
        programoptionsmessage = "The current language configuration is somehow invalid."
        textoptionmessage = "The current language configuration is somehow invalid."
        plainoptionmessage = "The current language configuration is somehow invalid."
        listsoptionmessage = "The current language configuration is somehow invalid."
        detailedtextoptionsmessage = "The current language configuration is somehow invalid."
        withunitsoptionsmessage = "The current language configuration is somehow invalid."
        invalidtextlayout = "The current language configuration is somehow invalid."
        imagegenerationerror = "The current language configuration is somehow invalid."
        speedteststartpopupmessage = "The current language configuration is somehow invalid."
        releasemessageinformation = "The current language configuration is somehow invalid."
        speedtestaccuracymodefoundmessage = "The current language configuration is somehow invalid."
        cloudsavingturnedoff = "The current language configuration is somehow invalid."
        cloudsavingenabled = "The current language configuration is somehow invalid."
        cloudsavingnotconfigured = "The current language configuration is somehow invalid."
        configurecloudsavingmessage = "The current language configuration is somehow invalid."
        skipingcloudsavingsetupmessage = "The current language configuration is somehow invalid."
        maxdownloadspeedinputmessage = "The current language configuration is somehow invalid."
        maxuploadspeedinputmessage = "The current language configuration is somehow invalid."
        maxpingspeedinputmessage = "The current language configuration is somehow invalid."
        connectiontypeinputmessage = "The current language configuration is somehow invalid."
        speedtestimagesaved = "The current language configuration is somehow invalid."
        generatingspeedtestreportmessage = "The current language configuration is somehow invalid."
        savedspeedtestreportmessage = "The current language configuration is somehow invalid."
        cloudserverreponsemessage = "The current language configuration is somehow invalid."
        viewresultslinkmessage = "The current language configuration is somehow invalid."
        downloadresultslinkmessage = "The current language configuration is somehow invalid."


        cloudsavingerror = "The current language configuration is somehow invalid."
        invalidapikey = "The current language configuration is somehow invalid."

        foundapikeyfile = "The current language configuration is somehow invalid."
        foundapikey = "The current language configuration is somehow invalid."
        pingspeednotputintoconsiderationmessage = "The current language configuration is somehow invalid."
        pressenterkeymessage = "The current language configuration is somehow invalid."


    # Main speedtest code:
    def processpeedtest(backupmode, filename, textlayout):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        results = s.results.dict()
        resultlist = list(results.values())
        download = str(round(resultlist[0] / 1000000)) + " mbit/s"
        upload = str(round(resultlist[1] / 1000000)) + " mbit/s"
        ping = str(resultlist[2]) + "ms"
        downloadlist.append(str(round(resultlist[0] / 1000000)))
        uploadlist.append(str(round(resultlist[1] / 1000000)))
        pinglist.append(str(round(resultlist[2])))
        if textlayout == "Text":
            fullresults = "Results: " + " Download: " + download + " Upload: " + upload + " Ping: " + ping + "."
        elif textlayout == "Plain":
            fullresults = download  + " " + upload + " " + ping
        elif textlayout == "Lists":
            fullresults = str(downloadlist) + ", " + str(uploadlist) + ", " + str(downloadlist) + "."
        elif textlayout == "Detailed-text":
            fullresults = "A test at " + str(time.ctime()) + " has been run. " + "The results was " + " Download speed (mbit/s): " + download + " Upload speed (mbit/s): " + upload + " Ping (milliseconds): " + ping + "."
        elif textlayout == "With-units":
            fullresults = "Results: " + " Download: " + download + " mbit/s " + " Upload: " + upload + " mbit/s "+ " Ping: " + ping + " milliseconds" + "."
        print(fullresults)
        if backupmode == False:

            with open(filename, "a+") as file:
                file.write(fullresults + "\n")
        elif backupmode == True:
            with open("speedtestbackup.txt", "a+") as backupfile:
                backupfile.write(fullresults + "\n")


    #(end of main speedtest code.)
    def processspeedtest_onlyupload(filename):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.upload()
        results = round(int(s.results.upload) / 1000000)
        with open(filename, "a+") as file:
            file.write("Upload: " + str(results) + " (only upload test)")




    try:
        import requests
        request = requests.get("https://www.google.com")
        print(pretestresults + str(request.elapsed.total_seconds()) + pretestresults2)
    except requests.exceptions.ConnectionError:
        print(nointernetconnectionmessage)
        noconnection = 1
        raise NoInternetConnection(nointernetconnectionmessage)
    print(lookingforupdatesmessage)
    print("\n")
    try:
        import requests
        from bs4 import BeautifulSoup

        updatecheck = requests.get("https://pispeedtestfiles.000webhostapp.com/latestversion.html")
        soup = BeautifulSoup(updatecheck.text, "html.parser")

        latestversionnumber = str(soup.get_text()).replace("\n", "")
        print(latestversionmessage + latestversionnumber + ".")
        if latestversionnumber == fileversionnumber:
            print(youhavethelatestversionmessage)
        elif float(latestversionnumber) < float(fileversionnumber):
            print(betaversionmessage + "( "+ fileversionnumber + ") . " + maybenotstable)
        else:
            releasemessage = requests.get("https://pispeedtestfiles.000webhostapp.com/releasemessage.html")
            releasemessageversion = requests.get("https://pispeedtestfiles.000webhostapp.com/releasemessageversion.html")
            soup = BeautifulSoup(releasemessageversion.text, "html.parser")
            releasemessageversionnumber = str(soup.get_text()).replace("\n", "")
            try:
                if float(releasemessageversionnumber) == float(latestversionnumber):
                    soup = BeautifulSoup(releasemessage.text, "html.parser")
                    messagefornewrelease = str(soup.get_text())
                    print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
                    print(releasemessageinformation + "\n" +  messagefornewrelease)
                else:
                    print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
            except:
                print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
    except Exception as e:
        print(lookingforupdateserror + " (" + str(e) + ").")
    print("\n")
    with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\status.txt"), "r") as cloudsavingstatustextfile:
        filecontents = cloudsavingstatustextfile.read().splitlines()
    if filecontents[0] == "ENABLED":
        print(cloudsavingenabled)
    elif filecontents[0] == "OFF":
        print(cloudsavingturnedoff)
    elif filecontents[0] == "NOT CONFIGURED":
        print(cloudsavingnotconfigured)
        confirm = input(configurecloudsavingmessage)
        if confirm == "ENABLE":
            import cloudsavingsetup
            cloudsavesetup.setup()
        else:

            print(skipingcloudsavingsetupmessage)

    print("\n")
    print(initialspeedtestinformation)
    print(normalmodedescription)
    print(accuratemodedescription)
    print(fastmodedescription)
    print(superbmodedescription)
    speedtestaccuracymode = input(speedtestmodeselection)
    initialspeedtestsfile = os.path.join(os.getcwd() + "/speedtestresults/" + "intialspeedtests.txt")
    #Message when a speedtest accuracy mode is found:
    def speedtestaccuracymodefound():
        print(speedtestaccuracymode + speedtestaccuracymodefoundmessage)
    if speedtestaccuracymode == "NORMAL" or speedtestaccuracymode.lower() == "normal":
        speedtestaccuracymodefound()
        timeone = time.time()
        if noconnection == 0:

            processpeedtest(0, filename=initialspeedtestsfile, textlayout="Text")
            speedtesttime = round(time.time() - timeone)
            print(speedtestran + str(speedtesttime) + speedtestseconds)
        elif noconnection == 1:
            print(nointernetconnectionmessage)

    elif speedtestaccuracymode == "ACCURATE" or speedtestaccuracymode.lower() == "accurate":
        timelist = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            for i in range(3):
                time1 = time.time()
                processpeedtest(False, "initialspeedtest.txt", textlayout="Text")
                timelist.append(str(round(time.time()-time1)))
                print(speedtestran + str(timelist[i]) + speedtestseconds)
            speedtesttime = round(eval("+".join(timelist)))
        elif noconnection == 1:
            print(nointernetconnectionmessage)
    elif speedtestaccuracymode == "FAST" or speedtestaccuracymode.lower() == "fast":
        timelist3 = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            timeone1 = time.time()
            processspeedtest_onlyupload("initialspeedtests.txt")
            speedtesttime = str(round((time.time() - timeone1)*2))
            print(speedtestran + str(round(int(speedtesttime)/2)) + speedtestseconds + " " + fastspeedtest)

    elif speedtestaccuracymode == "SUPERB" or speedtestaccuracymode.lower() == "superb":
        timelist2 = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            for i in range(5):
                timenumberone = time.time()
                processpeedtest(False, "initialspeedtest.txt", textlayout="Text")
                timelist2.append(str(round(time.time() - timenumberone, 1)))
                print(speedtestran + timelist2[i] + speedtestseconds)
            times = "+".join(timelist2)
            speedtesttime = round(eval(times)/5, 1)


        elif noconnection == 1:
            print(nointernetconnectionmessage)
    else:
        print(mode_error)

        exit()
    print("\n")

    try:
        configurationfile = os.path.join(os.getcwd() + "/configurationfiles/config.txt")

        with open(configurationfile, "r+") as configurationsfile:
            print(loadingconfigurationmessage)
            configurationfilecontent = configurationsfile.read().splitlines()
            if configurationfilecontent[9] in allowedmodes:
                configuredmode = configurationfilecontent[9]
                print(configuredmodemessage + configuredmode + ".")
                loadconfig[0] = 1
            elif configurationfilecontent[9] == "-SKIP-":
                print(skipdetected)
                loadconfig[0] = 0
            else:
                print(invalidmode)

                loadconfig[0] = 0
            try:
                configuredspeedtestduration1 = int(configurationfilecontent[10])
                configuredspeedtestduration = int(configuredspeedtestduration1 * 60)
                print(configuredspeedtestdurationmessage + str(configuredspeedtestduration / 60) + minutes)
                loadconfig[1] = 1
            except:
                if configurationfilecontent[10] == "-SKIP-":
                    print(skipdetected)
                    loadconfig[1] = 0
                else:
                    print(invalidduration)
                    loadconfig[1] = 0
            try:
                configuredruneverysecond = int(configurationfilecontent[11])
                print(configuredruneverysecondmessage + str(configuredruneverysecond) + seconds)
                loadconfig[2] = 1
            except:
                if configurationfilecontent[11] == "-SKIP-":
                    print(skipdetected)
                    loadconfig[2] = 0
                else:
                    print(runeverysecondinvalid)
                    loadconfig[2] = 0
        print("\n")
    except:
        print(speedtestconfignotfound)
        loadconfig[0] = 0
        loadconfig[1] = 0
        loadconfig[2] = 0
    if loadconfig[0] == 0:
        print("\n")
        print(programmodes)
        print(betamode)
        print(stablemode)
        print(compatiblemode)
        mode = input(pleaseselectaspeedtestmodemessage)
    elif loadconfig[0] == 1:
        mode = configuredmode
    else:
        print("\n")
        print(programmodes)
        print(betamode)
        print(stablemode)
        print(compatiblemode)
        mode = input(pleaseselectaspeedtestmodemessage)

    if mode == "BETA MODE" or mode.lower() == "beta mode":
        import ctypes

        print("\n")


        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        #inputmaxpingspeed = int(input(maxpingspeedinputmessage)) (not used for the connection score algorithm yet.)
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        print(speedteststartpopupmessage)
        ctypes.windll.user32.MessageBoxW(None, startingspeedtestmessage, "PiSpeedtest", 0)
        steps = int(times)


        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:
                    ctypes.windll.user32.MessageBoxW(None, errormessage, "PiSpeedtest", 0)

                    print(errormessage + "(" + str(e) + ").")

                    # This is being added in a later release:
                    # box = ctypes.windll.user32.MessageBoxW(None, "An error occured while running a speedtest. Would you like to try again? Everything will restart. The file with new speedtest data will be namned \"speedtestbackup.txt\".", "PiSpeedtest", 5)
                    # if box == 1:
                    # print(Running speedtest once more.")
                    # for speedtestindex in range(repeat):

                    # print("A speedtest is being started.")
                    # processpeedtest(0, filename="speedtestbackup.txt")
                    # print("A speedtest has been completed.")
                    # time.sleep(interval)
                    # elif box == 2:
                    # print("Quitting PiSpeedtest because of an error.")
                    # else:
                    # print("Quitting PiSpeedtest because of an error.")
            print("\n")
            try:
                from PIL import Image, ImageDraw, ImageFont


                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount)/len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount)/(len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount)/len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed/ 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")


                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"),"w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " +  "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)

    elif mode == "STABLE" or mode.lower() == "stable":
        import ctypes

        print("\n")

        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        print(speedteststartpopupmessage)
        ctypes.windll.user32.MessageBoxW(None, startingspeedtestmessage, "PiSpeedtest", 0)
        steps = int(times)

        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:
                    ctypes.windll.user32.MessageBoxW(None, errormessage, "PiSpeedtest", 0)

                    print(errormessage + "(" + str(e) + ").")
            print("\n")


            try:
                from PIL import Image, ImageDraw, ImageFont

                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount) / len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount) / (len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount) / len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(
                    mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(
                    os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")

                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace(
                                "A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"),"w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)
    elif mode == "COMPATIBLE" or mode.lower() == "compatible":
        print("\n")

        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        steps = int(times)

        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:

                    print(errormessage + "(" + str(e) + ").")
            print("\n")

            try:
                from PIL import Image, ImageDraw, ImageFont

                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount) / len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount) / (len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount) / len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(
                    mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(
                    os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")

                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"), "w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)
    else:
        print(invalidmodeselected)
        raise NoModeDefinded("\"" + mode + "\"" + " is not a valid mode.")

except Exception as e:

    print(erroroccurred + " (" + str(e) + ").")

finally:




    print("\n")
    input(pressenterkeymessage)
try:
    import speedtest

    import time


    import os


    # Defining errors - These are not implemented that much yet.
    def __main__():
        pass
    class PiSpeedtestErrors(Exception):
        pass


    class NoModeDefinded(PiSpeedtestErrors):
        pass


    class FileError(PiSpeedtestErrors):
        pass

    class NoInternetConnection(PiSpeedtestErrors):
        pass

    class UpdatecheckServerError(NoInternetConnection):
        pass


    downloadlist = []
    uploadlist = []
    pinglist = []

    smallestkbitsup = 1000
    largestkbitsup = 0
    smallestkbitsdown = 1000
    largestkbitsdown = 0
    noconnection = 0
    fileversionnumber = "3.5"
    allowedmodes = ["BETA MODE", "STABLE", "COMPATIBLE"]
    loadconfig = [0, 0, 0, 0, 0]

    allowedtextlayouts = ["Text", "Plain", "Lists", "Detailed-text", "With-units"]

    fontfilename = "Roboto-Bold.ttf" #Add a custom font filename here if you want a custom font for the images. Don´t forget the file extension! Only .ttf-files supported.
    print("PiSpeedtest " + fileversionnumber + ".")
    # Language settings:
    approved_languages = ["sv-se", "en-us"]  # To add a language that´s not in the list, make sure to add its name here.
    languageconfigpath = os.path.join(os.getcwd() + "/configurationfiles/languageconfiguration.txt")
    try:
        with open(languageconfigpath, "r+") as languagecofigurationfile:
            languageconfig = languagecofigurationfile.read().splitlines()
    except:
        print("Could not find language configuration. Please make sure that \"languageconfiguration.txt\" is in the directory /configurationfiles.")
        languageconfig = ["Configuration not found." + "ConfigurationNotFound"]
    if languageconfig[1] not in approved_languages:
        print("The current language configuration is not valid. Please check the file languageconfiguration.txt. Valid languages are:")
        for i in range(len(approved_languages)):
            print(approved_languages[i])
        languageconfiguration = "sv-se"
        print("For this time, the language has been set to sv-se, Swedish.")
    else:
        print("Language configuration " + str(languageconfig[1]) + " found.")
        languageconfiguration = languageconfig[1]
    print("\n")
    # Language configuration - feel free to add your own languages here!
    if languageconfiguration == "sv-se":
        pretestresults = "Pre-test-resultat: Ping till https://www.google.com. Resultat: "
        pretestresults2 = " sekunder."
        nointernetconnectionmessage = "En aktiv internetuppkopppling kunde inte hittas."
        lookingforupdatesmessage = "Letar efter uppdateringar..."
        latestversionmessage = "Senaste versionen av PiSpeedtest är: "
        youhavethelatestversionmessage = "Du har den senaste versionen av PiSpeedtest."
        initialspeedtestinformation = "För att få programmet att fungera optimalt så körs ett \"speedtest\" för att mäta tid m.m. Vänligen vänta."
        speedtestran = "Ett speedtest har nu körts. Det tog: "
        speedtestseconds = " sekunder."
        programmodes = "Programlägen:"
        stablemode = "STABLE - Kör de stabila funktionerna i PiSpeedtest."
        betamode = "BETA MODE - Betafunktioner som kan innehålla buggar."
        compatiblemode = "COMPATIBLE - Välj detta läge för kompatibilitet med Mac, vissa Linuxsystem eller andra system än Windows. En stabil version kommer att köras, inte en betaversion."
        pleaseselectaspeedtestmodemessage = "Vänligen välj ett PiSpeedtest-läge genom att skriva dess namn och trycka på enter: "
        programdurationseconds = "Hur länge vill du köra programmet (i sekunder)? 12 timmar = 43 200 sekunder: "

        programdurationminutes = "Hur länge vill du köra programmet (i minuter)? 12 timmar = 720 minuter: "
        howofteninput = "Hur ofta vill du köra programmet (i sekunder) tar cirka "
        seconds = " sekunder. "
        speedtestfilenameinput = "Vilket namn vill du ha på speedtestfilen? Använd inte punkter eller .txt, det läggs till automatiskt. "
        errormessage = "Ett fel inträffade när ett speedtest skulle köras."
        startingspeedtestmessage = "Startar test."
        speedtestcompletedmessage = "Test utfört."
        programdurationmodemessage = "Vill du ange hur länge du vill köra programmet i sekunder eller minuter? (Skriv \"SECONDS\" eller \"MINUTES\" för att välja.)"
        programdurationmodeerror = "Ett fel inträffade. Skrev du rätt när du valde läge? Läget \"MINUTES\" kommer att väljas automatiskt."
        newversionmessage = "Version: "
        newversionmessage2 = " av PiSpeedtest finns tillgänglig. Du har version: "
        newversionmessage3 = " installerad."
        lookingforupdateserror = "Ett fel inträffade när PiSpeedtest sökte efter nya uppdateringar."

        skipdetected = "SKIP DETEKTERAT"
        speedtestconfignotfound = "Kunde inte hitta konfigurationsfilen."
        loadingconfigurationmessage = "Laddar konfiguration..."
        configuredmodemessage = "Det konfiguerade läget är: "
        minutes = " minuter."
        configuredspeedtestdurationmessage = "Konfiguerad speedtest-tid: "
        invalidmode = "Konfigurationsfilen innehåller ett felaktigt läge."
        invalidduration = "Konfigurationsfilen innehåller en ogiltig spedtest-tid."
        configuredruneverysecondmessage = "Konfiguerad \"kör var ___ sekund\": "
        runeverysecondinvalid = "\"Kör var ___ sekund\"-konfigurationen är felaktig."
        invalidmodeselected = "Du valde inte ett giltigt program-läge. Vänligen starta om PiSpeedtest."
        waiterror = "Ett fel inträffad när speedtest-tider skulle beräknas. \"Kör programmet var ___ - sekund måste vara större än: "
        betaversionmessage = "Det verkar som att du använder en betaversion av PiSpeedtest "
        maybenotstable = "Betaversioner kan innehålla buggar och vara ostadiga."
        erroroccurred = "Ett fel inträffade när PiSpeedtest kördes. Fel: "

        normalmodedescription = "NORMAL - Endast ett speedtest kommer att köras för att mäta tid m.m."
        accuratemodedescription = "ACCURATE - Tre stycken speedtests kommer att köras för att mäta tid m.m, vilket betyder bättre nogrannhet. Detta tar cirka en minut."
        fastmodedescription = "FAST - Detta läge testar bara uppladdningshastigheten och multiplicerar den med två för att få tidsdata. Resultaten är inte nogranna, men programmet initieras snabbare."
        superbmodedescription = "SUPERB - Fem speedtests kommer att köras, vilket bara rekommenderas när du behöver en exakt tidsavläsning. Detta läge avrundar tidsdata till en decimal, vilket är mer exakt än andra lägen. Detta läge kommer dock att ta två minuter att köra."
        mode_error = "Ett fel inträffade när du skulle välja läge. Starta om PiSpeedtest och se till att läget är korrekt skrivet."
        fastspeedtest = "Detta speedtest testade bara uppladdningshastigheten."
        fastspeedtestnotice = "FÖR ATT FÅ PROGRAMMET ATT VARA SÅ NOGRANNT SOM MÖJLIGT REKOMMENDERAS DETTA LÄGE (\"FAST\") EJ!"
        speedtestmodeselection = "Skriv lägets namn och tryck sedan enter för att välja det: "
        programoptionsmessage = "Det finns olika alternativ för hur resultaten ska formatteras/skrivas ut. Här är en lista: "
        textoptionmessage = "Text - Resultaten är formatterade med hjälp av enkla ord och resultaten.(PiSpeedtest´s standard-layout)"
        plainoptionmessage = "Plain - Visar endast resultaten i siffror (Nedladdning, uppladdning och pinghastigheter). Ingen text. Resultaten är separerade med hjälp av mellanrum."
        listsoptionmessage = "Lists - Visar alla resultat från varje speedtest som körs sedan programet startades. (rekommenderas endast för debugging etc.)"
        detailedtextoptionsmessage = "Detailed-text - Perfekt för att presentera datan till allmänheten eftersom enheter, kommentarer och tidsstämplar är inkluderade."
        withunitsoptionsmessage = "With-units - Samma som \"Text\"-alternativet, men med enheter utskrivna."
        textlayoutconfigurationmessage = "Välj ett läge genom att skriva dess namn (t.ex. \"Text\") och sedan trycka på enter: "
        invalidtextlayout = "Du valde ett felaktigt läge. Standardläget, \"Text\" kommer att väljas istället."
        imagegenerationerror = "Ett fel inträffade när en resultat-bild skulle genereras."

        speedteststartpopupmessage = "Ett popupfönster kommer nu att visas. Kom ihåg att trycka på \"Ok\". Om du inte gör det så kommer ett speedtest inte att startas."

        releasemessageinformation = "Det finns ett meddelade angående den senaste versionen, vilket är: "
        speedtestaccuracymodefoundmessage = " har valts som speedtest-nogrannhets-läge."

        cloudsavingturnedoff = "Din molnlagring för PiSpeedtest är avstängd."
        cloudsavingenabled = "Din molnlagring för PiSpeedtest är aktiverad."
        cloudsavingnotconfigured = "Du har inte konfigurerat molnlagring för PiSpeedtest."
        configurecloudsavingmessage = "Skriv \"ENABLE\" och tryck enter för att aktivera molnlagring eller skriv \"NO\" för att gå vidare utan att konfiguera molnlagring. "
        skipingcloudsavingsetupmessage = "Okej, skippar setup-programmet."
        maxdownloadspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (nedladdningshastighet)?: "
        maxuploadspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (uppladdningshastighet)?: "
        maxpingspeedinputmessage = "Vilken är den förväntade hastigheten med den router och uppkoppling som du har (pinghastighet)?: "
        connectiontypeinputmessage = "Vilken uppkopplingstyp har du?? WIFI, CABLE eller CELLULAR: "

        speedtestimagesaved = "En speedtest-resultatsbild har nu sparats i mappen \"images\"."
        cloudsavingerror = "Ett fel inträffade när PiSpeedtest-resultaten skulle laddas upp till molnet."
        invalidapikey = "Din nuvarande API-nycjek för molnlagring är felaktig."
        foundapikeyfile = "Filen \"apikey.txt\" hittades. Letar efter API-nyckel."
        foundapikey = "En gilltig API-nyckel för molnlagring hittades."
        pingspeednotputintoconsiderationmessage = " Ping-hastighet är ej med i beräkningen."
        pressenterkeymessage = "Tryck på enter-knappen för att stänga PiSpeedtest."
    elif languageconfiguration == "en-us":
        pretestresults = "Pre-test-result: Ping to https://www.google.com. Result: "
        pretestresults2 = " seconds."
        nointernetconnectionmessage = "An active internet connection could not be established."
        lookingforupdatesmessage = "Looking for updates..."
        latestversionmessage = "The latest version of PiSpeedtest is: "
        youhavethelatestversionmessage = "You have the latest version of PiSpeedtest."
        initialspeedtestinformation = "To make the program work better, a \"speedtest\" is being run in the beginning of the program. You can choose between three different modes:"
        speedtestran = "A speedtest has now been run. It took: "
        speedtestseconds = " seconds."
        programmodes = "Program-modes:"
        stablemode = "STABLE - Run the stable and tested functions in PiSpeedtest."
        betamode = "BETA MODE - Functions in beta that might not work properly."
        compatiblemode = "COMPATIBLE - Select this mode for compatibility with more operating systems than Windows, including Mac, some Linux OSes and other operating systems. A stable release is being run, not a beta release."
        pleaseselectaspeedtestmodemessage = "Please select a PiSpeedtest-mode by typing its name and then pressing enter on your keyboard: "
        programdurationseconds = "For how long do you want to run the program (in seconds)? 12 hours = 43 200 seconds: "

        programdurationminutes = "For how long do you want to run the program (in minutes)? 12 hours = 720 minutes: "
        howofteninput = "How often do you want to run the program (in seconds)? A speedtest takes about "
        seconds = " seconds. "
        speedtestfilenameinput = "What name would you like the speedtestfile to have? Do not use any dots or .txt, it will be added automatically. "
        errormessage = "An error occured during the speedtest."
        startingspeedtestmessage = "Starting speedtest."
        speedtestcompletedmessage = "A speedtest has been run."
        programdurationmodemessage = "Do you want to enter how long you want to run the program in seconds or minutes? (Write \"SECONDS\" or \"MINUTES\" to select.) "
        programdurationmodeerror = "An error occured. Did you type everything in correctly when you choosed an option? The option \"MINUTES\" will be selected automatically. "
        newversionmessage = "Version: "
        newversionmessage2 = " of PiSpeedtest is available. You have version: "
        newversionmessage3 = " installed."
        lookingforupdateserror = "An error occured while looking for updates."
        skipdetected = "SKIP DETECTED"
        speedtestconfignotfound = "Could not find the configuration file."
        loadingconfigurationmessage = "Loading configuration..."
        languageconfigurationnotfound = "Could not find the language configuration file."
        configuredmodemessage = "The configured mode is: "
        minutes = " minutes."
        configuredspeedtestdurationmessage = "Configured speedtest duration: "
        invalidmode = "The speedtest file contains an invalid mode."
        invalidduration = "The speedtest file contains an invalid speedtest duration."
        configuredruneverysecondmessage = "Configured \"run every ___ seconds\": "
        runeverysecondinvalid = "The \"run every ___ seconds\" configuration is invalid."
        invalidmodeselected = "You didn´t select a valid mode. Please restart PiSpeedtest."
        waiterror = "An error occured when calculating speedtest wait times. Make sure that it is bigger than: "
        betaversionmessage = "It looks like you are running a beta version of PiSpeedtest "
        maybenotstable = "Beta versions may contain bugs and be unstable."

        erroroccurred = "An error occured while running PiSpeedtest. Error: "
        normalmodedescription = "NORMAL - Only one speedtest will be run to measure time."
        accuratemodedescription = "ACCURATE - Three speedtests will be run to measure time, which means increased accuracy. This takes about one minute."
        fastmodedescription = "FAST - This mode only tests the upload speed and then multiplies it by two to get time data. The results are not accurate, but the program loads faster."
        superbmodedescription = "SUPERB - Five speedtests will be run to measure time, which is only recommended for times when you need a perfect time measurement. This mode rounds the time to one decimal, which is more accurate than other modes. You have to wait about two minutes, though."
        speedtestaccuracymodefoundmessage = " has been chosen as speedtest accuracy mode."
        mode_error = "An error occurent when you selected a mode. Restart PiSpeedtest and make surte to enter the mode correctly."
        fastspeedtest = "This speedtest only tested the upload speed."
        fastspeedtestnotice = "TO MAKE THE PROGRAM ACCURATE ENOUGH, THIS MODE (\"FAST\") IS NOT RECOMMENDED!"
        speedtestmodeselection = "Type the mode´s name and then press enter to select it: "
        programoptionsmessage = "There are different types of options for how to format the results. Here is a list: "
        textoptionmessage = "Text - The results are formatted using simple words and the results. (the standard PiSpeedtest layout)"
        plainoptionmessage = "Plain - Only get the result values (Download, upload and ping speeds). No text. The values are separated using spaces."
        listsoptionmessage = "Lists - Shows all the results from every speedtest done since running the program. (this is only recommended for debugging etc.)"
        detailedtextoptionsmessage = "Detailed-text - Perfect for copy-pasting the data and presenting to the public as units, comments and timestamps are included."
        withunitsoptionsmessage = "With-units - The same as the \"Text\"-option, but with units."
        textlayoutconfigurationmessage = "Choose a mode by typing its name (e.g \"Text\") and the pressing enter: "
        invalidtextlayout = "You selected an invalid text layout. The standard text formatting mode, \"Text\" will be selected instead."
        imagegenerationerror = "An error occured while generating a results image."
        speedteststartpopupmessage = "A popup window will now be shown. Be sure to tap \"Ok\". If you don´t do that, the speedtests won´t start."

        releasemessageinformation = "There is a message about this release, which is: "
        speedtestaccuracymodemfoundessage = " has been selected as the speedtest accuracy mode."
        cloudsavingturnedoff = "Your cloudsaving for PiSpeedtest is currently turned off."
        cloudsavingenabled = "You have PiSpeedtest cloudsaving enabled."
        cloudsavingnotconfigured = "You haven´t configured cloudsaving for PiSpeedtest."


        configurecloudsavingmessage = "Type \"ENABLE\" and press enter to enable cloudsaving or type \"NO\" to skip. "

        skipingcloudsavingsetupmessage = "Okay, skipping setup."
        maxdownloadspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using (download speed)? "

        maxuploadspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using? (upload speed)?: "
        maxpingspeedinputmessage = "What is the expected/normal speed from the router and connection that you are currently using (ping speed)? "

        connectiontypeinputmessage = "What connection type are you using? WIFI, CABLE or CELLULAR: "
        speedtestimagesaved = "A result image has been generated and saved in the directory \"images\"."

        generatingspeedtestreportmessage = "Generating speedtest report..."
        savedspeedtestreportmessage = "A speedtest report has been saved."
        cloudserverreponsemessage = "Cloudsaving server response: "
        viewresultslinkmessage = "View your speedtest results here: "
        downloadresultslinkmessage = "Additionally, the speedtest results can be downloaded here: "


        cloudsavingerror = "An error occured while cloudsaving PiSpeedtest results. "
        invalidapikey = "Your current cloudsaving API key is invalid."
        foundapikeyfile = "The file \"apikey.txt\" was found. Looking for API-key."

        pressenterkeymessage = "Press the enter key to close PiSpeedtest."
        foundapikey = "A valid cloudsaving API keywas found."
        pingspeednotputintoconsiderationmessage = " Ping speed is not put into consideration."
        pressenterkeymessage = "Press the enter key to close PiSpeedtest."
    else:
        pretestresults = "The current language configuration is somehow invalid."
        pretestresults2 = "The current language configuration is somehow invalid."
        nointernetconnectionmessage = "The current language configuration is somehow invalid."
        lookingforupdatesmessage = "The current language configuration is somehow invalid."
        latestversionmessage = "The current language configuration is somehow invalid."
        youhavethelatestversionmessage = "The current language configuration is somehow invalid."
        initialspeedtestinformation = "The current language configuration is somehow invalid."
        speedtestran = "The current language configuration is somehow invalid."
        speedtestseconds = "The current language configuration is somehow invalid."
        programmodes = "The current language configuration is somehow invalid."
        stablemode = "The current language configuration is somehow invalid."
        betamode = "The current language configuration is somehow invalid."
        compatiblemode = "The current language configuration is somehow invalid."
        pleaseselectaspeedtestmodemessage = "The current language configuration is somehow invalid."
        programdurationseconds = "The current language configuration is somehow invalid."

        programdurationminutes = "The current language configuration is somehow invalid."
        howofteninput = "The current language configuration is somehow invalid."
        seconds = "The current language configuration is somehow invalid."
        speedtestfilenameinput = "The current language configuration is somehow invalid."
        errormessage = "The current language configuration is somehow invalid."
        startingspeedtestmessage = "The current language configuration is somehow invalid."
        speedtestcompletedmessage = "The current language configuration is somehow invalid."
        programdurationmodemessage = "The current language configuration is somehow invalid."
        programdurationmodeerror = "The current language configuration is somehow invalid."
        newversionmessage = "The current language configuration is somehow invalid."
        newversionmessage2 = "The current language configuration is somehow invalid."
        newversionmessage3 = "The current language configuration is somehow invalid."

        lookingforupdateserror = "The current language configuration is somehow invalid."
        skipdetected = "The current language configuration is somehow invalid."
        speedtestconfignotfound = "The current language configuration is somehow invalid."
        loadingconfigurationmessage = "The current language configuration is somehow invalid."
        configuredmodemessage = "The current language configuration is somehow invalid."

        minutes = "The current language configuration is somehow invalid."
        configuredspeedtestdurationmessage = "The current language configuration is somehow invalid."
        invalidmode = "The current language configuration is somehow invalid."
        invalidduration = "The current language configuration is somehow invalid."
        configuredruneverysecondmessage = "The current language configuration is somehow invalid."
        runeverysecondinvalid = "The current language configuration is somehow invalid."
        invalidmodeselected = "The current language configuration is somehow invalid."
        waiterror = "The current language configuration is somehow invalid."
        betaversionmessage = "The current language configuration is somehow invalid."
        maybenotstable =  "The current language configuration is somehow invalid."
        erroroccurred = "The current language configuration is somehow invalid."
        normalmodedescription = "The current language configuration is somehow invalid."
        accuratemodedescription = "The current language configuration is somehow invalid."
        superbmodedescription = "The current language configuration is somehow invalid."
        mode_error = "The current language configuration is somehow invalid."
        fastspeedtest = "The current language configuration is somehow invalid."
        fastspeedtestnotice = "The current language configuration is somehow invalid."
        speedtestmodeselection = "The current language configuration is somehow invalid."
        programoptionsmessage = "The current language configuration is somehow invalid."
        textoptionmessage = "The current language configuration is somehow invalid."
        plainoptionmessage = "The current language configuration is somehow invalid."
        listsoptionmessage = "The current language configuration is somehow invalid."
        detailedtextoptionsmessage = "The current language configuration is somehow invalid."
        withunitsoptionsmessage = "The current language configuration is somehow invalid."
        invalidtextlayout = "The current language configuration is somehow invalid."
        imagegenerationerror = "The current language configuration is somehow invalid."
        speedteststartpopupmessage = "The current language configuration is somehow invalid."
        releasemessageinformation = "The current language configuration is somehow invalid."
        speedtestaccuracymodefoundmessage = "The current language configuration is somehow invalid."
        cloudsavingturnedoff = "The current language configuration is somehow invalid."
        cloudsavingenabled = "The current language configuration is somehow invalid."
        cloudsavingnotconfigured = "The current language configuration is somehow invalid."
        configurecloudsavingmessage = "The current language configuration is somehow invalid."
        skipingcloudsavingsetupmessage = "The current language configuration is somehow invalid."
        maxdownloadspeedinputmessage = "The current language configuration is somehow invalid."
        maxuploadspeedinputmessage = "The current language configuration is somehow invalid."
        maxpingspeedinputmessage = "The current language configuration is somehow invalid."
        connectiontypeinputmessage = "The current language configuration is somehow invalid."
        speedtestimagesaved = "The current language configuration is somehow invalid."
        generatingspeedtestreportmessage = "The current language configuration is somehow invalid."
        savedspeedtestreportmessage = "The current language configuration is somehow invalid."
        cloudserverreponsemessage = "The current language configuration is somehow invalid."
        viewresultslinkmessage = "The current language configuration is somehow invalid."
        downloadresultslinkmessage = "The current language configuration is somehow invalid."


        cloudsavingerror = "The current language configuration is somehow invalid."
        invalidapikey = "The current language configuration is somehow invalid."

        foundapikeyfile = "The current language configuration is somehow invalid."
        foundapikey = "The current language configuration is somehow invalid."
        pingspeednotputintoconsiderationmessage = "The current language configuration is somehow invalid."
        pressenterkeymessage = "The current language configuration is somehow invalid."


    # Main speedtest code:
    def processpeedtest(backupmode, filename, textlayout):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        results = s.results.dict()
        resultlist = list(results.values())
        download = str(round(resultlist[0] / 1000000)) + " mbit/s"
        upload = str(round(resultlist[1] / 1000000)) + " mbit/s"
        ping = str(resultlist[2]) + "ms"
        downloadlist.append(str(round(resultlist[0] / 1000000)))
        uploadlist.append(str(round(resultlist[1] / 1000000)))
        pinglist.append(str(round(resultlist[2])))
        if textlayout == "Text":
            fullresults = "Results: " + " Download: " + download + " Upload: " + upload + " Ping: " + ping + "."
        elif textlayout == "Plain":
            fullresults = download  + " " + upload + " " + ping
        elif textlayout == "Lists":
            fullresults = str(downloadlist) + ", " + str(uploadlist) + ", " + str(downloadlist) + "."
        elif textlayout == "Detailed-text":
            fullresults = "A test at " + str(time.ctime()) + " has been run. " + "The results was " + " Download speed (mbit/s): " + download + " Upload speed (mbit/s): " + upload + " Ping (milliseconds): " + ping + "."
        elif textlayout == "With-units":
            fullresults = "Results: " + " Download: " + download + " mbit/s " + " Upload: " + upload + " mbit/s "+ " Ping: " + ping + " milliseconds" + "."
        print(fullresults)
        if backupmode == False:

            with open(filename, "a+") as file:
                file.write(fullresults + "\n")
        elif backupmode == True:
            with open("speedtestbackup.txt", "a+") as backupfile:
                backupfile.write(fullresults + "\n")


    #(end of main speedtest code.)
    def processspeedtest_onlyupload(filename):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.upload()
        results = round(int(s.results.upload) / 1000000)
        with open(filename, "a+") as file:
            file.write("Upload: " + str(results) + " (only upload test)")




    try:
        import requests
        request = requests.get("https://www.google.com")
        print(pretestresults + str(request.elapsed.total_seconds()) + pretestresults2)
    except requests.exceptions.ConnectionError:
        print(nointernetconnectionmessage)
        noconnection = 1
        raise NoInternetConnection(nointernetconnectionmessage)
    print(lookingforupdatesmessage)
    print("\n")
    try:
        import requests
        from bs4 import BeautifulSoup

        updatecheck = requests.get("https://pispeedtestfiles.000webhostapp.com/latestversion.html")
        soup = BeautifulSoup(updatecheck.text, "html.parser")

        latestversionnumber = str(soup.get_text()).replace("\n", "")
        print(latestversionmessage + latestversionnumber + ".")
        if latestversionnumber == fileversionnumber:
            print(youhavethelatestversionmessage)
        elif float(latestversionnumber) < float(fileversionnumber):
            print(betaversionmessage + "( "+ fileversionnumber + ") . " + maybenotstable)
        else:
            releasemessage = requests.get("https://pispeedtestfiles.000webhostapp.com/releasemessage.html")
            releasemessageversion = requests.get("https://pispeedtestfiles.000webhostapp.com/releasemessageversion.html")
            soup = BeautifulSoup(releasemessageversion.text, "html.parser")
            releasemessageversionnumber = str(soup.get_text()).replace("\n", "")
            try:
                if float(releasemessageversionnumber) == float(latestversionnumber):
                    soup = BeautifulSoup(releasemessage.text, "html.parser")
                    messagefornewrelease = str(soup.get_text())
                    print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
                    print(releasemessageinformation + "\n" +  messagefornewrelease)
                else:
                    print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
            except:
                print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
    except Exception as e:
        print(lookingforupdateserror + " (" + str(e) + ").")
    print("\n")
    with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\status.txt"), "r") as cloudsavingstatustextfile:
        filecontents = cloudsavingstatustextfile.read().splitlines()
    if filecontents[0] == "ENABLED":
        print(cloudsavingenabled)
    elif filecontents[0] == "OFF":
        print(cloudsavingturnedoff)
    elif filecontents[0] == "NOT CONFIGURED":
        print(cloudsavingnotconfigured)
        confirm = input(configurecloudsavingmessage)
        if confirm == "ENABLE":
            import cloudsavingsetup
            cloudsavesetup.setup()
        else:

            print(skipingcloudsavingsetupmessage)

    print("\n")
    print(initialspeedtestinformation)
    print(normalmodedescription)
    print(accuratemodedescription)
    print(fastmodedescription)
    print(superbmodedescription)
    speedtestaccuracymode = input(speedtestmodeselection)
    initialspeedtestsfile = os.path.join(os.getcwd() + "/speedtestresults/" + "intialspeedtests.txt")
    #Message when a speedtest accuracy mode is found:
    def speedtestaccuracymodefound():
        print(speedtestaccuracymode + speedtestaccuracymodefoundmessage)
    if speedtestaccuracymode == "NORMAL" or speedtestaccuracymode.lower() == "normal":
        speedtestaccuracymodefound()
        timeone = time.time()
        if noconnection == 0:

            processpeedtest(0, filename=initialspeedtestsfile, textlayout="Text")
            speedtesttime = round(time.time() - timeone)
            print(speedtestran + str(speedtesttime) + speedtestseconds)
        elif noconnection == 1:
            print(nointernetconnectionmessage)

    elif speedtestaccuracymode == "ACCURATE" or speedtestaccuracymode.lower() == "accurate":
        timelist = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            for i in range(3):
                time1 = time.time()
                processpeedtest(False, "initialspeedtest.txt", textlayout="Text")
                timelist.append(str(round(time.time()-time1)))
                print(speedtestran + str(timelist[i]) + speedtestseconds)
            speedtesttime = round(eval("+".join(timelist)))
        elif noconnection == 1:
            print(nointernetconnectionmessage)
    elif speedtestaccuracymode == "FAST" or speedtestaccuracymode.lower() == "fast":
        timelist3 = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            timeone1 = time.time()
            processspeedtest_onlyupload("initialspeedtests.txt")
            speedtesttime = str(round((time.time() - timeone1)*2))
            print(speedtestran + str(round(int(speedtesttime)/2)) + speedtestseconds + " " + fastspeedtest)

    elif speedtestaccuracymode == "SUPERB" or speedtestaccuracymode.lower() == "superb":
        timelist2 = []
        speedtestaccuracymodefound()
        if noconnection == 0:
            for i in range(5):
                timenumberone = time.time()
                processpeedtest(False, "initialspeedtest.txt", textlayout="Text")
                timelist2.append(str(round(time.time() - timenumberone, 1)))
                print(speedtestran + timelist2[i] + speedtestseconds)
            times = "+".join(timelist2)
            speedtesttime = round(eval(times)/5, 1)


        elif noconnection == 1:
            print(nointernetconnectionmessage)
    else:
        print(mode_error)

        exit()
    print("\n")

    try:
        configurationfile = os.path.join(os.getcwd() + "/configurationfiles/config.txt")

        with open(configurationfile, "r+") as configurationsfile:
            print(loadingconfigurationmessage)
            configurationfilecontent = configurationsfile.read().splitlines()
            if configurationfilecontent[9] in allowedmodes:
                configuredmode = configurationfilecontent[9]
                print(configuredmodemessage + configuredmode + ".")
                loadconfig[0] = 1
            elif configurationfilecontent[9] == "-SKIP-":
                print(skipdetected)
                loadconfig[0] = 0
            else:
                print(invalidmode)

                loadconfig[0] = 0
            try:
                configuredspeedtestduration1 = int(configurationfilecontent[10])
                configuredspeedtestduration = int(configuredspeedtestduration1 * 60)
                print(configuredspeedtestdurationmessage + str(configuredspeedtestduration / 60) + minutes)
                loadconfig[1] = 1
            except:
                if configurationfilecontent[10] == "-SKIP-":
                    print(skipdetected)
                    loadconfig[1] = 0
                else:
                    print(invalidduration)
                    loadconfig[1] = 0
            try:
                configuredruneverysecond = int(configurationfilecontent[11])
                print(configuredruneverysecondmessage + str(configuredruneverysecond) + seconds)
                loadconfig[2] = 1
            except:
                if configurationfilecontent[11] == "-SKIP-":
                    print(skipdetected)
                    loadconfig[2] = 0
                else:
                    print(runeverysecondinvalid)
                    loadconfig[2] = 0
        print("\n")
    except:
        print(speedtestconfignotfound)
        loadconfig[0] = 0
        loadconfig[1] = 0
        loadconfig[2] = 0
    if loadconfig[0] == 0:
        print("\n")
        print(programmodes)
        print(betamode)
        print(stablemode)
        print(compatiblemode)
        mode = input(pleaseselectaspeedtestmodemessage)
    elif loadconfig[0] == 1:
        mode = configuredmode
    else:
        print("\n")
        print(programmodes)
        print(betamode)
        print(stablemode)
        print(compatiblemode)
        mode = input(pleaseselectaspeedtestmodemessage)

    if mode == "BETA MODE" or mode.lower() == "beta mode":
        import ctypes

        print("\n")


        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        #inputmaxpingspeed = int(input(maxpingspeedinputmessage)) (not used for the connection score algorithm yet.)
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        print(speedteststartpopupmessage)
        ctypes.windll.user32.MessageBoxW(None, startingspeedtestmessage, "PiSpeedtest", 0)
        steps = int(times)


        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:
                    ctypes.windll.user32.MessageBoxW(None, errormessage, "PiSpeedtest", 0)

                    print(errormessage + "(" + str(e) + ").")

                    # This is being added in a later release:
                    # box = ctypes.windll.user32.MessageBoxW(None, "An error occured while running a speedtest. Would you like to try again? Everything will restart. The file with new speedtest data will be namned \"speedtestbackup.txt\".", "PiSpeedtest", 5)
                    # if box == 1:
                    # print(Running speedtest once more.")
                    # for speedtestindex in range(repeat):

                    # print("A speedtest is being started.")
                    # processpeedtest(0, filename="speedtestbackup.txt")
                    # print("A speedtest has been completed.")
                    # time.sleep(interval)
                    # elif box == 2:
                    # print("Quitting PiSpeedtest because of an error.")
                    # else:
                    # print("Quitting PiSpeedtest because of an error.")
            print("\n")
            try:
                from PIL import Image, ImageDraw, ImageFont


                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount)/len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount)/(len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount)/len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed/ 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")


                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"),"w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " +  "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)

    elif mode == "STABLE" or mode.lower() == "stable":
        import ctypes

        print("\n")

        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        print(speedteststartpopupmessage)
        ctypes.windll.user32.MessageBoxW(None, startingspeedtestmessage, "PiSpeedtest", 0)
        steps = int(times)

        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:
                    ctypes.windll.user32.MessageBoxW(None, errormessage, "PiSpeedtest", 0)

                    print(errormessage + "(" + str(e) + ").")
            print("\n")


            try:
                from PIL import Image, ImageDraw, ImageFont

                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount) / len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount) / (len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount) / len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(
                    mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(
                    os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")

                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace(
                                "A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"),"w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)
    elif mode == "COMPATIBLE" or mode.lower() == "compatible":
        print("\n")

        if loadconfig[1] == 0:
            programdurationmode = input(programdurationmodemessage)
            if programdurationmode == "MINUTES":
                times = int(input(programdurationminutes) * 60)
            elif programdurationmode == "SECONDS":
                times = int(input(programdurationseconds))
            else:
                print(programdurationmodeerror)
                times = int(input(programdurationminutes) * 60)
        else:
            times = configuredspeedtestduration
        if loadconfig[2] == 1:
            interval = configuredruneverysecond
        else:
            interval = int(input(howofteninput + str(speedtesttime) + seconds))
        inputfilename = str(input(speedtestfilenameinput))
        filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
        with open(filedirectory, "w") as file:
            file.close()
        inputmaxdownloadspeed = int(input(maxdownloadspeedinputmessage))
        inputmaxuploadspeed = int(input(maxuploadspeedinputmessage))
        connectiontype = input("What connection type are you using? WIFI, CABLE or CELLULAR: ")
        print("\n")
        wait = interval - speedtesttime
        if wait < 1:
            print(waiterror + str(speedtesttime) + seconds)

            exit()
        else:
            repeat = round(times / (wait))
        print("\n")
        print(programoptionsmessage)
        print(textoptionmessage)
        print(plainoptionmessage)
        print(listsoptionmessage)
        print(detailedtextoptionsmessage)
        print(withunitsoptionsmessage)
        configuredtextlayout = input(textlayoutconfigurationmessage)
        if configuredtextlayout in allowedtextlayouts:
            print(startingspeedtestmessage)
        else:
            print(invalidtextlayout)
        steps = int(times)

        print("\n")
        if noconnection == 0:
            for speedtestindex in range(repeat):
                try:

                    print(startingspeedtestmessage)
                    processpeedtest(0, filename=filedirectory, textlayout=configuredtextlayout)
                    print(speedtestcompletedmessage)
                    time.sleep(0.5)
                except Exception as e:

                    print(errormessage + "(" + str(e) + ").")
            print("\n")

            try:
                from PIL import Image, ImageDraw, ImageFont

                averagedowloadcount = "+".join(downloadlist)
                averagedownload = round(eval(averagedowloadcount) / len(downloadlist))
                maxdownload = 0

                mindownload = 10000000
                for i in range(len(downloadlist)):
                    if maxdownload < int(downloadlist[i]):
                        maxdownload = int(downloadlist[i])
                    if mindownload > int(downloadlist[i]):
                        mindownload = int(downloadlist[i])
                averageuploadcount = "+".join(uploadlist)
                averageupload = round(eval(averageuploadcount) / (len(uploadlist)))
                maxupload = 0
                minupload = 100000000
                for i in range(len(uploadlist)):
                    if maxupload < int(uploadlist[i]):
                        maxupload = int(uploadlist[i])
                    if minupload > int(uploadlist[i]):
                        minupload = int(uploadlist[i])

                averagepingcount = "+".join(pinglist)
                averageping = round(eval(averagepingcount) / len(pinglist))
                maxping = 0
                minping = 100000
                for i in range(len(pinglist)):
                    if maxping < int(pinglist[i]):
                        maxping = int(pinglist[i])
                    if minping > int(pinglist[i]):
                        minping = int(pinglist[i])
                if connectiontype == "CELLULAR" or connectiontype == "WIFI":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 70):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 50):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 70):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 10

                    elif averageupload < round((inputmaxuploadspeed / 100) * 50):
                        uploadscore = 5


                elif connectiontype == "CABLE":
                    if averagedownload > round((inputmaxdownloadspeed / 100) * 95):
                        downloadscore = 15

                    elif averagedownload > round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 10

                    elif averagedownload < round((inputmaxdownloadspeed / 100) * 90):
                        downloadscore = 5

                    if averageupload > round((inputmaxuploadspeed / 100) * 95):
                        uploadscore = 15

                    elif averageupload > round((inputmaxuploadspeed / 100) * 90):
                        uploadscore = 10
                    elif averageupload < round((inputmaxuploadspeed / 100) * 90):

                        uploadscore = 5
                mainscore = uploadscore + downloadscore
                print("ConnectionScore: " + str(
                    mainscore) + " (max 30, min 10)." + pingspeednotputintoconsiderationmessage)
                if mainscore > 24:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_goodscore.png")
                elif mainscore > 14:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notsogoodscore.png")
                else:
                    filepath = os.path.join(os.getcwd() + "/images/imagetemplates/template_notgoodscore.png")

                image = Image.open(filepath)

                draw = ImageDraw.Draw(image)
                fontpath = os.path.join(os.getcwd() + "\\images\\imagetemplates\\" + fontfilename)

                imagefont = ImageFont.truetype(fontpath, 15)
                imagefilepath = os.path.join(
                    os.getcwd() + "\\images\\" + "\\speedtestresultimages\\" + inputfilename + ".png")

                draw.text((360, 92), str(averageupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 132), str(averagedownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((360, 172), str(averageping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 92), str(maxupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 132), str(maxdownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((300, 172), str(maxping), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 92), str(minupload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 132), str(mindownload), fill="rgb(255,255,255)", font=imagefont)
                draw.text((430, 172), str(minping), fill="rgb(255,255,255)", font=imagefont)
                image.save(imagefilepath)

                print(speedtestimagesaved)
            except Exception as e:
                print(imagegenerationerror + " (" + str(Exception) + ").")

            try:
                download_data = str(downloadlist)

                upload_data = str(uploadlist)
                ping_data = str(uploadlist)
                with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
                    print(foundapikeyfile)

                    apikeyfilecontents = apikeytextfile.read().splitlines()
                cloudsavingapikey = apikeyfilecontents[1].replace(" ", "")
                if len(cloudsavingapikey) == 25:
                    print(foundapikey)

                    upload_url = "https://pispeedtestcloudsaving.pythonanywhere.com/upload-results/" + cloudsavingapikey + "/" + inputfilename + "/" + download_data + "/" + upload_data + "/" + ping_data
                    pispeedtestuploadresultstocloudrequest = requests.get(upload_url)
                    print(cloudserverreponsemessage + pispeedtestuploadresultstocloudrequest.text + ".")
                    if "A file with the name" in pispeedtestuploadresultstocloudrequest.text:
                        print(viewresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "") + ".")
                        print(downloadresultslinkmessage + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-") + ".")

                        print(generatingspeedtestreportmessage)
                        with open(os.path.join(os.getcwd() + "/speedtestreports/" + inputfilename + "_report" + ".txt"), "w") as speedtestreportfile:
                            speedtestreportfile.write("SPEEDTEST REPORT by PiSpeedtest." + "\n")
                            speedtestreportfile.write("Generated at " + str(time.ctime()) + "." + "\n")

                            speedtestreportfile.write("AVERAGE DOWNLOAD SPEED: " + str(averagedownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE UPLOAD SPEED: " + str(averageupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("AVERAGE PING SPEED: " + str(averageping) + " milliseconds" + "\n")
                            speedtestreportfile.write("LOWEST DOWNLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST UPLOAD SPEED: " + str(mindownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("LOWEST PING SPEED: " + str(mindownload) + " milliseconds" + "\n")
                            speedtestreportfile.write("HIGHEST DOWNLOAD SPEED: " + str(maxdownload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST UPLOAD SPEED: " + str(maxupload) + " mbit/s" + "\n")
                            speedtestreportfile.write("HIGHEST PING SPEED: " + str(maxping) + " milliseconds" + "\n")
                            speedtestreportfile.write("View full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ","") + "." + "\n")
                            speedtestreportfile.write("Download full results here: " + "https://pispeedtestcloudsaving.pythonanywhere.com" + pispeedtestuploadresultstocloudrequest.text.replace("A file with the name " + inputfilename + ".txt" + " has been saved in the cloud. Access it with: ", "").replace("show-", "download-") + "." + "\n")
                            speedtestreportfile.write("Powered- and generated by the application \"PiSpeedtest\"." + "\n")

                        print(savedspeedtestreportmessage)
            except Exception as e:
                print(cloudsavingerror + "(" + str(e) + ").")


        else:
            print(nointernetconnectionmessage)
    else:
        print(invalidmodeselected)
        raise NoModeDefinded("\"" + mode + "\"" + " is not a valid mode.")

except Exception as e:

    print(erroroccurred + " (" + str(e) + ").")

finally:




    print("\n")
    input(pressenterkeymessage)

