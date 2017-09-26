'''
Queue using a Python list


What is a queue?

A lost of items waiting to be processed. Items are processed by a
method caleed FiFO (first in, first out). The first item in is the
first item out.)

Objective
Imprement a queue using a Python list.

Must create a clsss called ListQueue.

The ListQueue class will contain the folling methods:
- enqueue - this will insert an item to the beginnng of the list.
- dequeue = this will remove the last itme in the list and return the last item.
- get_size - this will retun the sie of the list.

Extra Challenge

If you want to add a challenge consider how you would handle a queue of a
fixed size. For example, say you only can have 10 items in your queue but
the enqueue method is called. How would you handle that?

'''


class ListQueue:
    def __init__(self):
        self.contents = []

    def __repr__(self):
        return "{}".format(self.contents)

    def enqueue(self, item_to_insert):
        if len(self.contents) <= 10:
            self.contents.insert(0, item_to_insert)
        else:
            print("The list has reached its maximum content of 10 items.")
            print("Item not added.")
        return self.contents

    def dequeue(self):
        return self.contents.pop()

    def get_size(self):
        return len(self.contents)


ultimatelist = ListQueue()
print("List called `ultimatelist` created.")
print("Contents of `ultimatelist`: {}".format(ultimatelist))

print("Add 'alona' to list:")
ultimatelist.enqueue('alona')
print(ultimatelist)

print("Add 'liz' to list:")
ultimatelist.enqueue('liz')
print(ultimatelist)

print("Add 'mario' to list:")
ultimatelist.enqueue('mario')
print(ultimatelist)

print("dequeue last item in the list:")
print(ultimatelist.dequeue())
# print(ultimatelist)

print("The size of the list is {}.".format(ultimatelist.get_size()))


# repeat = True
# while repeat:
#     item_to_insert = input("What do you want to add to the list? ")
#     ultimatelist.enqueue(item_to_insert)
#     print("`ultimatelist`: {}".format(ultimatelist))
#     response = input("Do you want to add another?(y/n) ")
#     if response == 'n':
#         repeat = False


