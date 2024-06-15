Certainly! Here is the revised and proofread format of the text for clarity and better presentation:

## NOTES

- `.gitignore`: Ignore unnecessary files (choose Python when creating a project on GitHub).



## CLONE PROJECT

#### Clone Project to a Local Directory
```bash
git clone https://github.com/user_name/repo_name.git
```

#### Check the Status of the Local Repo (Any New Changes)
```bash
git status
```

##### List the Remote Repositories (Fetch and Push URLs)
```bash
git remote -v
```
*-v: verbose (detailed)*

##### Show Detailed Information About a Specific Remote Repository
```bash
git remote show origin
```
*origin: default name of remote repository*




## CONFIG USERNAME & EMAIL OF GITHUB ACCOUNT

Gets and sets repository or global options.

```bash
git config [--global] user.name "Your Name"
git config [--global] user.email "your.email@example.com"
```

*Note: Remove `--global` keyword to set for the current repo only.*





## CREATE/SWITCH/MERGE BRANCHES

#### Show all branches
git branch -a


#### Create a Branch & Push Develop Branch to GitHub
```bash
git checkout -b develop
git push origin develop
```
*Note: On GitHub, we will see two branches: `main` & `develop`.*

#### Create a Feature Branch from Develop
```bash
git checkout -b feature/w1_exs_basic_python
git push origin feature/w1_exs_basic_python
```

*Note: `origin` is the default name of the remote repo.*

##### Switch Branches
```bash
git checkout branch-name
```

##### Delete a Branch
```bash
git branch -d branch-to-delete          
git push origin --delete branch-name
```




## FETCH/PULL CHANGES FROM REMOTE REPO

#### Download Changes from a Branch of the Remote Repo
```bash
git fetch origin branch-name
```

#### Merge the Fetched Changes from the Remote Repo into Your Local Current Branch
```bash
git merge origin/branch-name
```

#### Fetch and Merge the Changes from the Remote Repo
```bash
git pull origin [branch-name]
```





## COMMIT & PUSH PROCESS

#### Stage Changes into the Staging Area
```bash
git add <filenames> ...<filenames>      ## Add some files
git add .                               ## Add all files
git status                              ## Check again
```

#### Commit Changes from the Staging Area to the Local Repo
```bash
git commit -m "message"
git status                              ## Check again
```

#### Push Commits from the Local Repo to GitHub

##### Push the Currently Checked-Out Branch to the Remote Repository
```bash
git push origin
```

##### Push a Specific Branch Other Than the Currently Checked-Out Branch
```bash
git push origin branch-name
```








## STASHING AND CLEANING

#### Save Uncommitted Changes and Return to a Clean State

*Temporarily store (stash) your uncommitted changes and revert your working directory to a clean state. This is useful in various scenarios, such as when you need to switch branches or pull in changes from a remote repository without committing your local changes.*

```bash
git stash
```

#### View the List of Stashes
```bash
git stash list
```

#### Apply and Remove the Top Stash

*(Applies the changes from the top stash entry and removes that entry from the stack)*
```bash
git stash pop
```



--------------------------------------------------------------------------
# ADVANCE GIT SKILS 
--------------------------------------------------------------------------


## HOW TO MERGE PREVIOUS COMMITS

#### Pull the Latest Source from the Remote Repo
```bash
git pull origin branch-name
git status
```

#### Check Commit History
```bash
git log                     ## See all previous commits
git log -n 5                ## See the last 5 commits
```

#### Merge Commits
```bash
git reset --soft HEAD~2     ## Return to the point before the last 2 commits
git status

git add .                   ## Stage changes
git commit -m "message"     ## Commit all changes
git push -f origin feature/w1_exs_basic_python   ## Push new commit (merged from the last two)
```




## ROLLING BACK TO A PREVIOUS COMMIT

#### Show Commit Log History
```bash
git log
```


#### Method 1: REVERT COMMIT - Create a New Commit that Undoes the Changes Made by

##### Create a New Commit that Reverses the Changes Made by `commit_id`
```bash
git revert commit_id
```

##### Create a New Commit that Reverses All Commits from `commit_id` to the Latest
```bash
git revert commit_id...HEAD
```


#### Method 2: RESET CHANGES

##### Option 1: Soft Reset - Resets the Commit History to the Specified Commit but Keeps the Changes in the Index and Working Directory. This is Useful if You Want to Re-Commit These Changes.
```bash
git reset --soft commit_id
```

##### Option 2: Mixed Reset - Resets the Commit History to the Specified Commit but Keeps the Changes in the Working Directory. You Can Then Commit These Changes if Desired.
```bash
git reset --mixed commit_id
```

##### Option 3: Hard Reset - Discards All Changes Made After the Specified Commit
```bash
git reset --hard commit_id
```






## VERSION TAG

#### Creating an Annotated Tag
```bash
git tag -a v1.0 -m "Version 1.0 release"
```

#### List All the Tags in Your Repository
```bash
git tag
```

#### Push Tag to Remote Repo

##### Pushing a Single Tag
```bash
git push origin v1.0
```

##### Pushing All Tags
```bash
git push origin --tags
```

#### Show Detailed Information About Each Tag
```bash
git show <tagname>
```

#### Delete a Tag

##### To Delete a Tag Locally
```bash
git tag -d v1.0
```

##### To Delete a Tag from the Remote Repository
```bash
git push origin --delete tag v1.0
```






## CREATE A PULL REQUEST ON GITHUB
Must be done on GitHub.