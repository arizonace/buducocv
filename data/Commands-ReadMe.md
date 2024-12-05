<!-- ReadMe.md - Arizona Edwards
# Created: 2024-12-04 00:17-EST -->

# Data and Conversion
The canonical resumé data is stored in text files maintained in source control. A series of utility programs and commands have been formulated to do conversions as necessary.

## Resumé Generation

### Competencies table

```sh
./csvfields.py -v -i competencies.csv -o competency.html  -f: --template competency --html -k skillid --row-order ccpp mcpp csdn py js javkot win web unix cloud db tcpip iptv
```

### Disciplines table

```sh
./csvfields.py -v -i disciplines.csv -f: --template discipline --html --droprows Cloud -k Discipline > discipline.html
```

### Summary table

```sh
./csvfields.py -v -i employment --template summary --html -f: -o summary.html
```

### Detail table

```sh
./csvfields.py -v -i employment.csv --join highlights2024.csv:jobid  --template detail --html -f: -o detail.html
```

## TODO
- Add the star legend
- Make the size responsive
- Add detailed pages or popups for each skill
- Compile all `welcome.html` from data sources without all the cutting and pasting.
- `focus` and `sparks` columns need to be dynamically generated and joined rather than being stored in a duplicated, non-canonical fashion.
- Investigate generating and inserting print media CSS on the fly without using files.
- `csvfields.py` requires `f:` to be specified to indicate all fields for several transformations where this could be the default.
- `highlights.py` could be able to generate XML.
- Delete `highlights.xml` once it can be generated.
- Delete `highlights.css` and link to `buducocv.css` from highlights sources.
- An SQL parser e.g. *`csvsql.py`* could parse an SQL statement and build a pipeline to run `csvfields.py` along with GNU tools to execute the statement.
- `csv2json.py` could be retired once all the json functionality has been verified in `csvfields.py`

## Highlights
The canonical source of highlights text is "highlights.ini.md". The file follows a specific format and does not allow arbitrary markdown.
The existing text provides sufficient examples of how to format highlights but note the following.
- Indenting is exactly 2 spaces. 
- Highlights may have both additional text lines and sub-highlights (collectively subs) appearing in any order, as long as they are all indented 2 from the parent highlight.
- No levels can be missing. A highlight cannot directly contain grandchildren indented 4 spaces in from themselves.
- The format supports nesting to any depth but the data contains only 2 levels.
All highlights related columns have been removed from the spreadsheets and CSVs as they are unwieldy.
`highlights.py` can produce HTML, CSV (containing HTML), and XML conforming to highlights.xsd (future) on the fly as needed.
These derivative products of `highlights.py` shall not be kept in source control.

Create a CSV 

```sh
./highlights.py --csv highlights.csv  highlights.ini.md
```

## CSVs
- *employment.csv*: The big one with most of the data about jobs held.
- *employers.csv*: More information about each employer. 
  So far I have worked for each employer only once so there is almost a 1-1 correspondence between employment.csv and employers.csv.
  However, employers.csv also holds contracting agencies.
- *transitions.csv*: Additional information about each employer. Name and ownership changes.
- *competencies.csv*: The other big table with all the self-marketing data about skills and experience
- *focus.csv*: Additional data about each skill in competencies.csv. Numerical time-series data about my level of engagement and focus on each skill.
- *spark.csv*: Additional data about each skill in competencies.csv. Numerical time-series data about my proficiency level with each skill.
- *disciplines.csv*: Additional self-marketing data about experience and practices.
- *star-legend.csv*: Legend explaining what each number of stars means.

There is currently a redundancy between competencies and its 2 numerical extension tables.
The tables `focus` and `spark` contain one column for each career year. 
The `focus` and `sparks` columns in competencies.csv contain all the columns from those tables as comma separated lists.
Ideally, these columns would be generated and joined as needed (future).

