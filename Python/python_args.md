# \*args, \*\*kwargs 의미와 사용

## \*args와 \*\*kwargs

[[출처]](https://toughbear.tistory.com/entry/python-args%EC%99%80-kwargs-%EC%9D%98%EB%AF%B8%EC%99%80-%EC%82%AC%EC%9A%A9)

외부라이브러리를 쓰다보면 많이 보는 글자가 바로 \*args 또는 \*\*kwargs 다.

\*args는 값을 넣으면 함수에 변수가 튜플형태로 입력되는 것

\*\*kwargs는 딕셔너리 형태로 입력되는 것

## 예제

```python
def a(*args):
    print(args)


a(1,2,3,4)
==> (1,2,3,4)


def b(**kwargs):
    print(kwargs)

b(a=1, b=2, c=3)
==>{'a': 1, 'b': 2, 'c': 3}

```

특히, \*\*kwargs의 경우 class 사용시 넘겨줄 인자를 관리하는데 좀 더 유연하게 사용할 수 있다.
[[출처]](https://toughbear.tistory.com/entry/python-args%EC%99%80-kwargs-%EC%9D%98%EB%AF%B8%EC%99%80-%EC%82%AC%EC%9A%A9)의 예제에 잘 정리되어 있다.

##### [[Python 돌아가기]](README.md) | [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
