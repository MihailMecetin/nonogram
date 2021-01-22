# Printable chars
value_empty = "-"
value_filled = "X"
value_unfilled = "O"

# row vars
row_length_1 = 4

nums_1 = [4]
row_1 = [value_empty] * row_length_1

nums_2 = [3]
row_2 = [value_empty] * row_length_1

# TODO Add a beginning row_length value to both functions. 

def fill_row_single_ranges(row, num, start_i, stop_i):
    # Case when number fits fully in row
    fill_length = stop_i - start_i
    if num == fill_length:
        # nums fit exactly
        ###print("number fits in row exactly")
        ###print("start_i is ", start_i, " stop_i is ", stop_i)
        for i in range(start_i, stop_i):
            row[i] = value_filled
    # case when number fits partially in row
    if num < fill_length:
        ###print("num fits in row not exactly")
        ###print("start_i is ", start_i, " stop_i is ", stop_i)
        buffer = fill_length - num
        for i in range (start_i + buffer, stop_i - buffer):
            row[i] = value_filled
    if num > fill_length:
        print("Error, number bigger that can fit in row")
    return row

def fill_row_multi_ranges(row, nums, start_i, stop_i):
    # If nums is a single number, send to single function
    if len(nums) == 1:
        fill_row_single_ranges(row, nums[0], start_i, stop_i)
        return row
    # else continue
    fill_length = stop_i - start_i
    # If all numbers fit neatly
    if get_min_space(nums) == fill_length:
        # calculate next start index 
        next_start_i = start_i
        for num in nums:
            # Fill from start index to number
            fill_row_single_ranges(row, num, next_start_i, next_start_i + num)
            # Put 'O' after every filled num, except the last one
            if (next_start_i - 1 < fill_length): row[next_start_i - 1] = value_unfilled
            # calculate next start index 
            next_start_i = next_start_i + num + 1
    # If all numbers don't fit neatly, split row with buffers, and deal as single numbers
    if get_min_space(nums) < fill_length:
        buffer = fill_length - get_min_space(nums)
        ###print ("The buffer is ", buffer)
        next_start_i = start_i
        for num in nums:
            fill_row_single_ranges (row, num, next_start_i, next_start_i + num + buffer)
            extend_from_unfilled_single (row, num, next_start_i, next_start_i + num + buffer)
            next_start_i = next_start_i + num + 1

    return row

def fill_row_single(row, nums, row_length):
    # Case when number fits fully in row
    if nums[0] == row_length:
        # nums fit exactly
        row = [value_filled] * row_length

    if nums[0] < row_length:
        print("nums fit in row length")
        # go through one way and back and count from 1 to num 
        # and create a list of indexes where it gone twice.
        # indeces to go through:
        # 0,1,2,3 and 
        # 4,3,2,1
        index_list = [0] * row_length
        print(index_list)

        for i in range(0, nums[0]):
            index_list[i] = index_list[i] + 1
        for i in range(row_length-nums[0], row_length):
            index_list[i] = index_list[i] + 1

        for i in range(0, row_length):
            if index_list[i] == 2: row[i] = value_filled
        print(index_list)
        #print(index_list[0:nums[0]]) # indeces from 0 to number
        #print(index_list[row_lenth-nums[0]:row_lenth]) # indeces from 

    if nums[0] > row_length:
        print("Error, number bigger that can fit in row")

    return row

def fill_row_multi(row, nums, row_length):
    if get_min_space(nums) == row_length:
        # all nums fit completly
        # fill all row with nums here:
        newrow = []
        for num in nums:
            for i in range(num):
                newrow.append(value_filled)
            newrow.append(value_unfilled)
            #print(newrow)
        newrow.pop()
        row = newrow
    if get_min_space(nums) < row_length:
        print("asdasd2")

    return row

def get_min_space(nums):
    return sum(nums) + len(nums) - 1

def extend_from_edges_single(row, num, start_i, stop_i):
    # checks i first or last tile is filled, and fills the rest.
    # maybe not useful
    if (row[start_i] == value_filled): 
        fill_row_single_ranges(row, num, start_i, num)
        if (start_i + num < len(row)): row[start_i + num] = value_unfilled

    if (row[stop_i - 1] == value_filled): 
        fill_row_single_ranges(row, num, stop_i - num, stop_i)
        if (stop_i - num - 1 >= 0 ): row[stop_i - num - 1] = value_unfilled

