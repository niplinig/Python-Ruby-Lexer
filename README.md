# BUILDING LEXER

## Install python-devel
Ubuntu
```
sudo apt install python-dev
```

Fedora
```
sudo dnf install python-devel
```

NixOS
```
nix-shell -p python311Packages.pydevtool
```

## Install pipenv

Pip
```
pip install --user pipenv
```

Ubuntu
```
sudo apt install pipenv
```

Fedora
```
sudo dnf install pipenv
```

## Install dependencies

```
pipenv install -e .
```

## Start developing

Use the shell
```
pipenv shell
```

## Using CLI

Commands
- -d --data
- -lf --lex_files
- -s --shell
- -yf --yac_files


```
./cli.py -d "data to analyse with lexer"
```

```
./cli.py -lf "file path"
```
