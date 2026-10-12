#!/usr/bin/env python3
"""Install the spec-docs stop hook into the current project.

Keeps existing Cursor and Claude Code hooks. Adds this hook only if missing.
Usage: python3 install.py [project_root]
"""
import json
import shutil
import stat
import sys
from pathlib import Path

HOOK_COMMAND = ".cursor/hooks/spec-docs.py"
CLAUDE_COMMAND = "python3 .cursor/hooks/spec-docs.py"
HERE = Path(__file__).resolve().parent


def load_json(path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        sys.stderr.write("{} is not valid JSON ({}). Merge the hook by hand.\n".format(path, exc))
        raise SystemExit(1)


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def install_script(root):
    dest = root / ".cursor" / "hooks" / "spec-docs.py"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "spec-docs.py", dest)
    dest.chmod(dest.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def install_cursor(root):
    path = root / ".cursor" / "hooks.json"
    data = load_json(path) or {"version": 1, "hooks": {}}
    if not isinstance(data, dict):
        sys.stderr.write("{} is not a JSON object.\n".format(path))
        raise SystemExit(1)
    data.setdefault("version", 1)
    hooks = data.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        sys.stderr.write("{} hooks is not an object.\n".format(path))
        raise SystemExit(1)
    stop = hooks.setdefault("stop", [])
    if not isinstance(stop, list):
        sys.stderr.write("{} stop hooks are not a list.\n".format(path))
        raise SystemExit(1)
    if any(HOOK_COMMAND in str(item.get("command", "")) for item in stop if isinstance(item, dict)):
        return
    stop.append({
        "command": HOOK_COMMAND,
        "timeout": 15,
        "loop_limit": 1,
    })
    save_json(path, data)


def install_claude(root):
    path = root / ".claude" / "settings.json"
    data = load_json(path) or {}
    if not isinstance(data, dict):
        sys.stderr.write("{} is not a JSON object.\n".format(path))
        raise SystemExit(1)
    hooks = data.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        sys.stderr.write("{} hooks is not an object.\n".format(path))
        raise SystemExit(1)
    stop = hooks.setdefault("Stop", [])
    if not isinstance(stop, list):
        sys.stderr.write("{} Stop hooks are not a list.\n".format(path))
        raise SystemExit(1)
    for group in stop:
        if not isinstance(group, dict):
            continue
        for hook in group.get("hooks") or []:
            if isinstance(hook, dict) and "spec-docs.py" in str(hook.get("command", "")):
                return
    stop.append({
        "hooks": [
            {"type": "command", "command": CLAUDE_COMMAND}
        ]
    })
    save_json(path, data)


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    if not root.is_dir():
        sys.stderr.write("not a directory: {}\n".format(root))
        raise SystemExit(1)
    install_script(root)
    install_cursor(root)
    install_claude(root)
    print("installed spec-docs hook in {}".format(root))


if __name__ == "__main__":
    main()
