## git init - start a new repository

This command initialises a new Git repository in the current directory, preparing it for version control. It's foundational and something you use everytime you start a new project locally.

```
git init
```

## git clone - copy an existing repository

This is the command you'll use to bring a copy of the repository to your local environment.
```
git clone
```

## git add - stage your work

Adding files to the staging area is one of the first steps in committing changes.
git add <file> stages specific files while git add -A stages all modified changes.
```
# add a specific file
git add <file>

# add all files with changes
git add -A
```
## git commit - create a snapshot of your changes
This command creates a snapshot of your current changes with a message, making it easier to understand the project history.
```
git commit -m "Implement user login feature"
```
## git add [-p] - stage changes in parts
Sometimes you only want to commit specific changes from a file. git add -p (patch) lets you review and add individual changes in parts, making it easier to keep each comment focused on a single task.
```
git add -p
```
This command allows you to keep commits clean and organized. It's invaluable when working on multiple fixes and features simultaneously.

## git status - check your workspaces current state
This command gives you a quick look at your working directory. It shows what is staged, modified and untracked. This command is essential to avoid committing changes you didn't intend to.
```
git status
```
## git log - review commit history
Provides a detailed commit history showing all commits, authors and timestamps. Using git log --oneline is also helpful when you want a more concise view of the commit history, with each commit condensed into a single line.
```
# full commit history
git log
# condensed history
git log --oneline
```

## git diff - view changes between commits or states
git diff is invaluable for viewing changes between your working directory and the last commit. 

```
git diff
```
## git branch - list, create, and delete branches
```
# List all branches
git branch

# create a new branch
git branch feature-login

# delete a branch
git branch -d feature-login
```
## git checkout - switch or create new branches
git checkout <branch> lets you move between branches whilst git checkout -b <new-branch> creates a new branch and switches to it immediately.
```
# Switch to an existing branch called feature-login
git checkout feature-login

# create and switch to a new branch called feature-signup
git checkout -b feature-signup

# delete a branch
git branch -d feature-login
```
## git remote add origin - link local and remote repositories
When setting up a new repo, linking it to a remote is often one of the first tasks. git remote add origin connects your local repo to a remote, making it ready for collaborative work.
```
git remote add origin https://github.com/user/
```
## git pull and git push - sync local and remote changes
```
# pull changes from remote
git pull origin main

# push changes to remote
git push origin main
```

## git reset <commit> - undo recent commits
git reset helps you undo commits by moving the HEAD pointer to a specific commit. Use it to clean out commits that are mistakes. Be careful when using it, as it alters the commit history. This is the code to use to cover up crimes...

```
# Undo to the previous commit
git reset HEAD-1
```

## git stash - temporarily save changes without committing

```
git stash
# for untracked files you'd like to stash
git stash -u

```

## git reflog - access historical changes and recover lost commits
If something goes wrong, reflog can provide a trail to recover lost changes.

```
git reflog
```

## git help

usage: git [--version] [--help] [-C <path>] [-c name=value]
       [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
       [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
       [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
       <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Forward-port local commits to the updated upstream head
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
