function [distance] = get_distance(city1,city2)
    % input format : city1 = 'city1, STATE' , city2 = 'city2, STATE'
    % NOTES: City names are only to be found on column A and row 1.
    
    [~, citylist1] = xlsread('Distances.xlsx',1,'A:A');
    [~, citylist2] = xlsread('Distances.xlsx',1,'1:1');
    % numel(citylist1) and numel(citylist2) are the same.
    
    matchfound1 = false; matchfound2 = false;
    for i = 1:numel(citylist1)
        if strfind(city1,citylist1{i,1}) == 1
            coord1 = i;
            matchfound1 = true;
        end    
        if strfind(city2,citylist2{1,i}) == 1
            coord2 = i;
            matchfound2 = true;
        end
    end
    
    if matchfound1 == false || matchfound2 == false
        fprintf('One or both of the specified cities are not in the file.\n');
        distance = -1;
    else
        num = xlsread('Distances.xlsx');
        distance = num(coord1,coord2);
        fprintf('The distance between [%s] and [%s] is %u miles.\n',city1,city2,distance);
    end
