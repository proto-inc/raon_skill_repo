# raon_skill_repo

Raon에서 사용하는 AI 에이전트 스킬 모음입니다. Claude Code·Codex·Cursor 등 `SKILL.md`를 읽는 도구에서 씁니다. 스킬마다 이름과 같은 폴더가 있고, 폴더 안에 `SKILL.md`와 `README.md`가 있습니다.

| 스킬 | 설명 | 만든 사람 |
|---|---|---|
| [raon-spec-to-docs](raon-spec-to-docs/) | 질문지로 사양을 확정하며 기획~출시 준비 문서를 `docs/`에 단계별로 정리 (앱·웹 공용). 구현 시 사양 변경이면 문서를 먼저 고치게 하는 훅을 설치 | u.kim |
| [raon-codebase-to-docs](raon-codebase-to-docs/) | 그 스킬 없이 만든 프로젝트의 코드를 읽어 같은 `docs/`를 다시 구성. 기존 문서는 `legacy/`로 이동. 같은 훅을 설치 | u.kim |

## 설치

```bash
# Codex·Cursor 공용
cp -R <스킬 폴더> ~/.agents/skills/
# Claude Code
ln -s ~/.agents/skills/<스킬 폴더> ~/.claude/skills/<스킬 폴더>
```

도구별 자세한 위치는 각 스킬의 README를 참고하세요.

## 만들어지는 docs 폴더

두 스킬 모두 프로젝트 루트에 아래 `docs/`를 만듭니다. 없는 영역은 파일을 만들지 않습니다. 외부 데이터 갱신이 없으면 `data-sync.md`가 없고, 조사할 주제가 없으면 `02-research/`는 `README.md`만 둡니다.

`raon-spec-to-docs`는 질문지로 한 단계씩 채웁니다. `raon-codebase-to-docs`는 코드를 읽고 한 번에 다시 쓰며, 예전 문서는 `legacy/<날짜>/`로 옮깁니다.

```
docs/
├── README.md                  목차, 단계별 상태, 결정 ID 규칙, 문서 변경 규칙
├── 01-planning/
│   └── product-requirements.md   왜·누구를·무엇을 (기능 F-xx)
├── 02-research/
│   ├── README.md              조사 요약, 결정 D-xx, 위험, 결정 대기
│   └── <주제>.md              주제별 조사 (출처 포함)
├── 03-design/
│   ├── README.md              화면 결정 DS-xx
│   ├── screen-flow.md         화면 목록 S-xx, 이동 흐름
│   ├── screens.md             화면별 스케치·상태 (빈 화면, 오류 등)
│   ├── display-rules.md       공통 표시 규칙
│   ├── notifications.md       알림·위젯 또는 이메일
│   ├── visual-design.md       색·글자·간격 (VD-xx)
│   └── preview/index.html     시각 미리보기
├── 04-technical/
│   ├── README.md              기술 결정 TD-xx
│   ├── architecture.md        구성, 폴더, 빌드·배포
│   ├── data-model.md          데이터 구조
│   ├── api-spec.md            API
│   ├── data-sync.md           외부 데이터 갱신 (있을 때만)
│   └── security.md            인증, 권한, 비밀 정보
├── 05-implementation/
│   ├── README.md              구현 결정 IM-xx
│   ├── milestones.md          M0~ 마일스톤
│   └── setup-checklist.md     사용자가 직접 할 계정·콘솔 작업
├── 06-testing/
│   ├── README.md              테스트 결정 TS-xx
│   ├── test-strategy.md
│   └── scenarios.md           시나리오 T-xx
└── 07-release/
    ├── README.md              출시 결정 RL-xx
    ├── store-listing.md       스토어 등록 또는 SEO
    ├── privacy.md             개인정보·약관
    └── launch-checklist.md
```
