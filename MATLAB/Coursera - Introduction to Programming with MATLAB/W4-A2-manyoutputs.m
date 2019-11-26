%%% Week 04 - Assignment: Multiple Outputs
% Function with Multiple Outputs

% Write a function called 'corners' that takes a matrix as an input argument and returns four outputs:
% the elements at its four corners in this order: top_left, top_right, bottom_left and bottom_right.
% (Note that loops and if-statements are neither necessary nor allowed as we have not covered them yet.)

function [top_left, top_right, bottom_left, bottom_right] = corners(matrix)
top_left = matrix(1,1);
top_right = matrix(1,end);
bottom_left = matrix(end,1);
bottom_right = matrix(end,end);
end

% Code to call your function:

A = randi(100,4,5)
[top_left, top_right, bottom_left, bottom_right] = corners(A)
B = [1; 2]
[top_left, top_right, bottom_left, bottom_right] = corners(B)
