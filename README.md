# Introduction To Robotics Aug18
This repo will hold the code assignments from the students of the 2018 Introduction to the Elements of Robotics

It is organized into folders for each student where each should contribute the assignment code to.

# Instructions

1. Create a fork of this Repository on your GitHub Account
2. Clone your fork on your computer
    `git clone https://github.com/addressofyourfork`
3. Change into the folder of the repository you just cloned
4. Add the original repository and upstream remote `git remote add upstream https://github.com/jmachuca77/IntroToRoboticsAug18.git`
5. Create a branch so you can work on the files (we will learn what this is later) `git checkout -b GitTutorialStudentID` (use your **own** Student ID)

# Creating a new Branch

Branches are used to develop features isolated from each other. The `master` branch is the main branch when you create a repository. Create branches to work on changes and when ready merge them back to the `master` branch. The following are useful commands when working with branches.

1. To create a new branch `git checkout -b branch_name` This creates a new branch and switched to it.
2. To go back to the `master` branch, `git checkout master`
3. If you want to change to an existing branch `git checkout branch_name`
4. To delete a branch `git branch -d branch_name`
5. To upload (push) a new branch and set your local branch to track it `git push --set-upstream remote_name branch_name`
6. To upload (push) a branch to a remote repository `git push remote_name branch_name`
7. To check what branch you are currently working on `git branch`

# Working with files Commits, pushes, etc...

When working with files on a git repository, any changes you make are tracked, but they are not automatically uploaded to the remote repository. Uploading the changes is called a **push**.

When you change a file the changes are tracked, so in order for git to know that you want to keep the changes you made, you have to **commit** the changes. When you commit these changes you also have the opportunity to write a message stating what the changes are for, or why they were made.

You can check what the status of your repository is by using this command `git status`. This will tell you if your folder is in sync with the remote repository:

```
On branch GitTutorial
Your branch is up to date with 'origin/GitTutorial'.

nothing to commit, working tree clean
```

Or if there are changes to the files but that have not yet been commited:

```
On branch GitTutorial
Your branch is up to date with 'origin/GitTutorial'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

In the example above the file `README.md` has been changed but the changes have not been commited. To commit the chages we have to **stage** the files to commit first. Since a commit can contain multiple files you need to tell git which files are the ones you want to **commit**, this is what staging means. To stege the files you **add** them to the commit like this:

`git add README.md`

Once you add the files and check the status again you will see that git now tells you there are files waiting to be commited:

```
On branch GitTutorial
Your branch is up to date with 'origin/GitTutorial'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   README.md
```

You are now ready to commit the files, this will add (save the changes) them to your local repository. When you do this it is good practice to write a note of what you changed and why:

```
git commit -m 'Added branch creation instructions'
```

In the above example the **-m** is used to append the message text. If you don't use that, then after using the `git commit` command, a text editor will open. In this case **vim** will most likely open, here you have to input the text you want to add to the commit. For more information on how to use **vim** you can follow this tutorial https://www.openvim.com.

You will see a similar output to this:
```
[GitTutorial 12de098] Added branch creation instructions
 1 file changed, 106 insertions(+), 1 deletion(-)
```

Once your changes are commited on your local repository then you have the option of pushing the changes to your remote GitHub repository. If we check the status now you will see the following:

```
On branch GitTutorial
Your branch is ahead of 'origin/GitTutorial' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

So now lets go ahead and **push** our changes with the following command `git push`

you should see something like this:

```
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 474 bytes | 474.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/jmachuca77/IntroToRoboticsAug18.git
   12de098..ed4b7cf  GitTutorial -> GitTutorial
```

This means that your changes have been pushed to the remote Repository. Check the status now and you will see that your local repository is up to date with the remote.

```
On branch GitTutorial
Your branch is up to date with 'origin/GitTutorial'.

nothing to commit, working tree clean
```

# Creating a Pull Request

You now have changed some files and uploaded them to your remote repository. In order to contribute your changes back to the class repository you have to create what is called a **pull request**. You will do this on the GitHub web page.

Access your account on github and go to your fork of the class repository. There you will see a button that allows you to create a pull request:

![Alt text](SupportFiles/pullrequest1.png?raw=true "PullRequest1")

Then you have to again write a name for the pull request and a description of what you did, and why you want it included in the repository you are making the pull request to.

![Alt text](SupportFiles/pullrequest2.png?raw=true "PullRequest2")

Thats it you have now created a pull request and it is now up to the maintainer of the repostory to **merge** your changes into it.

![Alt text](SupportFiles/pullrequest3.png?raw=true "PullRequest3")
