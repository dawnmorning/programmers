def solution(players, callings):
    # for call in callings:
    #     idx = players.index(call)
    #     players[idx], players[idx-1] = players[idx-1], players[idx]
    idx = {i : player for i, player in enumerate(players)}
    p = {player : i for i , player in enumerate(players)}
    
    for call in callings:
        cur_idx = p[call]
        pre_cur_idx = cur_idx - 1
        pre_player = idx[pre_cur_idx]
        
        idx[cur_idx] = pre_player
        idx[pre_cur_idx] = call
        
        p[call] = pre_cur_idx
        p[pre_player] = cur_idx
        
    return list(idx.values())