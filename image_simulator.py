import numpy as np
import random
import string

# while True:
#     print("\n🖼️ Welcome to HARRYIMAGE Simulator 🖼️")

#     rows = int(input("Enter number of rows (e.g. 5): "))
#     cols = int(input("Enter number of columns (e.g. 5): "))

#     # Create a random 2D array (values 0–255 to simulate pixel brightness)
#     image = np.random.randint(0, 256, (rows, cols))
#     print("\nOriginal Image Matrix (0 = dark, 255 = bright):")
#     print(image)


# Create a 5x5 grid of random uppercase letters
rows, cols = 5, 5
letters = np.random.choice(list(string.ascii_uppercase), size=(rows, cols))

print("🔠 Your Word Matrix:")
print(letters)
