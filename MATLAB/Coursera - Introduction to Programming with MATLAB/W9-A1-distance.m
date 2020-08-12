%%% Week 09 - Assignment: Excel Files
% Practice Excel file I/O.

% The attached 'Distances.xlsx' file contains a spreadsheet with the pairwise distances in miles of the top 100 US cities by population.
% Write a function called 'get_distance' that accepts two character vector inputs representing the names of two cities.
% The function returns the distance between them as an output argument called 'distance'.
% If one or both of the specified cities are not in the file, the functions returns -1.
% Your function should load the data only once. File I/O is a time consuming operation.

function [distance] = get_distance(city1,city2)
    % input format : city1 = 'city1, STATE' , city2 = 'city2, STATE'
    % NOTES: City names are only to be found on column A and row 1.
    
    [~, citylist] = xlsread('Distances.xlsx',1,'A:A'); % Distances is a square matrix.
    
    matchfound1 = false; matchfound2 = false;
    for i = 1:numel(citylist)
        if strfind(city1,citylist{i,1}) == 1
            coord1 = i;
            matchfound1 = true;
        end
        if strfind(city2,citylist{i,1}) == 1
            coord2 = i;
            matchfound2 = true;
        end
    end
    
    if matchfound1 == false || matchfound2 == false
        %fprintf('One or both of the specified cities are not in the file.\n');
        distance = -1;
    else
        num = xlsread('Distances.xlsx');
        distance = num(coord1,coord2);
        %fprintf('The distance between [%s] and [%s] is %u miles.\n',city1,city2,distance);
    end
