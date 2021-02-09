import numpy as np
import argparse
import pandas as pd

from utils import str_human_to_number, number_to_human_str


def create_df(num_posts: int, start: str, end: str):
    np.random.seed(1234)
    posts_ids = np.arange(num_posts)
    dates = pd.date_range(start=start, end=end).date
    initial_views = np.exp(
        np.random.lognormal(mean=1, sigma=0.4, size=num_posts)
    ).astype(int)
    daily_returns = 1 + np.random.pareto(a=100, size=[len(dates), num_posts])
    df = pd.DataFrame(
        daily_returns,
        index=pd.Series(dates, name="date"),
        columns=pd.Series(posts_ids, name="post_id"),
    )
    df = df.cumprod()
    df = df * initial_views
    df = df.astype(int)
    df = df.stack()
    df.name = "views"
    df = df.reset_index()
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate events.csv file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "posts",
        type=str,
        default="100",
        help="number of posts. To have datasets with different cardinality",
    )
    parser.add_argument(
        "-s",
        "--start-date",
        type=str,
        default="20200101",
        help="Start date for events, optional. Format YYYYMMDD. The min start date is 20170101",
    )
    parser.add_argument(
        "-e",
        "--end-date",
        type=str,
        default="20201231",
        help="End date for events, optional. Format YYYYMMDD. The max end date is 20201103",
    )
    args = parser.parse_args()

    num_rows = str_human_to_number(args.posts)
    print(f'Generating dataset for {args.posts} posts')
    df = create_df(num_rows, start=args.start_date, end=args.end_date)
    filename = f"posts_{number_to_human_str(num_rows)}.csv"
    print(f'Saving file to {filename}')
    df.to_csv(filename, index=False)