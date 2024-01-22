# Hybrid Algorithms:
#     It combines more Algorithms to solve a given problem.
#     It choses one algorithm depending on the data or switching  between them over the course of the algorithm.
#     This is generally done to combine desired features of each, so that the overall algorithem is better than the individual components
#     IMPORTANT:
#         Hybrid algorithm does not refer to simply combining multiple Algorithms to solve a different problem but only to combining
#         algorithms to solve a different problem but only to combining algorithms that solve the saame problem
#         but differ in other characteristics such as performance.
#         The technique can be used when sorting.
        
#         Heapsort:  it has an advantage of a guaranteed running time O(N logN)
#         Quicksort: Optimal implementations are outperform both mergesort and heapsort.
#                    BUT quicksort can have quadratic running time when we keep choosing bad pivots.
#                    Solution: Let's combine two algorithms.

        
#         => Introsort:
#                         Also knows as introspective sort.
#                         It is a hybrid sorting algorithm that provides both fast avarage performance and optimal worst-case performance.
#                         It begins with quicksort and switches to heapsort when quicksort becomes too slow.
#                         INTROSORT = QUICKSORT + HEAPSORT
        
#         => Timsort:
#                         Insertion sort: very efficient on small data (5 - 10 elements)
#                         Mergesort / quicksort: asymptotically optimal on large datasets, but the overhead becomes significant if applying them to small datasets.
#                         Solution:   Let's combine the two algorithms.
#                         Highly optimized hybrid algorithm: timsort.
#                             TIMSORT = INSERTION SORT + MERGESORT
#                         It is a stable sorting algorithm however not in-pace because merge sort requires extra space.
#                         It was implemented in the Python programming language.
#                         Best case O(N)
#                         Worst canse O(N logN)
#                         Worst case space O(N)

                
