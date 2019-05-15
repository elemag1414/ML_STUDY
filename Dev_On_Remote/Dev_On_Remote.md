# 리모트 서버를 이용한 개발 환경

---

## Basic Connection 설정

- [X를 통한 ssh 연결](x_ssh.md)

---

## VSCode

- [서버의 VSCode와 연동하기](remote_ssh.md)
  > [Remote FS을 이용한 연동방법](https://www.youtube.com/watch?v=bl4tivz7kpo&t=3s)을 사용하긴 했으나, 자동 코드완성이 안되는 등 좀 문제가 있었다.
  > 이러한 문제를 해결하기 위해 [Remote SSH를 이용한 방법](https://www.youtube.com/watch?v=lKXMyln_5q4)을 설명한다.

---

## 서버의 Tensorboard log를 local에서 보기

@Local
L옵션을 사용하여 서버에 ssh 접속

```bash
$ xhost +
$ ssh -L 16006:127.0.0.1:6006 elemag1414@my_server_ip

# After Login
# Run tensorboard
$ tensorboard --logdir=log
```

이렇게 하면 서버의 포트 `6006`가 local 포트`16006`로 transfer된다.
이후 webbrowser로 `localhost:16006` 또는 `http://127.0.0.1:16006`로
텐서보드 로그를 local에서 확인할 수 있다.

---

##### [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
