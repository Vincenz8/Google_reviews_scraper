# standard libraries
import pickle


def load_reviews(file: str):
    with open(file, "rb") as f:
        return pickle.load(f)


if __name__ == "__main__":
    reviews = load_reviews("data/raw_reviews/opel_raw_rev.pickle")

    for rev in reviews:
        print(rev if rev != "" else "vuota")
        print("--------------")

    print(len(reviews))
    print("finished")
