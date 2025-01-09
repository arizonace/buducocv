[Source controlled basis]

[bio.json]
Written by hand in Cot Editor. There was minimal bio data in the resume. 
Phone number, city, state, email, Bachelors; LinkedIn link

[disciplines.csv]
From ResumeWorksop/Skills-disciplines.csv
Note: The original csv from skills.numbers had no data in the header. 
I filled in the headers in all the tables in the Skills sheet and regenerated.

[From ResumeWorksop -> Export to CSV]
disciplines.csv			<-- Skills-disciplines.csv
employers.csv			<-- Skills-employers.csv
competencies.csv		<-- Competencies-Competencies-doc-order.csv
star.csv			<-- Ratings-star.csv  # with year guide and jobids
spark.csv			<-- Ratings-spark.csv # with year guide and jobids
employment.csv			<-- Employment-Employment.csv
employment-no-para.csv		<-- Employment-no-para-Employment-no-para.csv # Adds columns: Company, Responsibilities, Did, 
employment-short-para.csv	<-- Employment-short-para-Employment-short-para.csv # Adds columns: Activities, HighlightsHTML
jobs.csv			<-- Skills-jobs.csv
transitions.csv			<-- Skills-transitions.csv
star-legend.csv			<-- Ratings-Star Legend.csv
narratives.ini.txt		& Ini style text file with plain-text narratives and comments
narratives.ini.rtf		& Ini style rich text file with formatted narratives and comments
narratives.html			<-- Divs are entries

[via Boop]
disciplines.json
employers.json
competencies.json
star.json
spark.json
employment.json
employment-rt.csv
employment-no-para.json
employment-no-para-rt.csv
employment-short-para.json
employment-short-para-rt.csv
jobs.json
jobs-rt.csv
transitions.json
transitions-rt.csv




# ------ Redundant copies of references data
resume.json 			<-- Combination of all .json files. (Some non-JSON data may be excluded).
resume.[x|ht]ml  		<-- Combination of all html/xml files, maybe partially flattened. Not formatted for presentation but may be formatted via XSLT.
resume.xsl  			<-- Maybe. A cool exercise on the above.



-----

bio.json/.[x|ht]ml		<-- From detailed.pages
disciplines.json/.[x|ht]ml	<-- From skills.numbers::skills::disciplines
& disciplines.csv		&
competencies.json		<-- From skills.numbers::skills::ratings and skills.numbers::skills::keywords and sparks.csv and stars.csv
& competencies.csv		&   The flat columns from the skills table. ["Name", Star-level, Years, 3x Description lengths, "Narrative"]
sparks.csv			<-- From HTML-extracts.numbers::Ratings. No separate JSON. Included in skills.json
stars.csv			<-- From HTML-extracts.numbers::Ratings. No separate JSON. Included in skills.json

Highlights.[x|ht]ml/.json	<-- From detailed.pages. Each record is the innerHTML of a div identified by id.
& Highlights.ini.rtf		<-- From detailed.pages. To demonstrate the desired presentation from other formats 
&? Highlights.ini.md		<-- From detailed.pages
& Highlights.txt		<-- Plain text formatting with space indentation and dashes. No bold, no wrap.
employers.json			<-- From skills.numbers::skills::employers & skills.numbers::skills::jobs & skills.numbers::skills::transitions
& employers.csv			&
employment.json			<-- From detailed.pages + summ.pages via Detailed-Pages.numbers and [skills|HTML-Extracts].numbers
& employment.csv		&



-----

references.json			<-- From the future
&? references.csv		&

? aspects.json/.[x|ht]ml	<-- From skills.numbers::skills::disciplines & the future
agencies.json			<-- From skills.numbers::skills::employers & skills.numbers::skills::jobs & skills.numbers::skills::transitions
& agencies.csv			&

narratives.json/.[x|ht]ml	<-- From detailed.pages || summ.pages. 
& narratives.ini.txt		& Ini style text file with plain-text narratives and comments
& narratives.ini.rtf		& Ini style rich text file with formatted narratives and comments


======
======
======
ResumeData.numbers: Copied ResumeWorksop.numbers to new spreadsheet ResumeData.numbers with the intent of trimming down

[**Delete**]
ResumeWorksop.numbers can now be archived for future deletion as interesting and also to recover anything accidentally deleted from ResumeData.



