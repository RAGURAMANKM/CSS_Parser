import re
import json


def parse_css(file_path):

    # Read the CSS file
    with open(file_path, "r", encoding="utf-8") as file:
        css_content = file.read()

    # Remove CSS comments
    css_content = re.sub(
        r"/\*.*?\*/",
        "",
        css_content,
        flags=re.DOTALL
    )

    # Find CSS selectors and their declarations
    pattern = r"([^{}]+)\{([^{}]*)\}"

    matches = re.findall(pattern, css_content)

    result = []

    # Process each CSS rule
    for selector, declarations in matches:

        properties = {}

        # Extract individual properties and values
        for declaration in declarations.split(";"):

            if ":" in declaration:

                property_name, value = declaration.split(":", 1)

                property_name = property_name.strip()
                value = value.strip()

                if property_name and value:
                    properties[property_name] = value

        # Store the extracted information
        result.append({
            "selector": selector.strip(),
            "properties": properties
        })

    return result


# Execute the parser
parsed_data = parse_css("style.css")

# Display the structured output
print(json.dumps(parsed_data, indent=4))