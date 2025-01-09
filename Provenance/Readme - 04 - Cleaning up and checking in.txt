[Narrative:]
Replace: </*b>
with nothing

Replace: <span class="Apple-converted-space">\s*</span>
with space

Noticed that the narrative in Competencies used Tahoma where the rest of the resume uses Helvetica.
Ditched Tahoma.

Cloned $CASAREPO/buducocv and merged it with the files in Source Control Basis
The repo already had a "cv" directory at the top level. It only contains files from the cv directory and is therefore non-working as there will be missing references to ../img and ../lib.
The source basis files contain 3 top level directories, "web", "data", and "artifacts"

[Installed GitHub CLI (gh)]
%  brew install gh
==> Auto-updating Homebrew...
Adjust how often this is run with HOMEBREW_AUTO_UPDATE_SECS or disable with
HOMEBREW_NO_AUTO_UPDATE. Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
ansible@10         cmake-lint         eslint_d           gci                havn               mergiraf           xcresultparser
==> New Casks
beyond-compare@4                 font-departure-mono-nerd-font    last-window-quits                teleport
djstudio                         font-maple-mono-nf               pixpin                           testfully

You have 6 outdated formulae installed.

==> Downloading https://ghcr.io/v2/homebrew/core/gh/manifests/2.62.0
############################################################################################################################## 100.0%
==> Fetching gh
==> Downloading https://ghcr.io/v2/homebrew/core/gh/blobs/sha256:239c26cefbc6c61ba5918191ec8aca05aaf9ed6d2198dccd4cbcebe3b4980d31
############################################################################################################################## 100.0%
==> Pouring gh--2.62.0.arm64_sequoia.bottle.tar.gz
==> Caveats
zsh completions have been installed to:
  /opt/homebrew/share/zsh/site-functions
==> Summary
🍺  /opt/homebrew/Cellar/gh/2.62.0: 207 files, 41.3MB
==> Running `brew cleanup gh`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).


[Authenticated GitHub CLI]
With several missteps. I didn't realize the device code it was asking for was the one it had printed on the console. I checked all my devices for notifications and tried a few times.

Last login: Wed Nov 20 23:51:51 on ttys015
(base) [24-11-20 23:52:56]   ~ %  cd "/Users/arizonaedwards/data/Projects/resume-basis-workshop/Source controlled basis/buducocv"
(base) [24-11-20 23:53:08]   buducocv %  git:(main) which -a gh
/opt/homebrew/bin/gh
(base) [24-11-20 23:53:18]   buducocv %  git:(main) gh repo create
To get started with GitHub CLI, please run:  gh auth login
Alternatively, populate the GH_TOKEN environment variable with a GitHub API authentication token.
(base) [24-11-20 23:56:33]   ?4 buducocv %  git:(main) gh auth login
? Where do you use GitHub? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: 308B-25D8
Press Enter to open https://github.com/login/device in your browser...
failed to authenticate via web browser: This 'device_code' has expired. (expired_token)
(base) [24-11-21 0:12:05]   ?1 buducocv %  git:(main) gh auth login
? Where do you use GitHub? GitHub.com
? What is your preferred protocol for Git operations on this host? arizonace  [Use arrows to move, type to filter]

(base) [24-11-21 0:31:50]   ?2 buducocv %  git:(main) gh auth login
? Where do you use GitHub? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: 5445-EFAD
Press Enter to open https://github.com/login/device in your browser...

✓ Authentication complete.
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as arizonace
(base) [24-11-21 0:36:11]   buducocv %  git:(main)
(base) [24-11-21 0:36:11]   buducocv %  git:(main)

[Pushed buducocv to GitHub]
[24-11-21 0:36:11]   buducocv %  git:(main) gh repo create
? What would you like to do? Push an existing local repository to GitHub
? Path to local repository .
? Repository name buducocv
? Repository owner arizonace
? Description Data driven, source-controlled resume.
? Visibility Public
✓ Created repository arizonace/buducocv on GitHub
  https://github.com/arizonace/buducocv
? Add a remote? Yes
? What should the new remote be called? github
✓ Added remote https://github.com/arizonace/buducocv.git
? Would you like to push commits from the current branch to "github"? Yes
Enumerating objects: 71, done.
Counting objects: 100% (71/71), done.
Delta compression using up to 12 threads
Compressing objects: 100% (62/62), done.
Writing objects: 100% (71/71), 1.71 MiB | 1.90 MiB/s, done.
Total 71 (delta 21), reused 19 (delta 4), pack-reused 0
remote: Resolving deltas: 100% (21/21), done.
To https://github.com/arizonace/buducocv.git
 * [new branch]      HEAD -> main
branch 'main' set up to track 'github/main'.
✓ Pushed commits to https://github.com/arizonace/buducocv.git

[GitHub Basis-2024]
This is the basis of the data-driven, source-controlled resume repository. All data derived from the 2016 resume is checked in and any initial files checked into the repo before the basis have been either incorporated into the basis or deleted.
The contents of web, particularly web/cv/welcome.html should function almost exactly* as it did in 2016. The data has not yet been used to produce anything.
* There are already some changes to welcome.html (particularly the Competencies table) that are included in the change history.

[Future]
Track further changes on Repos
https://github.com/arizonace/buducocv
$CASAREPO/buducocv
