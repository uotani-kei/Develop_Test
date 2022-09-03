def make_judge(grade, points):
    is_retest = True if sum((data <= 30 for data in points)) >= 3 else False 
    is_out = any((data < 10 for data in points))
    if is_out:
        return 3
    elif is_retest:
        return 2
    elif grade == 'A' or grade == 'B' or grade == 'C':
        return 1
    elif grade == 'D':
        return 2
    elif grade == 'E':
        return 3

