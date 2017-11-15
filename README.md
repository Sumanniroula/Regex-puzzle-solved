# Regex-puzzle-solved

Question: There is a log file which contains the many GET requests. Using regular expression, parse the request that contain images(only images, not others). These are the vertical pieces of the images that are distributed all over internet. You need to collect them and make a single image. Make a list of the image urls after parsing(without repeatation), sort them alphabetically and finally merge the images in a html file to know what the image contains !!
Logpuzzle exercise

Given an apache log file, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"

read_urls():
Returns a list of the puzzle urls from the given log file,
extracting the hostname from the filename itself.
Screens out duplicate urls and returns the urls sorted into increasing order."""

download_images():
Given the urls already in the correct order, downloads
each image into the given directory.
Gives the images local filenames img0, img1, and so on.
Creates an index.html in the directory
with an img tag to show each local image file.
Creates the directory if necessary.
