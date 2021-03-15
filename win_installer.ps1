# Choco package manager install
Set-ExecutionPolicy Bypass -Scope Process -Force;
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

choco install -y python --version 3.7.9
choco install -y chromedriver
pip install -r requirements.txt
Write-Host "[ chromedriver launch ]"
Write-Host "[ run following command on another shell tab : python Napoleon.py ]"
chromedriver
python3 Napoleon.py
