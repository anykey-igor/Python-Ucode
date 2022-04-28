def bubble_sort(sort_case):
    stop_flag = True
    while stop_flag:
        stop_flag = False
        for i in range(len(sort_case) - 1):
            if sort_case[i] > sort_case[i + 1]:
                sort_case[i], sort_case[i + 1] = sort_case[i + 1], sort_case[i]
                stop_flag = True
    return sort_case
