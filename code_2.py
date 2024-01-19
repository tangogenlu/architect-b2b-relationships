    return data
    main()
def generate_random_data():

    data = [random.randint(1, 100) for _ in range(10)]
def main():


    data = generate_random_data()
    for item in data:
        print(f"Random Number: {item}")
if __name__ == "__main__":

import random