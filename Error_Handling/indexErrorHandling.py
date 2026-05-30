fruits = ["Apple", "Pear", "Orange"]

# This will cause an IndexError because there is no item at index 4
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
make_pie(4)
