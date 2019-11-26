%%% Week 08 - Assignment: Character Vectors
% Simple Encryption. Work with text stored as character vectors.

% Caesar's cypher is the simplest encryption algorithm. It adds a fixed value to the ASCII (unicode) value of each character of a text.
% In other words, it shifts the characters. Decrypting a text is simply shifting it back by the same amount, that is, it substracts the
% same value from the characters.
% Write a function called 'caesar' that accepts two arguments: the first is the character vector to be encrypted, while the second is the
% shift amount. The function returns the output argument 'coded', the encrypted text. The function needs to work with all the visible
% ASCII characters from space to ~. The ASCII codes of these are 32 through 126. If the shifted code goes outside of this range,
% it should wrap around. For example, if we shift ~ by 1, the result should be space. If we shift space by -1, the result should be ~.
% Here are a few things you may want to try with MATLAB before starting on this assignment:
%    double(' ')
%    ans =
%        32
%    double('~')
%    ans =
%       126
%    char([65 66 67])
%    ans =
%        'ABC'
%    ' ' : '~'
%    ans =
%        ' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
% And here are a few example runs:
%    caesar('ABCD',1)
%    ans =
%        'BCDE'
%    caesar('xyz ~',1)
%    ans =
%        'yz{! '
%    caesar('xyz ~',-1)
%    ans =
%        'wxy~}'

function [coded] = caesar(charvec,shift)
    % Caesar's cypher is the simplest encryption algorithm. It adds a fixed value to the ASCII (unicode) value of each character.
    % This function accepts two arguments: the first is the character vector to be encrypted, while the second is the shift amount.
    % The function returns the encrypted text. It works with all the visible ASCII characters from space to ~ (32 through 126).
    
    %% VERSION 3 - USING circshift
    strbank = char(32:126);
    fprintf('%s\n\n',strbank);
    for i = 1:numel(charvec) % for each letter of the charvec sentence...
        pos = findstr(strbank,char(charvec(i))); % ...we find the POSITION where said letter is on the list of valid chars (NOT DOUBLE VALUE)...
        shiftedbank = circshift(strbank,-shift); % ...then SHIFT the valid chars to find which letter will substitute the original...
        coded(i) = shiftedbank(pos); % ...and finally we put the new letter (on the original POSITION) on the coded vector.
    end

    fprintf('ORIGINAL : %s\n',charvec);
    fprintf('ENCRYPTED: %s\n\n',coded);
%     double(charvec)
%     double(coding)
%     double(coded)
end

% Code to call your function:

coded    = caesar('ABCD',  3)
decoded  = caesar(coded,  -3)
wrap     = caesar('1234', 96)
back     = caesar(wrap,  -96)
