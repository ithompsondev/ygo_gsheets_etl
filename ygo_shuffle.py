import csv
import sys
import random

command = sys.argv[1]
deck_file = f"{sys.argv[2]}"

def proc_args(cards):
    if command == "--shuffle":
        shuffle_cards(cards)
    elif command == "--sample" and len(sys.argv) == 4:
        run_trials(cards, int(sys.argv[3]))


def run_trials(cards, trials):
    random.shuffle(cards)
    with open(f"samples/{deck_file}_sample.txt".replace(".csv", ""),'w') as sample:
        for n in range(0,trials):
            random.shuffle(cards)
            sample.write(f"Trial {n + 1}\n")
            sample.write("First Hand\n")
            for i in range(1,11):
                if i < 6:
                    sample.write(f'\t{cards[-i]["Card Name"]}\n')
                else:
                    sample.write(f"Turn {i - 4}:\n")
                    sample.write(f'\t{cards[-i]["Card Name"]}\n')
            sample.write("\n")


def shuffle_cards(cards):
    random.shuffle(cards)
    for card in cards:
        print(f"{card['Card Name']}")


def main():
    cards = open(f"decks/{deck_file}", 'r')
    proc_args(list(csv.DictReader(cards)))


if __name__ == "__main__":
    main()
