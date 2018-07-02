# min heap
#
class Heap:
  def __init__(self):
    self.heap = []
    self.size = 0

  def add(self, val):
    self.heap.append(val)
    self.size += 1
    self.heapify_up()

  def peek(self):
    if self.size > 0:
      return self.heap[0]
    else:
      return False

  def poll(self):
    if self.size > 0:
      current_min = self.heap[0]
      self.heap[0] = self.heap.pop()
      self.size -= 1
      self.heapify_down()
      return current_min
    else:
      return False


  def swap(self, index1, index2):
    self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

  def heapify_down(self):
    current_index  = 0
    while self.has_left_child(current_index):
      small_child_index = self.left_child_index(current_index)
      if (self.has_right_child(current_index) and self.left_child(current_index) > self.right_child(current_index) ):
        small_child_index = self.right_child_index(current_index)
      if self.heap[small_child_index] < self.heap[current_index]:
        self.swap(small_child_index, current_index)
        current_index = small_child_index
      else:
        break

  def heapify_up(self):
    current_index = self.size - 1
    while self.has_parent(current_index):
      if self.parent(current_index) > self.heap[current_index]:
        self.swap(current_index, self.parent_index(current_index))
      else:
        break
      current_index = self.parent_index(current_index)

  def left_child_index(self, index):
    return index * 2 + 1

  def right_child_index(self, index):
    return index * 2 + 2

  def parent_index(self, index):
    return (index - 1) / 2


  def has_left_child(self, index):
    return self.left_child_index(index) < self.size

  def has_right_child(self, index):
    return self.right_child_index(index) < self.size

  def has_parent(self, index):
    return self.parent_index(index) >= 0


  def left_child(self, index):
    return self.heap[self.left_child_index(index)]

  def right_child(self, index):
    return self.heap[self.right_child_index(index)]

  def parent(self, index):
    return self.heap[self.parent_index(index)]



# a = Heap()


# print a.heap
# a.add(3)
# print a.heap
# a.add(1)
# print a.heap
# a.add(6)
# print a.heap
# a.add(5)
# print a.heap
# a.add(2)
# print a.heap
# a.add(4)
# print a.heap

# print a.peek()
# print a.heap

# print a.poll()
# print a.heap

# print a.poll()
# print a.heap

# print a.poll()
# print a.heap

# print a.poll()
# print a.heap

# print a.peek()
# print a.heap



