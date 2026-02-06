from collections import defaultdict

def normalize(prob_dict):
    total = sum(prob_dict.values())
    for key in prob_dict:
        prob_dict[key] /= total
    return prob_dict
