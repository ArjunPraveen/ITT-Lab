n = int(input("Enter number of elements: "))
a = list(map(int,input("\nEnter the elements: ").strip().split()))[:n]

print(a)
if a == a[::-1]:
    print("Its is a Palindrome")
else:
    print("It is not a palindrome") 