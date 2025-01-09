resume-basis-workshop
Data Provenance

As of November 2024, resume data and files are going into a repository where changes will be tracked.
The entire previous body of resume data and output will be permanently frozen and backed up redundantly in a readonly manner.
Not all files in the new regime will need to be source controlled. In particular, PDFs and other files composed from source-controlled files do not need to be source-controlled.

---------
[Folders]
---------
'$/resume-basis-workshop/budu.co%cv website' --DELETE after
The files from the website as they were in 2016
These files are all tracked as they were. They are part of the starting basis for the repository
~ 2.1 MB: Includes images, downloads, third-party libraries.

'$/resume-basis-workshop/2016 original sources' --DELETE after
Copies of the original sources (Apple Office files) exactly as they were in 2016
~ 1.4 MB:

'$/resume-basis-workshop/2016 original derivations' --ARCHIVE after
Working drafts and intermediate files.
Information and files derived, copied, or exported from the original sources as they were in 2016. 
-- In particular: No data was derived or extracted from "2024 updated sources". 
~ 2.9MB @ 2024-11-05 22:25

'$/resume-basis-workshop/Source controlled basis'
Output of this process. All required resume data stored in text based files that can be tracked in a source control repository.


-----------
[Artifacts]
------------
Useful intermediate files, tools, and journals created during this process will not be placed into source control but will be archived after the basis repository is successfully created.

-------------
[Terminology]
-------------
Competencies:	# Languages and platforms, also technologies and frameworks
		#  - Rows: 12 are shown on budu.co/cv[2016]. Windows, Web, Unix, C++, DotNet, Python, Java, Fortran, PHP, Databases, IPTV, TCP/IP
		#    - The print docs have a different order: C++, DotNet, Python, Java, Fortran, PHP, Databases, IPTV, TCP/IP, Windows, Web, Unix
		#  - Columns: On front page (YOE, star rating, spark rating span, engagement, short description). 
		#    - In other data there are longer descriptions and a complete narrative for each competency.
		#  - a.k.a. Skills. I was thinking of calling this "Skills" but I might reserve that for a broader umbrella including this.
		#  - a.k.a. Technologies - label used for table on file versions of "Detailed Resume"

Disciplines:	# Special areas of expertise within the activities involved in software engineering. 
		#  - Rows: 8 are shown on budu.co/cv[2016]. Multi-Sector, Travel/Consulting, User Experience/UI, 
		         + Multimedia, Education, Team Lead, low level coding, Mobile
		#  - Columns: Narrative of engagement
		# These are the disciplines captured in disciplines.json/.csv in the basis.
		# Only 4 are shown on the print versions: Multi-Sector, Travel/Consulting, Team Lead, low level coding,

Disciplines (II): Activities involved in software engineering that are not captured in the basis but should be added quickly:
		# - Rows: Requirements gathering, Planning, Architecture, Software design, Database design, Capacity planning, Project management,
		        + Prototyping, Programming, Testing, Documentation, User Training, User support, Demoing. 
		# Some of the existing rows under Disciplines should be deleted or moved to other sections such as Industries, Architectures, or Platforms.
		#  - Multi-Sector, Multimedia, Education, low-level coding, Mobile

Aspects:	# All the dimensions along which software development can branch and the axes of those dimensions. 
		# The concerns and puzzle pieces that have to come together to develop software. 
		# - Examples: Development style, environment, activities, attitudes, soft skills, 
		# Concepts, aspects, qualified keywords, or substantiated keywords. Engagement with those concepts.
		#  - Rows: UX/UI, Multimedia, Media Encode/decode, File formats conversion, Data ETL, 
			 + Security, Big Data, Algorithms, low-level coding.
		         + Retail software, Enterprise software, Data Center,  Cloud computing
		         + Desktop, Web, Mobile, Set top box, (LCDP - Limited capabilities device profile),
		         + Requirements gathering, Requirements Analysis, Capacity planning, Database design, Query pattern analysis
		         + Design, Planning, Programming, Testing, Documentation, Delivery, Integration, User Training, Travel/Consulting,
                         + Prototype, Demo, Tradeshow, Sales support, User acceptance testing (UAT), On site liaison,
		         + Full stack, Back end, Front end, Full Stack, Database, Micro service, Shell integration, Automation (scripting)
		         + Arduino, Phone, early x86 specific (80286, 80386, MS-DOS, .COM executables (tiny memory model), early Windows), 
		         + Modet, Big IBM, Big Sun, Indigo, RS6000, Apple II* Xerox Star**, 
		         + Active-X, Netscape Plugin, Java applets, COM/DCOM, Windows GDI, Windows UI Controls
		         + TCP/IP, FTP, SSH, POP3* 
		         + Team leadership, Mentoring, Engagement, Team spirit
		#  - Columns: Engagement
		# - a.k.a. Disciplines - label used for this section on "Summary Resume" and "2016 budu.co/cv".
		# - a.k.a. Competencies - label used for this section on "Detailed Resume"
		# - Alternate names: Concepts, Keywords, Special Skills, Encounters, Notable Expertise

