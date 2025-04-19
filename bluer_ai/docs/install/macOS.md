# macOS

```bash
# change shell to bash
chsh -s /bin/bash

mkdir git
cd git
git clone git@github.com:kamangir/bluer-ai.git

nano ~/.bash_profile
# add "source $HOME/git/bluer-ai/bluer_ai/.abcli/bluer_ai.sh"
# restart the terminal

cd ~/Downloads
curl -o Miniconda3-latest-MacOSX-x86_64.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash ./Miniconda3-latest-MacOSX-x86_64.sh

git config --global user.name kamangir
git config --global user.email arash@kamangir.net
```