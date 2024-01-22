# https://www.youtube.com/watch?v=Yg5a2FxU4Fo&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=12
# https://practice.geeksforgeeks.org/problems/power-set-using-recursion/1/?track=sp-recursion&batchId=105
# https://leetcode.com/problems/subsets/

# https://www.interviewbit.com/problems/subset/

# This type of problems can be easily solved using recursion tree
# Let's take example of input string ab
# initially we have input = "ab" and output = ""
# On each level of tree we either consider first value of input to output or not consider it
# and on each level we remove first value from input
    #                                             input = "ab", output = ""
    #                     /                                                               \
    #                    /                                                                 \
    #             not considering "a" in output                                               considering a in output
    #             input = "b", output = ""                                                    input = "b", output = "a"
    #         /                               \                                            /                              \
    #        /                                 \                                          /                                \
    # not considering "b" in output           considering "b" in output         not considering "b" in output         considering "b" in output
    #     input = "", output = ""             input = "", output = "b"            input = "", output = "a"            input = "", output = "ab"


# so our final answer would be all the outputs of leaf node


def solve(input, output, final_answer):
    # current output
    if len(input) == 0:
        final_answer.append(output)
        return
    
    # Considering first value of input in output
    solve(input[1::], output+input[0], final_answer)
    
    # Not considering first value of input in output
    solve(input[1::], output, final_answer)
    
    
    
    
def powerSet(s):
    #code here
    input = s
    output = ""
    final_answer  = []
    solve(input, output, final_answer)
    return final_answer

print(powerSet("abc"))