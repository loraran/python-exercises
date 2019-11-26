%%% Week 03 - Assignment: Matrix Arithmetic
% Matrix arithmetic practice.
% Given a Matrix 'A':
% 1. Create a row vector of 1's that has same number of elements as A has rows. 
% 2. Create a column vector of 1's that has the same number of elements as A has columns. 
% 3. Using matrix multiplication, assign the product of the row vector, the matrix A, and the column vector
% (in this order) to the variable 'result'. Think about what the result represents...

A = [1:5; 6:10; 11:15; 16:20];
row_vector(1,1:numel(A(:,1))) = 1;
column_vector(1:numel(A(1,:)),1) = 1;
result = (row_vector*A)*column_vector;
