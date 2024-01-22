# Algorithms are two types

# 1) Comparison based Algorithms
#     bubble sort, insertion sort, selection sort, merge sort, quick sort
# 2) Non-comparison based Algorithms
#     radix sort, bucket sort

# Features of sorting Algorithms

# 1) In place:
#     In place algorith does not need any extra memory like temporary variables or arrays
# 2) Recursive:
#     Some sorting algorithms are implemented in a Recursive manner(the divide and conquer ones especially)
#     Ex: merge sort and quick sort
# 3) Stable:
#     stable sorting algorithms maintian the relative order of records with equal values

#         For ex:
#             Given list  =>  4, 12(first), 12(second), -3
#             If answer =>    -3, 4, 12(first), 12(second) => It is called as Stable
#             If answer =>    -3, 4, 12(second), 12(first) => It is not stable

#     Merge sort  => Stable
#     Quicksort   => Unstable
# 4) Internal and External sort
#     In Internal sort all the records are in RAM or main memory where as in External sort some records are on disk.


# ** Adaptive algorithms
#     =>  An aadaptive algorithms is an algorithm that changes its  behavior based on information available at runtime
#     =>  It takes advantage of existing order in its input.
#     => It benefits from local orders 
#             => Sometimes an unsorted array contains sequences that are sorted by default
#     => Most of the times we just have to modify existing sorting algorithms in order to end up with an adaptive one.
#     => Comparison based algorithms have optimal O(N logN) running time complexity
#     => Adaptive sort takes advantage of the existing order of the input to try to achieve better times:
#             maybe O(N) could be reached.
#     =>  Ex: Shell sort is an adaptive algorithm so performs better if the input is partially sorted.
#             Heapsort, merge sort: not adaptive algorithms, do not take advantage of presorted sequences.
