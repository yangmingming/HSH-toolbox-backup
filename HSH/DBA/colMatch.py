##encoding=utf8

def hist(array):
    '''对数组进行频率统计
    '''
    res = dict()
    for i in array:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res

def text_dist(hist1, hist2):
    '''给两个频率统计字典，计算频率字典的欧式距离（定义为"文本距离"）
    '''
    difference = list()
    for key in list( set.union(set(hist1.keys()), set(hist2.keys())) ):
        difference.append(  (hist1.get(key,0) - hist2.get(key,0))**2  )
    return sum(difference)

def keep_alpha(text):
    '''返回：删除掉text除a-z之外的字符之后的小写字符串
    '''
    res = list()
    text = text.lower()
    for char in text:
        if char.isalpha():
            res.append(char)
    return ''.join(res)

def column_dist(name1, name2):
    '''返回两个文本间的文本距离
    '''
    return text_dist(hist(keep_alpha(name1)), hist(keep_alpha(name2)) )

def matchone(pattern, array, tolerance = 4):
    '''从array中找到最匹配pattern的那个match
    只有match与pattern的文本距离小于tolerance才会被判定为成功匹配
    '''
    min_dist = 9999
    for text in array:
        if column_dist(pattern, text) < min_dist:
            min_dist = column_dist(pattern, text)
            match = text
#     print 'pattern = "%s" MATCH array = "%s", distance = %s' % (pattern, match, min_dist)
    if min_dist > tolerance:
#         print '"%s" found nothing to match.' % pattern
        return None
    else:
        return match

def unit_test():
    a = ['employee name', 'enroll date']
    b = ['employee_name', 'enroll_date']
    for i in a:
        match = matchone(i, b)
        print '<%s> - <%s>' % (i, match)
        
if __name__ == '__main__':
    unit_test()
    
    

