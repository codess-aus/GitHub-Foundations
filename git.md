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


