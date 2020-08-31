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
    for i = 1:numel(M(:,1))  % for each row in M... numel(M(:,1)) = # of rows
        fprintf('Now reading: LINE %d\n',i);
        biggest = [M(i,1),i,1]; % suppose the first element is the highest of its row
        for j = 2:numel(M(1,:))  % for each column in M... numel(M(1,:)) = # of columns
            if M(i,j) > biggest(1)
                biggest = [M(i,j),i,j];  % [number lin col]
            end
        end
        fprintf(' BIGGEST ELEMENT IN LINE %d: M(%d,%d) = %f\n',i,biggest(2),biggest(3),biggest(1));
        
        %fprintf('   For the possible saddle point M(%d,%d) = %f ...\n',biggest(2),biggest(3),biggest(1));
        smallest = M(1,biggest(3)); % suppose the first element is the smallest of its column
        for k = 1:numel(M(:,1))  % # rows
            if M(k,biggest(3)) < smallest
                smallest = [M(k,biggest(3)),k,biggest(3)];
            end
            %smallest
        end
        fprintf(' SMALLEST ELEMENT IN COLUMN %d: M(%d,%d) = %f\n\n',biggest(3),smallest(2),smallest(3),smallest(1));
        
        if biggest(1) == smallest(1)
            indices = [indices ; biggest(2),biggest(3)]
        end
        
    end