def extend_from_edges_single2(row, num, start_i, stop_i):
    # only extends one num, fails with extra 'X' in row
    # From starting edge
    filled = False
    for i in range(start_i, start_i + num):
        ###print("range is from ", start_i, " to ", start_i + nums[0])
        # find first filled, and continue it for num length
        if row[i] == value_filled: filled = True
        if (filled): row[i] = value_filled 
    # if filled starts at first value, put 'O' after
    if (row[start_i] == value_filled and stop_i - start_i != num): row[start_i + num] = value_unfilled

    # From ending edge
    filled = False
    for i in range (stop_i - 1, stop_i - num - 1, -1):
        ##print("range is from ", stop_i - 1, " to ", stop_i - nums[-1] - 1)
        if row[i] == value_filled: filled = True
        if (filled):
            ##print ("Putting 'X' at index ", i) 
            row[i] = value_filled 
    if (row[stop_i - 1] == value_filled and stop_i - start_i != num): row[stop_i - num - 1] = value_unfilled
    
    return row


def zero_out(row, start_i, stop_i):
    for i in range(start_i, stop_i): row[i] = value_unfilled

def find_first_value(row, char, start_i, stop_i):
    for i in range(start_i, stop_i):
        if row[i] == char:
            return i
    return -1

def extend_from_edges_multi(row, nums, start_i, stop_i):
    # only extends first and last numbers in nums
    # From starting edge
    filled = False
    for i in range(start_i, start_i + nums[0]):
        ###print("range is from ", start_i, " to ", start_i + nums[0])
        # find first filled, and continue it for num length
        if row[i] == value_filled: filled = True
        if (filled): row[i] = value_filled 
    # if filled starts at first value, put 'O' after
    if (row[start_i] == value_filled and stop_i - start_i != nums[0]): row[start_i + nums[0]] = value_unfilled

    # From ending edge
    filled = False
    for i in range (stop_i - 1, stop_i - nums[-1] - 1, -1):
        ##print("range is from ", stop_i - 1, " to ", stop_i - nums[-1] - 1)
        if row[i] == value_filled: filled = True
        if (filled):
            ##print ("Putting 'X' at index ", i) 
            row[i] = value_filled 
    if (row[stop_i - 1] == value_filled and stop_i - start_i != nums[-1]): row[stop_i - nums[-1] - 1] = value_unfilled
    
    return row

def zero_edges_multi(row, nums, start_i, stop_i):
    # From left edge
    if (row[start_i + nums[0]] == value_filled):
        for i in range(start_i + nums[0], start_i + 2 * nums[0]):
            if (row[i] == value_filled): row[i - nums[0]] = value_unfilled
            else: break
    # From right edge
    if (row[stop_i - nums[-1] - 1] == value_filled):
        print("in loop")
        print("range is ", stop_i - nums[-1] - 1, " to ", stop_i - 2 * nums[-1] - 1)
        for i in range(stop_i - nums[-1] - 1, stop_i - 2 * nums[-1] - 1, -1):
            print("i is ", i)
            if (row[i] == value_filled): row[i + nums[-1]] = value_unfilled
            else: break

