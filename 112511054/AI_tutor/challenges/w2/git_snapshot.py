"""Simulate one tracked file's working, staged, committed and pushed content."""
import sys


def simulate(commands):
    working = staged = local = remote = -1
    for command in commands:
        parts = command.split()
        if parts[0] == "EDIT":
            working = int(parts[1])
        elif parts[0] == "ADD":
            staged = working
        elif parts[0] == "COMMIT":
            if staged != -1:
                local = staged
        elif parts[0] == "PUSH":
            if local != -1:
                remote = local
        else:
            raise ValueError("unknown command")
    return working, staged, local, remote


if __name__ == "__main__":
    count = int(sys.stdin.readline())
    print(*simulate(sys.stdin.readline() for _ in range(count)))
