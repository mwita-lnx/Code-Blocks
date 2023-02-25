def merge_sorted_lists(list1, list2):

    merged_list = []

    # Loop through the lists until one of them is empty
    while len(list1) > 0 and len(list2) > 0:
        # Compare the first elements of the lists and append the smaller one to the merged list
        if list1[0] < list2[0]:
            merged_list.append(list1[0])
            list1 = list1[1:]
        else:
            merged_list.append(list2[0])
            list2 = list2[1:]

    # Append the remaining elements of the non-empty list to the merged list
    if len(list1) > 0:
        merged_list += list1
    else:
        merged_list += list2

    return merged_list

if __name__ == '__main__':
    lista = [1,2,3,45,]
    listb = [3,34,43,3]
    print(merge_sorted_lists(lista,listb))
