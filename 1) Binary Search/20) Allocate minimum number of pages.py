def isPossible(books, number_of_student, maximum_pages_for_each_student):
    # 1) We allocate pages to student if total allocation is less than maximum_pages_for_each_student.
    # 2) if pages_allocated_to_current_student is greater than the maximum_pages_for_each_student,
        # we assign current book to next student and decrease student count.
    # 3) At last we check if student is less than zero that means we require more student to allocate pages.
    # 4) if student is greater than zero that means we have successfully allocated pages to other students and if we can allocate less number of students
        # we can definately allocate more number of students if we have books equal or more than the number of students,
        # that is we have already check in books function using if n < number_of_student:.
    
    pages_allocated_to_current_student = 0
    # For the first book allocation 
    number_of_student -= 1
    for pages in books:
        # If we have pages count greater than the maximum_pages_for_each_student at that time we cannot allocate pages so return False
        if pages > maximum_pages_for_each_student:
            return False

        pages_allocated_to_current_student += pages
        
        if pages_allocated_to_current_student > maximum_pages_for_each_student:
            pages_allocated_to_current_student = pages
            number_of_student -= 1
    # We can also write this False condition in loop to avoid extra loops however for readability we have written here.
    return False if number_of_student < 0 else True
def solve(books, number_of_student):
    # Here we have given that array is not in sorted order and we need to allocate books in contingous order.
    # If you read problem statement you have no clue to use binary search
    # You have to practice this type of question to  get better grasp on it

    # First we check that if number_of_student is greater than the books length then we return -1 as each student should have at least one books
    # The idea is we apply binary search between (minimum pages of given books) and (total sum of given books)
    # for the mid element we check is it possible to allocate books where total pages sum of each student is less than or equal to the mid
    # if it is possible to allocate we decrease mid by end = mid - 1 and apply binary search again.
    # if it is not possible to allocate we increase mid by start = mid + 1 and apply binary search again.
    # at the end we get mid as the minimum of maximum number of pages alloted to a student

    # To find sum of pages of all the books and minimum pages books have (so basically start and end position)
    start = books[0]
    end = 0
    n = 0
    for x in books:
        end += x
        start = min(start, x)
        n += 1
    
    if n < number_of_student:
        return -1

    answer = - 1
    # Now apply binary search between start and end
    while start <= end:
        mid = start + (end-start)//2
        if isPossible(books, number_of_student, mid):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

books = [ 73, 58, 30, 72, 44, 78, 23, 9 ]
number_of_student = 5
print(solve(books, number_of_student))
