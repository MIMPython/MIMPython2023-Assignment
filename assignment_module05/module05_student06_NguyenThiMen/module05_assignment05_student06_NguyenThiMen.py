def infinitive_loop_use_while():
    '''
    vòng lặp vô hạn với while
    '''
    while 1:
        1


def infinitive_loop_use_for():
    '''
    vòng lặp vô hạn với for
    '''
    infinitive_list = [0]
    for i in infinitive_list:
        print(i)
        infinitive_list.append(i)


def infinitive_loop_use_for2():
    '''
    vòng lặp vô hạn với for, sau in không phải list, tuple, set hay dict
    '''
    def call_again():
        return 1
    # iter() nhận 1 hàm gọi lại và 1 giá trị dừng, hàm chỉ dừng khi callable = sentinel
    for i in iter(call_again, 0):
        print('infinitive loop')