Industries	# Industry, Sector, Field
		#  - Rows: Finance (Trading, Accounting), Education (Test Development, Computer Based Training), 
		         + Healthcare, Defense, Networking, Retail

--------------
[File Formats]
--------------
.[x|ht]ml			# Any or all of xml, xhtml, html. Organization is contextual based on which filetype and the data itself. 
				 - For non-hierarchical html, each record is the innerHTML of a div and the div id is the record label.
				 - Can link shared CSS and/or include own style sheet.
				 - Great for comments, narratives, and data that may need formatting changes tracked.
				 - [x]html Not great for hierarchical or structured data.
.json				# Great for hierarchical data and fields that may contain lists. Great for Document DB storage.
.md				# Not great for this purpose. Will include the already built file in the basis.
.ini/.ini.txt			# More readable than JSON or un-rendered markup, suitable for simple, non-hierarchical structures
.ini.rtf			# Very readable but less automation friendly that plain-text.
				 - Not very readable un-rendered.
.css				# For formatting and presenting html in a trackable way
.xslt				# For formatting and presenting xml in a trackable way

-------------------------
[Source Controlled Files]
-------------------------
[data/]
agencies.json/.csv/.[x][ht]ml	<-- Future? From skills.numbers::skills (::employers & ::jobs & ::transitions) & the future
aspects.json/.[x|ht]ml		<-- Future? From skills.numbers::skills::disciplines & the future
bio.json			<-- From detailed.pages. Future /.[x][ht]ml
competencies.json		<-- From skills.numbers::skills::ratings and skills.numbers::skills::keywords and sparks.csv and stars.csv
				  -  SubSkills from budu.com/cv/competencies.html 
& competencies.csv		&   The flat columns from the skills table. ["Name", Star-level, Years, 3x Description lengths, "Narrative"]
disciplines.csv/.json		<-- From skills.numbers::skills::disciplines. Future /.[x][ht]ml
employers.csv/.json		<-- From skills.numbers::skills::employers & skills.numbers::skills::jobs & skills.numbers::skills::transitions
employment.csv/.json		<-- From detailed.pages + summ.pages via Detailed-Pages.numbers and [skills|HTML-Extracts].numbers
& employment-rt.csv
& employment.no-para.csv/.json
& employment.no-para-rt.csv
& employment.short-para.csv/.json
& employment.short-para-rt.csv
# ------ Redundant versions of the highlights narratives in multiple formats that preserve formatting. I haven't decided on the canonical storage format for formatted highlights but I am currently leaning towards HTML with a canonical stylesheet.
highlights.css			<-- Formatting for highlights.html
highlights.html			<-- From detailed.pages. Each record is the innerHTML of a div identified by id. Future /.x[ht]ml
& highlights.ini.md		<-- From detailed.pages
& highlights.ini.rtf		<-- From detailed.pages. To demonstrate the desired presentation from other formats 
& highlights.txt		<-- Future? Plain text formatting with space indentation and dashes. No bold, no wrap.
jobs.csv/.json			<-- From skills.numbers::skills::jobs
& jobs-rt.csv			<-- Roundtrip back to csv
narratives.html			<-- From detailed.pages. Future /.json/.x[ht]ml from summ.pages
& narratives.ini.rtf		<-- Ini style rich text file with formatted narratives and comments.  
& narratives.ini.txt		<-- Ini style text file with plain-text narratives and comments
spark.csv/.json			<-- From HTML-extracts.numbers::Ratings. No separate JSON. Included in skills.json
& spark-rt.csv			<-- Roundtrip of spark.json to csv
star.csv/.json			<-- From HTML-extracts.numbers::Ratings. No separate JSON. Included in skills.json
star-legend.csv			<-- From detailed.pages.
& star-rt.csv			<-- Roundtrip of star.json to csv
transitions.csv/.json		<-- From skills.numbers::skills::transitions
& transitions-rt.csv		<-- Roundtrip back to csv
# ------ Redundant copies of references data
references.csv/.json		<-- Future? From the future
resume.json/.[x][ht]ml		<-- Future? Combination of all resume data. (Some data may be excluded from some formats). Not formatted for presentation but may be formatted via XSLT.
resume.xsl  			<-- Future? Maybe. A cool exercise on the above.
[web/]				<-- All needed files from the original Go Daddy website. Dependencies 
[artifacts/]			<-- Archivable artifacts generated while processing the data.


