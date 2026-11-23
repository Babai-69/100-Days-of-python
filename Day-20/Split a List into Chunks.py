numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

chunk_size = int(input("Enter chunk size: "))

chunks = []

for i in range(0, len(numbers), chunk_size):
    chunks.append(numbers[i:i + chunk_size])

print("Chunks:", chunks)