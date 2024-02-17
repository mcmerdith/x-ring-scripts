# Slider Generator

## Usage

```
<python> generator.py [category_file]
```

### Arguments

```plaintext
category_file: The file to read categories from
    (default: "categories.txt")
```

### categories.txt syntax

The `categories.txt` file has each category on a seperate line

#### Example:

```
CATEGORY_ID|IMAGE_REF|IS_GROUP|CUSTOM_URL_ID|HEADER TEXT
ALL_GLOCK_PARTS|code=GLOCK_PARTS|TRUE|glock-platform|Custom Glock Parts
GLOCK_FRAMES|||Custom Glock Frames
```

#### Parameters

```
CATEGORY_ID: The ID of the category in the database
    Used as the text on the slider button and output file name
    Note: Used in the url if no CUSTOM_URL_ID is provided
    Note: The "_" will be replaced with "-"
    (ex: GLOCK_FRAMES => /product-category/glock-frames)
IMAGE_REF (optional): The ID of the image in coreFORCE
    Default: code=CATEGORY_ID
    (ex: code=GLOCK_PARTS, id=123456)
IS_GROUP (optional): If the category is a category group
    Default: <empty>
    Set to "TRUE" to enable
    Changes the URL from "/product-category/CATEGORY_ID" to "/product-category-group/CATEGORY_ID"
CUSTOM_URL_ID (optional): A custom url to replace the default CATEGORY_ID
    Default: <empty>
    Note: This field must exactly match the URL on the website. No substitution will be performed
    (ex: glock-platform => /product-category/glock-platform)
HEADER_TEXT (optional): The text to place in the page header
    Default: CATEGORY_ID
    (ex: Custom Glock Parts)
```
