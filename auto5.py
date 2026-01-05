import subprocess


calc = subprocess.Popen("C:\\Windows\\System32\\calc.exe")
calc.wait()
web = subprocess.Popen("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
web.wait()


print("Hi Saška")
