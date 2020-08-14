%%% Week 09 - Assignment: Text Files
% Practice text file I/O.

% Write a function called 'char_counter' that counts the number of a certain character in a text file.
% The function takes two input arguments, 'fname', a char vector of the filename, and 'character', the char it counts in the file.
% The function returns 'charnum', the number of characters found.
% If the file is not found or 'character' is not a valid char, the function returns -1.
% As an example, consider a text file that contains a single line: "This file should have exactly three a-s..."
%     charnum = char_counter('file.txt','a')
%     charnum =
%        3

% function [charnum] = char_counter(fname,character)
%     file = fopen(fname,'rt');
%     if file < 0 || not(ischar(character))
%         %fprintf('Could not open file %s.\n\n',fname);
%         charnum = -1;
%         return
%     elseif not(ischar(character)) || length(character) ~= 1
%         %fprintf('The specified character is invalid.\n\n');
%         charnum = -1;
%         return
%     end
%     
%     charnum = 0;
%     verifychar = fgets(file,1);
%     while ischar(verifychar)
%         if verifychar == character
%             charnum = charnum + 1;
%         end
%         verifychar = fgets(file,1);
%     end
%     
%     if charnum == 0
%         charnum = -1;
%     end
%     fclose(file);
    
function [charnum] = char_counter(fname,character)
    file = fopen(fname,'rt');
    if file < 0
        %fprintf('Could not open file %s.\n\n',fname);
        charnum = -1;
        return
    elseif not(ischar(character)) || length(character) ~= 1
        %fprintf('The specified character is invalid.\n\n');
        charnum = -1;
        return
    end

    charnum = 0;
    verifyline = fgetl(file);
    while ischar(verifyline)
        idx = strfind(verifyline, character);
        charnum = charnum + length(idx);
        verifyline = fgetl(file);
    end
    fclose(file);
