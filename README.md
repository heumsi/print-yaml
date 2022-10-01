# print-yaml

print-yaml is a CLI tool that prints yaml files according to the desired depth.

## Installation

```
# using pip
$ pip install print_yaml

# using poetry
$ poetry add print_yaml
```

## Usage

Let's say you have the following yaml file.

```yaml
# data.yaml

a:
  b: 1
  c:
    - one
    - two
    - three:
        A: 6
        B: 7
    - four:
        - 8
        - 9
  d:
    e: 3
    f: 4
g: 5
```

### Basic

The following values can be obtained using `print_yaml`

```bash
$ print_yaml data.yaml -d 1

a: 
g: 
```


```bash
$ print_yaml data.yaml -d 2

a:
  b: 
  c: 
  d: 
g: 5
```

```bash
$ print_yaml data.yaml -d 3

a:
  b: 1
  c:
  - one
  - two
  - three: 
  - four: 
  d:
    e: 
    f: 
g: 5
```

### With value

By default, only the "key" in the yaml file is output.  
If you add the `--value` or `-v` option, it also outputs a single value.

```bash
$ print_yaml data.yaml -d 1 -v

a: 
g: 5
```

```bash
$ print_yaml data.yaml -d 2 -v
a:
  b: 1
  c: 
  d: 
g: 5
```

```bash
$ print_yaml data.yaml -d 3 -v
a:
  b: 1
  c:
  - one
  - two
  - three: 
  - four: 
  d:
    e: 3
    f: 4
g: 5
```

### All Commands

```bash
$ print_yaml --help
                                                                                                             
 Usage: print_yaml [OPTIONS] FILE_PATH                                                                       
                                                                                                             
╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    file_path      TEXT  [default: None] [required]                                                      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────╮
│                       -d      INTEGER RANGE [x>=0]  [default: 0]                                          │
│ --value               -v                                                                                  │
│ --install-completion                                Install completion for the current shell.             │
│ --show-completion                                   Show completion for the current shell, to copy it or  │
│                                                     customize the installation.                           │
│ --help                                              Show this message and exit.                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
