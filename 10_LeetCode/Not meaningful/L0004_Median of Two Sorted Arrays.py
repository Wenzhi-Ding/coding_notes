def findMedianSortedArrays_fast_short(nums1, nums2):
    merged = sorted(nums1 + nums2)
    size = len(merged)
    odd = size % 2
    half = size // 2
    return merged[half] if odd else (merged[half] + merged[half-1]) / 2

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    total_length = len(nums1) + len(nums2)
    ind_1 = 0
    ind_2 = 0

    for _ in range((total_length - 1) // 2 + 1):
        if ind_1 >= len(nums1):
            median_pre = nums2[ind_2]
            ind_2 += 1
        elif ind_2 >= len(nums2):
            median_pre = nums1[ind_1]
            ind_1 += 1
        else:
            if nums1[ind_1] < nums2[ind_2]:
                median_pre = nums1[ind_1]
                ind_1 += 1
            else:
                median_pre = nums2[ind_2]
                ind_2 += 1
            
    if total_length % 2 == 0:
        if ind_1 >= len(nums1):
            median_post = nums2[ind_2]
        elif ind_2 >= len(nums2):
            median_post = nums1[ind_1]
        else:
            if nums1[ind_1] < nums2[ind_2]:
                median_post = nums1[ind_1]
            else:
                median_post = nums2[ind_2]
        return (median_pre + median_post) / 2
    else:
        return median_pre

def findMedianSortedArrays_2(nums1, nums2):
    '''
    这个用了全局变量，虽然代码看上去干净了，但是变慢了，而且还是尽量避免使用全局变量吧
    '''
    total_length = len(nums1) + len(nums2)
    global ind_1
    ind_1 = 0
    global ind_2
    ind_2 = 0

    def move_index():
        global ind_1, ind_2
        if ind_1 >= len(nums1):
            tmp_out = nums2[ind_2]
            ind_2 += 1
        elif ind_2 >= len(nums2):
            tmp_out = nums1[ind_1]
            ind_1 += 1
        else:
            if nums1[ind_1] < nums2[ind_2]:
                tmp_out = nums1[ind_1]
                ind_1 += 1
            else:
                tmp_out = nums2[ind_2]
                ind_2 += 1
        return tmp_out
    
    for _ in range((total_length - 1) // 2):
        move_index()
    
    if total_length % 2 == 0:
        return (move_index() + move_index()) / 2
    else:
        return move_index()


## Test Unit
args_lst = [([1, 3], [2]),
            ([1, 2], [3, 4]),
            ([], [1, 2]),
            ([], [1]),
            ([1], [2, 3, 4])
            ]
for arg in args_lst:
    print(findMedianSortedArrays(arg[0], arg[1]))