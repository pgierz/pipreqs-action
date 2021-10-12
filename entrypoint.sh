#!/bin/sh -l

echo `git pull`
pipreqs --force --no-pin --savepath $INPUT_REQUIREMENT_PATH $INPUT_PROJECT_PATH
set -e
echo $PATH
python3 --version
python3 /recreate_conda_reqs.py
sh -c "ls"

sh -c "cat $INPUT_CONDA_REQS"

sh -c "git config --global user.name '${GITHUB_ACTOR}' \
      && git config --global user.email '${GITHUB_ACTOR}@users.noreply.github.com'"
echo `git fetch && git add -A && git commit -m "Updated $INPUT_CONDA_REQS requirements file" && git push -u origin HEAD`
