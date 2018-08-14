def cloudsavinglinks(response, filename):
    if "A file with the name" in response:
        cloudsavinglinks.downloadlink = "https://pispeedtestcloudsaving.pythonanywhere.com" + response.replace("A file with the name " + filename + ".txt" + " has been saved in the cloud. Access it with: ","").replace("show-", "download-")

        cloudsavinglinks.accesslink = "https://pispeedtestcloudsaving.pythonanywhete.com" + response.replace("A file with the name " + filename + ".txt" + " has been saved in the cloud. Access it with: ", "")
    else:

        cloudsavinglinks.downloadlink = "ERROR!"
        
        cloudsavinglinks.accesslink = "ERROR!"

