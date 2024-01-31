import os
import pathlib
import requests
import shutil

# I'd suggest you keep this on unless most of the tiles you have are corrupted. 
# Having this true will allow you to skip the tiles you already have if you decide to stop and rerun it at any point. 
patchingMode = True

minX = -56
maxX = 43
minY = -56
maxY = 43
total = (minX - maxX) * (minY - maxY)
tileCount = 0

thisDir = str(pathlib.Path(__file__).parent.resolve())
pathlib.Path(thisDir + "/Tiles/Teyvat/").mkdir(parents=True, exist_ok=True)
nameFmt = thisDir + "/Tiles/Teyvat/{0}_{1}.jpg"

urlFmt = "https://game-cdn.appsample.com/gim/map-teyvat/v44-rc1/15/tile-{0}_{1}.jpg"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
for x in range(minX, maxX):
    for y in range(minY, maxY):
        is404 = False
        imgURL = urlFmt.format(x, y) 
        filePath = nameFmt.format(x - minX, y - minY)
        if os.path.isfile(filePath) and patchingMode:
            tileCount += 1
        else: 
            result = requests.get(imgURL, headers=headers, stream=True)
            if (result.status_code != 404):
                with open(filePath, 'wb') as outFile:
                    shutil.copyfileobj(result.raw, outFile)
                del result
                tileCount += 1
            else:
                total -= 1
                is404 = True

        # Logging
        print("Total: {0}/{1} \t\t| {2}  ({3}, {4}) => ({5}, {6}) \t\t| At URL: {7}".format(tileCount, total, "404" if is404 else "Tile", x, y, x - minX, y - minY, imgURL))

print("All tiles successfully downloaded to directory:")
print(thisDir.replace("\\", "/") + "/Tiles/Teyvat")

exit() #sometimes it doesn't auto exit in VS Code, so adding this
