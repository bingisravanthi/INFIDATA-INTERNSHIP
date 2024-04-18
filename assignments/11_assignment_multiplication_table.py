def generate_multiplication_table(n):
    if n<1 or n>10:
        print("multiplication_table for", n,":")
    for i in range(1,11):
        result=n*i
        print(f"{n}x{i}={result}")
table=int(input("enter a number(1 to 10)for the multiplication table:"))
generate_multiplication_table(table)