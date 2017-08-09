# LintCode
programmed by python

### kthLargestElement
采用快排的思想，不断只对第k大的数所在的部分进行细分排序，最后可得到第k大的数在（有序）数组中的正确位置。

### lengthOfLongestSubstring
才用hash的思想，存储一个字母上一次出现的位置，若出现重复，则更新当前字符串的开始位置为这个字母上次出现的位置加1。

### mergeSortedArray
简单另开了一个数组进行存储新的有序数组。

### trailingZeros
res = (n/5^1)+(n/5^2)+(n/5^3)+....
