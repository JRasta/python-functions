def min_max(nums):
    min_max_list = [min(nums), max(nums)]
    print(min_max_list)


min_max([14, 35, 6, 1, 34, 54])  # [1, 54]
min_max([1.346, 1.6532, 1.8734, 1.8723])  # [1.346, 1.8734]
min_max([0.432, 0.874, 0.523, 0.984, 0.327, 0.2345])  # [0.2345, 0.984])
min_max([13, 72, 98, 43, 24, 65, 31])  # [13, 98]
min_max([-54, -23, -54, -21])  # [-54, -21]
min_max([-0.473, -0.6834, -0.1287, 0.5632])  # [-0.6834, 0.5632]
min_max([0, 0, 0, 0])  # [0, 0]
