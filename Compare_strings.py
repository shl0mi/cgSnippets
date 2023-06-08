def create_comparison_table(starters, completions1, completions2):
    table = "<table style='border-collapse: separate; border-spacing: 10px;'>"
    table += "<tr><th style='border: 1px solid black; background-color: #f2f2f2;'>Starter</th>"
    table += "<th style='border: 1px solid black; background-color: #e6f2ff;'>Completion 1</th>"
    table += "<th style='border: 1px solid black; background-color: #ffcccc;'>Completion 2</th></tr>"

    for starter, completion1, completion2 in zip(starters, completions1, completions2):
        table += "<tr>"
        table += f"<td style='border: 1px solid black;'>{starter}</td>"
        table += f"<td style='border: 1px solid black;'>{completion1}</td>"
        table += f"<td style='border: 1px solid black;'>{completion2}</td>"
        table += "</tr>"

    table += "</table>"
    return table

# Rest of the code remains the same...

# Example usage
starters = [
    "I love",
    "The weather is",
    "In my free time, I enjoy"
]

completions1 = [
    "I love chocolate.",
    "The weather is sunny.",
    "In my free time, I enjoy reading books."
]

completions2 = [
    "I love ice cream.",
    "The weather is cloudy.",
    "In my free time, I enjoy playing soccer."
]

comparison_table = create_comparison_table(starters, completions1, completions2)

# Write the comparison table to an HTML file
with open('comparison.html', 'w') as file:
    file.write(comparison_table)

# Open the HTML file in the default web browser
import webbrowser
webbrowser.open('comparison.html')
