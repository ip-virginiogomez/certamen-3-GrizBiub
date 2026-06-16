km1 = int(input("Ingresa 5 velocidades en km/h : "))
km2 = int(input("Ingesa 4 velocidades en km/h : "))
km3 = int(input("Ingresa 3 velocidades en km/h : "))
km4 = int(input("Ingresa 2 velocidades en km/h : "))
km5 = int(input("Ingresa 1 velocidades en km/h : "))
limite = 120
minimo = 20

if km1 or km2 or km3 or km4 or km5 >= limite:
    print("Peligro")
elif km1 or km2 or km3 or km4 or km5 <= minimo:
    print("Peligro")


