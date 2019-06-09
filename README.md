# markdown_to_slides-dot-com_html

A python script that convert a release.js Markdown slide to html. Useful transfer your slides from markdown to the import 
utility of Slides.com (which don't support markdown import from urls )

## Usage

> python3 import_to_slides.com.py <your markdown file>

Then copy the all the output after "RESULT : " from the terminal.

If you prefer to ouptput to a file directly.

> python3 import_to_slides.com.py <your markdown file> 2</dev/null > index.html 

## Example

**INPUT markdown file content : **
```markdown
# Markdown for slides

###### *Powered with reveal.js*



# One more slide


# A vertical one



# And for proof of concept

## An other one
```
**OUTPUT in html : **
```html
<!doctype html>
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
			<div class="slides">
			
			<section data-markdown>
				<textarea data-template>
				# Markdown for slides
				
				###### *Powered with reveal.js*
			
				</textarea>
			</section>
			<section>	
				<section data-markdown>
					<textarea data-template>
					# One more slide
				
					</textarea>
				</section>
				
				<section data-markdown>
					<textarea data-template>
					# A vertical one
				
					</textarea>
				</section>
			</section> 
			<section data-markdown>
				<textarea data-template>
				# And for proof of concept
				
				## An other one
			
				</textarea>
			</section>


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
</html>
```