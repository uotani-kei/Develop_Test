from judge_maker import make_judge

def test_make_judge_no1():
    """マトリックスNo1 ←テストを行うマトリックスの番号
    10点より下の点数がある場合 ←テストの内容
    """
    result = make_judge('A', [9, 100, 100, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 3

def test_make_judge_no2():
    """マトリックスNo2 ←テストを行うマトリックスの番号
    30点以下の点数が3回以上ある場合 ←テストの内容
    """
    result = make_judge('B', [10, 15, 20, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 2

def test_make_judge_no3():
    """マトリックスNo2 ←テストを行うマトリックスの番号
    30点以下の点数が3回以上ある場合 ←テストの内容
    """
    result = make_judge('B', [10, 15, 100, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 1
    
def test_make_judge_no4():
    """マトリックスNo2 ←テストを行うマトリックスの番号
    30点以下の点数が3回以上ある場合 ←テストの内容
    """
    result = make_judge('D', [10, 15, 100, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 2

def test_make_judge_no5():
    """マトリックスNo2 ←テストを行うマトリックスの番号
    30点以下の点数が3回以上ある場合 ←テストの内容
    """
    result = make_judge('E', [10, 15, 100, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 3