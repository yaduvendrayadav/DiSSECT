import pandas as pd
import dissect.analysis.data_processing as dp
import sys


def main():
    if len(sys.argv) != 3:
        print(f"USAGE: {sys.argv[0]} <INPUT> <OUTPUT>", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(sys.argv[1], sep=";")
    clusters = dp.find_clusters(df, df.columns[2:])
    clusters.value_counts(["cluster", "category"]).to_csv(sys.argv[2], sep=";")


if __name__ == "__main__":
    main()
