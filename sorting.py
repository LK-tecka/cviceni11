import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def bubble_sort(zoznam_cisel):
    for i in zoznam_cisel:
        for idx in range(len(zoznam_cisel)-1):
            if zoznam_cisel[idx] > zoznam_cisel[idx+1]:
                zoznam_cisel[idx], zoznam_cisel[idx+1] = zoznam_cisel[idx+1], zoznam_cisel[idx]

    return zoznam_cisel

def main():
    zoznam_cisel=random_numbers(20)
    print(zoznam_cisel)
    zoradeny= bubble_sort(zoznam_cisel)
    print(zoradeny)


if __name__ == "__main__":
    main()