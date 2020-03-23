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

template = open('./templates/base.html').read()

view = ".view {{ height:50%;}}"

<<<<<<< HEAD
#insert CSS into template if page only displays half of background image
=======
>>>>>>> parent of 9bba7fc... main() for loop debugging, page_view() works with return variable
def page_view():
	view_template = template.replace("{{view}}", view)
	return view_template

def main():
	print("Building static site")

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


if __name__ == "__main__":
	main()

