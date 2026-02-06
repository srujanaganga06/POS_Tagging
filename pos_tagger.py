import pickle

def load_model():
    with open("hmm_model.pkl", "rb") as f:
        return pickle.load(f)

def tag_sentence(sentence):
    model = load_model()
    words = sentence.lower().split()
    tags = model["tags"]

    result = []

    for word in words:
        best_tag = None
        best_prob = 0

        for tag in tags:
            emission_prob = model["emission"].get(tag, {}).get(word, 0.0001)
            if emission_prob > best_prob:
                best_prob = emission_prob
                best_tag = tag

        result.append((word, best_tag))

    return result
