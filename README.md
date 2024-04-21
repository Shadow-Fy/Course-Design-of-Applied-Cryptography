# README

## 使用git进行版本管理操作

*<u>如果本文内容有误，欢迎提出问题进行修改~</u>*

如果不熟悉 git 的使用就按下面的方法操作，在本地创建自己的分支，**所有的项目操作都在自己的分支上进行**，修改完成后推送到自己的分支上，然后提（pr） pull request，**提  pr 前还需将自己本地分支和远程分支进行同步**。

==(**中括号以及中括号中的内容**需要全部替换为对应的内容)==

---

拉取GitHub仓库有两种方法，**二选一**即可：

1. 选择直接 clone 仓库（这种步骤少，此时 [remote name] 默认为 origin）：

   + 默认 clone 主分支：

     ```
     git clone [仓库地址(https)]
     ```

   + 如果需要 clone 指定分支：

     ```
     git clone -b [branch name] [仓库地址]
     ```

     

2. 选择在本地创建仓库绑定远程仓库：
   + **本地仓库初始化**：在你需要保存项目的文件夹下，打开Git Bash或是终端，然后输入如下指令，指令执行后你可以查看你的项目文件夹会多一个 .git 文件
   
     ```
     git init
     ```
   
   + 创建remote
   
     ```
     git remote add [remote name] https://github.com/mnqTEEM/project
     ```
   
   + 将GitHub仓库下拉至本地
   
     ```
     git pull --rebase [remote name] main
     ```



上述方法会将将内容下拉至本地的 master 分支，因此我们还需要对分支进行管理

---

分支管理：

+ 查看本地的所有分支：

  ~~~
  git branch
  git branch -a // 这个可以查看远程分支
  ~~~

+ 创建本地分支：

  ```
  git branch [branch name]
  ```

+ 切换到创建的新分支：

  ```
  git checkout [branch name]
  ```

+ 创建分支同时切换到创建的分支（上面两个操作合并）：

  ```
  git checkout -b [branch name]
  ```

---

在完成内容的修改后，需要进行提交执行以下操作：

+ 检查当前的所有修改：

  ~~~
  git status
  ~~~

+ 将所有修改的文件添加到暂存区：

  ```
  git add .
  ```

  注意，上述指令是将当前所有修改都加入暂存区，使用时需**确认当前的内容是否为自己需要提交的内容**，避免覆盖他人修改。

  更多内容可以查看下面的 **仓库提交常见问题**.

+ 记录本地暂存区的修改：

  ```
  git commit -m "[此次文件更改的备注]"
  ```

+ 将远程主分支的内容下拉：

  ```
  git fetch [remote name]/[main branch name]
  ```

+ 将主分支内容合并到自己分支：这里使用交互式 rebase，可以对提交进行修改 ，在后面加上了 -i

  ```
  git rebase [remote name]/[main branch name] -i
  ```

  

  关于 rebase ，一般下拉其他分支的代码来更新本地分支会使用 git pull ，git pull = git fetch + git merge ，但是 git merge 会在代码分支中引入新的提交，可能会增加代码审核人的负担，如果使用 git rebase 来合并分支，可以线性查看提交记录，并且对部分提交进行合并或者丢弃等操作，rebase 最大的好处是避免merge的交织，开发人员多起来可能导致分支历史变成蜘蛛网。具体使用哪个可以根据个人习惯或者具体情况考虑
  
  rebase的基础信息可以参考下面两个链接：
  
  https://www.bilibili.com/video/BV1Xb4y1773F
  
  [Git - 变基 (git-scm.com)](https://git-scm.com/book/zh/v2/Git-分支-变基)
  
  执行了这个指令后会进入下图类似页面，这个是使用的vim编辑器，上面是你最近的全部提交，下面是可以执行的操作
  
  ![image-20240405161941750](https://gitee.com/Shadow_Fy/images/raw/master/img/202404051619955.png)
  
  使用vim的语法；如果是将所有提交合并，除了第一个其他的pick全部改为 f ，然后保存退出
  
  ![image-20240405162023745](https://gitee.com/Shadow_Fy/images/raw/master/img/202404051620769.png)
  
+ 重命名提交备注：因为 rebase 之后是会默认用最早的 commit 的备注，所以需要重新更改备注，方便之后进行回退（同样是使用 vim 编辑器）

  ```
  git commit --amend
  ```

+ 将本地内容推送到远程：这里的 [branch name] 是你当前的分支（之前创建用于自己使用的分支），并非主分支

  ```
  git push [remote name] [branch name] -f
  ```

  这里为什么要 -f 强制推送：git reabase 操作后会使自己现在的分支树和远程的是不一样的，想直接 push 是无法推送上去的，确保自己本地的是正常且最新的，直接强制 push 到自己远程对应的分支即可，最后在 github 上提 pr 把本地分支合并到主分支，可以查看自己有哪些代码和主分支是不一样的，进行审核后合并（合并需要有这个仓库管理权限的人执行）。



## 仓库提交常见问题&解决办法

​	如果你已经能够熟练使用Git，或是已经看过上面的仓库管理方式，那么一定熟悉 git add . 这个指令。该指令所做的操作是将你当前所有的修改内容加入缓存区，但这只是少数情况。

​	大多数情况是，因为某些原因（测试性代码、引擎修改、ide配置），你并不想将所有的修改提交，此时git add . 指令就不能够满足我们的需求。当然Git也考虑了这种情况，你可以使用 git add -h 指令来查看如何只将部分代码加入缓存区。

​	如果你遇到了上诉情况，你会发现当你正确的将你需要提交的代码add 并且 commit，仍然会有部分代码是没有 commit 甚至没有 add 的，此时 git 不允许你的 rebase 操作，因此我们来看两种**解决方法**

### 解决办法一：临时Commit

发生上述情况，我们可以将所有剩余的修改加入一个临时性的commit中，来保证rebase能够正确运行

+ 将所有修改添加进缓存区

  ```
  git add .
  ```

+ 将缓存区内容记录为一个临时性Commit

  ~~~
  git commit -m "WIP"
  ~~~

结束上述操作后，你就可以继续rebase操作来保证你本地分支与主干的一致性。

但是在 push 前，必须 **将该临时Commit删除**，否则会将你的临时修改提交到GitHub仓库，删除方法如下：

+ 每个commit都有一个独立的编号，可以使用如下指令查看：

  ~~~
  git log
  ~~~



+ 找到临时commit WIP 的 **前一个 commit 的编号**，并执行如下指令进行代码回溯：

  ~~~
  git reset --soft [commit log]
  ~~~

  其中 commit log 对应为前一个 commit 的编号，--soft 后缀必须要输入，此后缀是为了告诉指令需要保存你的所有本地修改。



执行完上述所有操作，终于可以安心push了！一定要给push多加几个后缀狠狠push进去



### 解决办法二：Stash

这种方法就比较简单，确保当前所有commit都是你想要提交的，然后将所有修改存入一个脏工作区，rebase 和 push完后再取回来

+ 将当前所有未add进缓存区的修改隐藏：

  ~~~
  git stash
  ~~~

+ 在 rebase 和 push完毕后，将所有隐藏的修改回溯：

  ```
  git stash pop
  ```
