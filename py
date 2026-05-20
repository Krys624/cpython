cd cpython
git remote add upstream https://github.com/python/cpython
git config --local branch.main.remote upstream
git remote set-url --push upstream git@github.com:<your-username>/cpython.git
git remote -v
git config branch.main.remote
