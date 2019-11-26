%%% Week 05 - Assignment: Built-in functions
% Built-in function practice

% Write a function called 'minimax' that takes 'M', a matrix input argument and returns 'mmr', a row vector containing
% the absolute values of the difference between the maximum and minimum valued elements in each row.
% As a second output argument called 'mmm', it provides the difference between the maximum and minimum element in the entire matrix.

function [mmr,mmm] = minimax(M)
    mmr = abs(max(M,[],2) - min(M,[],2))';
    mmm = max(max(M,[],2)) - min(min(M,[],2));
end

% Code to call your function:

[mmr, mmm] = minimax([1:4;5:8;9:12])
