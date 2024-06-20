def get_starting_number():
    while True:
        num = input("How many bottles of beer on the wall? ")
        if num.isdigit() and int(num) >= 1:
            return int(num)
        else:
            print("Please enter a number 1 or greater.")

def sing(num_bottles):
    for i in range(num_bottles, 0, -1):
        if i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} {'bottle' if i-1 == 1 else 'bottles'} of beer on the wall.")

if __name__ == "__main__":
    num_bottles = get_starting_number()
    sing(num_bottles)