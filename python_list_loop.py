"""

Problem Statement : 

Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be
printed in a comma-separated sequence on a single line.

"""

# Set Start Limit and End Limit Ranges
start_limit = 2000
end_limit = 3200

# Set Range , assuming End Limit inclusive
full_range = range(start_limit,end_limit + 1)

# init List
final_output_list = []

# Loop over range to select numbers which are divisible by 7 but are not a multiple of 5
# Append to list
for i in full_range:
    if(i%7 == 0 and i%5 != 0):
        final_output_list.append(i)
        
# Convert final list into comma separated value string for display
csv = ','.join(map(str, final_output_list))
print (csv)

