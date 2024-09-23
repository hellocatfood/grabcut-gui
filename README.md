# grabcut-gui

An implementation of grabcut that allows you to select a region using a GUI. 

# Requirements
OpenCV and matplotlib are required. This can be installed in globally on Ubuntu via the packages

`python3-opencv`
`python3-matplotlib`

or in a python virtual environment via the packages

`opencv-python`
`matplotlib`

# Usage
Run `python grabcut.py inputimage`

Draw around region using your mouse

Press enter

THe resultant file will but output with the same file name as teh input with the region dimensions appended. This is so you can manually execute the region selection at a later date without using a GUI

# Limitations
One ouput of Grabcut produces a nearly black image except the mask has the colour #060606. To produce an alpha mask this is replaced with #FFFFFF. This fill process sometimes overspills and so your output image may have some random #000000 pixels.
