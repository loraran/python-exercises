%%% Week 07 - Assignment: Lesson 6 Wrap-up
% SUMMA

% Write a function called 'max_sum' that takes 'v', a row vector of numbers, and 'n', a positive integer as inputs.
% The function needs to find the n consecutive elements of v whose sum is the largest possible.
% In other words, if 'v' is [1 2 3 4 5 4 3 2 1] and 'n' is 3, it will find 4 5 and 4 because their sum of 13 is the largest of any 3
% consecutive elements of v. If multiple such sequences exist in v, max_sum returns the first one.
% The function returns 'summa', the sum as the first output argument and 'index', the index of the first element of the n consecutive ones
% as the second output. If the input n is larger than the number of elements of v, the function returns 0 as the sum and -1 as the index.

function [summa,index] = max_sum(v,n)
summa = -inf;
    if n > numel(v)
        summa = 0;
        index = -1;
    elseif n <= 0 || rem(n,1) ~= 0
        error("Error! Input n must be a positive integer.");
    else
        for i = 1:(numel(v)-n+1)
            subv = v(i:i+n-1);
            sumv = sum(subv);
            if sumv > summa
                summa = sumv;
                index = i;
            end
        end
    end
end

% Code to call your function:

[summa, index] = max_sum([1 2 3 4 5 4 3 2 1],3)
