---------------------------------------------------------------------------------------------------------------------
版本:v1.0.1002
版本資訊:更改Readme檔案
Git:https://github.com/milkfalling/offline_package_maker.git
---------------------------------------------------------------------------------------------------------------------
事前準備
	1.C:\BiDaETech資料夾
	2.python最新版

製作offline_module_package
	1.連網
	2.安裝最新版Python
	3.執行offline_package_maker.cmd檔，它將會自動執行以下步驟
		1.將舊的BOT資料夾跑一次bot_py_duplicator.py，將BOT資料夾中的所有.py檔案複製一份
		2.執行lost_module_inspector.py取得所有.py檔案中缺少的module(無版號)並自動存成requirements.txt
		3.使用installpackacges.py將requirements.txt中的依賴項都安裝至環境
		4.執行pip freeze → requirements.txt指令將原本的requirements.txt替換為有版號的版本
		5.執行pip install pip-download指令安裝能夠下載離線包的模組
		6.執行pip-download -r requirements.txt指令下載所有依賴項的離線包
		7.將第一步複製的檔案清除
	4.離線包做好以後，即可安心帶到案場

如何將離線包安裝到案場?
	1.執行install_dependency.cmd
---------------------------------------------------------------------------------------------------------------------