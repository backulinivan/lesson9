def row(n):
    if n == 0:
        return(4e0)
    elif n == 1:    
        return(4.25e0)
    else:
        return(108e0 - (815e0 - 1500e0/row(n-2))/row(n-1))

print(row(int(input())))

''' row(int(input())) != 5 т.к. существует проблема округления, и, по сути, человек умнее машины, и восстание машин невозможно '''            
