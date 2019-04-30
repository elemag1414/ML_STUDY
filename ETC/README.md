# ETC

- [Ubuntu Version 확인하기](#ubuntu-version-확인하기)
- [Ubuntu 사용자 추가](#사용자-추가)

## Ubuntu

### Ubuntu Version 확인하기

```bash
$ cat /etc/issue
```

### 사용자 추가

```bash
$ # 새로운 사용자 (new_user_account)를 추가
$ sudo adduser new_user_account

$ # 비밀번호 변경
$ sudo passwd new_user_account

$ # 생성한 계정이 들어갈 그룹 생성
$ sudo groupadd devgroup

$ # 새로 생성한 계정을 devgroup에 추가
$ sudo usermod -a -G devgroup new_user_account

$ # 계정의 홈 디렉토리 설정
$ sudo usermod -d /var/devgroup/new_user_account user
```

`useradd`로 사용자를 추가하면 계정만 생성해주며 기타 계정 정보등을 수동으로 생성 및 설정해야 한다.

##### [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
