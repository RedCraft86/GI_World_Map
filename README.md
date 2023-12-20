# Genshin World Map
A map downloader and combiner to get the Genshin Impact world map.
Check [releases](https://github.com/RedCraft86/Genshin_World_Map/releases) if you only care about the map images and not the process.

## Other Maps
Places like Enkanomiya and Chasm does not have maps that keep on updating and therefore does not have scripts for them, find them in [releases](https://github.com/RedCraft86/GI_World_Map/releases) for the map images.

## Teyvat
**Teyvat Map Downloader** scrapes the [interactive map website](https://genshin-impact-map.appsample.com/#) to pull out the highest resolution variants of the map tiles. Each tile is 256x256 and there's a lot of tiles that needs to be downloaded, so if you're running it, go do something else while you wait, it will take a while. 

**Teyvat Map Combiner** takes the tiles and combines them into one single image, this process is a lot quicker than the downloading but the saving process takes a minute or two as the final image is very large.

If you're downloading the scripts, make sure to put both scripts in the same folder as the paths are made to be specific, you can have them anywhere, but they need to be together. First run the Teyvat_Map_Downloader.py and once it finishes, run the Teyvat_Map_Combiner.py

# Requirements 
The scripts were made and tested with Python 3.12, I can't guarantee that it will work for other versions but it should, the main limitations may be the following external modules.
[The Python Requests Module](https://pypi.org/project/requests/) is needed for the map downloader and [Pillow (Python Image Library Fork)](https://pillow.readthedocs.io/en/stable/installation.html) is needed for the map combiner.
