import matplotlib.pyplot as plt


def do_plot(results, title):

    # Extract data from the dictionary
    num_rules = list(results.keys())
    average_hashed = [v[0] for v in results.values()]
    average_compiled = [v[1] for v in results.values()]

    # Create the plot
    plt.figure(figsize=(10, 6))

    plt.plot(num_rules, average_hashed, label='Average Hashed', marker='o')
    plt.plot(num_rules, average_compiled, label='Average Compiled', marker='o')

    # Add titles and labels
    plt.title(title)
    plt.xlabel('Number of Rules')
    plt.ylabel('Average Search Time (ms)')

    # Add a legend
    plt.legend()

    # Add grid lines for better readability
    plt.grid(True)

    # Show the plot
    plt.show()

    # Keep the plot open
    plt.ioff()
    plt.show()