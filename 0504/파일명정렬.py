def solution(files):
    files_leng = len(files)
    answer = [0] * files_leng
    files_list = []
    for inner_file in files:
        file_arr = [0, 0, inner_file]
        file_leng = len(inner_file)
        temp = ''
        for i in range(file_leng):
            if inner_file[i].isdigit():
                file_arr[0] = temp
                break
            else:
                temp += inner_file[i]
          
        temp_digit = ''
        for j in range(i, i + 5):
            if j < file_leng:
                if inner_file[j].isdigit():
                    temp_digit += inner_file[j]
                else:
                    break
        file_arr[1] = int(temp_digit)
        files_list.append(file_arr)
    # print(files_list)
    
    # 여기서부터 람다로 정렬
    files_list.sort(key=lambda x: (x[0].upper(), x[1])) # 이게 아마도 순서대로?
    # 이 코드 한줄에 꽤 많은 개념과 노하우가 들어있어.
    # print(files_list)
    for k in range(files_leng):
        answer[k] = files_list[k][2]
    return answer


solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG'])