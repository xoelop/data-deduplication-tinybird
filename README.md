# Social media views dataset generator

Will create datasets of the daily views for N post for each day of 2020, like this

```csv
date,post_id,views
2020-01-01,0,26
2020-01-01,1,5
2020-01-01,2,125
2020-01-01,3,11
2020-01-01,4,7
2020-01-01,5,48
2020-01-01,6,46
2020-01-01,7,8
2020-01-01,8,15
2020-01-01,9,3
```

## Installation

```bash
python3 -mvenv .e
source .e/bin/activate
pip install -r requirements.txt
```

Run it 

```bash
python gen.py cardinality_of_posts
```


You can also specify start and end dates
```bash
usage: gen.py [-h] [-s START_DATE] [-e END_DATE] posts

Generate events.csv file

positional arguments:
  posts                 number of posts. To have datasets with different cardinality

optional arguments:
  -h, --help            show this help message and exit
  -s START_DATE, --start-date START_DATE
                        Start date for events, optional. Format YYYYMMDD. The min start date is 20170101 (default: 20200101)
  -e END_DATE, --end-date END_DATE
                        End date for events, optional. Format YYYYMMDD. The max end date is 20201103 (default: 20201231)
```


## Tinybird project

Start the CLI with docker mounting 2 volumes, one for the project data files and another one for the datasets like this

```bash
docker run -v $(pwd)/tb_project:/mnt/data -v $(pwd)/datasets:/mnt/datasets -it tinybirdco/tinybird-cli-docker
```