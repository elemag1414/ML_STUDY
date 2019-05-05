# Python에서 CSV file 다루기

## CSV 파일 읽기

```python
import csv

file_name = 'data.csv'

f = open(file_name, 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    print(line)
f.close()
```

[출력예]

```bash
(입력 : data.csv 파일 내용)
1,Kevin,2017-01-19 11:30:00,25
2,Charles,2017-02-07 10:22:00,35
3,Janett,2017-03-22 09:10:00,33

(출력)
[\'1\', \'Kevin\', \'2017-01-19 11:30:00\', \'25\']
[\'2\', \'Charles\', \'2017-02-07 10:22:00\', \'35\']
[\'3\', \'Janett\', \'2017-03-22 09:10:00\', \'33\']
```

## CSV 파일 쓰기

```python
import csv
f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "Kevin", False])
wr.writerow([2, "Halsey", True])
f.close()
```

##### [[Python 돌아가기]](README.md) | [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
