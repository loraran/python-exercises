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
    
    if size(M) == [1 1]
        indices = [1 1];
    elseif numel(M(:,1)) == 1  % row matrix
        % procura somente o maior número
        biggest = [M(1,1),1,1];
        for j = 2:numel(M(1,:))  % # columns
            if M(1,j) > biggest(1)
                biggest = [M(1,j),1,j];  % [number lin col]
            elseif M(1,j) == biggest(1)
                biggest = [biggest ; M(1,j),1,j];
            end
        end
        %biggest
        indices = [biggest(:,2),biggest(:,3)];
        
    elseif numel(M(1,:)) == 1  % column matrix
        % procura somente o menor número
        smallest = [M(1,1),1,1];
        for k = 2:numel(M(:,1))  % # rows
            if M(k,1) < smallest(1)
                smallest = [M(k,1),k,1];
            elseif M(k,1) == smallest(1)
                smallest = [smallest ; M(k,1),k,1];
            end
        end
        %smallest
        indices = [smallest(:,2),smallest(:,3)];
        
    else  % rectangular matrix
        for i = 1:numel(M(:,1))  % for each row in M... numel(M(:,1)) = # of rows
            biggest = [M(i,1),i,1]; % suppose the first element is the highest of its row
            for j = 2:numel(M(1,:))  % for each column in M... numel(M(1,:)) = # of columns
                if M(i,j) > biggest(1)
                    biggest = [M(i,j),i,j];  % [number lin col]
                elseif M(i,j) == biggest(1)
                    biggest = [biggest ; M(i,j),i,j];
                end
            end
            biggest
            
            smallest = M(1,biggest(3)); % suppose the first element is the smallest of its column
            for k = 2:numel(M(:,1))  % # rows
                if M(k,biggest(3)) < smallest
                    smallest = [M(k,biggest(3)),k,biggest(3)];
                end
            end
            %smallest

            if biggest(1) == smallest(1)
                indices = [indices ; biggest(:,2),biggest(:,3)];
            end
        end
    end
    
    
    
% create an interesting surface
%[X,Y] = meshgrid(-2:0.5:2,-1:0.5:1); Z = (X.^2-Y.^2)'
%Z = [4 2 3 4 4 3 2 1]
%Z = [1; 2; 3; 4; 4; 3; 2; 1]
%Z = [1 2 3 5 4 3 2 1 ; 2 3 4 5 4 3 2 1]
Z = zeros(randi([3 6]),randi([3 6]))
% find saddle points
indices = saddle(Z)
