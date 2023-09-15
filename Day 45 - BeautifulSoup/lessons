from bs4 import BeautifulSoup


with open("website.html", encoding="utf-8") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())

#------- find_all()

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.string) # use .string to get the string

# Use CSS Selector and soup.select()
