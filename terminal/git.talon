tag: terminal
and tag: user.git
-
git show head: "git show HEAD\n"
git clean: "git clean -f -d"
git checkout main branch: "git checkout main\n"
git diff staged: "git diff --staged\n"
git commit work in progress: "git commit -m 'wip'\n"
git add all: "git add --all\n"
git commit messy:
    "git commit -m ''"
    key(left)
git log list: "git log\n"
git branch list: "git branch\n"

git search conflicts: "ag \">>>>>\"\n"
git new branch clipboard:
    "git checkout -b "
    edit.paste()
git checkout clipboard:
    "git checkout "
    edit.paste()
