class Node(object):
    def __init__(self,val):
        self.data=val
        self.next=None

    def set_data(self,data):
        self.data=data

    def get_data(self):
        return self.data

    def set_next(self,next):
        self.next=next

    def get_next(self):
        return self.next
class LinkedList(object):
    def __init__(self,head=None):
        self.head=head
        self.count=0

    def get_count(self):
        return self.count

    def insert(self,val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
        self.count+=1

    def find(self,val):
        item=self.head
        while (item!=None):
            if item.get_data() == val:
                return item.get_data()
            else:
                item=item.get_next()
        return None

    def deleteAt(self,idx):
        if idx >= self.count:
            return
        elif self.head == None :
            return
        else:
            idxCtr=0
            node=self.head
            while idxCtr < idx-1 :
                node=node.get_next();
                idxCtr+=1
            node.set_next(node.get_next().get_next())
            self.count-=1

    def dump_list(self):
        node=self.head
        while node != None :
            print(node.get_data())
            node=node.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)

itemlist.dump_list()

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13))
print("Finding item: ", itemlist.find(78))

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()
