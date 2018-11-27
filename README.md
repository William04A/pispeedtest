# π-speedtest
-----
A really easy way to run multiple automated speedtest on your computer using Speedtest.net. Powered by [speedtest-cli](https://github.com/sivel/speedtest-cli).

_____________
### Features:
**Here are some of PiSpeedtest´s features:**

 - The ability to process multiple speedtests using Speedtest.net.
 - Lots of customization features like different result text formatting, different languages, custom speedtest duration and much more.
 - Advanced features like free and unlimited cloudsaving of speedtest results and result image generation (see [this](https://image.ibb.co/ckjFUz/Screenshot_454.png) example).
 - Automatic update checking, the ability to choose test servers, great error handing and much more!

____________
### Quickstart:
Please see the [Wiki](https://github.com/William04A/pispeedtest/wiki/Quickstart) for a really good and detailed quickstart guide of PiSpeedtest. If you want to roughly know what to do, here is a super short version of the quickstart guide:

 - You need to have Git and Python 3 installed (both applications needs to have the command line interface enabled).
 - The follow Python modules are required to use PiSpeedtest´s all functions:
  - `speedtest-cli` (Basic speedtesting code)
 - `requests` (Update checking, connection verifying and more)
 - `Pillow` (Speedtest results image generation)
 - `beautifulsoup4` (Parsing the responses when checking for updates and more)
 
 - `netifaces` (Used for getting the adress of your network gateway)
 - `ping3` (Pinging your wifi network when performing initial tests)
 - `tqdm` (For displaying progress bars in the cloudsaving setup program)
(all of the mentioned modules above can be installed using pip).


**If you don´t want to do a manual setup, just run the file \"automaticsetup.py\" and all the required requirements for PiSpeedtest will be installed.**
________
### Changelog/Updates:
**Application updates:**

**V4.6**:

Unfortunately, some big and small bugs has been found in PiSpeedtest. These have now been fixed. Here is the changelog:

- Fixed issue #1 (on GitHub) that made waiting between speedtests and speedtest calculations broken. These are two major bugs that have been around for a while, sadly. They are now fixed, so please re-clone PiSpeedtest if you have these errors.
- Also, some other issues and bugs have been fixed. Another critical error has also been fixed, so please update PiSpeedtest.

**V4.5**:

PiSpeedtest 4.5 includes one new, cool feature. It is also worth to note that an improved cloudserver and other things that will be added to PiSpeedtest 5.0, most likely the next major release of PiSpeedtest, is currently in development. However, this is what you will get with PiSpeedtest 4.5:

- The initial test that PiSpeedtest does to verify your network connection has now been updated. Using two new modules "ping3" and "netifaces", your network gateway is also pinged, so that you will be able to identify if you have connection to your network gateway, but not to the internet.

**V4.3**:

PiSpeedtest 4.3 is an enhancement update before the release of PiSpeedtest 4.5. This is what´s new:
- A new updater.py file has been added to PiSpeedtest. It is an automatic updater that can update PiSpeedtest to the latest version
(currently compatible with PiSpeedtest 3.0 and higher). Please note that the updater is in beta and only currently available in English. All your progress and your old pispeedtest folders will be saved during an update. The updater will only copy files from the version you run the updater on to the updated version.

- Also, several changes has been made since PiSpeedtest 4.0 without calling it another major relase, so if you haven´t updated PiSpeedtest in a while and have PiSpeedtest 4.0 installed, make sure to update as this fixes some bugs from PiSpeedtest 4.0.


**V4.0:**

PiSpeedtest 4.0 is another major update to PiSpeedtest that includes these new things:
- PiSpeedtest does now have more options when speedtesting. You can now choose what server to perform speedtests against or select servers automatic, like it has been in PiSpeedtest before. Being able to choose servers improves the accuracy some times.
- You now get more information when processing speedtests.
- Better error handling.
- PiSpeedtest has more graphical popups in some places, which makes PiSpeedtest look nicer overall.

- And much more!

**V3.5:**

This update is focusing on PiSpeedtest setup programs, which needed an update.
- The automaticsetup.py now works with most platforms and not only Windows as the pip module is used. The program is alrady configured to work with pip 10.0 and higher because of the pip.main() module changes with pip 10.
- The cloudsaving setup now has options to turn off or on cloudsaving, batch-upload data to the cloud and to show your API-key.
Big application updates are also in progress!

**V3.0:**
This release is a major PiSpeedtest update, which includes new features like:
- Input fields accepts both lowercase and uppercase characters.
- Free, unlimited and automatic cloud backup for all PiSpeedtest result files. You can enable cloud saving
by running the file "cloudsavingsetup.py". **The cloud saving application is written in Python using Flask as
the web framework. It is stored on PythonAnywhere. The source code is not being shared yet for different reasons,
including some security concerns (what if somebody cloned the whole server code and used it for hacking?**
- An algorithm for image generation has now been implemented. Before your speedtests are being run, you get
some questions about your current connection. That data is then used to change the background of the speedtest
images depending on how bad or good your connection is.
- Bug fixes and improvements.
- And much more!

**V2.5 (previously 2.3, but changed to 2.5 because of more changes than planned.):**

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

**Cloudserver updates:**

**V1.1:**

- Fixed a bug that used the upload results for both ping and upload values while sending backups to the server. Unfortunately, this applied to all uploaded backups and all data uploaded to the cloud before 4th August 2018 is affected.


**Other updates:**

(This section is not complete)
_________
### For more information:
If you want guides and more information about PiSpeedtest, please check the [Wiki](https://github.com/William04A/pispeedtest/Wiki).
Starting from PiSpeedtest 5.0, application updates will be documented at the [Projects](https://github.com/William04A/pispeedtest/Projects) page.
Issues can be found on the [Issues](https://github.com/William04A/pispeedtest/Issues) page. If I, the PiSpeedtest main developer, finds any errors and/or exceptions, I will open an issue there and then update its progress. And everyone are free to open Issues and contribute to PiSpeedtest in any way, of course.
_________
### Accuracy information:
 As with almost every speedtesting software, 100% accurate results cannot be guaranteed. Most results are rounded to the closest number without decimals. For more information, you can read the "Inconsistency" information [here](https://github.com/sivel/speedtest-cli). With that said, PiSpeedtest is really reliable and the results that you get will be pretty accurate. The application is trustworthy to use for speedtesting.
________
