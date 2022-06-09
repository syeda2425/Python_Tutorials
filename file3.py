f = open("demofile.txt.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt.txt", "r")
print(f.read())