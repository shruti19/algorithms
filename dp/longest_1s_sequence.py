'''
Given a binary array, find the index of 0 to be replaced with 1 to get 
maximum length sequence of continuous ones.

Example: 
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
#=> position: 7
[0, 1, 1, 1]
#=> position: 0
'''
def longest_1s_sequence(arr):
	length = len(arr)
	so_far_max_1s = 0
	count_0 = new_start = 0
	current_substituted_index = best_substituted_index = 0
	start_i = end_i = 0

	for i in range(length):
		if arr[i] == 0:
			count_0 += 1
			if count_0 == 2:
				new_start = current_substituted_index + 1
				count_0 -= 1
			current_substituted_index = i

		if so_far_max_1s < (i - new_start + 1):
			so_far_max_1s = i - new_start + 1
			end_i = i
			start_i = new_start
			best_substituted_index = current_substituted_index 

	print "substituted index: %s (%s)" % (best_substituted_index,\
		arr[start_i:end_i + 1])
	print "max 1's sequence length: %s\n" % (so_far_max_1s)
