def main():
	print("Building site...")
	page_view()
	apply_template()
	build_site()

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

#function to insert CSS value into template if page only displays half of background image
def page_view():
	for page in pages:
		template = open('./templates/base.html').read()
		image_display = page['image_display']
		if image_display == 'half':
			view_template = template.replace('{{view}}', '50%').replace('{{content_fullpage}}','')
		else:
			view_template = template.replace('{{view}}', '50%').replace('{{content_halfpage}}','')
	return view_template

def apply_template():
	for page in pages:
		page_filename = page['filename']
		page_content = open(page_filename).read()
		image_display = page['image_display']
		view_template = page_view()
		if image_display == 'half':
			combined_page = view_template.replace("{{content_halfpage}}", page_content)
		else:
			combined_page = view_template.replace("{{content_fullpage}}", page_content)
	return combined_page

def build_site():
	for page in pages:
		combined_page=apply_template()
		page_output = page['output']
		open(page_output, 'w+').write(combined_page)

if __name__ == "__main__":
	main()

