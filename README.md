MOUNTAIN SOUNDS!
By Patrick Lloyd and Heather Martin

This Matlab script makes beautiful, screechy music from pictures of mountains (and maybe trees).

It works like an optical soundtrack decoder where the frequency information is embedded in the distance between the top and bottom white pixels in each column. All the example sounds and 'greyscale_mountain.bmp' are made from mountain6.jpg in the 'landscapes' folder.

It uses im2bw() to convert a greyscale image to a binary one which requires the image processing toolbox. You can use a program like Gimp or Photoshop (or even MS Paint) to generate the binary image if you don't have that toolbox.

TODO:
*   Import unaltered image and have script generate envelope itself
    --> Perform edge detection with Sobel filter or something
    --> Trace upper and lower boundary with bwtraceboundary() or bwboundaries()