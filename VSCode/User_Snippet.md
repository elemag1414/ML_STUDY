## Create User Snippets

- VSCode의 Preferences에서 User Snippets을 선택한다.
  ![Preferences](https://github.com/elemag1414/ML_STUDY/blob/master/VSCode/Snippet_Config.png)

- 이후, command 팔레트에 language를 선택하는 창이 나타나는데,
  python.json을 선택하면 User Snippet Configuration 창이 뜬다.
  ![CommandPallet](https://github.com/elemag1414/ML_STUDY/blob/master/VSCode/command_pallet_language.png)

- Python.json 파일에 원하는 Snippet을 추가 할 수 있는데,
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

> 여기서
> Print to console: <br>
> prefix: VSCode에서 Trigger할 word <br>
> body: snippet body <br>
> description: 설명 (Optional) <br>

> body 내용을 작성할때 indentation등 여러가지 불편한 점이 많다.
> 다음 web기반 작성기을 사용하면 좀 더 편하게 작성할 수 있다.
> [[snippet 작성기]](https://snippet-generator.app/)

- 작성예

```json
{
  "Add Path to PYTHONPATH": {
    "prefix": "sn_addPYPATH",
    "body": [
      "def addPYTHONPath(dir):",
      "    import os",
      "    import sys",
      "    path = os.getcwd()",
      "    path += '/' + dir",
      "    sys.path.append(path)"
    ],
    "description": "Add Path to PYTHONPATH"
  }
}
```

##### [[VSCode로 돌아가기]](https://github.com/elemag1414/ML_STUDY/tree/master/VSCode)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
