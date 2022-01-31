Presentations
=============

Presentation archive using [lookatme](https://github.com/d0c-s4vage/lookatme).

Setup
-----
```bash
# TODO: automate all of this...
pip3 install lookatme lookatme.contrib.grapheasy
SITE_PKGS=$(python3 -c 'import site; print(site.getsitepackages())')
cp ./themes/pygments/* $SITE_PKGS/pygments/styles/
vi $SITE_PKGS/pygments/styles/__init__.py
# append style names and classes to STYLE_MAP dictionary
brew install rust
cargo install tai
ln -s ~/.cargo/bin/tai /usr/local/bin/tai
cd plugins/lookatme.contrib.tai && pip3 install .
```
Run
---
```bash
lookatme --no-ext-warn [presentation].md             # run presentation
lookatme --no-ext-warn --live [presentation].md      # live update
```
Sources / Tools
---------------

- [lookatme](https://github.com/d0c-s4vage/lookatme) CLI presentation tool.
- [DOT Language](https://graphviz.org/doc/info/lang.html) Graph syntax supported by grapheasy plugin.
- [Sketchviz](https://sketchviz.com/new) Graphviz playground with a great into to the syntax.
- [vim2pygments](https://github.com/honza/vim2pygments) Convert vim color schemes to pygments styles.
- [Syntax-Themes](https://github.com/StylishThemes/Syntax-Themes) Collection of themes copied here.
- [Theme Viewer](https://stylishthemes.github.io/Syntax-Themes/pygments/) Theme viewer for the above Syntax-Themes.
- [Slides](https://github.com/maaslalani/slides) Successor to lookatme written in Go.
- [ASCIIFlow](https://asciiflow.com/#/) Hand draw ascii graphics.
