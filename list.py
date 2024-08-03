# Go through all the image files in this folder, and create a list of them. 
# The format of each item should be a markdown image link, pointing to the root of the domain istic.uk

import os

# Get the current working directory
path = os.getcwd()

# Get the list of files in the current directory
files = os.listdir(path)

# Filter out the files that are not images (webp is supported)
images = [f for f in files if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.webp')]
images.sort()

# Create the markdown list
list = ""
for image in images:
    list += f"![](https://istic.uk/{image})"
    list += "\n" * 16

