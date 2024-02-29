# Build and install the health check service

This is a non functionnal template for a windows service. The Windows service build and install but can't start.

the service is named MAGE_MTE_MonitoringService and will appear has such in the windows services.msc

this folder contains two files:
- SMWinservice.py - an abstract class that we will use to build the service
- MAGE_MTE_MonitoringService.py - the actual service


## Build, Install and Start the service

### Build

First create a python venv


```
cd .\windowsServices
```

```
python venv -m venv_name
```

```
.\venv_name\Scripts\activate
```

Setup the venv

```
pip install -r .\requirements.txt
```

```
.\venv_name\Scripts\pywin32_postinstall.py -install
```

```
.\venv_name\Scripts\deactivate
```

Build the service
```
.\venv_name\Scripts\pyinstaller.exe --hiddenimport win32timezone -F .\MAGE_MTE_MonitoringService.py
```

### Install

Install the service (Admin PowerShell required for this step)

```
.\dist\MAGE_MTE_MonitoringService.exe --startup=auto install
```
### Start

Start the service
```
.\dist\MAGE_MTE_MonitoringService.exe start
```
At this point you will probably get the following error that we where not able to solve.
```
File "C:\YOUR_PATH\MAGE_MTE_MonitoringService.py", line 45, in <module>
    servicemanager.StartServiceCtrlDispatcher()
pywintypes.error: (1063, 'StartServiceCtrlDispatcher', 'Le processus de service n’a pas pu se connecter au contrôleur de service.')
```