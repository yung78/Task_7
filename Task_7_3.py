def sort_text_in_file():
    files_list = ['1.txt', '2.txt', '3.txt']
    text_dict = {}
    for files in files_list:
        count = 0
        text = ''
        with open(files, encoding="utf-8") as file:
            for line in file:
                count += 1
                text += line
        text_dict[files] = [count, text]
    str_count = []
    for key in text_dict:
        str_count.append(text_dict.get(key)[0])
    str_count.sort()
    for num_str in str_count:
        for key in text_dict:
            if num_str == text_dict.get(key)[0]:
                with open('result.txt', 'a', encoding="utf-8") as file:
                    file.write(f'{key} \n')
                    file.write(f'{text_dict.get(key)[0]} \n')
                    file.write(f'{text_dict.get(key)[1]} \n')


sort_text_in_file()
