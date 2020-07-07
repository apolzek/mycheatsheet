
### Git(github/gitlab)

```
git config --global user.name "Sam Smith"
git config --global user.email sam@example.com
git config --global http.proxy http://proxyUsername:proxyPassword@proxy.server.com:port

# First steps
git init
git add README.md
git commit -m "first commit"
git remote add origin https:/<URL>
git push -u origin master

# Check ssh connection
ssh -vT git@github.com
git remote -v
git remote set-url --add origin  https://<URL>

git checkout -b <branchname>
git branch -d <branchname>
git merge <branchname>
git diff <sourcebranch> <targetbranch>
git tag 1.0.0 <commitID>
git log
```

* Undo changes without confirming anything yet

```
git checkout -- . # Reverse all changes to files that were versioned
git clean -f -d # Delete all created files and directories
git reset HEAD . # If you add files to the index (using git add)
# Revert changes to modified files.
git reset --hard
# Remove all untracked files and directories.
# '-f' is force, '-d' is remove directories.
git clean -fd
git reset --hard origin/master

```
* Renaming Git Branch

```
git checkout <old_name>
git branch -m <new_name>
git push origin -u <new_name>
git push origin --delete <old_name>
```
