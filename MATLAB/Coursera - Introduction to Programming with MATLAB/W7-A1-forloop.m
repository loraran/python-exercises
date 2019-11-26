%%% Week 07 - Assignment: for-loop practice
% Practice for-loops

% Write a function called 'halfsum' that takes as input a matrix and computes the sum of its elements that are in the diagonal
% or are to the right of it. The diagonal is defined as the set of those elements whose column and row indexes are the same.
% In other words, the function adds up the element in the uppertriangular part of the matrix. The name of the output argument is 'summa'.

function [summa] = halfsum(A)
summa = 0;
    for i = 1:numel(A(:,1)) % number of lines
        for ii = 1:numel(A(1,:)) % numer of columns
            if ii >= i
                summa = summa + A(i,ii);
        end
    end
end

% Code to call your function:

summa = halfsum([1 2 3; 4 5 6; 7 8 9])
