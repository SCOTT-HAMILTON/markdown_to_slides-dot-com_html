#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
	exit()

import re

def split_regex(regex, content, flags=0):
	table = []
	indexes = [ (m.start(0), m.end(0)-m.start(0)) for m in re.finditer(regex, content, flags)]
	end=0
	j=0
	for i in range(0,len(indexes)):
		j=i
		start = 0
		end = indexes[i][0]
		if i>0:
			start = indexes[i-1][0]+indexes[i-1][1]
		table.append(content[start:end])
	if len(indexes)==0:
		table.append(content)
	elif end < len(content)-indexes[j][1]:
		table.append(content[end+indexes[j][1]:])

	return table

def tabulify_string(str, nth=1):
	lines = split_regex(r'(\r\n|\n)', str, re.M|re.I|re.MULTILINE)
	tab = '\t'*nth
	return ''.join( [tab + line + "\n" for line in lines ] )

def try_to_solo_slide_html(slide):
	html = ""
	if len(slide) > 1:
		return html
	solo_slide = (
"""<section data-markdown>
	<textarea data-template>\n""",
"""\r\n\t</textarea>
</section>""")
	
	html+='\n'
	html+=solo_slide[0]
	html+=tabulify_string(slide[0])
	html+=solo_slide[1]
	return html

def SlideTable_to_html(slides):
	html = ""
	verticals_slides = ("""<section>""",
						"""</section> """)
	for slide in slides:
		str = try_to_solo_slide_html(slide)
		if str != "":
			html += str
		else:
			html+='\n'
			html+=verticals_slides[0]
			tmp=""
			for s in slide:
				s = [s]
				str2 = try_to_solo_slide_html(s)
				if str2 != "":
					tmp += str2
					tmp += '\n'
			html+=tabulify_string(tmp)
			html+=verticals_slides[1]
	return html

regex_slides_separator = r'(\r\n|\n)(\r\n|\n)(\r\n|\n)(\r\n|\n)'
regex_slides_vertical_separator = r'(\r\n|\n)(\r\n|\n)(\r\n|\n)'

slides = []
final_slides = []
html_text = ""


print("major slides : ", file=sys.stderr)
with open(sys.argv[1], 'r') as file:
	content = ''.join(file.readlines())
	slides = split_regex(regex_slides_separator, content)
	print(slides, file=sys.stderr)
print("\nmajor slides verticals : ", file=sys.stderr)
for slide in slides:
	vert_slides = split_regex(regex_slides_vertical_separator, slide)
	print(vert_slides, file=sys.stderr)
	final_slides.append(vert_slides)

print("RESULT : \n", file=sys.stderr)

snippet = SlideTable_to_html(final_slides)
for tabslides in final_slides:
	print(tabslides, file=sys.stderr) 
print(snippet, file=sys.stderr)
index_html = (
"""<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

		<title>Heinrich Schliemann</title>

		<link rel="stylesheet" href="css/reset.css">
		<link rel="stylesheet" href="css/reveal.css">
		<link rel="stylesheet" href="css/theme/black.css">

		<!-- Theme used for syntax highlighting of code -->
		<link rel="stylesheet" href="lib/css/monokai.css">

		<!-- Printing and PDF exports -->
		<script>
			var link = document.createElement( 'link' );
			link.rel = 'stylesheet';
			link.type = 'text/css';
			link.href = window.location.search.match( /print-pdf/gi ) ? 'css/print/pdf.css' : 'css/print/paper.css';
			document.getElementsByTagName( 'head' )[0].appendChild( link );
		</script>
	</head>
	<body>
		<div class="reveal">
			<div class="slides">""","""
			</div>
		</div>

		<script src="js/reveal.js"></script>

		<script>
			// More info about config & dependencies:
			// - https://github.com/hakimel/reveal.js#configuration
			// - https://github.com/hakimel/reveal.js#dependencies
			Reveal.initialize({
				dependencies: [
					{ src: 'plugin/markdown/marked.js' },
					{ src: 'plugin/markdown/markdown.js' },
					{ src: 'plugin/notes/notes.js', async: true },
					{ src: 'plugin/highlight/highlight.js', async: true }
				]
			});
		</script>
	</body>
</html>""")


snippet = tabulify_string(snippet, 3)
final_result = index_html[0]
final_result += '\n'
final_result += snippet
final_result += '\n'
final_result += index_html[1]

print(final_result)

