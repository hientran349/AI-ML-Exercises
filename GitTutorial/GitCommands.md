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
#### Fetch changes for all branches
git fetch --all

#### Show all branches
git branch -a

#### Check out remote branch
git checkout -b branch-name origin/branch-name


#### Create a Branch & Push Develop Branch to GitHub
```bash
git checkout -b develop
Note: any uncommitted changes in your working directory will be carried over to the new branch

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
Note: any uncommitted changes in your working directory may not be carried over to the new branch
```

#### Create a new branch from a specific commit
Save the state of the repository at commit_id in a new branch for recovery or further development (but does not switch to this new branch)
`git branch new-branch commit_id`

Note: You must switch to the new branch with `git checkout new-branch` if you would like to work on it.


##### Delete a Branch
```bash
git branch -d branch-to-delete          
git push origin --delete branch-name
```







##### Detached HEAD:  BE CAREFUL !!!
If you see a message indicating you're in a detached HEAD state or your prompt shows something like `HEAD detached at <commit-id>`, you are not on a branch.
`git status`
`HEAD detached at <commit-id>`

When you are in a detached HEAD state, your commits are not associated with any branch, but rather on a specific commit. This means that while the commit exists in your repository, it's not part of any branch, so when you switch branches, the changes aren't there


###### REASONS

A detached HEAD state occurs when you check out a commit, tag, or remote branch directly, instead of a local branch. In this state, HEAD points directly to a specific commit rather than a branch

- You checked out a commit or tag
`git checkout <commit-id>`
`git checkout <tag-name>`
This points HEAD directly to the specified commit/ TAG.

- You checked out a remote branch as a detached HEAD
`git checkout origin/<branch-name>`
This checks out the remote branch as a detached HEAD, not a local branch tracking the remote branch

###### HOW TO AVOID THIS ISSUE:

1. Option 1: Create and checkout a Local Branch, then push it to remote repo
`git checkout -b my-branch`
`git push origin my-branch`

2. Option 2: When checking out a remote branch, create a local tracking branch
`git checkout -b branch-name origin/branch-name`





###### HOW TO FIX THE **Detached HEAD** ISSUE:

1. Commit Your Changes in Detached HEAD State [Optional step to be sure]
`git add .`
`git commit -m "Your commit message"`

2. Create a New Temporary Branch:
To ensure your work is not lost, create a new branch from your current detached HEAD state. This will associate your current state including recent changes with a branch name.
`git checkout -b temporary-branch`
Replace `temporary-branch` with a name that makes sense for your work.

3. Switch Back to Your Desired Branch:
`git checkout branch-name`

4. Merge the changes from temporary-branch
`git merge temp-branch`

5. Push the merged changes to the remote repository
`git push origin branch-name`


*** NOTE: If you already lost your files**, you can get it back from your lastest commit of the detached HEAD state:
`git branch recovery-branch last_commit_id`

Then continue from step 3 above !








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
base: branch to be imported
