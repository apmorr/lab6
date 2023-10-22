class OrderedList:
    def __init__(self, items=None):
        """creates an ordered list"""
        self._L = sorted(list(items)) if items is not None else list()
            
    def add(self, item):
        """adds item to list"""
        self._L.append(item)
        self._L.sort()

    def remove(self, item):
        """removes the first occurrence of item"""
        if not item in self: raise RuntimeError(f"{item} not in OrderedList")

        self._L.remove(item) # O(n) to find, then O(n) to remove

    def __getitem__(self, index):
        """returns the item with index in the list"""
        return self._L[index]

    def __iter__(self):
        """returns an iterator over list that returns the items in sorted order"""
        return iter(self._L)

    def __len__(self):
        """returns length of the ordered list."""
        return len(self._L)

    def __contains__(self, item):
        """returns true if there is an item in the list equal to item"""
        return self._bs(item, 0, len(self)) 
        

    def _contains_list(self, item):
        """returns True if there is an item of the list equal to item."""
        return item in self._L # Works, but slow (O(n))

    def _contains_bs_slow(self, item):
        return self.__contains_bs_slow(self._L[:], item)
    
    def __contains_bs_slow(self, L, item):
        """searches L for item"""
        #item not in list
        if len(L) == 0: return False            

        median = len(L) // 2

        #item is found
        if item == L[median]: return True

        #item is in first half
        elif item < L[median]: return self.__contains_bs_slow(L[:median], item)
        
        #item is in other half
        else: return self.__contains_bs_slow(L[median + 1:], item)



    def _bs(self, item, left = 0, right = None):
        """serches through list for item using 'left' or 'right' instead of slicing"""
        if right is None: right = len(self)
        if right - left == 0: return False
        if right - left == 1: 
            print(self._L[left])
            return self._L[left] == item
        median = (right + left) // 2
        if item < self._L[median]:
            return self._bs(item, left, median)
        else: 
            return self._bs(item, median, right)
