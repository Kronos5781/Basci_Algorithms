import numpy as np
#Recursive Finder Class
class RecursiveFinder:

    def find(self, arr, key, low, high):
        if low > high:
            return False
        else:
            mid = (low + high) // 2
            if  key == arr[mid]:
                return True
            elif key < arr[mid]:
                return RecursiveFinder.find(self, arr, key, low, mid - 1)
            else:
                return RecursiveFinder.find(self, arr, key, mid + 1, high)

