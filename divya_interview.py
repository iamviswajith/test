"""

1. Given the names of students along with their physics, math and chemistry scores, store them in a nested list and print the names of students who are the bottom two in each subject.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on the same line.

For example,

Input:

John, 100, 80, 70

Alice,  80, 90, 96

Steve, 89, 95, 98

Jane, 80, 88, 98

Harry, 90, 100, 99

Output:

Physics:

  Steve

      Alice, Jane

Math:

  Jane

  John

Chemistry:

  Alice

  John


"""

input_list = [
['John', 100, 80, 70],
['Alice',  80, 90, 96],
['Steve', 89, 95, 98],
['Jane', 80, 88, 98],
['Harry', 90, 100, 99],
['Jake', 80, 88, 96],
]

p_lower = []
m_lower = []
c_lower = []


def insert_smallest( subject_list, name, score ):
    """
    maintains a subject list of lowest two scores
    if equal scores, it prefers to have the name that comes first in lexicographic order
    :param subject_list: [[name, 1],[name, 2]]
    :param name: str
    :param score: int
    :return:
    """
    if len(subject_list) == 1:
        if subject_list[0][1] < score:
            subject_list.append([name, score] )
        elif subject_list[0][1] > score:
            subject_list.insert(0, [name, score])
        else:
            if subject_list[0][0] < name:
                subject_list.append([name, score])
            else:
                subject_list.insert(0, [name, score])
    else:
        if subject_list[1][1] > score:
            subject_list[1] = [name,score]

        if subject_list[0][1] > score:
            subject_list[0], subject_list[1] = [name,score], subject_list[0]

        # if score is equal to the smallest score
        if subject_list[1][1] == score:
            if subject_list[1][0] > name:
                subject_list[1] = [name,score]
        if subject_list[0][1] == score:
            if subject_list[0][0] > name:
                subject_list[0], subject_list[1] = [name,score], subject_list[0]



for i, row in enumerate(input_list):
    if i == 0:
        p_lower.append( [row[0], row[1]] )
        m_lower.append( [row[0], row[2]] )
        c_lower.append( [row[0], row[3]] )
    else:
        insert_smallest(p_lower, row[0], row[1])
        insert_smallest(m_lower, row[0], row[2])
        insert_smallest(c_lower, row[0], row[3])

print("Phys lowest: ", p_lower)
print("Math lowest: ", m_lower)
print("Chem lowest: ", c_lower)




"""
Given 2 lists, get the row wise common items in them.Provide a solution which should scale to very large lists by using
many CPUs

For
example,

list1 = [[1, 3, 5], [5, 6, 7, 8], [10, 11, 12], [20, 21]]

list2 = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]

Output:

[[3, 5], [6], [11, 12], [21]]

"""

# from multiprocessing.pool import Pool






# def compare_elements(p,i):
#     # print(p.target_list)
#     p.target_list[i] = list(set(p.l1[i]) & set(p.l2[i]))
#     # print(l1[i], l2[i])
#     # print("\t", target_list[i])
#     # return target_list
# class common_elements:
#     def __init__(self):
#         self.l1 = [[1, 3, 5], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
#         self.l2 = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
#         self.target_list = [[]] * min(len(self.l1), len(self.l2))
#
#
#     def let_it_be_parallel(self):
#         with Pool(len(self.target_list)) as p:
#             p.map( compare_elements(self), range(len(self.target_list)) )
#
#
# ce = common_elements()
# ce.let_it_be_parallel()
# print(ce.target_list)