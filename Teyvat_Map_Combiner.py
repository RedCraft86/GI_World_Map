import os
import pathlib
from PIL import Image

maxX = 100
maxY = 100
sizeXY = 256
fileNum = 0

thisDir = str(pathlib.Path(__file__).parent.resolve())
pathlib.Path(thisDir + "/Full/").mkdir(parents=True, exist_ok=True)
directory = thisDir + "/Tiles/Teyvat/"

canvas = Image.new("RGB", (sizeXY * maxY, sizeXY * maxX))
fileNames = next(os.walk(directory), (None, None, []))[2]
for file in fileNames:
    filePath = directory + file

    fileNameSplit = file.replace(".jpg", "").split("_")
    xPos = int(fileNameSplit[0])
    yPos = int(fileNameSplit[1])

    bSkipped = False
    try:
        if os.path.isfile(filePath):
            image = Image.open(filePath)
            canvas.paste(image.rotate(-90), (sizeXY * yPos, sizeXY * xPos))
    except: 
        bSkipped = True 

    fileNum += 1

    # Logging
    print("{0} {1}/{2}  |  Position ({3}, {4})  |  File {5}".format( "Skipped" if bSkipped else "Processed", fileNum, len(fileNames), sizeXY * xPos, sizeXY * yPos, file))

print("Saving, Please Wait...")
canvas.rotate(90).save(thisDir + "/Full/Teyvat.png")
print("Successfully saved to directory:")
print(thisDir.replace("\\", "/") + "/Full")

exit()  #sometimes it doesn't auto exit in VS Code, so adding this
