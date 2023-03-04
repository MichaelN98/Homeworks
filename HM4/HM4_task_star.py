
html = [('google', 'www.google.com', 'Google'), ('facebook', 'http://facebook.com/dign-in', ' Facebook'), ('amazon', 'amazon.com', 'Amazon')]

import re


text = """<div id="google", "www.google.com">Google</div>
<div id="facebook", "http://facebook.com/dign-in">Facebook</div>
<div id="amazon", "amazon.com">Amazon</div>
"""

print(re.findall(r"div id=\"(.+)\">(.+)<", text))


