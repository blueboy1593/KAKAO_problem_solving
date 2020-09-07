def solution(numbers, hand):
    answer = ''
    left_finger = (3, 0)
    right_finger = (3, 2)
    numbers_pos = { 0: (3,1), 1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8:(2,1), 9:(2,2)}
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            left_finger = numbers_pos[number]
            answer += 'L'
        elif number == 3 or number == 6 or number == 9:
            right_finger = numbers_pos[number]
            answer += 'R'
        else:
            number_pos = numbers_pos[number]
            left_dis = abs(number_pos[0] - left_finger[0]) + abs(number_pos[1] - left_finger[1])
            right_dis = abs(number_pos[0] - right_finger[0]) + abs(number_pos[1] - right_finger[1])
            if hand == 'left':
                if right_dis < left_dis:
                    answer += 'R'
                    right_finger = number_pos
                else:
                    answer += 'L'
                    left_finger = number_pos
            elif hand == 'right':
                if left_dis < right_dis:
                    answer += 'L'
                    left_finger = number_pos
                else:
                    answer += 'R'
                    right_finger = number_pos
    return answer