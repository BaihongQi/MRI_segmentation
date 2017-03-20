I = imread('test.jpg');
Iout=segmentation(I,4,'pso');
imshow(Iout);