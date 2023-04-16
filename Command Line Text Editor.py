from bs4 import BeautifulSoap4
print("Command Line Tet Editor as 3rd Beginner Projects")
print("--------------------------------")
print("First choose a file format")
print("example: main.py, index.html or style.css etc")
extensionChooser = input(" Enter Extension here (With out *Dot): ")
fileName = input("Enter File Name Also: ")



def writeFunction():
    global editingMode
    input("Type Here...\n")
    editingMode = True
    linesOfText = []
    while editingMode == True:
        text = input()
        if text == '/saveAndExit':
            editingMode = False
        else:
            linesOfText.append(text)
        if editingMode==False:
            with open(f'{fileName}.{extensionChooser}', 'a') as f:
                f.write('\n'.join(linesOfText))

with open(f'{fileName}.{extensionChooser}', 'a') as f:
    writeFunction()

