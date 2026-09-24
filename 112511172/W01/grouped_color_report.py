def color_report(colors):
    # Step 1: Flatten the nested list
    colors_flatten = []
    for group in colors:
        for color in group:
            colors_flatten.append(color)

    # Step 2: Sort the flattened list
    colors_flatten.sort()

    # Step 3: Count each color
    result = []
    i = 0

    while i < len(colors_flatten):
        current_color = colors_flatten[i]
        count = 1

        # Count consecutive occurrences of the current color
        while i + 1 < len(colors_flatten) and colors_flatten[i + 1] == current_color:
            count += 1
            i += 1

        # Save the result for this color
        result.append((current_color, count))

        # Move to the next unprocessed color
        i += 1

    return result

'''
colors = [
    ["b", "r", "b"],
    ["g", "r"],
    ["b", "g"]
]
print(color_report(colors))
'''