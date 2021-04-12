
### Windows

* Powershell

```
(get-date) - (gcim Win32_OperatingSystem).LastBootUpTime # uptime
Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize # List of Your Installed Programs on Windows

```
