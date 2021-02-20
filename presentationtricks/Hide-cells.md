```
from IPython.display import HTML
import IPython.core.display as di
from IPython.display import display
from IPython.display import Markdown as md
import warnings
warnings.filterwarnings('ignore')

display(HTML("<style>.container { width:90% !important; }</style>"))
di.display_html('<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>', raw=True)

HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
    "}
    "</style>
    """
    )
```

