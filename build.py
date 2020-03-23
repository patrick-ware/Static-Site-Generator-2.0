template = open('./templates/base.html').read()
view = ".view {{ height:50%;}}"

def page_view():
	view_template = template.replace("{{view}}", view)
	return view_template

def main():
	print("Building static site")

	top_html = open('./templates/top.html').read()
	bottom_html = open('./templates/bottom.html').read()

	template = open('./templates/base.html').read()

	for page in pages:
		if page['image_display'] == 'half':
			page_view()
			page_filename = page['filename']
			page_content = open(page_filename).read()
			page_output = page['output']
			combined_page = template.reaplce("{{view}}", view
			open(page_output, 'w+').write(combined_page)
		else:
			page_filename = page['filename']
			page_content = open(page_filename).read()
			page_output = page['output']
			combined_page = top_html + page_content + bottom_html
			open(page_output, 'w+').write(combined_page)


#'display' item used to inform how much of background image is shown on each page

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

