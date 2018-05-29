# π-speedtest
##### Coming from a tutorial? The program has been changed in some ways, see "How to set up" for more information.
A code for easy measuring of internet speeds using Speedtest.net and Python. The module/package used is "speedtest-cli" which can be easy retrived doing:
` ` `
pip install speedtest-cli
 ` ` `
 

### Release notes
**See the code history for more information.**
##### Upcoming in version 2.0:

- An easier way to translate all texts will be implemented.
- The "run the program every ___ seconds" will most likely be in the Stable mode.
- More imporvements ad fixes.
**V1.8**
- Release 2.0 is upcoming. This is what´s new in release V1.8:
- More customization:
 - You can run the program in Beta mode, Stable mode or Compatibility mode.
  - Stable mode: Run a totally stable version of the program.
  - Beta mode: Run Beta functions that might not be stable.
  - Compatible mode: A mode with all the functions in the stable release, although it works for Mac, some Linux OSes and more operating  systems.
 - Edit the file "languageconfiguration.txt" to select a language. **This means that PiSpeedtest now supports both English and Swedish.**
 - To ensure internet connectivity and to make the "Run the speedtest every __ seconds" more accurate, a speedtest is now being run in the beginning of the program. This feature applies to the "BETA MODE".
 - Windows users can now get alerts (message boxes) on their screen. This feature is available in all modes except the "Compatible" mode.
**V1.0**
- Several improvements, including:
 - File saving works properly.
 - Fixed file formatting.
 - Result is now rounded and saved in megabit/s.
- First "industrial" tests


**V0.1**
- Initial code submitted.

### How to set up:
#### HEADS UP:
##### As with most software, 100% accurate results cannot be guaranteed. The program is powered by the speedtest-cli Python API.
**Beta functions might not work properly. When you need as accurate results as possible, run the mode "STABLE" or "COMPATIBLE".**
___________________________________________
**Perhaps you´ve just read a tutorial and you found out that the version was different compared to the one showed there. Don´t be scared, here is how you start a speedtest:**

- Run the mainprogram.py file.
- Wait for a initial speedtest to be completed.
- Choose a mode. For industrial usage, "STABLE" or "COMPATIBLE" is the best mode as it ensures that everything works to 100%. However, - "BETA" mode gives you the newest features that most likely will work.
- Choose for how long you want to run the program and then press enter.
- The next option currently depends on what mode you have chosen. Type in your choise and then press enter.
- Choose a file name. Make sure to include ".txt" in the end and don´t type in the name of a file that you already have used for speedtesting or other purposes before.
- Now, wait for the speedtests to be run and then check the file with speedtestdata.
**If you want to run older versions of the program that you´ve might seen in tutorials, check the "oldreleases" folder.**
**Want to cancel the program? Ctrl+Z or Ctrl+C will work in most cases.**
