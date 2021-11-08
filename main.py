# Лабораторная работа 5
# По двум отсортированным спискам чисел с разными размерами и элементами вернуть медиану объединения этих двух списков
import statistics

def medians(nums1, nums2):
    return statistics.median(nums1+nums2)
    
