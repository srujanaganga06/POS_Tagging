def load_data(filename):
    sentences = []
    with open(filename, 'r') as f:
        for line in f:
            pairs = []
            words = line.strip().split()
            for w in words:
                word, tag = w.rsplit('/', 1)
                pairs.append((word.lower(), tag))
            sentences.append(pairs)
    return sentences
