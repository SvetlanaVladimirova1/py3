a = int(input("Введите сторону треугольника a"))
b = int(input("Введите сторону треугольника b"))
c = int(input("Введите сторону треугольника c"))
if  a > b+c or b > a+c or c > a+b:
    print("Треугольника с такими сторонами не существует")
elif a < b+c and b < a+c and  c < b+a and a == b == c:
    print("Треугольник является равносторонним")
elif a < b+c and b < a+c and  c < b+a and a == b or a == c or b == c:
    print("Треугольник является равнобедренным")
elif a < b+c and b < a+c and  c < b+a and a != b and a != c and b != c:
    print("Треугольник является разносторонним")
