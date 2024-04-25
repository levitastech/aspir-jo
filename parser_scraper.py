import re
from html.parser import HTMLParser

"""
    for now : deprecated
    
    no more need for it , the main purpose of writing this module it to replace beautiful soup
    since it has been replaced effectively with simple regular expressions , it is deprecated now
"""

class HTMLTagParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.contents = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self.contents.append("")

    def handle_endtag(self, tag):
        if not self.tags or self.tags[-1] != tag:
            raise ValueError(f"Unbalanced tag: </{tag}>")
        self.tags.pop()

    def handle_data(self, data):
        if self.contents:
            self.contents[-1] += data


def parse_html2(html_string):
    """
    Parse the HTML string and return a list of tuples (tag, content).
    """
    # Check if the input HTML string is empty or consists of only whitespace
    if not html_string.strip():
        raise ValueError("Input HTML string is empty or consists of only whitespace.")

    parser = HTMLTagParser()
    parser.feed(html_string)

    return list(zip(parser.tags, parser.contents))


def parse_html(html_string):
    """
    Parse the HTML string and return a list of tuples (tag, content).

    Args:
        html_string (str): The HTML string to be parsed.

    Returns:
        list: A list of tuples (tag, content), where 'tag' is the HTML tag
              and 'content' is the text between the opening and closing tags.

    Raises:
        ValueError: If the input HTML string is empty or consists of only whitespace characters.
        ValueError: If the input HTML string is not a valid HTML document
                        (does not start with <html> and end with </html>).
    """
    # Check if the input HTML string is empty or consists of only whitespace characters
    if not html_string.strip():
        raise ValueError("Input HTML string is empty or consists of only whitespace characters.")

    # Check if the input HTML string is a valid HTML document
    if not html_string.startswith("<html") or not html_string.endswith("</html>"):
        raise ValueError("Input HTML string is not a valid HTML document.")

    pattern = r'<(\w+)>(.*?)</\1>'
    return [(match.group(1), match.group(2)) for match in re.finditer(pattern, html_string, re.DOTALL)]


def validate_html(html_string):
    """
    Validate the HTML structure by checking if it starts with <html> and ends with </html>.
    """
    if not html_string.strip().startswith('<html>') or not html_string.strip().endswith('</html>'):
        raise ValueError("Invalid HTML structure. The HTML string should start with <html> and end with </html>.")


def search_tags(html_string, tag):
    """
    Search for specific HTML tags within the parsed HTML string.

    Args:
        html_string (str): The HTML string to be searched.
        tag (str): The HTML tag to search for.

    Returns:
        list: A list of text content between the opening and closing tags.

    Raises:
        ValueError: If the provided tag is not a valid HTML tag name.
    """
    # Check if the provided tag is a valid HTML tag name
    if not is_valid_tag_name(tag):
        raise ValueError(f"Invalid tag name: '{tag}'")

    parsed_html = parse_html(html_string)
    contents = [content for tag_name, content in parsed_html if tag_name == tag]
    return contents


def is_valid_tag_name(tag):
    """
    Check if the provided tag is a valid HTML tag name.

    Args:
        tag (str): The tag name to be checked.

    Returns:
        bool: True if the tag is a valid HTML tag name, False otherwise.
    """
    # List of valid HTML tag names (not exhaustive)
    valid_tags = [
        "html", "head", "body", "title", "h1", "h2", "h3", "h4", "h5", "h6",
        "p", "div", "span", "a", "img", "ul", "ol", "li", "table", "tr", "th", "td",
        "form", "input", "button", "select", "option", "textarea", "style", "script"
    ]
    return tag.lower() in valid_tags


def recursive_search(html_string, tags):
    """
    Recursively search for nested HTML tags within the parsed HTML string.

    Args:
        html_string (str): The HTML string to be searched.
        tags (list): A list of tags to search for, in the order of nesting.

    Returns:
        list: A list of text content between the innermost tags.

    Raises:
        ValueError: If the provided list of tags contains an invalid tag name.
        ValueError: If the provided list of tags is not properly balanced or does not match the structure of
                        the input HTML string.
    """
    # Check if the provided list of tags contains any invalid tag names
    for tag in tags:
        if not is_valid_tag_name(tag):
            raise ValueError(f"Invalid tag name: '{tag}'")

    validate_nested_tags(html_string, tags)

    # Implement tag structure validation logic here
    # ...

    if not tags:
        return [html_string]

    outer_tag = tags[0]
    inner_tags = tags[1:]

    outer_contents = search_tags(html_string, outer_tag)
    results = []

    for content in outer_contents:
        inner_results = recursive_search(content, inner_tags)
        results.extend(inner_results)

    return results


def validate_nested_tags(html_string, tags):
    """
    Validate the nested tag structure by ensuring that the tags are properly balanced.
    """
    stack = []

    # Validate and push valid tags onto the stack
    for tag in tags:
        if not is_valid_tag_name(tag):
            raise ValueError(f"Invalid tag name: '{tag}'")
        stack.append(tag)

    # Parse HTML string into (tag_name, content) tuples
    parsed_html = parse_html(html_string)

    # Iterate through parsed HTML structure
    for tag_name, content in parsed_html:
        if tag_name == stack[0]:  # Matching opening tag found
            stack.pop(0)  # Pop the matched tag from stack

            # Check for nested tags in the content
            for inner_tag in stack:
                if inner_tag in content:
                    raise ValueError(f"Unbalanced nested tags: '{tag_name}' and '{inner_tag}'")

            stack = []  # Reset stack since tag is properly closed
        elif tag_name in stack:  # Found an unexpected closing tag
            raise ValueError(f"Unbalanced nested tags: '{tag_name}' and '{stack[0]}'")

    # Check if there are remaining unclosed tags in stack
    if stack:
        raise ValueError(f"Unbalanced nested tags: '{stack[0]}' is missing a closing tag.")


class TagIterator:
    """
    Iterator class for iterating over search results.
    """

    def __init__(self, html_string, tags):
        self.results = recursive_search(html_string, tags)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.results):
            raise StopIteration
        result = self.results[self.index]
        self.index += 1
        return result
