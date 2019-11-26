%%% Week 07 - Assignment: Logical Indexing
% Logical Arrays Practice

% Write a function called 'freezing' that takes a vector of numbers that correspond to daily low temperatures in Fahrenheit.
% Return 'numfreeze', the number of days with sub freezing temperatures (that is, lower than 32 F) without using loops.

function [numfreeze] = freezing(daily_low)
    numfreeze = numel(daily_low(daily_low < 32));
end

% Code to call your function:

numfreeze = freezing([45 21 32 31 51 12])
