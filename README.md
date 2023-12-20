# Genshin World Map
A map downloader and combiner to get the Genshin Impact world map

**Map Downloader** scrapes the [interactive map website](https://genshin-impact-map.appsample.com/#) to pull out the highest resolution variants of the map tiles. Each tile is 256x256 and there's nearly 10k tiles that needs to be downloaded, so if you're running it, go do something else while you wait, it will take a while. 

**Map Combiner** takes the tiles and combines them into one single image, this process is a lot quicker than the downloading but the saving process takes a minute or two as the final image size is nearly 25600x25600.

If you're downloading the scripts, make sure to put both scripts in the same folder as the paths are made to be specific, you can have them anywhere, but they need to be together. First run the Teyvat_Map_Downloader.py and once it finishes, run the Teyvat_Map_Combiner.py

# Requirements 
The scripts were made and tested with Python 3.12, I can't guarantee that it will work for other versions but it should, the main limitations may be the following external modules.
[The Python Requests Module](https://pypi.org/project/requests/) is needed for the map downloader and [Pillow (Python Image Library Fork)](https://pillow.readthedocs.io/en/stable/installation.html) is needed for the map combiner.
