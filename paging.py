no_of_pages = int(input('Enter the number of pages: '))
page_size = int(input('Enter the page size: '))

mem_size = no_of_pages*page_size
print('Total size of memory: ', mem_size)
no_of_frames = int(input('Enter the number of frames: '))

page_table = []

for i in range(no_of_pages):
    fno = int(input(f'Enter frame number for page {i+1}: '))
    page_table.append([i, fno])
    
inp_pno, inp_off = map(int, input('Enter page number and offset: ').split())
inp_fra = None

for i in page_table:
    if i[0] == inp_pno:
        inp_fra = i[1]

if inp_fra is None:
    print('Page not found')
else:
    base_reg = int(input('Enter the base register: '))
    phy_add = base_reg + inp_fra * page_size + inp_off
    print('Physical address is: ', phy_add)