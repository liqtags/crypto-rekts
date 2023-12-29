# from the rekt db create a newly format readme of all the rekts

import json
import datetime
import html2text
import time
import os
import urllib.request
import consts
import subprocess

def rekt_loop(items, start):
    for index, item in enumerate(items[start:], start=start):
    # for item in items:
        print(f"index: {index} - item: {item['title']}")
        # download image
        markdownLogo = consts.imageBaseUrl + item['logo_link']
        # Bitrue (2)
        slugged_name = item['title'].replace(" ", "-")
        slugged_name = slugged_name.replace("(", "")
        slugged_name = slugged_name.replace(")", "")
        slugged_name = slugged_name.replace("/", "-")
        project_name = item['project_name']
        # save item to json file, nicely formatted
        with open(f'./rekts/{slugged_name}.json', 'w') as rekt:
            json.dump(item, rekt, indent=4)

        markdownTitle = f"# {project_name}"
        markdownLink = f"[{project_name}]({item['website_link']})"
        formatted_funds_lost = "${:,.2f}".format(item['funds_lost'])
        formatted_returned = "${:,.2f}".format(item['funds_returned'])
        markdownAmountLost = f"Amount Lost: {formatted_funds_lost}"
        markdownFundsReturned = f"Funds Returned: {formatted_returned}"
        markdownCategory = f"Category: {item['name_categories']}"
        markdownDate = f"Date: {item['date']}"
        markdownscamNetworks = f"Network: {item['scamNetworks'][0]['networks']['name']}"
        markdownLogoFromRepo = f"/rektimages/{slugged_name}.png"
        markdownImage = f"![{project_name}]({markdownLogoFromRepo})"
        markdownDescription = convert_html_to_markdown(item['description'])
        markdownFullWithScamNetworks = f"{markdownTitle}\n{markdownImage}\n- {markdownAmountLost}\n- {markdownFundsReturned}\n- {markdownCategory}\n- {markdownDate}\n- {markdownscamNetworks}\n\n"
        linkToMarkdownFile = f'/rekts/{slugged_name}.md'
        markdownFullwithLinkToLearnMore = f"{markdownFullWithScamNetworks}\n[Learn More]({linkToMarkdownFile})\n\n"
        markdownFullWithDescription = f"{markdownTitle}\n{markdownImage}\n- {markdownAmountLost}\n- {markdownFundsReturned}\n- {markdownCategory}\n- {markdownDate}\n\n{markdownDescription}\n\n"            
        
        proof_link = item['proof_link']
        if proof_link is not None:
            proof_link_array = proof_link.split(",")
            links = ""
            for link in proof_link_array:
                links += f"- [{link}]({link})\n"
            markdownFullWithDescription += f"Proof Links:\n{links}\n"

        # download image
        # print(f"downloading image: {markdownLogo}")
        urllib.request.urlretrieve(markdownLogo, f"rektimages/{slugged_name}.png")
        # print(f"finished downloading image: {markdownLogo}")

        with open(f'./rekts/{slugged_name}.md', 'w') as rekt:
            rekt.write(markdownFullWithDescription + '\n')
        
        commandToRun = f"git add * && git commit -m 'add {project_name} to rekts'"
        returned_value = subprocess.call(commandToRun, shell=True, )  # returns the exit code in unix
        # os.system(commandToRun)

def convert_html_to_markdown(html):
    # print(f"starting converting html to markdown")
    # if html is none: contine
    if html is None:
        return ""

    text_maker = html2text.HTML2Text()
    text_maker.body_width = 0  # This sets the body width to unlimited which helps in not wrapping the text automatically.
    markdown_content = text_maker.handle(html)
    # print(f"finished converting html to markdown")

    return markdown_content

def make_toc(items, filename):
    # from all the items, make a table of contents for the readme with - [Project Name](#project-name)
    tocsWithTitle = "# Table of Contents\n\n"
    for item in items:
        project_name = item['title']
        formatted_funds_lost = "${:,.2f}".format(item['funds_lost'])
        formatted_returned = "${:,.2f}".format(item['funds_returned'])
        slugged_name = project_name.replace(" ", "-")
        slugged_name = slugged_name.replace("(", "")
        slugged_name = slugged_name.replace(")", "")
        slugged_name = slugged_name.replace("/", "-")
        linkToMarkdownFile = f'/rekts/{slugged_name}.md'
        tocsWithTitle += f"- [{project_name}]({linkToMarkdownFile}) - Lost: {formatted_funds_lost} Recovered: {formatted_returned} \n"
        # tocsWithTitleAndSumLost
    with open(filename, 'w') as readme:
        readme.write(tocsWithTitle + '\n')

def make_title(filename):
    # from all the items, make a table of contents for the readme with - [Project Name](#project-name)
    title = "# Rekt Projects\n\n"
    with open(filename, 'w') as readme:
        readme.write(title + '\n')
                
def download_project_images():
    # with open('1-small.json', 'r') as f:
    with open('rektdb.json', 'r') as f:
        data = json.load(f)
        items = data['items']
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # readme_file_name = f'README-{timestamp}.md'
        readme_file_name = f'README.md'
        add_title = f"# Rekt Projects\n\n"
        # make_title(readme_file_name)
        make_toc(items, readme_file_name)
        rekt_loop(items, 3311)

download_project_images()

# convert_html_to_markdown("<h1>This is a heading</h1><p>This is a paragraph.</p>")
