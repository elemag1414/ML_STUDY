# Python에서 dictionary list 검색

## dictionary list에서 조건에 맞는 dictionary 추출하기

다음과 같이 dictionary list가 있다고 가정하자.

```python
people_list = [
    {'name': "Tom", 'age': 10},
    {'name': "Mark", 'age': 5},
    {'name': "Pam", 'age': 7}
]
```

이 `people_list` 리스트에서 `'age'` key 값이 5보가 큰 dictionary만 추출해서 리스트를 만들어 보자.

```python
people = [people for people in people_list if people['age'] > 5]
```

<결과>
```python
>>> people
[{'name': 'Tom', 'age': 10}, {'name': 'Pam', 'age': 7}]
```


##### [[Python 돌아가기]](README.md) | [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)