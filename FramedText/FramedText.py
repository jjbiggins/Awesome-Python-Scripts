import os
borderstyle = "║"

def drawboxtext(dat):
    height = len(dat)
    for y in range(height):
        dat[y] = f" {dat[y]} "
    x = 0
    line = "╔"
    width = len(max(dat, key=len))+1
    while x < width-1:
        line = f"{line}═"
        x += 1
    line = f"{line}╗"
    print(line)
    for counter in range(height):
        reqspaces = width -1- len(dat[counter])
        xsp = ""
        while reqspaces > 0:
            xsp = f"{xsp} "
            reqspaces -= 1
        print(borderstyle+dat[counter]+xsp+borderstyle)
    x = 0
    line = "╚"
    while x < width-1:
        line = f"{line}═"
        x += 1
    line = f"{line}╝"
    print(line)


print("Framed text generator by Julian Drake.\n")
print("")
while True:
    print("Enter the items in the frame. (Leave blank to submit.)")

    items=[]
    i=0
    while 1:
        i+=1
        item=input('Enter item %d: '%i)
        if item=="":
                break
        items.append(item)

    print("")
    drawboxtext(items)
    print("")
    input("")
    os.system('cls')

