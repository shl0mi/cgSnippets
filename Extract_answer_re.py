import re

templates = [
    "Answer: A",
    "Answer A",
    "The correct answer is B",
    "The correct answer is B)",
    "The answer is C",
    "The answer is C).",
    "A is correct",
    "A. is correct",
    "A) is correct",
    "A). is correct",
    "B is the correct answer",
    "B) is the correct answer",
    "B). is the correct answer",
    "C.",
    "The answer to your question is A"
]

letter_regex = [
    r'Answer: ([A-Z])',
    r'Answer ([A-Z])',
    r'The correct answer is ([A-Z])',
    r'The correct answer is ([A-Z])\)',
    r'The answer is ([A-Z])',
    r'The answer is ([A-Z])\).',
    r'(?:^|\s)([A-Z]) is correct',
    r'(?:^|\s)([A-Z])\. is correct',
    r'(?:^|\s)([A-Z])\) is correct',
    r'(?:^|\s)([A-Z])\)\. is correct',
    r'(?:^|\s)([A-Z]) is the correct answer',
    r'(?:^|\s)([A-Z])\) is the correct answer',
    r'(?:^|\s)([A-Z])\)\. is the correct answer',
    r'(?:^|\s)([A-Z])\.',
    r'The answer to your question is ([A-Z])'
]

for template, regex in zip(templates, letter_regex):
    match = re.search(regex, template)
    if match:
        extracted_letter = match.group(1)
        print(f'From "{template}", extracted: {extracted_letter}')
    else:
        print(f'No match in "{template}"')
