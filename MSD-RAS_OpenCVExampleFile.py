# import libraries used in the script
# in this case we will import cv2 - the opencv module and argparse for command line argument inputs

import cv2
import argparse


# Review of argparse documentation shows us the syntax for adding command line arguments

parser = argparse.ArgumentParser()

# In this function we add a nickname to be used in the command line (-f) and a name to be used in the script (File)
parser.add_argument("-f", "--File")
args = parser.parse_args()
filename = args.File

# Now we write our openCV Methods here ---------

# Read an Image
img = cv2.imread(args.File)

# Write an Image
cv2.imwrite('output.jpg',img)