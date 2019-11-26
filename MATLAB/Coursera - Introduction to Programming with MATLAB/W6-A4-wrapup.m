%%% Week 06 - Assignment: Lesson 5 Wrap-up

% Write a function called 'valid_date' that takes three positive integer scalar inputs 'year', 'month', 'day'.
% If these three represent a valid date, return a logical 'true', otherwise 'false'. The name of the output argument is 'valid'.
% If any of the inputs is not a positive integer scalar, return 'false' as well.
% Note that every year that is exactly divisible by 4 is a leap year, except for years that are exactly divisible by 100.
% However, years that are exactly divisible by 400 are also leap years.
% For example, the year 1900 was not leap year, but the year 2000 was.
% Note that your solution must not contain any of the date related built-in MATLAB functions.

function [valid] = valid_date(year,month,day)
    fprintf("%g / %g / %g",day,month,year);
    if ~(isscalar(year) && isscalar(month) && isscalar(day))                % Scalar condition
        valid = false;
        fprintf("\nInvalid date! Input must be a scalar.\n\n");
    elseif (rem(year,1) ~= 0) || (rem(month,1) ~= 0) || (rem(day,1) ~= 0)   % Integer condition
        valid = false;
        fprintf("\nInvalid date! Input must be an integer.\n\n");
    elseif year < 0                                                         % Positive condition (year)
        valid = false;
        fprintf("\nInvalid date! Year must be a positive integer.\n\n");
    elseif (month < 0) || (month > 12)                                      % Valid month condition
        valid = false;
        fprintf("\nInvalid date! Month does not exist.\n\n");
    elseif day < 1                                                          % Valid day condition
        valid = false;
        fprintf("\nInvalid date! Day must be a positive integer.\n\n");
    elseif ((month == 4) || (month == 6) || (month == 9) || (month == 11)) && (day > 30)
        valid = false;
        fprintf("\nInvalid date! This month does not have more than 30 days.\n\n");
    elseif ((month == 1) || (month == 3) || (month == 5) || (month == 7) || (month == 8) || (month == 10) || (month == 12)) && (day > 31)
        valid = false;
        fprintf("\nInvalid date! Day does not exist.\n\n");
    elseif (month == 2)                                                     % Leap year/February conditions
        if (rem(year,4) ~= 0) && (day > 28)
            valid = false;
            fprintf("\nInvalid date! February does not have this many days in this year (more than 28).\n\n");
        elseif (rem(year,4) == 0) && (day > 29)
            valid = false;
            fprintf("\nInvalid date! February does not have this many days in this year (more than 29).\n\n");
        elseif ((rem(year,100) == 0) && ~(rem(year,400) == 0)) && (day > 28)
            valid = false;
            fprintf("\nInvalid date! February does not have this many days in this century year (more than 28).\n\n");
        else
            valid = true;
            fprintf("\nValid date!\n\n");
        end
    else
        valid = true;
        fprintf("\nValid date!\n\n");
    end
end

% Code to call your function:

valid = valid_date(2018,4,1)
valid = valid_date(2018,4,31)
