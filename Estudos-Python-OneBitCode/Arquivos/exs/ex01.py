# with open('names.txt','r', encoding='utf-8') as file:
#     for line in file:
#         print(line.rsplit())
        
def file_read_from_line(fname, nlines):
        from itertools import islice
        with open(fname, encoding="utf-8") as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_line('names.txt',1)