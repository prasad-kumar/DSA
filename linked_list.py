# Linkedlist in Python


class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linkedlist is Empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr  = itr.next
        return count

    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr =self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            node = self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_values(self,data):
        self.head = None
        for data in data:
            self.insert_at_end(data)


    




if __name__ == "__main__":
    ll = Linkedlist()
    ll.insert_at_begining(3)
    ll.insert_at_begining(2)
    ll.insert_at_begining(1)
    ll.insert_at_end(5)
    ll.insert_at_end(6)
    ll.insert_at(3,4)
    ll.remove_at(5)
    #ll.insert_values(['Prasad', 'Maruthi', 'Sai Tharun'])
    ll.print()