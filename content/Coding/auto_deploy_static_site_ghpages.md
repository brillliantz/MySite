---
title: "Blog generator"
date: 2018-09-22
draft: false
---

## Static sites v.s. Dynamic ones
difference

### why I choose static ones


## static sites generator ranking
ref

## why I choose Pelican

## gh-pages of project site
from `/doc` folder or from a separate branch? the former is messy when commit and push.

ref:
- [User, Organization, and Project Pages](https://help.github.com/articles/user-organization-and-project-pages/#project-pages)
- [Creating Project Pages using the command line](https://help.github.com/articles/creating-project-pages-using-the-command-line/)
- [Configuring a publishing source for GitHub Pages](https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/)

### orphan branch and remove files


## `ghp-import`'s job

## `Makefile` in Pelican
- `make publish`
- `make github`

## Continuous Integration for deployment
[extact match](http://shaunagordon.com/blog/2016/01/13/pelican-travis-and-github/)

### requirements list
#### Pelican main
ghp-import==0.5.4
Markdown==2.6.8
pelican>=3.7.1

#### plugin `ipynb.markup`
jupyter>=1.0
ipython>=4.0
nbconvert>=4.0
beautifulsoup4

#### plugin `extract_toc`
beautifulsoup4

#### plugin `tipue_search`
beautifulsoup4

#### other dependency known from Travis CI log
- six (required by [simplegeneric], but [simplegeneric] doesn't mark this, which will cause error)


## test
- gh-pages branch for project site test: just use the tutorial given by GitHub
- make publish for Pelican test: manually do it. must use a different command in `Makefile`

