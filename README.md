# grabcut-gui

An implementation of grabcut that allows you to select a region using a GUI. 

# Dependencies
python3-opencv
python3-matplotlib

# Usage

python grabcut.py inputimage

Draw around region using your mouse

Press enter

THe resultant file will but output with the same file name as teh input with the region dimensions appended. This is so you can manually execute the region selection at a later date without using a GUI

# Limitations
One ouput of Grabcut produces a nearly black image except the mask has the colour #060606. To produce an alpha mask this is replaced with #FFFFFF. This fill process sometimse overspills and so your output image may have some random #000000 pixels.
