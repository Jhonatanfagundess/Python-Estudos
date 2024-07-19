from pathlib import Path
from datetime import datetime

patch = Path('files/dados/a.txt')
#print(patch.stat())
stats = patch.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
#print(date_created)
date_created_str = date_created.strftime('%Y-%M-%d__%H_%M_%S')
print(date_created_str)