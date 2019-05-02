# Anaconda에서 Python 가상환경 관리

## 가상환경 생성

> conda create --name 가상환경명 설치할패키지

```bash
\$ conda create --name VirEnvName python=3.5
```

## 가상환경 삭제

> conda env remove --name 가상환경명

```bash
\$ conda env remove --name VirEnvName
```

## 설치된 가상환경 리스트 확인

```bash
\$ conda info --envs
```

또는

```basj
\$ conda env list
```

## 가상환경 활성화

> source activate 가상환경명

```bash
\$ source activate VirEnvName
```

## 가상환경 비활성화

> source deactivate 가상환경명

```bash
\$ source deactivate VirEnvName
```

---

Related Links: [[Anaconda UserGuide Doc]](https://conda.io/docs/user-guide/tasks/manage-environments.html)

##### [[Python 돌아가기]](README.md) | [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