def extend_from_unfilled_single(row, num, start_i, stop_i):
    # Split row into segments between 'O' and rerun extend_from_edges_multi
    print("The row is ", row, "and the number is ", num, "start_i is ", start_i, "and stop_i is", stop_i)
    segment_count = 0
    segment_length = 0
    segment_start_i = 0
    segment_stop_i = 0
    in_segment = False
    for i in range(start_i, stop_i):
        print("Current i is ", i)
        #find first non value_unfilled, cound until next value unfilled, if <= than num, add 1 to count_val.
        if (row[i] != value_unfilled and in_segment): 
            # if segment continues
            segment_length += 1
            print("New segment length is ", segment_length)
        if (row[i] == value_unfilled and in_segment):
            # found segment end
            print("Found segment end at ", i, "length was ", segment_length)
            in_segment = False
            #inc segment count and reset length
            if (segment_length >= num): 
                # segment was long enough to fit num
                print("Found segment that is long enough. From ", segment_start_i, " to ", i)
                segment_count += 1
                # document valid segment range
                segment_stop_i = i
            segment_length = 0
        if (row[i] != value_unfilled and not in_segment): 
            # found segment start
            segment_length = 1
            print("Found new segment start at ", i)
            in_segment = True
            # document segment start if it's the first valid one we found
            if (segment_count < 1): 
                segment_start_i = i
                print("New valid segment start is ", i)
        #if count = 1, run extend edges.
    if (in_segment and segment_length >= num): segment_count += 1; segment_stop_i = stop_i
    if (segment_count == 1):
        print("Only one valid segment, running subprogram with ", segment_start_i, " and ", segment_stop_i)
        fill_row_single_ranges(row, num, segment_start_i, segment_stop_i)
    return row

#def find_unreachable_single(row, num, start_i, stop_i):
    


#fill_row_single_ranges(row_1, nums_1[0], 0, row_length_1)
#fill_row_multi_ranges(row_2, nums_2, 0, row_length_1)
#print(row_2)
#row_1[3] = value_filled
#extend_from_edges_multi(row_1, nums_1, 0, row_length_1)
#print(row_1)

#print (find_first_value(row_1, value_unfilled, 0, row_length_1))



# Init empty Board
board = []
for i in range(20):
    board.append(['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'])

nums_hori = [
    [2, 4, 1, 1],
    [3, 3, 2],
    [2, 4, 2],
    [7],
    [1, 2, 3, 5],

    [1, 3, 1, 5],
    [4, 6, 1, 3],
    [4, 4, 1, 2],
    [1, 2, 6, 1],
    [4],

    [2, 3, 2],
    [10, 2],
    [4, 4, 8],
    [2, 1, 8, 4],
    [1, 1, 2, 4, 3],

    [1, 1, 8, 4],
    [3, 4, 1, 2],
    [1, 1, 2, 1, 3],
    [6, 1, 1],
    [5, 3] ]
nums_vert = [
    [3, 2],
    [3, 1, 6],
    [1, 3, 2, 1, 2],
    [1, 5, 8],
    [1, 1, 2],
    [1, 1, 1, 1, 1],
    [2, 1, 1],
    [3, 1, 6],
    [3, 1, 1, 8],
    [2, 4, 3],
    [3, 3, 1],
    [5, 1, 1, 1],
    [1, 1, 11, 1],
    [4, 1, 8, 3],
    [3, 8, 1],
    [10, 1, 1, 1],
    [3, 2, 3],
    [4, 1, 7],
    [7, 6],
    [8, 6] ]

def print_board():
    for i in range(0, 20):
        if (i % 5 == 0): print("_" * 113)
        print ('{0: >2}'.format(i), "|", board[i][0:5], board[i][5:10], board[i][10:15], board[i][15:20])
        #print ('{0: >2}'.format(i), "|", board[i])

for i in range (0, 3):
    # Main Board
    for i in range(0, 20):
        # Fill horizontal rows
        fill_row_multi_ranges(board[i], nums_hori[i], 0, 20)
        ###print ("Board row ", i, " after fill_row is ", board[i])
        ###print ("Sending row id ", id(board[i]) )
        # Fill vertical rows
        column = ([row[i] for row in board])
        fill_row_multi_ranges(column, nums_vert[i], 0, 20)
        #print (column)
        for ii in range(20):
            board[ii][i] = column[ii]

    for i in range(0, 20):
        extend_from_edges_multi(board[i], nums_hori[i], 0, 20)
        zero_edges_multi(board[i], nums_hori[i], 0, 20)
        column = ([row[i] for row in board])
        extend_from_edges_multi(column, nums_vert[i], 0, 20)
        zero_edges_multi(column, nums_vert[i], 0, 20)
        for ii in range(20):
            board[ii][i] = column[ii]

#    print_board()


test_row_length = 5
test_row = [value_empty] * test_row_length
test_nums = [3] 
test_row[0] = value_filled

print (test_row) 

# Test 
extend_from_edges_single2(test_row, test_nums[0], 0, test_row_length)



print (test_row)



