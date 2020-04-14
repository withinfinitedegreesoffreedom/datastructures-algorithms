import unittest

class LinkedList:
    def __init__(self, val=None):
        self.head = Node(val)

    def insert(self, val):
        if self.head.value is None:
            self.head = Node(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)

    def peek(self):
        return self.head

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Animal:
    def __init__(self, type):
        self.type = type
        self.order = None

class AnimalShelter:
    def __init__(self):
        self.cats = LinkedList()
        self.dogs = LinkedList()
        self.order = 0

    def enqueue(self, animal):
        if animal.type == "cat":
            self.order += 1
            animal.order = self.order 
            self.cats.insert(animal)
        elif animal.type == "dog":
            self.order += 1
            animal.order = self.order
            self.dogs.insert(animal)
        else:
            raise ValueError("Animal type not accepted")

    def dequeueAny(self):
        peek_cat = self.cats.peek()
        peek_dog = self.dogs.peek()
        if peek_cat.value.order < peek_dog.value.order:
            return self.dequeueCat()
        else:
            return self.dequeueDog()
        
    def dequeueDog(self):
        head_node = self.dogs.head
        next_node = head_node.next
        self.dogs.head = next_node
        return head_node

    def dequeueCat(self):
        head_node = self.cats.head
        next_node = head_node.next
        self.cats.head = next_node
        return head_node

class Test(unittest.TestCase):
    def setUp(self):
        self.animal_shelter = AnimalShelter()
        self.cat1 = Animal("cat")
        self.cat2 = Animal("cat")
        self.dog1 = Animal("dog")
        self.cat3 = Animal("cat")
        self.dog2 = Animal("dog")

        self.animal_shelter.enqueue(self.cat1)
        self.animal_shelter.enqueue(self.cat2)
        self.animal_shelter.enqueue(self.dog1)
        self.animal_shelter.enqueue(self.cat3)
        self.animal_shelter.enqueue(self.dog2)

    def test(self):
        self.assertEqual(self.animal_shelter.dequeueCat().value.type,"cat")
        self.assertEqual(self.animal_shelter.dequeueAny().value.type,"cat")
        self.assertEqual(self.animal_shelter.dequeueDog().value.type, "dog")

if __name__=="__main__":
    unittest.main() 