------------------
[Filename aliases]
------------------
detailed.pages		# detailed 2016-11-05.pages
summ.pages		# summ-2016-10-19.pages
skills.numbers		# skills 2016-11-07.numbers
HTML-extracts.numbers	# extracted tables 2016 -- 2024-10-02.numbers
Detailed-Pages.numbers	# detailed 2016-11-05.pages -- 2024-11-04.numbers 
			# f. detailed 2016-11-05.pages -- 2024-10-02.numbers
sparks.pages		# sparks 2016-10-20.pages	
functional.svg		# functional 2016-08-16.svg

------------------
[Original Sources]
------------------
detailed.pages		# Detailed resume: Bio(x3), Skills, aspects as Competencies, 14 x Detailed work experience tables.
			#  - via extraction into Detailed-Pages.numbers
			# = bio.json: Keep bio information. Format as single record and free text.
			#  - Bio data is Name, NY Address, Phone number, email, QR code (links), education, references
			# = references.csv/.json: Create references file although no actual references data is in the product.
			# = Highlights.[x|ht]ml/.md/.rtf: From work experience details
			# = employment.csv/.json[ most columns] 
			#= skills.csv/.json 
skills.numbers		# 6 tables of background data in one sheet named skills.
	rating		# Per skill: Skill, YOE, (27x) 27-col star-rating up to (and including) 3 yrs at BB
			# = skills.csv/.json [columns: "Skill", "Years", "27 x Stars" ]
	keywords	# Per skill: Various buzz word collections
			# = skills.csv/.json ["keywords" columns]
	disciplines	# List and description of 8 aspects including Team Lead, Multimedia, Education, Mobile, UX, Travel, low level
			# = disciplines.csv/.json
	jobs		# jobcode to agency, position, dates, and activity summary
			# = employment.csv/.json[ "Performed" column, "id" column]  
	employers	# job code: company, phone, website, address
			# = employers.csv/.json[most columns] 
	transitions	# changes to each company
			# = employers.csv/.json["transitions" columns] & agencies.csv/.json["transitions" columns]
HTML-extracts.numbers   # 7 Sheets total, combination of extracts, primarily from original html pages on website.
			#  - <{}> Original web resume html tables (4 sheets) 
			#  - <{}> Copy of original skills.numbers::skills sheet (1 sheet)
			#  - Ratings sheet with "Star and Spark Ratings" table (1 sheet)
			#  - summ.pages sheet with Work Summary
			# See HTML Sources described below for descriptions of the 4 original files.
			# See "skills 2016-11-07.numbers" above for description of duplicated skills.numbers.skills sheet
			# = sparks.csv, stars.csv
			# = employment["Performed" column]
summ.pages		# <{}+> Two page resume: Bio(x3), Skills, Aspects as Competencies, Work Experience summary table
			#  - Subset of a combination from multiple sources, not a strict subset of a single source
			#  - First page is subset (first page) of Detailed resume. 
			#  - Second page is Work experience Summary table with 2 rows per job: 
			#    - 1st row of each job is 3 cols ["Company", "position", "dates"] 
			#      - already in "Detailed-Pages.numbers::Employment Flat" and skills.numbers::skills::jobs
			#    - 2nd row is ["activity summary (performed)" column] already in skills.numbers::skills::jobs
sparks.pages		# <{}> Subset (first page) of detailed.pages
functional.svg		# {0} Sample svg resume, mashup of Nick's resume data with mine.



# HTML Sources and their csv derivatives. Compiled into HTML-extracts.numbers along with other stuff.
HTML Sources			# <{}> Original web resume + redundant files: welcome.html, versions.html, skills.html, competencies.html
				#  - NOTE: All data already extracted into HTML-extracts.numbers
welcome.html			# 4 tables. Contact info. education, references, 8-row Discipline.
versions.html			# Downloads page, versions table. Links to downloadable versions of resume. Linked to by welcome.html
skills.html			# Scrap file. Not linked to on web. Working copy of welcome.html.
competencies.html		# Scrap file. Not linked to on web. Working copy of Competencies table with different stylesheet. 
				#  - NOTE: All tables from all 4 pages then exported to csv from HTML-extracts.numbers
welcome.arizona.csv 		#
welcome.competencies.csv 	#
welcome.disciplines.csv 	#
welcome.education+referencies.csv
skills.arizona.csv 		#
skills.competencies.csv 	#
skills.disciplines.csv 		#
skills.education+references.csv #
competencies.competencies.csv 	#
competencies.local.competencies.csv 
versions.versions.csv 		#

