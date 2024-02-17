# FAQ Generator

## Usage

```
<python> generator.py [category_file]
```

### Arguments

```plaintext
category_file: The file to read categories from
    (default: "categories.yml")
```

### categories.yml syntax

The `categories.yml` file is structured as a root category group with nested categories

```yml
CATEGORY_GROUP_NAME:
    title: "Category Name"
    header: "Header text"
    description: "Description meta text"
    image_code: "IMAGE_CODE"
    category_id: "override-category-url"
    categories:
        CATEGORY_ID:
            header: "Header text"
            description: "Description meta text"
```

#### Example:

```yml
GLOCK_PARTS:
    title: "All Glock Parts"
    header: "Custom Glock Parts: Upgrade Your Firearm with quality parts from X-Ring Supply"
    description: "A short paragraph about custom glock parts"
    image_code: "GLOCK_PARTS"
    category_id: "glock-platform-parts"
    categories:
        GLOCK_FRAMES:
            header: "Custom Glock Frames: Upgrade Your Firearm with quality parts from X-Ring Supply"
            description: "A short paragraph about custom glock frames"

```

#### Parameters

```
CATEGORY_NAME:
    The name of the category.

    title (optional): 
        The title of the category
        Default: "CATEGORY_NAME" formatted as title case
    
    header (optional):
        Custom header text for the category
        Default: "CATEGORY_NAME" formatted as title case
    
    description (optional):
        A short paragraph description of the category
        Default: blank
    
    image_code OR image_id (optional):
        Code: character based image code in coreFORCE
        ID: number based image ID in coreFORCE
        image_code has a higher priority than image_id
        Default: image_code=CATEGORY_NAME

    category_id (optional):
        The ID of the category in coreFORCE
        Default: CATEGORY_NAME
