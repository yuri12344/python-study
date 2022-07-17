import random

def main() -> None:
    test_list = [120, 68, -20, 0, 5, 67, 14, 99]

    # built in imutable sort  
    sorted_list = sorted(test_list)
    print("Original list: ", test_list) 
    print("Sorted list: ", sorted_list)

    # built in mutable sort
    test_list.sort()
    print("Original list: ", test_list) 

    # other example of mutable vs imutable operation
    cards = ["2", "3", "A", "B", "5", "6", "8", "Q", "L", "K", "I", "N", "M", ]
    shuffled_cards = random.sample(cards, key=len(cards)) # Cards mutable or imutable
    print("Shuffled cards: ", shuffled_cards)
    print("Original cards: ", cards)

    random.shuffle(cards) # Shuffle the cards, needs to be imutable
    print("Cards shuffled inplace: ", cards)

if __name__ == "__main__":
    main()