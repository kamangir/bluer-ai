title:::

```bash
# change shell to bash
chsh -s /bin/bash

mkdir git
cd git
git clone git@github.com:kamangir/bluer-ai.git
cd bluer-ai

python3 -m venv ~/venv/bluer_ai
source ~/venv/bluer_ai/bin/activate

pip3 install -e .

nano ~/.bash_profile
# add "source $HOME/git/bluer-ai/bluer_ai/.abcli/bluer_ai.sh"
# restart the terminal
```