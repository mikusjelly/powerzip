# powerzip
It's zipfile wrapper.


### Install

> pip install powerzip


###Usage
```python
from powerzip import PowerZip

pzip = PowerZip('test.zip')
print(pzip.namelist())
pzip.add('test', 'test.txt')
print(pzip.namelist())
pzip.delete('test')
print(pzip.namelist())
pzip.save("tmp.zip")
pzip.close()
```

