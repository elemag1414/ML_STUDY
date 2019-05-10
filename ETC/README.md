# ETC

- [Ubuntu Version 확인하기](#ubuntu-version-확인하기)
- [Ubuntu 사용자 추가하기](#사용자-추가하기)
- [SCP로 파일 전송하기](#scp-file-전송)
- [GPU monitor하기](#GPU-monitor하기)
- [file 사이즈 확인하기](#file-사이즈-확인하기)
- [tmux사용하기](#tmux사용하기)
- [Redirect Screen log to file](#Redirect-Screen-log-to-file)

## Ubuntu

### Ubuntu Version 확인하기

```bash
$ cat /etc/issue
```

### 사용자 추가하기

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

### SCP file 전송

```bash
$ # upload local file local_dir/a.file to remote server
$ scp local_dir/a.file user@host.com:~/remote_dir/

$ # upload folder local_dir to remote server::: use -r option
$ scp -r local_dir/* user@host.com:~/remote_dir
```

### GPU monitor하기

```bash
$ nvidia-smi
Tue Apr 30 12:33:04 2019
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.56       Driver Version: 418.56       CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  TITAN V             Off  | 00000000:21:00.0 Off |                  N/A |
| 46%   64C    P2   133W / 250W |   8944MiB / 12036MiB |     66%      Default |
+-------------------------------+----------------------+----------------------+
|   1  TITAN V             Off  | 00000000:23:00.0 Off |                  N/A |
| 28%   37C    P8    25W / 250W |    318MiB / 12036MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0     29720      C   python3                                     8933MiB |
|    1     29720      C   python3                                      307MiB |
+-----------------------------------------------------------------------------+
```

### file 사이즈 확인하기

> h 옵션 사용

```bash
$ ls -lah
```

### tmux사용하기

See [this](tmux.md)

<br>

### Redirect Screen log to file

[Source](https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file/420983) <br>

Just redirect the output to a file:

```bash
SomeCommand \> SomeFile.txt
```

Or if you want to append data:

```bash
SomeCommand >> SomeFile.txt
```

If you want stderr as well use this:

```bash
SomeCommand &> SomeFile.txt
```

or this to append:

```bash
SomeCommand &>> SomeFile.txt
```

if you want to have both stderr and output displayed on the console and in a file use this:

```bash
SomeCommand 2>&1 | tee SomeFile.txt
```

(If you want the output only, drop the 2 above)

##### [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
