# importing all our handy classes
from classes import AppleTree, PearTree, Cider

# create a bunch of trees using a list comprehension
trees = [AppleTree() for x in range (5)]

# telling all the trees to grow fruit
for tree in trees:
    tree.blossom()

# collecting a crop by harvesting each tree in turn
crop = []
for tree in trees:
    crop.extend(tree.harvest())

# making cider from the group
print(Cider(crop))