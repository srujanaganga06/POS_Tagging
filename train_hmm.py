from collections import defaultdict
from preprocess import load_data
from utils import normalize
import pickle

def train_hmm(train_file):
    sentences = load_data(train_file)

    transition = defaultdict(lambda: defaultdict(int))
    emission = defaultdict(lambda: defaultdict(int))
    tag_count = defaultdict(int)
    start_prob = defaultdict(int)

    for sent in sentences:
        prev_tag = "<START>"
        start_prob[sent[0][1]] += 1

        for word, tag in sent:
            tag_count[tag] += 1
            emission[tag][word] += 1
            transition[prev_tag][tag] += 1
            prev_tag = tag

    transition_prob = {}
    for prev in transition:
        transition_prob[prev] = normalize(dict(transition[prev]))

    emission_prob = {}
    for tag in emission:
        emission_prob[tag] = normalize(dict(emission[tag]))

    start_prob = normalize(dict(start_prob))

    model = {
        "transition": transition_prob,
        "emission": emission_prob,
        "start": start_prob,
        "tags": list(tag_count.keys())
    }

    with open("hmm_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model trained successfully!")

if __name__ == "__main__":
    train_hmm("training_data.txt")
