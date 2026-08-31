def player(prev_play, opponent_history=[], play_order={}):
    # গ্লিচ ফিক্স: শুরুতে মেমরি ক্লিয়ার করার বদলে 'R' দিয়ে গেম কন্টিনিউ রাখা
    if not prev_play:
        prev_play = "R"
        
    opponent_history.append(prev_play)
    prediction = "P"
    
    n = 5 # গ্লোবাল প্যাটার্ন ম্যাচিংয়ের সুইট-স্পট
    
    if len(opponent_history) >= n:
        last_sequence = "".join(opponent_history[-n:])
        # গ্লোবাল মেমরি ট্র্যাক করা হচ্ছে
        play_order[last_sequence] = play_order.get(last_sequence, 0) + 1
        
        last_n_minus_1 = "".join(opponent_history[-(n-1):])
        
        potential_plays = [
            last_n_minus_1 + "R",
            last_n_minus_1 + "P",
            last_n_minus_1 + "S",
        ]
        
        sub_order = {k: play_order[k] for k in potential_plays if k in play_order}
        
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]
            
    # পারফেক্ট কাউন্টার-অ্যাটাক
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]