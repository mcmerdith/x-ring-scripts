import sys
import os
from string import Template

domain = "https://x-ringsupply.com"


def main():
    categories_file = sys.argv[1] if len(sys.argv) > 1 else "categories.txt"
    output_dir = 'output/' + categories_file.split('.')[0]

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    with open('templates/slider_template.html', 'r') as file:
        SLIDER_TEMPLATE = Template(file.read())

    with open('templates/slider_item_template.html', 'r') as file:
        ITEM_TEMPLATE = Template(file.read())

    with open('templates/slider_scripts.html', 'r') as file:
        SCRIPTS = file.read()

    with open('templates/slider_styles.html', 'r') as file:
        STYLES = file.read()

    category_items = {}

    with open(categories_file, 'r') as file:
        for line in file:
            # Get line contents
            raw = line.strip()

            # Get attributes
            try:
                category_id, image_ref, category_group, custom_slug, page_title = raw.split(
                    '|')
            except ValueError as e:
                print("Syntax error in line: " + raw.split('|')[0], "...")
                print(e)
                continue

            if not category_id:
                print("Sytax error in line: ", raw)
                print("Missing category")
                sys.exit(1)

            if not image_ref:
                image_ref = 'code=' + category_id

            # Get category url and display name
            category_id = category_id.replace('_', '-').lower()
            category_display = category_id.replace('-', ' ').title()

            if not page_title:
                page_title = category_display

            # Substitute variables into ITEM_TEMPLATE
            item_html = ITEM_TEMPLATE.substitute(
                category=custom_slug if custom_slug else category_id,
                imageref=image_ref,
                category_display=category_display,
                slug="product-category-group" if category_group else "product-category",
                domain=domain
            )

            # Add item_html to content
            category_items[category_id] = (item_html, page_title)

    # Create a slider for each category
    for output_category_id, (_, page_title) in category_items.items():
        with open(output_dir + '/' + output_category_id + '.html', 'w') as output_file:
            content = ""
            for item_category_id, (item_html, _) in category_items.items():
                # skip the current category
                if item_category_id == output_category_id:
                    continue
                # write the category to the file
                content += item_html
            output_file.write(SLIDER_TEMPLATE.substitute(
                content=content, page_title=page_title
            ))
            output_file.write(SCRIPTS)
            output_file.write(STYLES)


if __name__ == '__main__':
    main()
