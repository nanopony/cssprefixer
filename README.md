# CSSPrefixer with console agent and Python3 support

A tool that rewrites your CSS files, adding vendor-prefixed versions of (popular) CSS3 rules.
It also can combine and minify your stylesheets.

**Keep your styles clean!**

It supports many CSS3 stuff including keyframe animations, Flexbox and gradients.

For example, this
```css
#wrapper {
    border-radius: 1em;
    transform: rotate(45deg)
}
```

becomes this:
```css
#wrapper {
    -moz-border-radius: 1em;
    -webkit-border-radius: 1em;
    border-radius: 1em;
    -o-transform: rotate(45deg);
    -moz-transform: rotate(45deg);
    -webkit-transform: rotate(45deg);
    transform: rotate(45deg)
}
```

Requires [cssutils](http://cthedot.de/cssutils/).

## How to install 
### from git
    $ sudo pip install -e git+https://github.com/nanopony/cssprefixer.git

## How to use
### Console Tool

    usage: prefixize [-h] [-m MUTE] [-o OUTPUT | -i | -s SUFFIX] filename

    positional arguments:
      filename              Input CSS file

    optional arguments:
     -h, --help
     show this help message and exit
     
     -m MUTE, --mute MUTE
     Don't check for errors
     
     -o OUTPUT, --output OUTPUT
     Specity output filename
     
     -i, --inplace
     Convert CSS in-place
     
     -s SUFFIX, --suffix SUFFIX
     Save to suffixed filename, like input main.css, suffix: processed, gives main.processed.css

### From Python
```python
from cssprefixer.engine import process
cssprefixer.process(open('my.css').read(), debug=False, minify=True)
````

## Credits

Currently maintained by Nanopony,
[Original Contributors](https://github.com/myfreeweb/cssprefixer/graphs/contributors)
