# VSCode Remote SSH를 이용한 원격 서버와 연동하기

다음의 내용은 MacOS 기준이며, 윈도우의 경우는 약간 다른 절차가 있음을 알린다.

## 준비사항

- [[VSCode Insiders 다운 로드 및 설치하기]](https://code.visualstudio.com/insiders/)

MacOS에서 작업하면서, Remote SSH extension이 설치안되서 이상하다 싶었는데,
이를 사용하려면, VSCode (일반적으로 사용하는 버전은 VSCode Stable이라 부르는 모양이다. ㅡㅡ;;)가 아니라
VSCode Insiders를 설치해야 한다고 한다.

## VSCode에서 Remote SSH를 통해 원격 코딩을 위한 설정 절차. (MacOS Only)

1.  Generate RSA key for SSH connection

    You need to store the public key generated on your local MBP, and copy this to linux server.

    - Key generation

    \$ ssh-keygen -t rsa -b 4096 -f /Users/my_account/.ssh/ubuntu_rsa

    Note,
    /User/my_account is my local user directory on MBP
    (Create .ssh, if it’s not on the system)
    ubuntu_rsa is the name of key creating now.
    Once you enter the above, computer asks passphrases. You may either just enter or some word you like.

        	Then…
        	 Check if the key is generated.
        	 Go to /Users/my_account/.ssh/. Then, you should see files, ‘ubuntu_rsa’ and ‘ubuntu_rsa.pub’.
        	 Note, ubuntu_rsa.pub is the public key that should be stored in remote server

2.  Copy the public RSA key to the remote server.


    The file  ‘ubuntu_rsa.pub’ is the public key just generated. This guy needs to be copied on the server. So scp it to server like:
    $ scp /Users/my_account/.ssh/ubuntu_rsa.pub my_id@server_ip:~/key.pub

    Note the public key is copied as key.pub on the server

    Now, on server, the public key should be located in .ssh folder.
    So, move it to the right directory.
    server$ cat ~/key.pub >> ~/.ssh/authorized_keys

        You may wondering why the public key is not transferred directly to .ssh folder on server side.
        I think this is to make sure the folder .ssh exists on the server. Otherwise, scp won’t work.
       (May be not. I’m not sure….)

       Once the public key is copied on the right place on the server.
       You may want to change the privilege of the file for safety reason:
       server$ chmod 600 ~/.ssh/authorized_keys

       Then remove the key.pub file on the home directory which was transferred from MBP.
       server$ rm key.pub


    <Sanity Check>
    You may want to check if the key works fine for ssh connection.
    By typing the following, see if the remote asks password for ssh connection.

    $ ssh -i /User/my_account/.ssh/ubuntu_rsa my_id@server_ip

    If the remote doesn’t ask the password for ssh connection and allow you to connect, you’re successful.

4.  Configure Remote SSH in VSCODE insider
    Launch VSCODE insider and bring the command pallet.
    Search command ‘Remote SSH: Open Configure File…’
    Then, select the configuration option like: /User/user/.ssh/config
    (If you don’t the the configuration option, just create empty file config on /User/user/.ssh/)

    Then, set the configuration, at least, like the minimum settings as following:

    ```bash
      Host name_of_config_U_want_to_call
        HostName server_ip
        User my_id
        IdentityFile /User/my_account/.ssh/ubuntu_rsa
    ```


    Save the config above, and open command pallet again.
    And search
    	Remote SSH: Connect to Host…
    Then, pick the server connection config that you just setup (e.g. name_of_config_U_want_to_call)

    This will bring you to new vscode insider window connected to the Remote Server.

    Now, you can access the remote files and folders just as like the ones in the local MBP.
    Also, all code completion and code navigation shall work.
        (Remote Debugging features are said to be working. But I didn’t test it.)

##### [[Remote 서버를 통한 개발]](Dev_On_Remote.md) | [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
