# git branch & merge

```bash
student@DESKTOP MINGW64 ~
$ cd Desktop/

student@DESKTOP MINGW64 ~/Desktop
$ mkdir git-test

student@DESKTOP MINGW64 ~/Desktop
$ cd git-test/

student@DESKTOP MINGW64 ~/Desktop/git-test
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/git-test/.git/

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ vi s1.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        s1.txt

nothing added to commit but untracked files present (use "git add" to track)

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git add s1.txt
warning: LF will be replaced by CRLF in s1.txt.
The file will have its original line endings in your working directory

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   s1.txt


student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git commit -m "11"
[master (root-commit) 3514de9] 11
 1 file changed, 1 insertion(+)
 create mode 100644 s1.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log
commit 3514de9c37d315abec18a8c0316e252766812ed1 (HEAD -> master)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:29:04 2019 +0900

    11

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ vi s1.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   s1.txt

no changes added to commit (use "git add" and/or "git commit -a")

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git add s1.txt
warning: LF will be replaced by CRLF in s1.txt.
The file will have its original line endings in your working directory

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git commit -m "22"
[master a4353d1] 22
 1 file changed, 1 insertion(+), 1 deletion(-)

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log
commit a4353d1546893e7cd3d9ac6ea56679c966078cfe (HEAD -> master)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:30:05 2019 +0900

    22

commit 3514de9c37d315abec18a8c0316e252766812ed1
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:29:04 2019 +0900

    11

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git branch
* master

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git branch dev

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git branch
  dev
* master

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git checkout dev
Switched to branch 'dev'

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ ls
s1.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ cat s1.txt
ab

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ vi s1.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ git add s1.txt
warning: LF will be replaced by CRLF in s1.txt.
The file will have its original line endings in your working directory

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ git commit -m "33"
[dev 9d3e9b8] 33
 1 file changed, 3 insertions(+), 1 deletion(-)

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ git log
commit 9d3e9b80bdfa85be12a1294186613e58b2c7f6d4 (HEAD -> dev)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:32:31 2019 +0900

    33

commit a4353d1546893e7cd3d9ac6ea56679c966078cfe (master)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:30:05 2019 +0900

    22

commit 3514de9c37d315abec18a8c0316e252766812ed1
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:29:04 2019 +0900

    11

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ vi s2.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ git status
On branch dev
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        s2.txt

nothing added to commit but untracked files present (use "git add" to track)

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ git add .
warning: LF will be replaced by CRLF in s2.txt.
The file will have its original line endings in your working directory

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ git commit -m "44"
[dev bc8a9b8] 44
 1 file changed, 1 insertion(+)
 create mode 100644 s2.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ git log
commit bc8a9b80d44224149d099adee5623bda9ef1183b (HEAD -> dev)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:34:33 2019 +0900

    44

commit 9d3e9b80bdfa85be12a1294186613e58b2c7f6d4
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:32:31 2019 +0900

    33

commit a4353d1546893e7cd3d9ac6ea56679c966078cfe (master)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:30:05 2019 +0900

    22

commit 3514de9c37d315abec18a8c0316e252766812ed1
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:29:04 2019 +0900

    11

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ git checkout master
Switched to branch 'master'

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log
commit a4353d1546893e7cd3d9ac6ea56679c966078cfe (HEAD -> master)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:30:05 2019 +0900

    22

commit 3514de9c37d315abec18a8c0316e252766812ed1
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:29:04 2019 +0900

    11

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log --branchs
fatal: unrecognized argument: --branchs

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log --branches
commit bc8a9b80d44224149d099adee5623bda9ef1183b (dev)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:34:33 2019 +0900

    44

commit 9d3e9b80bdfa85be12a1294186613e58b2c7f6d4
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:32:31 2019 +0900

    33

commit a4353d1546893e7cd3d9ac6ea56679c966078cfe (HEAD -> master)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:30:05 2019 +0900

    22

commit 3514de9c37d315abec18a8c0316e252766812ed1
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:29:04 2019 +0900

    11

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log --branches --graph
* commit bc8a9b80d44224149d099adee5623bda9ef1183b (dev)
| Author: woonji913 <johnnyboy0913@gmail.com>
| Date:   Tue May 14 10:34:33 2019 +0900
|
|     44
|
* commit 9d3e9b80bdfa85be12a1294186613e58b2c7f6d4
| Author: woonji913 <johnnyboy0913@gmail.com>
| Date:   Tue May 14 10:32:31 2019 +0900
|
|     33
|
* commit a4353d1546893e7cd3d9ac6ea56679c966078cfe (HEAD -> master)
| Author: woonji913 <johnnyboy0913@gmail.com>
| Date:   Tue May 14 10:30:05 2019 +0900
|
|     22
|
* commit 3514de9c37d315abec18a8c0316e252766812ed1
  Author: woonji913 <johnnyboy0913@gmail.com>
  Date:   Tue May 14 10:29:04 2019 +0900

      11

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log --branches --graph --oneline
* bc8a9b8 (dev) 44
* 9d3e9b8 33
* a4353d1 (HEAD -> master) 22
* 3514de9 11

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ vi s3.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git add .
warning: LF will be replaced by CRLF in s3.txt.
The file will have its original line endings in your working directory

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git commit -m "55"
[master 513d326] 55
 1 file changed, 1 insertion(+)
 create mode 100644 s3.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log --branches --graph --decorate --oneline
* 513d326 (HEAD -> master) 55
| * bc8a9b8 (dev) 44
| * 9d3e9b8 33
|/
* a4353d1 22
* 3514de9 11

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log master ..dev
commit bc8a9b80d44224149d099adee5623bda9ef1183b (dev)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:34:33 2019 +0900

    44

commit 9d3e9b80bdfa85be12a1294186613e58b2c7f6d4
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:32:31 2019 +0900

    33

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log dev ..master
commit bc8a9b80d44224149d099adee5623bda9ef1183b (dev)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:34:33 2019 +0900

    44

commit 9d3e9b80bdfa85be12a1294186613e58b2c7f6d4
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:32:31 2019 +0900

    33

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log -p master..dev
commit bc8a9b80d44224149d099adee5623bda9ef1183b (dev)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:34:33 2019 +0900

    44

diff --git a/s2.txt b/s2.txt
new file mode 100644
index 0000000..7898192
--- /dev/null
+++ b/s2.txt
@@ -0,0 +1 @@
+a

commit 9d3e9b80bdfa85be12a1294186613e58b2c7f6d4
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:32:31 2019 +0900

    33

diff --git a/s1.txt b/s1.txt
index 81bf396..de98044 100644
--- a/s1.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log dev..master
commit 513d3268d00981f47dd14f3d3026fe17d39178b5 (HEAD -> master)
Author: woonji913 <johnnyboy0913@gmail.com>
Date:   Tue May 14 10:40:52 2019 +0900

    55

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git merge dev
Merge made by the 'recursive' strategy.
 s1.txt | 4 +++-
 s2.txt | 1 +
 2 files changed, 4 insertions(+), 1 deletion(-)
 create mode 100644 s2.txt

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log --branches --graph --decorate --oneline
*   67a5005 (HEAD -> master) Merge branch 'dev'
|\
| * bc8a9b8 (dev) 44
| * 9d3e9b8 33
* | 513d326 55
|/
* a4353d1 22
* 3514de9 11

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git checkout dev
Switched to branch 'dev'

student@DESKTOP MINGW64 ~/Desktop/git-test (dev)
$ git checkout master
Switched to branch 'master'

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log --branches --graph --decorate --oneline
*   67a5005 (HEAD -> master) Merge branch 'dev'
|\
| * bc8a9b8 (dev) 44
| * 9d3e9b8 33
* | 513d326 55
|/
* a4353d1 22
* 3514de9 11

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git branch -d dev
Deleted branch dev (was bc8a9b8).

student@DESKTOP MINGW64 ~/Desktop/git-test (master)
$ git log --branches --graph --decorate --oneline
*   67a5005 (HEAD -> master) Merge branch 'dev'
|\
| * bc8a9b8 44
| * 9d3e9b8 33
* | 513d326 55
|/
* a4353d1 22
* 3514de9 11

```

