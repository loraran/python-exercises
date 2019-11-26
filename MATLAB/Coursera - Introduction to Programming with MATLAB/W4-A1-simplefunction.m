%%% Week 04 - Assignment: A Simple Function
% Write your first function.

% Write a function called 'tri_area' that returns the area of a triangle with base b and height h,
% where b and h are input arguments of the function in that order.

function area = tri_area(b,h)
    area = (b*h)/2;
end

% Code to call your function:

area = tri_area(5,4)
