from pos_tagger import tag_sentence

def run():
    sentence = input("Enter a sentence: ")
    tagged = tag_sentence(sentence)

    print("\nPOS Tagged Output:")
    for word, tag in tagged:
        print(word, "/", tag)

if __name__ == "__main__":
    run()
