class Inventory(object):
    
    def __init__(self, list, slots):
        self.list = list
        self.slots = slots

    def append_item(self, item):
        self.list.append(item)

    def remove_item(self, item):
        self.list.remove(item)


bag = Inventory(["pen", "sandwich", "penny", "bottle"], 10)
bag_new = Inventory([], 10)