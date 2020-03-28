def main():
	print("Initializing site...")
	for page in pages:
		generate_template(page)
		construct_page()
		write_page()

def generate_template(page):
	print("Gererating", page['title'], "template...")
	filename = page['filename']
	image_display = page['image_display']
	content = open(filename).read()
	template = open('./templates/base.html').read()
	return template

def construct_page():
	print("Constructing page...")
	template = generate_template(page)
	if image_display == 'half':
		combined_page = template.replace('{{view}}', '50%').replace('{{content_halfpage}}', content).replace('{{content_fullpage}}','')
	else:
		combined_page = template.replace('{{view}}', '100%').replace('{{content_fullpage}}', content).replace('{{content_halfpage}}','')
	return combined_page

def write_page():
	combined_page = contstruct_page()
	output = page['output']
	print("Writing to file...")
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

