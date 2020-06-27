"""
letcode 350
给定两个数组，编写一个函数来计算它们的交集。
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
"""


def intersect(nums1, nums2):
    d1 = {}
    for num in nums1:
        d1[num] = d1.setdefault(num, 0) + 1

    print(d1)

    res = []

    for num in nums2:
        if num in d1:
            res.append(num)
            d1[num] -= 1
            if d1[num] == 0:
                del d1[num]

    return res


if __name__ == '__main__':
    l1 = [4, 9, 5]
    l2 = [9, 4, 9, 8, 4]

    print(intersect(l1, l2))
