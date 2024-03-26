# wit - Git Implementation in Python

## Introduction
wit is a lightweight Git implementation written in Python. It aims to provide the core functionality of Git, allowing users to version control their projects, manage branches, and track changes efficiently.
## Installation
1. Clone the wit repository from GitHub:
   
```
   git clone https://github.com/ChaniChalamish/Wit.git
  ``` 

2. Navigate to the wit directory:
   
```
   cd wit
   ```
3. Run the wit command-line tool:
   
```
   python wit.py
   ```

## Usage
- Initialize a new Wit repository in the current directory:
  
```
  wit init
  ```

- Add files\directories to the staging area:
```
  wit add file1.txt file2.py
  wit add folder1
```
  Inserting an internal file\directory includes the current path:
  ```
  wit add folder1\file1.txt
  wit add folder1\folder2
```

- Commit changes with a descriptive message:
  
```
  wit commit -m "Initial commit"
  ```

- Create and switch to a new branch:
  
```
  wit branch <feature-branch>
  wit checkout <feature-branch>
  ```

- Merge changes from one branch into another:
  
```
  wit checkout <target-branch>
  wit merge <source-branch>
  ```

- View commit history:
  
```
  wit log
  
```
- Revert to a previous commit:
  
```
  wit checkout <commit-hash>
  ```

- Push changes to a remote repository:
  
```
  wit push origin master
  ```

- Pull changes from a remote repository:
  
```
  wit pull origin master
  ```

## Features
- Initialize a new Wit repository
- Stage and commit changes
- Create and switch between branches
- Merge branches
- View commit history
- Track changes and file modifications
- Ignore specific files or directories using .witignore
- Revert to previous commits
- Push and pull changes to remote repositories
