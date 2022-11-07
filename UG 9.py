class Node:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority # 1 (tertinggi), 2, 3, 4, ...

class PriorityQueueSortedList:
    def __init__(self):
        self._data = []
        self._size = 0

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def __len__(self):
        return self._size

    #mengambil data prioritas tinggi
    def peek(self):
        print("Data Priotitas tertinggi: ", self._data[0])
        
    
    # #menambah data
    def add(self, data, priority):
        if len (self._data):
            x = 0
            while self._data[x][1]< priority:
                x +=1
            self._data.insert(x,(data,priority))
        else:
            self._data.append((data,priority))


    #mengupdate data dengan prioritas yang diberikan
    def update(self,prioBaru,dataBaru):
        x = 0
        self._data[x]=(prioBaru,dataBaru)

    # #menghapus data dengan prioritas tertinggi 1x
    def remove(self):
        del(self._data[0])
    
    def removeWithPrio(self,prio):
        x = 0
        del(self._data[x])
        
    #menampikan isi
    def printIsiQueue(self):
        print("Isi Semua Queue: ",end="")
        if self.is_empty() == True:
            print('Priority Queue is empty')
        else:
            bantu = self._data
        while bantu != None:
            print('(', bantu._data, ',', bantu._priority, ')', end=' ')
            bantu = bantu._next
    print()



sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()