major_list = []
n = int(input('Enter the number of smallest and largest values to remove:'))
s = input('Enter an integer (q or Q to quit):')
'''若input為Q or q 則停止運行'''
while s != 'Q' and s != 'q':
    major_list.append(int(s))
    s = input('Enter an integer (q or Q to quit):')
def remove_outliers(List, n):    #Define Function
    List.sort()  # 將列表由小至大排列
    Newlist = List[n:-n]
    outliers = List[:n] + List[-n:]
    return Newlist,outliers
NewList,outliers= remove_outliers(major_list,n)
print('The original data:', major_list)
print('The data with the outliers removed:',NewList)
print('The outlier:', outliers)

