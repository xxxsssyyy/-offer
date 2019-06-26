# -*- coding:utf-8 -*-
#这个题很重要，涉及到堆的数据结构
"""
题目描述:
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法
读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""
"""
由于堆是一棵完全二叉树，存在n个元素，那么他的高度为:log2(n+1)，这就说明代码中的for循环会执行
O(log2(n))次。因此插入函数的时间复杂度为：O(log2(n))
"""
class Solution:
    def Insert(self, num):
        #读取数据流
    def GetMedian(self):
        #读取数据中的中位数