# raon_skill_repo

Raon에서 사용하는 AI 에이전트 스킬 모음입니다. Claude Code·Codex·Cursor 등 `SKILL.md`를 읽는 도구에서 씁니다. 스킬마다 이름과 같은 폴더가 있고, 폴더 안에 `SKILL.md`와 `README.md`가 있습니다.

| 스킬 | 설명 | 만든 사람 |
|---|---|---|
| [raon-spec-to-docs](raon-spec-to-docs/) | 질문지로 사양을 확정하며 기획~출시 준비 문서를 `docs/`에 단계별로 정리 (앱·웹 공용) | u.kim |

## 설치

```bash
# Codex·Cursor 공용
cp -R <스킬 폴더> ~/.agents/skills/
# Claude Code
ln -s ~/.agents/skills/<스킬 폴더> ~/.claude/skills/<스킬 폴더>
```

도구별 자세한 위치는 각 스킬의 README를 참고하세요.
