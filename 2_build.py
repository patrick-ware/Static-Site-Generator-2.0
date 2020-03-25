def main():
	print("Building site...")
	for page in pages:
		page_filename = page['filename']
		image_display = page['image_display']
		output = page['output']
		page_content = open(page_filename).read()
		template = open('./templates/base.html').read()
		if image_display == 'half':
			combined_page = template.replace('{{view}}', '50%').replace('{{content_halfpage}}', page_content).replace('{{content_fullpage}}','')
			open(output, 'w+').write(combined_page)
		else:
			combined_page = template.replace('{{view}}', '100%').replace('{{content_fullpage}}', page_content).replace('{{content_halfpage}}','')
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

