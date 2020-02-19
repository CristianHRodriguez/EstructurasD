class Item():
  def __init__(self, obj):
    self.item = obj
    self.nxt = None

class ListDynamic(object):

  def __init__(self):
    self.head = None
    self.size = 0  

  def add_element(self, ele):
    new_item = Item(ele)
    if self.size == 0:
      self.head = new_item
    else:
      elem = self.head
      while(elem.nxt != None):
        elem = elem.nxt
      elem.nxt = new_item
    self.size += 1

    def remove_tail(self):
      if self.head == none:
        print("Sin elementos")
      else:
        ele = self.head
        while(ele.next != none):
          ele = ele.nxt
        del(ele)
    
    def remove_element(self, val):
      if self.head == none:
        print("Sin elementos")
      else:
        ele1 = self.head
        while (ele1.nxt != none):
          if(ele1.v == v):
            del(ele1)
            break
            ele1=ele1.nxt
            if(ele1.v == v):
              del(ele1)
            else:
              print("sin completar")

  def print_list(self):
    item = self.head
    for i in range(self.size):
      print(item.item)
      item =  item.nxt
