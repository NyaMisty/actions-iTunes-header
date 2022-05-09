cd %~dp0

curl -LO https://secure-appldnld.apple.com/itunes12/091-87819-20180912-69177170-B085-11E8-B6AB-C1D03409AD2A6/iTunes64Setup.exe
iTunes64Setup.exe /extract

@REM start /wait msiexec.exe /i AppleApplicationSupport.msi /qn
start /wait msiexec.exe /i AppleApplicationSupport64.msi /qn
@REM start /wait msiexec.exe /i AppleMobileDeviceSupport64.msi /qn
@REM start /wait msiexec.exe /i AppleSoftwareUpdate.msi /qn
@REM start /wait msiexec.exe /i Bonjour64.msi /qn
start /wait msiexec.exe /i iTunes64.msi /qn

python3 patch_itunes.py