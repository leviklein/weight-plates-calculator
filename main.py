import argparse
from collections import OrderedDict, defaultdict
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def main():
    parser = argparse.ArgumentParser(description='Computes all combinations of weights given a set of plates')
    parser.add_argument('plates', metavar='N', type=float, nargs='+',
                        help='weight of plate')

    args = parser.parse_args()
    plates = sorted(args.plates, reverse=True)
    print(f"Plates provided: {plates}")
    weights = defaultdict(list)

    for it in set(powerset(plates)):
        weight = sum(it)
        if weight == 0:
            continue
        weights[weight].append(it)

    sorted_dict = OrderedDict(sorted(weights.items(), key=lambda t: t[0]))
    print(f"\nAll possible weights")
    for item, v in sorted_dict.items():
        print(f"{item:5.4}: {v[0]}")
        for i in range(len(v)-1):
            print(f"       {v[i+1]}")


if __name__ == '__main__':
    main()
