# Introduction To Robotics Aug18
This repo will hold the code assignments from the students of the 2018 Introduction to the Elements of Robotics

It is organized into folders for each student where each should contribute the assignment code to.

# Instructions

1. Create a fork of this Repository on your GitHub Account
2. Clone your fork on your computer
    `git clone https://github.com/addressofyourfork`
3. Change into the folder of the repository you just cloned
4. Add the original repository and upstream remote `git remote add upstream https://github.com/jmachuca77/IntroToRoboticsAug18.git`

# Creating a new Branch

Branches are used to develop features isolated from each other. The `master` branch is the main branch when you create a repository. Create branches to work on changes and when ready merge them back to the `master` branch.

1. To create a new branch `git checkout -b branch_name` This creates a new branch and switched to it.
2. To go back to the `master` branch, `git checkout master`
3. If you want to change to an existing branch `git checkout branch_name`
4. To delete a branch `git branch -d branch_name`
5. To upload (push) a branch to a remote repository `git push remote_name branch_name`

# Working with files Commits, pushes, etc...

When working with files on a git repository, any changes you make are tracked, but they are not automatically uploaded to the remote repository. Uploading the changes is called a **Push
**.

When you change a file the changes are tracked, so in order for git to know that you want to keep the changes you made, you have to **commit** the changes. When you commit these changes you also have the opportunity to write a message stating what the changes are for, or why they were made.

You can check what the status of your repository is by using this command `git status`. This will tell you if there are files that have changed but are not commited
