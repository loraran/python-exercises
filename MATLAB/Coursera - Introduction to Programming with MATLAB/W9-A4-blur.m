%%% Week 09 - Final Assignment 2: Image Blur
% Write a function to blur an image.

% Write a function called 'blur' that blurs the input image. The function is to be called like this:
%   output = blur(img,w);
% where 'img', the input image is a two-dimensional matrix of grayscale pixel values between 0 and 255.
% Blurring is to be carried out by averaging the pixel values in the vicinity of every pixel.
% Specifically, the output pixel value is the mean of the pixels in a square submatrix of size 2w+1,
% where the given pixel sits in the center. (for example: if w = 1, we use a 2w+1 = 3x3 matrix)
% Only use valid pixels when portions of the blurring matrix fall outside the image (respect borders).
% Both input 'img' and output 'output' are of type UINT8.

function [output] = blur(img,w)
    [row col] = size(img);  % img dimensions  
    % setting up a submatrix compatible with blurtool
    output = [];
    for i = 1:col
        istart = i-w;        
        if istart < 1
            istart = 1;
        end
        iend = i+w;
        if iend > col
            iend = col;
        end

        row_output = [];
        for j = 1:row
            jstart = j-w;
            if jstart < 1
                jstart = 1;
            end
            jend = j+w;
            if jend > row
                jend = row;
            end
            subimg = img(jstart:jend,istart:iend);  % submatrix that will be used to calculate the mean value
            row_output = [row_output , mean(subimg, 'all')];
        end
        output = [output ; row_output];
    end
    output = uint8(output');
    
    
    
img = imread('vandy.png');
%image(img);
output = blur(img,2);
imshow(output);
