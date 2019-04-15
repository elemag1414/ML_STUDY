# VSCode Tips

## Create User Snippets

VSCode의 Preferences에서 User Snippets을 선택한다.
![Preferences](https://github.com/elemag1414/ML_STUDY/blob/master/VSCode/Snippet_Config.png)

이후, command 팔레트에 language를 선택하는 창이 나타나는데,
python.json을 선택하면 User Snippet Configuration 창이 뜬다.
![CommandPallet](https://github.com/elemag1414/ML_STUDY/blob/master/VSCode/command_pallet_language.png)

Python.json 파일에 원하는 Snippet을 추가 할 수 있는데,
형식은 다음과 같다.

```json
{
  "Print to console": {
    "prefix": "log",
    "body": ["console.log('$1');", "$2"],
    "description": "Log output to console"
  }
}
```

여기서
Print to console:
prefix: VSCode에서 Trigger할 word
body: snippet body
description: 설명 (Optional)
