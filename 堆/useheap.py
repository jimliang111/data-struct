"""
letcode 347 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
"""

import heapq


def topKFrequent(nums, k):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1

    min_heap = []

    for item in d.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (item[1], item[0]))
        elif min_heap[0][0] < item[1]:
            heapq.heapreplace(min_heap, (item[1], item[0]))

    return [num for _, num in min_heap]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))

    nums = [-1, 1, 4, -4, 3, 5, 4, -2, 3, -1]
    k = 3
    print(topKFrequent(nums, k))
