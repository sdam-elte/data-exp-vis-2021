In case you want to have larger fonts, or wider cell size etc. You can use
``` from IPython.core.display import display, HTML```

With the `HTML` function you can insert extra styles or modifications into the already displayed html file you are working in. 
What you need to know is the *html tag* and *class* of which property you want to modify.
For example in Firefox if you rightclick on a text, choose *Inspect Element* in the and in the inspector tab it will show you the html code.

Let's say you want to make the cells wider! For that we need to modify the `.container` class, and we insert 
```display(HTML("<style>.container { width:100% !important; }</style>"))```
into a code cell and run it.

If we have slides and we want to increase the size of the fonts we do:
```display(HTML("<style>.rendered_html { font-size: 150% !important; }</style>")) ```

``` 
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

```
