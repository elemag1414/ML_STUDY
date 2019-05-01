# OS Module

```python
import os
```

많이 쓰이는 attributes

- 현재 directory: `os.curdir`
-

## 사용 Tips

- 디렉토리내 파일 리스트

```python
from os import listdir
from os.path import isfile, join

cur_path = os.curdir

onlyfiles = [f for f in listdir(cur_path) if isfile(join(cur_path, f))]
```

- 파일 리스트에서 이름과 확장자 추출하기

```python
# file_split is a list of tuples, where each tuple is (file_name, file_ext)
file_split = [splitext(f) for f in onlyfiles]
```

##### [[Python 돌아가기]](README.md) | [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
