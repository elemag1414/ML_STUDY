# tmux 사용하기

[[원본 블로그]](https://edykim.com/ko/post/tmux-introductory-series-summary/)

## tmux 구성

session : tmux 실행 단위. 여러개의 window로 구성. <br>
window : 터미널 화면. 세션 내에서 탭처럼 사용할 수 있음. <br>
pane : 하나의 window 내에서 화면 분할. <br>
status bar : 화면 아래 표시되는 상태 막대.

## 명령어 구성

tmux는 prefix 키인 ctrl+b를 누른 후 다음 명령 키를 눌러야 동작할 수 있다. 다음 내용에서 ctrl + b, 어쩌고 내용이 있다면 tmux 내에서 쓸 수 있는 단축키다.

```bash
ctrl + b, <key>
```

일부 직접 명령어를 입력해야 할 때는 명령어 모드로 진입해야 한다. 명령어 모드의 key는 :다.

```bash
ctrl + b, :
```

## Session 관련

```bash
# 새 세션 생성
$ tmux new -s <session-name>

# 세션 이름 수정
ctrl + b, $

# 세션 종료
$ (tmux에서) exit

# 세션 중단하기 (detached)
ctrl + b, d

# 세션 목록 보기 (list-session)
$ tmux ls

# 세션 다시 시작
$ tmux attach -t <session-number or session-name>
```

##### [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
