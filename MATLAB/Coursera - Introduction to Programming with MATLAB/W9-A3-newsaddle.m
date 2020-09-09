%%% Week 09 - Final Assignment 1: Saddle Points
% Find the saddle points of a matrix.

% Write a function called 'saddle' that finds saddle points in the input matrix 'M'. For the purposes of this problem:
% A saddle point is defined as an element whose value is greater than or equal to every element in its row,
% and less than or equal to every element in its column. Note that there may be more than one saddle point in 'M'.
% Return a matrix called 'indices' that has exactly two columns.
% Each row of indices corresponds to one saddle point with the first element of the row containing the row index of the saddle point,
% and the second element containing the column index. If there is no saddle point in 'M', then 'indices' is the empty array.

function [indices] = saddle(M)
    indices = [];
    [row col] = size(M);
    
    if col == 1
        biggest = M;
    else
        biggest = max(M');  % biggest elements on every row
    end
    if row == 1
        smallest = M;
    else
        smallest = min(M);  % smallest elements on every row
    end
    
    for i = 1:row  % # rows
        for j = 1:col  % # columns
            if M(i,j) == biggest(i) && M(i,j) == smallest(j)  % saddle point
                indices = [indices ; i,j];
            end
        end
    end
