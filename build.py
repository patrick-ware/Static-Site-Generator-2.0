print("Building static site")

print("Reading in template html variables")
top_html = open('./templates/top.html').read()
bottom_html = open('./templates/bottom.html').read()

print("Reading in content html variables")
index_html = open('./content/index.html').read()
aboutme_html = open('./content/aboutme.html').read()
resume_html = open('./content/resume.html').read()
contact_html = open('./content/contact.html').read()

print("Combining html")
combined_index = top_html + index_html + bottom_html
combined_aboutme = top_html + aboutme_html + bottom_html
combined_resume = top_html + resume_html + bottom_html
combined_contact = top_html + contact_html + bottom_html

open('./docs/index.html', 'w+').write(combined_index)
open('./docs/aboutme.html', 'w+').write(combined_aboutme)
open('./docs/resume.html', 'w+').write(combined_resume)
open('./docs/contact.html', 'w+').write(combined_contact)
