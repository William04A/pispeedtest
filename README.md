# π-speedtest

### - A critical file writing error was found! Please update to PiSPeedtest 2.0.1 or higher in order to make sure that you can use PiSpeedtest!
### As of the version PiSpeedtest 2.0, the package "beautifulsoup4" is needed in order to use the "check for updates" feature of PiSpeedtest. Some users might also ahve to install the "requests" package if it isn´t installed.

### The image generation (in beta) added in PiSpeedtest 2.5 also requires the Python package "Pillow" to be installed.

##### Coming from a tutorial? The program has been changed in some ways, see "How to set up" for more information.
A code for easy measuring of internet speeds using Speedtest.net and Python. The module/package used is "speedtest-cli" which can be easy retrived doing:
` ` `
pip install speedtest-cli
 ` ` `
 For additional stuff (update-checking and more), BeautifulSoup 4 is used. Install it using:
  ` ` `
  pip install beautifulsoup4
   ` ` `
  For PiSpeedtest result image generation, the library "Pillow" is used. "Pillow" can be installed with pip:
  ` ` `
  pip install Pillow
   ` ` `
### Release notes
**See the code history for more information.**
**Upcoming in V3.0: (these are planned features and/or features under development as of 10th July 2018)**

- Input fields accepts both lowercase and uppercase characters.
- Free and automatic cloud backup for all PiSpeedtest result files.

- The algorithm for image generation will be implemented.
**V2.5 (previously 2.3, but changed to 2.5 because of more changes than planned. In beta.):**

- Two new options: different initial speedtest measuring and different speedtest results text formatting. These options
makes PiSpeedtest even more customzieable and easy to use.
- Better error handling.
- The "check for updates" - function now finds and tells you about beta versions. It also displays release notes for future versions if those are found.
- A new feature which most likely will be fully integraded to PiSpeedtest 3.0 is image generation. Now, PiSpeedtest can generate a custom image which is saved in PiSpeedtest\Images\Speedtestresultimages. The images shows an approximate max speed, minimum speed and ping times  for each speedtest. This feature is currently in beta and will be updated in the future. **For custom image generation, please install the library "Pillow" using "pip install Pillow".**
- Configuration files are now integrated into the main application.
- More improvements, additions and fixes.

**V2.0.1**
- Fixed a critical file naming bug: an update is required to make PiSpeedtest work properly.
**V2.0:**
- Lots of improvements, including:

 - It is now super easy to translate the program as all the code for languages is variable-based.
 - Speedtest-results does now save in the directory "speedtestresults" and .txt as well as file path is added to the file automatically.
 - The program now checks for updates for PiSpeedtest from a server online.
 - You can now choose to enter the duration of the program in minutes or seconds.
 - Most of the beta features are in the stable release.
 - Configuration files are now stored in the direcctory "configurationfiles" and a more customizeable "config.txt" file is available.
 - Improved error handling and messaging, which will be updated even more in the future.
 - Newlines (\n, also known as the thing that happens when you press the "Enter" key on your keyboard), have been added to make the text and messages in PiSpeedtest easier to read.
 
 - You can now choose between seconds and minutes while specifying a speedtest duration.
 - More improvements and fixes.

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
- Choose a file name. Make sure to not include ".txt" in the end and don´t type in the name of a file that you already have used for speedtesting or other purposes before.
- Now, wait for the speedtests to be run and then check the file with speedtestdata.
**If you want to run older versions of the program that you´ve might seen in tutorials, check the "oldreleases" folder.**
**Want to cancel the program? Ctrl+Z or Ctrl+C will work in most cases.**
