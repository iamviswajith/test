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

phys_dict = {}
math_dict = {}
chem_dict = {}


def insert_smallest_list( subject_list, name, score ):
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

        if subject_list[1][1] == score:
            if subject_list[1][0] > name:
                subject_list[1] = [name,score]
        if subject_list[0][1] == score:
            if subject_list[0][0] > name:
                subject_list[0], subject_list[1] = [name,score], subject_list[0]

def insert_smallest(score_dict, name , score):
    if len(score_dict) < 2:
        if score not in score_dict:
            score_dict[score] = [name]
        else:
            score_dict[score].append(name)
    else:
        scores = sorted(score_dict.keys())
        if score in score_dict:
            score_dict[score].append(name)
        elif score < scores[1]:
            del score_dict[scores[1]]
            score_dict[score] = [name]

for i, row in enumerate(input_list):
    insert_smallest(phys_dict, row[0], row[1])
    insert_smallest(math_dict, row[0], row[2])
    insert_smallest(chem_dict, row[0], row[3])

print("\nphysics lowest: \n\t")
for key in sorted(phys_dict.keys(), reverse=True):
    for name in sorted(phys_dict[key]):
        print(name, end=", ")
    print("\n")

print("\nmaths lowest: \n\t")
for key in sorted(math_dict.keys(), reverse=True):
    for name in sorted(math_dict[key]):
        print (name,end=", ")
    print("\n")
print("\nchemistry lowest: \n\t")
for key in sorted(chem_dict.keys(), reverse=True):
    for name in  sorted(chem_dict[key]):
        print(name, end=", ")
    print("\n")



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