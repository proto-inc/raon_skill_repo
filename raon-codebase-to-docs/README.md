# raon-codebase-to-docs

**raon-spec-to-docs로 만들지 않은** 기존 프로젝트의 코드를 읽고, 같은 단계의 사양 문서를 `docs/`에 다시 씁니다. Claude Code·Codex·Cursor에서 같이 씁니다.

만든 사람: **u.kim (Raon)** · u.kim@raon.co.jp

## 무엇을 하나요

- 진입점, 화면, 데이터, API, 테스트를 읽고 기획→출시 준비 문서를 채웁니다.
- 이미 `docs/`나 다른 형식의 사양 문서가 있으면 `legacy/<날짜>/`로 옮긴 뒤 다시 씁니다.
- 코드에서 확인되지 않는 의도·비용·법적 판단은 지어내지 않고 '결정 대기'에 둡니다.
- 사양이나 동작이 나중에 바뀌면 `docs/`를 먼저 고치도록 훅을 설치합니다.

이미 `docs/01-planning/`과 결정 ID 규칙이 있는 프로젝트는 다시 쓰지 않습니다. 훅만 없으면 설치합니다.

## 설치

```bash
mkdir -p ~/.agents/skills
cp -R raon-codebase-to-docs ~/.agents/skills/

mkdir -p ~/.claude/skills
ln -s ~/.agents/skills/raon-codebase-to-docs ~/.claude/skills/raon-codebase-to-docs
```

도구별 위치는 [raon-spec-to-docs](../raon-spec-to-docs/README.md)와 같습니다.

## 사용 예시

```
/raon-codebase-to-docs
```

```
이 저장소는 문서 없이 코드만 있어. 코드 기준으로 사양 문서를 docs에 만들어줘.
```

```
지금 docs는 예전 방식이야. legacy로 옮기고 raon 문서 구조로 다시 써줘.
```
