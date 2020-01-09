def check_overlap(point1, point2):
    '''
    Input: tuple1, tuple2
    '''
    if max(point1) > min(point2):
        return "Overlap"
    else:
        return "Not Overlap"

'''
Example:
check_overlap((1,5), (2,6))

Return:
Overlap
'''

