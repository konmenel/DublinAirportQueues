import sys
import pandas as pd
import matplotlib.pyplot as plt


def main() -> int:
    """Main function."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    for terminal, ax in enumerate(axes, 1):
        data = pd.read_csv(
            f'data/T{terminal}_queues.csv',
            sep=',',
            parse_dates=[0],
        )

        ax.plot(data['Timestamp[%Y-%m-%d %H:%M]'], data['Queue[mins]'])

    fig.autofmt_xdate()
    plt.show()
    return 0


if __name__ == '__main__':
    sys.exit(main())
