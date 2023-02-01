def pick_peaks(arr):
    if len(arr) < 3:
        return {'pos': [], 'peaks': []}
    pos_dict = {}
    candidate_pos, candidate_element = 0, 0
    position = 1
    # last_element = arr[position]
    # current_element = arr[position]
    # next_element = arr[position + 1]
    platoe = False
    while position < len(arr)-1:
        last_element, current_element, next_element = arr[position -
                                                          1], arr[position], arr[position+1]

        if last_element < current_element and current_element > next_element:
            platoe = False
            pos_dict[position] = arr[position]

        elif platoe == True and current_element > next_element:
            platoe = False
            pos_dict[candidate_pos] = candidate_element
            candidate_pos, candidate_element = 0, 0
        elif last_element < current_element and current_element == next_element:
            candidate_pos = position
            candidate_element = arr[position]
            platoe = True
            position += 1
            continue

        position += 1

    # format results
    result_dict = {}
    result_dict['pos'] = list(pos_dict.keys())
    result_dict['peaks'] = list(pos_dict.values())
    return result_dict


print(pick_peaks([7, 0, 6, 6, 8, 17, 11, 14, -3,
      3, 20, 11, -5, 8, 4, -2, 19, 5, 13, -3, 7]))
