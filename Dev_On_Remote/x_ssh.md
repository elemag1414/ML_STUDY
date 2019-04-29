# X를 통한 ssh 연결

## 준비사항

- [XQuartz 설치](https://www.xquartz.org)
- X11 Forwarding 설정

  > `/etc/ssh/sshd_config`파일의 `X11Forwarding` 설정을 `yes`로 변경한다.
  >
  > 맨 처음 사용시 해당 설정이 comment처리 되어있을 것이다.

## Basic Connection 설정

- 클라이언트 (MacBookPro) connection 설정

```bash
$ xhost +
```

해당 설정을 하면, 클라이언트가 모든 host로부터 x 연결을 허용한다.

- x 를 통한 ssh 연결

```bash
$ ssh -X sever_account@xxx.xxx.xxx.xxx
```

> PyCharm에서 X11 어플 열기
>
> > open a ssh session that support X11 display(remember to keep this session)
> >
> > `run echo \$DISPLAY` in that ssh session
> >
> > set `DISPLAY` environment variable for your PyCharm

##### [[Remote 서버를 통한 개발]](Dev_On_Remote.md) | [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
