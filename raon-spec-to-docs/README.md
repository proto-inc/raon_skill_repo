# raon-spec-to-docs

앱·웹사이트 아이디어를 **질문지(선택지)로 하나씩 결정**하면서 구체화하고, 기획부터 출시 준비까지 **확정 사양 문서**를 `docs/` 폴더에 단계별로 정리하는 AI 에이전트 스킬입니다. Claude Code·Codex·Cursor에서 같이 쓸 수 있습니다.

만든 사람: **u.kim (Raon)** · u.kim@raon.co.jp

## 무엇을 하나요

```
아이디어 ─▶ 01 기획 ─▶ 02 조사 ─▶ 03 화면·시각 설계 ─▶ 04 기술 설계
        ─▶ 05 구현 계획 ─▶ 06 테스트 계획 ─▶ 07 출시 준비 ─▶ 확정·이관
```

- **문서 순서대로 하나씩** 진행하고, 단계가 끝날 때마다 완료를 알린 뒤 다음으로 넘어갑니다.
- 결정이 필요한 질문은 **선택지가 있는 질문지**로 묻습니다. 추천안이 첫 번째에 있고, 모르는 용어는 질문 안에서 설명합니다.
- 가격·약관·플랫폼 제약은 **웹 조사로 확인**하고 출처를 남깁니다. 독립된 주제는 여러 조사를 동시에 진행합니다.
- 모든 결정은 ID(F-, D-, DS-, TD- …)와 함께 각 단계 `README.md`에 기록됩니다.
- 시각 디자인은 HTML 미리보기로 만들고, 스크린샷과 색 대비 계산으로 검증합니다.
- 앱(iOS·Android·Flutter)과 웹(사이트·웹 서비스) 모두에 맞는 질문 목록이 들어 있습니다.

## 만들어지는 폴더

```
docs/
├── README.md            목차·상태·결정 ID 규칙
├── 01-planning/         기획서
├── 02-research/         조사 (주제별 + 요약·결정)
├── 03-design/           화면 흐름·화면별 상세·표시 규칙·시각 디자인·미리보기
├── 04-technical/        구조·데이터 모델·API 명세·보안
├── 05-implementation/   마일스톤·준비 체크리스트
├── 06-testing/          테스트 전략·시나리오
└── 07-release/          스토어(SEO) 정보·개인정보·출시 체크리스트
```

필요 없는 파일은 만들지 않습니다. (예: 외부 데이터 갱신이 없으면 `data-sync.md` 생략)

## 지원 도구

`SKILL.md` 형식을 읽는 AI 코딩 도구라면 사용할 수 있어요. 질문지 기능이 없는 도구에서는 번호 선택지(`1-A, 2-B`)로 묻는 텍스트 질문지로 대신해요.

| 도구 | 질문지 | 부르는 법 |
|---|---|---|
| Claude Code | `AskUserQuestion` | `/raon-spec-to-docs` |
| Codex (CLI·IDE) | `request_user_input` (꺼져 있으면 텍스트 질문지) | `$raon-spec-to-docs` 또는 `/skills` |
| Cursor | `AskQuestion` | `/raon-spec-to-docs` |

세 도구 모두 설명(description)을 보고 상황에 맞으면 스킬을 자동으로 고르기도 해요.

## 설치

**한 곳에 두고 세 도구에서 같이 쓰기 (추천)**

```bash
# Codex·Cursor 공용 위치에 설치
mkdir -p ~/.agents/skills
cp -R raon-spec-to-docs ~/.agents/skills/

# Claude Code는 ~/.claude/skills 를 읽으므로 링크 연결
mkdir -p ~/.claude/skills
ln -s ~/.agents/skills/raon-spec-to-docs ~/.claude/skills/raon-spec-to-docs
```

**도구별 위치**

| 도구 | 사용자 전체 | 특정 프로젝트만 |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `<프로젝트>/.claude/skills/` |
| Codex | `~/.agents/skills/` | `<프로젝트>/.agents/skills/` |
| Cursor | `~/.agents/skills/` 또는 `~/.cursor/skills/` | `<프로젝트>/.agents/skills/` 또는 `.cursor/skills/` |

Cursor는 `.claude/skills/`, `.codex/skills/`도 함께 읽어요. 그래서 위 추천 방식으로 설치하면 Cursor 목록에 같은 스킬이 두 번 보일 수 있어요. 그럴 때는 하나만 남기면 돼요.

참고: [Codex Agent Skills](https://learn.chatgpt.com/docs/build-skills) · [Cursor Agent Skills](https://cursor.com/docs/skills) (2026-10 확인)

## 사용 예시

**스킬 이름으로 시작**
```
/raon-spec-to-docs        # Claude Code, Cursor
$raon-spec-to-docs        # Codex
```

**자연어로 시작**
```
항공편 알림 앱을 만들려고 해. 기획부터 출시까지 사양을 같이 정리하자.
```
```
회사 소개 사이트를 새로 만들 거야. 개발 전에 문서부터 docs 폴더에 정리해줘.
```
```
기존 docs는 참고만 하고, 새로 사양을 확정하면서 문서를 다시 써줘.
```

**진행 중 대화 예**
```
Claude: 앱의 컨셉을 알려 주세요. (한 줄 소개, 계기, 사용자, 기능 …)
나:     예매한 비행기 일정과 게이트를 알려 주는 앱이야 …
Claude: [질문지] 항공편은 어떤 방법으로 등록할까요?
        ① 편명+날짜 입력 (Recommended) ② 탑승권 스캔 ③ 메일 자동 인식
나:     ①
Claude: ✅ 첫 번째 문서(기획서) 작성 완료 … ▶️ 다음: 02-research
나:     다음
```

## 팁

- 모르는 질문은 "추천대로"라고 답해도 됩니다. 질문 없이 정한 기본값은 "검토 필요"로 표시되어 나중에 한꺼번에 확인할 수 있습니다.
- 디자인을 고칠 때는 "이 부분만" 바꿔 달라고 하면 기존 컨셉을 유지한 채 그 부분만 바뀝니다.
- 실제 API 키나 비밀번호는 채팅에 붙여 넣지 마세요. 스킬은 키를 요구하지 않습니다.
- 구현을 시작하면 사양 문서 훅이 설치됩니다. 동작이 바뀌는데 `docs/`를 안 고치면, 턴이 끝날 때 한 번 문서부터 고치라고 되돌립니다.
