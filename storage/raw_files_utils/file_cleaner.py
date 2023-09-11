def clean_md_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Lines that signify the start and end of navigation content.
    start_phrases = ["Contents  Menu  Expand", "Hide navigation sidebar", "Give us a ⭐️ on [ Github ]", "Playgrounds API", "Meta"]
    end_phrases = ["Auto light/dark mode", "Toggle site navigation sidebar", "Improving the Docs", "Back to top"]

    # Additional lines or phrases to skip
    skip_phrases = [
        "Made with [ Furo ](https://github.com/pradyunsg/furo)",
        "[ Next",
        "[ Previous",
        "[ ![Light Logo]",
        "[ ](https://github.com/0xPlaygrounds/subgrounds)",
        "](https://discord.gg/v4r4zhBAh2)",
        "](https://twitter.com/Playgrounds0x)",
        "Toggle Light / Dark / Auto color theme",
        "Toggle table of contents sidebar",
        "_ _",
        "[ Playgrounds  ](../../../)",
        "Logo](../../../_static/assets/pg-logotype-primary.svg)",
        "](https://playgrounds.network)"
    ]

    skip = False
    cleaned_lines = []

    for line in lines:
        if any(line.startswith(phrase) for phrase in start_phrases):
            skip = True
        if not skip and not any(phrase in line for phrase in skip_phrases):
            cleaned_lines.append(line)
        if any(line.startswith(phrase) for phrase in end_phrases):
            skip = False

    with open(output_file, 'w') as f:
        f.writelines(cleaned_lines)

    print(f"Cleaned markdown saved to {output_file}")


# Usage:
input_file = 'playgrounds_docs.md'
output_file = 'playgrounds_docs_cleaned.md'
clean_md_file(input_file, output_file)
