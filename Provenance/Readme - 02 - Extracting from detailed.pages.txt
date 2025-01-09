[detailed.pages]
The Numbers file "detailed 2016-11-05.pages -- 2024-10-02.numbers" (a.k.a. Detailed-Pages-Oct.numbers) was created to capture all the tables from "detailed 2016-11-05.pages" (a.k.a. detailed.pages)
The default starting table was deleted from the first sheet in the Numbers file and the sheet was named "Bio".
All 5 tables of the first page of the Pages file were copied to it 1 by 1.

=== x3 
Three new sheets created in the Numbers file (Details1, Details2, Details3)
The head of each employment detail section in the Pages file is a 3-row, 2-column table with merged cell spans in the two bottom rows. 4 cells total.
All 14 of these were copied 1 by 1 to the new sheets.
There were 4 or 5 tables on each sheet to keep from having to scroll down too far but the tables weren't copied in any order and so this hindered almost as much as it helped.

=== x3 
These 3 sheets were duplicated to (Details 1-H, Details 2-H, Details 3-H)
Two additional columns were added into which the "Duties Performed" and Highlights data were copied. The two new columns were each merged down across the two bottom rows. The top row was not used in these columns.
The tables now have 4 columns and 3 rows with 6 out of 8 cells used. The 2 rightmost cells in the header are not used.
The tables are now awkward with merges going in both directions. 
The left 2 columns are treated as 1 column except in the header row which looks like 2 cells.  The 2 lower rows are each merged horizontally across the left 2 columns. 
In both the 2 right columns, the two lower rows are each merged vertically into one cell. There is no merging in the header so we have 4 header cells sitting on 3 columns.
So the 8 cells look like this. 
Left half (horizontal merge) Two header cells are sitting side by side atop a stack of 2 cells.
Right half (vertical merge) Two empty header cells each sitting atop a single tall cell


=== 
A new sheet is created, "Details All-H" and all 14 tables from the 3 previous sheets were copied to it.

===
A new sheet is created, Details All-HW and all 14 tables are combined into 1 table with 29 rows. 2 rows per job.
All merged cells were split. There are now 4 columns. The column below the 2nd header cell is empty and the lower left cell is now alone in the 3rd row.
The 2nd header cell is moved to the 3rd header cell leaving the 2nd column empty. The lower left cell is moved to the 4th header cell leaving the bottom row empty.
The bottom row and 2nd column are deleted leaving 3 columns over 2 rows, 6 cells, all in use. 
These manipulations are done to each table before adding them to the growing joined table.
-
3 columns are added on the left and the start date, end date and job name are copied to the top row in each of those. 
The 3 left cells in the lower row are still unused. The table is 6 columns wide, 12 cells with 9 in use.


===
The sheet is duplicated into a new sheet "Details All-H-VW" for the table to be flattened.
3 new columns are added to the right and the 3 used cells from the bottom row are moved into the new cells on the top row.
The bottom row is then deleted. Each job is now 1 row and 9 columns. But not for long.
-
Position is copied out into its own column and an ill-advised column is added for the highlights formatted as markdown. 
The jobs are now stored in 11 columns and 15 rows. (1 row is the header)


======
======
======
The entire spreadsheet file is factored into a new spreadsheet file, "detailed 2016-11-05.pages -- 2024-11-04.numbers" (a.k.a. Detailed-Pages.numbers)

The data is transformed as follows:

===
Bio sheet comes over intact
All 3 detail sheets (Details1, Details2, Details3) are copied over in order into sheet "Job Headers" 
All 3 summary sheets (Details 1-H, Details 2-H, Details 3-H) are copied in order into sheet "Job Summaries"
The sheet "Details All-HW" is cleaned up and copied over as "Joined Job Summaries"
The sheet "Details All-H-VW" is cleaned up and copied over as "Job Rows"
There were 4 sheets where I was trying out different layouts for individual job headers and summaries (GAP, HVL, Nova, Fed). These were all copied into "Job Layout Experiments"

=== 
"Job Rows" is duplicated into a new sheet. 
All structured data is broken out into separate columns. A column is added for HTML Highlights. The table is now 23 columns wide, (A:W)

[**Garbage**]
The old spreadsheet "Detailed-Pages-Oct.numbers" can now be deleted.

[CSV]
Detailed-Pages.numbers is exported into several CSV files.

[RTF/HTML]
The Highlights (which were copied from Pages into Numbers) are now copied one at a time from each cell and pasted into TextEdit twice.
The first time it is saves as RTF and the second time as HTML. TextEdit did not provide a straightforward way to export an already saved RTF file as HTML.
For each file I pasted the formatted text into a new file and saved it as HTML. In fact, saving each file as RTF was superfluous.

TextEdit has a really tidy HTML output with minimal css. 
I examined all 14 stylesheets and determined that they were all basically the same and the few additions could be combined into a basic one.

I created a second set of HTML files with all classes and embedded style sheets removed. I linked them all to a single stylesheet with combined styles that selected based on the elements. 
I added 1 class "highlights" for the "Highlights:" labels and removed the bold tag from those paragraphs. 
After verifying the behavior, I did some more cleanup to remove empty spans and special blank space codes.
I also removed the invalid hyperlink tags around ASP.Net. 

Then I created a simple HTML file with an embedded stylesheet using the simple combined styles. 
Highlights were placed, in order, into divs with the job name as the div id. The div id is rendered as a label using a :before tab.
After verifying, I copied the inner contents of each div, (what will be the innerHTML) into the HTML column in the spreadsheet.

[**Keep**]
Detailed-Pages.numbers will be useful for more steps.

[**Archive**]
All the individual RTF and HTML files as well as the class based "combined-styles.css". 

[**Basis**]
highlights.html		
highlights.css		<-- even though highlights.html has its styles embedded, this is the basis for the resume's canonical stylesheet.
highlights.ini.rtf	<-- Highlight sections in order with ini style labels.
highlights.ini.md	<-- Highlight sections in order with ini style labels.

======
======
======
Copied Detailed-Pages.numbers to new spreadsheet ResumeWorkshop and merged in sheets from HTML-Extracts.numbers

[**Garbage**]
Detailed-Pages.numbers: Everything useful is now in ResumeWorkshop.numbers. It can be deleted.
skills.numbers  Everything useful from was also in and is now in ResumeWorkshop.numbers. It will remain in the permanent historical scrapbook but the working copy can be deleted from the workspace.
Employment-2024-11-04.numbers 

[**Archive**]
HTML-Extracts.numbers can be archived. It has interesting sheets that are not merged into ResumeWorkshop.

[ResumeWorkshop]
This spreadsheet will have all the data needed plus interesting artifacts.
A final spreadsheet will be distilled at the end with the sole purpose of being able to re-export as close to the source control basis as possible and without any bulky artifacts. This will be buducocv.numbers
