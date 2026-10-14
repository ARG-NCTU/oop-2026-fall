import subprocess
import pytest
from git_snapshot import simulate


@pytest.mark.parametrize("commands, expected", [
    (["EDIT 10", "ADD", "EDIT 20", "COMMIT", "PUSH"], (20, 10, 10, 10)),
    (["EDIT 7", "ADD", "COMMIT", "EDIT 9"], (9, 7, 7, -1)),
    (["EDIT 1", "ADD", "COMMIT", "PUSH", "EDIT 2", "ADD", "COMMIT"], (2, 2, 2, 1)),
    ([], (-1, -1, -1, -1)),
    (["EDIT 0"], (0, -1, -1, -1)),
    (["COMMIT", "PUSH"], (-1, -1, -1, -1)),
    (["EDIT 4", "ADD", "COMMIT", "EDIT 8", "COMMIT", "PUSH"], (8, 4, 4, 4)),
    (["EDIT 5", "ADD", "EDIT 6", "ADD", "COMMIT", "PUSH"], (6, 6, 6, 6)),
    (["EDIT 1000000000", "ADD", "COMMIT", "PUSH", "PUSH"], (1000000000,) * 4),
])
def test_snapshots(commands, expected):
    assert simulate(commands) == expected


def test_maximum_commands():
    assert simulate("EDIT 1" for _ in range(100000)) == (1, -1, -1, -1)


def test_against_real_git(tmp_path):
    """Compare snapshots with a real local repository and bare remote."""
    remote = tmp_path / "remote.git"
    work = tmp_path / "work"
    subprocess.run(["git", "init", "--bare", "-q", str(remote)], check=True)
    subprocess.run(["git", "init", "-q", str(work)], check=True)

    def git(*args, check=True):
        return subprocess.run(
            ["git", "-c", "user.name=SnapshotTest", "-c",
             "user.email=snapshot@example.invalid", *args],
            cwd=work, text=True, capture_output=True, check=check,
        )

    git("remote", "add", "origin", str(remote))
    commands = ["EDIT 10", "ADD", "EDIT 20", "COMMIT", "PUSH",
                "EDIT 30", "ADD", "EDIT 40", "COMMIT"]
    for command in commands:
        if command.startswith("EDIT "):
            (work / "value.txt").write_text(command.split()[1] + "\n")
        elif command == "ADD":
            git("add", "value.txt")
        elif command == "COMMIT":
            git("commit", "-qm", "snapshot")
        elif command == "PUSH":
            git("push", "-q", "origin", "HEAD:main")
    working = int((work / "value.txt").read_text())
    staged = int(git("show", ":value.txt").stdout)
    committed = int(git("show", "HEAD:value.txt").stdout)
    pushed = int(subprocess.run(
        ["git", "--git-dir", str(remote), "show", "main:value.txt"],
        text=True, capture_output=True, check=True,
    ).stdout)
    assert simulate(commands) == (working, staged, committed, pushed)
