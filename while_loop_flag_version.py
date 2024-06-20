def get_starting_number():
    while True:
        num = input("How many bottles of beer on the wall? ")
        if num.isdigit() and int(num) >= 1:
            return int(num)
        else:
            print("Please enter a number 1 or greater.")

def sing(num_bottles):
    flag = True
    while flag:
        if num_bottles == 1:
            print(f"{num_bottles} bottle of beer on the wall, {num_bottles} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            flag = False
        else:
            print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
            print(f"Take one down, pass it around, {num_bottles-1} {'bottle' if num_bottles-1 == 1 else 'bottles'} of beer on the wall.")
            num_bottles -= 1

if __name__ == "__main__":
    num_bottles = get_starting_number()
    sing(num_bottles)