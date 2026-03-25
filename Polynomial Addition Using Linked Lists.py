class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    # Insert term into polynomial
    def insert(self, coeff, power):
        new_node = Node(coeff, power)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Display polynomial
    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.coeff}x^{temp.power}", end="")
            temp = temp.next
            if temp:
                print(" + ", end="")
        print()


def add_polynomials(p1, p2):
    result = Polynomial()

    t1 = p1.head
    t2 = p2.head

    while t1 and t2:

        if t1.power == t2.power:
            result.insert(t1.coeff + t2.coeff, t1.power)
            t1 = t1.next
            t2 = t2.next

        elif t1.power > t2.power:
            result.insert(t1.coeff, t1.power)
            t1 = t1.next

        else:
            result.insert(t2.coeff, t2.power)
            t2 = t2.next

    # Remaining terms
    while t1:
        result.insert(t1.coeff, t1.power)
        t1 = t1.next

    while t2:
        result.insert(t2.coeff, t2.power)
        t2 = t2.next

    return result


# -------- MAIN PROGRAM --------

poly1 = Polynomial()
poly2 = Polynomial()

# Input for Polynomial 1
n1 = int(input("Enter number of terms in Polynomial 1: "))

for i in range(n1):
    coeff = int(input("Enter coefficient: "))
    power = int(input("Enter power: "))
    poly1.insert(coeff, power)

# Input for Polynomial 2
n2 = int(input("\nEnter number of terms in Polynomial 2: "))

for i in range(n2):
    coeff = int(input("Enter coefficient: "))
    power = int(input("Enter power: "))
    poly2.insert(coeff, power)

print("\nPolynomial 1:")
poly1.display()

print("Polynomial 2:")
poly2.display()

result = add_polynomials(poly1, poly2)

print("Result Polynomial after Addition:")
result.display()
