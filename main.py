def len_file(file1, file2, file3):
    with open(file1, encoding='utf8') as f:
        list1 = f.readlines()
    with open(file2, encoding='utf8') as f:
        list2 = f.readlines()
    with open(file3, encoding='utf8') as f:
        list3 = f.readlines()
    file_list = [list1, list2, list3]
    dict_file = {file1:list1, file2:list2, file3:list3}
    file_list.sort()
    file_list.reverse()
    with open('4.txt', 'a', encoding='utf8') as f:
        num =0
        for list in file_list:
            len_file = str(len(file_list[num]))
            num += 1
            if dict_file[file1] == list:
                f.write(f' \n {file1} \n')
            elif dict_file[file2] == list:
                f.write(f' \n {file2} \n')
            else: f.write(f' \n {file3} \n')
            # f.write('\n')
            f.write(f' {len_file} \n')
            for write in list:
                f.write(f' {write} ')

len_file('1.txt', '2.txt', '3.txt')
