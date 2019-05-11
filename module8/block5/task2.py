class DummyStorage:
      def __init__(self, default=0):
          self.storage = {}
          self.default = default
      
      def save(self, key, value):
          self.storage[key] = value
      
      def load(self, key):
          if key in self.storage:
              return self.storage[key], True
          else:
              self.storage[key] = self.default
              return self.storage[key], False

obj1=DummyStorage()

obj1.storage = {"d1" : 1111}
print(obj1.load("d1"))
obj1.save("d2",2222)
print(obj1.load("d2"))
print(obj1.load("d1"))

print(obj1.load("d3"))