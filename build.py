def main():
	print("Initializing site...")
	for page in pages:
		generate_template(page)
		construct_page(page)
	print("Site built")
def generate_template(single_page):
	print("Generating", single_page['title'], "template...")
	filename = single_page['filename']
	template = open('./templates/base.html').read()	
	return template

def construct_page(single_page):
	print("Constructing", single_page['title'], "page...")
	template = generate_template(single_page)
	filename = single_page['filename']
	output = single_page['output']
	content = open(filename).read()
	image_display = single_page['image_display']
	if image_display == 'half':
		combined_page = template.replace('{{view}}', '50%').replace('{{content_halfpage}}', content).replace('{{content_fullpage}}','')
	else:
		combined_page = template.replace('{{view}}', '100%').replace('{{content_fullpage}}', content).replace('{{content_halfpage}}','')
	
	open(output, 'w+').write(combined_page)

pages = [	
	{
		'filename': './content/index.html',
		'output': './docs/index.html',
		'title': 'Patrick Ware',
		'image_display': 'full'
	},
	{
		'filename': './content/aboutme.html',
		'output': './docs/aboutme.html',
		'title': 'About Me',
		'image_display': 'half'
	},
	{
		'filename': './content/resume.html',
		'output': './docs/resume.html',
		'title': 'Resume',
		'image_display': 'half'
	},
	{
		'filename':'./content/contact.html',
		'output': './docs/contact.html',
		'title':'Contact',
		'image_display': 'full'
	}
]
	
if __name__ == "__main__":
	main()


