import speedtest

import time

import datetime
downloadlist = []
uploadlist = []
pinglist = []
filename = "speedtestdata_date:" + str(datetime.datetime.now().day) + ".txt"
file = open("speedtestdata.txt", "w")
smallestkbitsup = 1000
largestkbitsup = 0
smallestkbitsdown = 1000
largestkbitsdown = 0
def processpeedtest():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    results = s.results.dict()
    resultlist = list(results.values())
    download = str(resultlist[0]) + "kbit/s"
    upload = str(resultlist[1]) + "kbit/s"
    ping = str(resultlist[2]) + "ms"
    downloadlist.append(download)
    uploadlist.append(upload)
    pinglist.append(ping)
    fullresults = "Results: " + " Download: " + download + " Upload: " + upload + " Ping: " + ping + "."
    print(fullresults)
    file.write("Test number: "  + str(speedtestindex) + fullresults + " Captured at " + str(time.ctime()) + "." + "\n")


times = int(input("Hur länge vill du köra programmet? (I sekunder) 12 timmar = 43 200 sekunder: "))
interval = int(input("Hur ofta vill du köra programmet (i sekunder)? Ett \"speedtest\" tar cirka 10 sekunder: "))
repeat = round(times/interval-12)

for speedtestindex in range(repeat):
    print("Startar test.")
    processpeedtest()
    print("Test utfört.")
    time.sleep(interval-12)
file.close()
