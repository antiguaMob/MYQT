@ECHO OFF
cls
C:\Users\fernandomoreira\AppData\Local\Programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\UI\LAYOUT\MainWindow.ui        -o .\Lib\UI\SCRIPT\MainWindow.py  
C:\Users\fernandomoreira\AppData\Local\Programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\UI\LAYOUT\ConnectorWindow.ui        -o .\Lib\UI\SCRIPT\ConnectorWindow.py  
C:\Users\fernandomoreira\AppData\Local\Programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\UI\LAYOUT\Testes.ui        -o .\Lib\UI\SCRIPT\Teste_ui.py  

py.exe Connector.py