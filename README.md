# Skupper install script

[![main](https://github.com/skupperproject/skupper-install-script/actions/workflows/main.yaml/badge.svg)](https://github.com/skupperproject/skupper-install-script/actions/workflows/main.yaml)

## Install the Skupper command

~~~ shell
curl https://raw.githubusercontent.com/skupperproject/skupper-install-script/main/install.sh | sh
~~~

## Uninstall the Skupper command

~~~ shell
curl https://raw.githubusercontent.com/skupperproject/skupper-install-script/main/uninstall.sh | sh
~~~

## More

~~~ shell
curl https://raw.githubusercontent.com/skupperproject/skupper-install-script/main/install.sh | bash -s -- main
~~~

~~~ shell
install.sh [opts] [version]
install.sh latest
install.sh main
install.sh 1.4.4
~~~

~~~ shell
install.sh --verbose --scheme home --version main --interactive
install.sh latest
install.sh main
install.sh 1.4.4
~~~
