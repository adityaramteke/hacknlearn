# Scalene Triangle: All sides have different lenghts.
# Isosceles Triangle: Two sides have the same lenghts.
# Equilateral triangle: All sides are

a = input("Lenght of side a = ")
b = input("Lenght of side b = ")
c = input("Lenght of side c = ")

if a != b and b != c and c != a:
    print("Triangle is Scalene. ")
elif a == b and b == c:     # elif is like if else
    print("Triangle is Equilateral")
else:
    print("Triangle isIsosceles") 
