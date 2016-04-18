def turns(list_of_players):
    """
    Returns list of players sorted by roll dice result
    """
    turns_list = []
    for each in list_of_players:
        turns_list.append(list((sum(roll_dice()), each)))
    turns_list.sort(reverse=True)
    while True:
        repet_index = set()
        for i in range(len(list_of_players)-1):
            if turns_list[i][0] == turns_list[i+1][0]:
                repet_index.add(i)
                repet_index.add(i+1)
        if len(repet_index) == 0:
            break
        else:
            for i in repet_index:
                turns_list[i][0] = sum(roll_dice())
            turns_list.sort(reverse = True)
    turns = [x[1] for x in turns_list]
    return turns
