def main():
	print("Building site...")
	for page in pages:
		generate_page(page)
		write_data(page)
	print("Site built")


#Conditional statement used to correctly place content and modify background image based on image_display value, and insert title
def generate_page(webpage):
	filename = webpage['filename']
	template = open('./templates/base.html').read()	
	content = open(filename).read()
	image_display = webpage['image_display']
	if image_display == 'half':
		combined_page = template.replace(webpage['title'], '>>'+webpage['title']).replace('{{title}}', webpage['title']).replace('{{view}}', '50%').replace('{{content_halfpage}}', content).replace('{{content_fullpage}}','')
	else:
		combined_page = template.replace(webpage['title'], '>>'+webpage['title']).replace('{{title}}', webpage['title']).replace('{{view}}', '100%').replace('{{content_fullpage}}', content).replace('{{content_halfpage}}','')
	
	return combined_page

#Combined_page value data passed to write_data function to write file to disk
def write_data(webpage):
	output = webpage['output']
	combined_page = generate_page(webpage)
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


