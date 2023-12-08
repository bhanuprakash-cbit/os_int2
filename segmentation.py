import traceback

no_of_segments = int(input('Enter the no of segments: '))

seg_table = {}

for i in range(no_of_segments):
    name = input('Enter the name of the segment: ')
    s_base,s_size = map(int, input(f'Enter the base and size of {name} segment: ').split())
    seg_table.update({name:[s_base,s_size]})

seg_name, offset = map(str, input(f'Enter logical address as segment name and offset: ').split())

try:
    seg = seg_table[seg_name]
except Exception:
    traceback.print_exc()

if 0 <= int(offset) < seg[1]:
    phy_add = seg[0] + int(offset)
    print('Physical address of given logical address is: ',phy_add)
else:
    print('Offset is greater than limit')