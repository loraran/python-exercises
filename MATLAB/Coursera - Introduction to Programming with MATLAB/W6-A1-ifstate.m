%%% Week 06 - Assignment: If-statement practice
% Practice if-statements

% Write a function called 'picker' that takes three input arguments called 'condition', 'in1' and 'in2' in this order.
% The argument condition is a logical. If it is true, the function assigns the value of in1 to the output argument 'out'.
% Otherwise, it assigns the value of in2 to out.

function [out] = picker(condition,in1,in2)
    if condition == 1
        out = in1;
    else
        out = in2;
end

% Code to call your function:

out = picker(true,1,2)
out = picker(false,1,2)
