# arXiv Renamer

This package has a utility called `arxiv-renamer` that can be used to rename `pdf` files downloaded from [arXiv](https://arxiv.org).
It creates a slug of the form `<id>-<authors>-<title>` and renames the original file to that slug.

Another utility called `arxiv-watcher` can be used to watch for new (or moved) files in a directory and rename them.

## Installation

```bash
pip install arxiv_rename
```
## Usage

```bash
    usage: arxiv_rename [-h] [-w] PATH

    Rename PDFs downloaded from arXiv.org

    positional arguments:
    PATH         path to arXiv PDF or a folder of arXiv PDFs

    optional arguments:
    -h, --help   show this help message and exit
    -w, --watch  watch for new files in the folder specified by PATH
```
