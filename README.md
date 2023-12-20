# Genshin World Map
A map downloader and combiner to get the Genshin Impact world map

Teyvat_Map_Downloader scrapes the interactive map website to pull out the highest resolution variants of the map tiles. Each tile is 256x256 and there's nearly 10k tiles that needs to be downloaded, so if you're replicating me, go do something else while you wait, it will take a while. 
Teyvat_Map_Combiner takes the tiles and combines them into one single image, this process is a lot quicker than the downloading but the saving process takes a minute or two as the final image size is nearly 25600x25600.

If you're downloading the scripts, make sure to put both scripts in the same folder as the paths are made to be specific, you can have them anywhere, but they need to be together. First run the Teyvat_Map_Downloader.py and once it finishes, run the Teyvat_Map_Combiner.py

# Note
This requires [The Python Requests Module](https://pypi.org/project/requests/) for the map downloader and [Pillow (Python Image Library Fork)](https://pillow.readthedocs.io/en/stable/reference/Image.html) for the map combiner
