from heapq import heappop, heappush, heappushpop



class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        else:
            heappush(self.max_heap, -heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else (self.min_heap[0] - self.max_heap[0]) / 2



# class MedianFinder:

#     def __init__(self):
#         self.max_heap = []
#         self.min_heap = []
#         self.mid = 0
#         self.is_odd = True

#     def addNum(self, num: int) -> None:
#         if num > self.mid:
#             heappush(self.min_heap, num)
#             if self.is_odd:
#                 self.mid = heappop(self.min_heap)
#                 self.is_odd = False
#             else:
#                 heappush(self.max_heap, -self.mid)
#                 self.mid = (self.min_heap[0] - self.max_heap[0]) / 2
#                 self.is_odd = True
#         else: 
#             heappush(self.max_heap, -num)
#             if self.is_odd:
#                 self.mid = -heappop(self.max_heap)
#                 self.is_odd = False
#             else:
#                 heappush(self.min_heap, self.mid)
#                 self.mid = (self.min_heap[0] - self.max_heap[0]) / 2
#                 self.is_odd = True
            

#     def findMedian(self) -> float:
#         return self.mid


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

obj = MedianFinder()
for i in [2, 1, 4, 3, 6, 5, 7]:
    obj.addNum(i)
    print(obj.findMedian())