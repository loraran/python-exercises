%%% Week 08 - Assignment: Using Cell Arrays
% Sparse Matrix. Practice using cell arrays.

% A sparse matrix is a large matrix with almost all elements of the same value (typically zero).
% The normal representation of a sparse matrix takes up lots of memory when the useful information can be captured with much less.
% A possible way to represent a sparse matrix is with a cell vector whose first element is a 2-element vector representing the size
% of the sparse matrix. The second element is a scalar specifying the default value of the sparse matrix.
% Each successive element of the cell vector is a 3-element vector representing one element of the sparse matrix that has a value other
% than the default. The three elements are the row index, the column index and the actual value.
% Write a function called 'sparse2matrix' that takes a single input of a cell vector as defined above and returns the output argument
% called 'matrix', the matrix in its traditional form. Consider the following run:
%     cellvec = {[2 3], 0, [1 2 3], [2 2 -3]};
%     matrix = sparse2matrix(cellvec)
%     matrix =
%          0     3     0
%          0    -3     0

function [matrix] = sparse2matrix(cellvec)
    % input format: cellvec = {[2 3], 0, [1 2 3], [2 2 -3]}
    % cellvec{1} : 2-element vector representing the size of the sparse matrix.
    % cellvec{2} : scalar specifying the default value of the sparse matrix.
    % cellvec{3...} : 3-element vector representing one element of the sparse matrix that has a value other than the default.
    % The three elements are the row index, the column index and the actual value.
    matrix = zeros(cellvec{1}(1),cellvec{1}(2)) + cellvec{2};
    for i = 3:numel(cellvec)
        matrix(cellvec{i}(1),cellvec{i}(2)) = cellvec{i}(3);
    end
end

% Code to call your function:

matrix = sparse2matrix({[2 3], 0, [1 2 3], [2 2 -3]})
