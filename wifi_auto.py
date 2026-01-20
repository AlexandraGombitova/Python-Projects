import subprocess

meta_data = subprocess.check_output(["netsh", "wlan", "show", "profiles"])
print(meta_data)
data = meta_data.decode("utf-8", errors="backslashreplace")
print(data)
data = data.split("\n")

profiles = []

for i in data:
    if "All User Profile" in i:
        i = i.split(":")


        i = i[1]

        i = i[1:-1]

        profiles.append(i)


print("{:<40} {:<}".format("Name","Password"))
print("--------------------------------------")
for i in profiles:

    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "profile", i , "key=clear"])
        result = result.decode("utf-8", errors="backslashreplace")
        result = result.split("\n")
        result = [b.split(":") [1] [1:-1] for b in result if "Key Content" in b]





        try:
            print("{:<30} {:<}".format(i, result[0]))
        except IndexError:
            print("{:<30} {:<}".format(i, ""))

    except subprocess.CalledProcessError:
        print("Error occured")


