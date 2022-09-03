def make_judge(grade, points):
    is_retest = ()
    is_out = ()
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

