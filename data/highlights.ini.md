# [Bloomberg]
## Highlights:
-   I developed and enhanced several applications to collect data about financial instruments (securities) from various instantaneous pricing sources both internal and external to Bloomberg and collate    them into files that are delivered to clients.
    -   The data gathering and delivery systems on which I worked, consisted of many instances of many interoperating bits of software, across distributed systems. Market driven changes in our product constantly required new applications as well as enhancements to existing ones.
    -   I worked under the implicit requirement for space and time efficiency. Bloomberg data files are typically very large, often containing several hundred fields and potentially millions of rows.
-   I developed and enhanced parts of the "snap-shot" infrastructure that captures market data as of certain critical moments, particularly closing times for major market centers around the world including New York, London, Tokyo, and Australia.
    -   The infrastructure maintains a pipeline of customer requests respecting enforced delays, time embargoes, customer entitlements, customer portfolios, and customer preferences.
    -   I also developed and enhanced some of the software to monitor the workflow from customer request to customer retrieval.
-   I developed and enhanced applications to perform quality control of our data, including day-over-day differential checks, and formatting checks.
-   I was the principal software engineer on the project to migrate the product we deliver to the Philadelphia Federal Reserve from an older custom infrastructure into the main Data License infrastructure.
    -   Quality control for this project included format and value comparison of a wide spectra of fields for millions of securities without any metadata. I was able to validate the contents of each field against information derived from the whole file.
    -   I was also the principal software engineer in projects to provide the Fed with sample data to answer RFPs for new products under my team's responsibility.
-   I was one of the key developers on a project migrating several classes of mortgage securities from Bloomberg Generic pricing (BGN) to the more accurate Bloomberg Valuation (BVAL) pricing.
-   I developed functionality to configure and manage customer entitlement to orthogonal categories of both securities and fields. Data gathering programs needed very efficient access to customer entitlement and usage for every piece of data written to a file. Field entitlements vary from one security to the next

# [GTRI]
## Highlights:
-   I developed and enhanced applications to monitor and control communications between devices over a MILSTD1553 serial interface and display real-time visualizations of the traffic.
    -   My object-oriented data model allowed very flexible design and implementation of multiple views of the protocol analysis of each type of packet, ranging from visual depictions of elements in the aircraft dashboard, down to raw data, all the way down to individual bits.
    -   I used code structure, self documenting code, and the .Net reflection capabilities of Managed C++ to extract metadata about the meanings of bits and bit sets so that even in hexadecimal and binary raw data views, I show tooltips with interpretive information when the mouse hovers over data.
    -   When communicating with devices on the serial bus, the program can act as bus master or slave, it can emulate the aircraft control system, it can capture traffic, it can playback one side of a captured conversation and monitor/capture the other, and it can control playback of PIR and RADAR sensor data captured during real events in real aircraft.
    -   I developed and enhanced software to control a PCI card that can capture multi-channel PIR data from the system's optical sensors and can playback recorded sequences to the central processor during testing. This software communicates with the card using PCI FIFO channels mapped to virtual memory addresses.
-   I designed and developed an AN/APR-39 (Radar Warning System) simulator that could communicate with a physical AN/AAR-47 (Laser Warning System) and emulate and test the protocols for startup, version detection, and control/display integration for aircraft with both systems.
-   I designed, prototyped, and programmed an electronic device on a powered breadboard in a nicely enclosed package with RS485 over USB connectivity and external power. The Arduino based device controlled several relays and switches including a cascading relay control of the 24VDC 3.5A main power to the test rack. I was assisted in this project by my own interns and an electrical engineering intern. This allowed the software to control the physical configuration of the test rack, reducing human intervention, improving reliability, and enabling long-running overnight test suites.
-   I Developed auxiliary servers and libraries using C++ and C# along with Python interface classes so the binary applications could interoperate with Python in the test framework.

# [Alcatel-Lucent]
## Highlights:
-   Domestic and International Travel. I travelled to Poland, India, Singapore, England and to many cities in the United States for trade shows and to meet with customers, partners and other business units to perform a variety of software lifecycle activities.
-   Software Prototyping and Pre-Sales support. I created several software prototypes and proofs of concept for the set-top-box including a Pandora client using REST and OAuth, an app to browse movies at nearby cinemas, and an Instant Messaging client.
-   I created an Android application to showcase our RDVR, VOD, EPG, video playback and Mediaroom integration at trade shows and client visits.
-   I was a key developer in the architecture and development of one our flagship products which was a mediation layer that among other things, allowed a single Mediaroom instance to be partitioned among multiple service providers via web services using federated authentication along with comprehensive web method authorization.
-   I created an website in ASP.Net to demonstrate the ability to securely log in as one of several different broadcasters and separately manage media, subscribers, channel lineup etc. The website provided fully journaled and audited role-based management of the underlying Mediaroom instance.
-   Development Team Liaison. Most of our development took place outside the USA in distant time zones (primarily Poland and India, and some in England). I acted as a local liaison to the development teams for local managers, customers and deployment teams.
-   I maintained a Mediaroom lab in which I kept recent versions of the software and operating systems in use so I could quickly test reported customer bugs and deployment problems and relay information to the developers and other deployment teams.
-   Deployment. I travelled to customer sites to work directly inside their VHOs (Video Head-end Offices), labs and data centers and with their engineers to deploy our software products.
    -   I installed and configured Windows Server 2008, Windows Server 2008 R2 and Linux on rack servers, blade servers and VMs. I installed and configured SANs, Multi-Path I/O, Database clusters, Windows clusters, Windows domains, Mediaroom servers, and custom software in various network architectures.

# [AT&T]
## Highlights:
-   I developed the Preferences section of the U-Verse application, including the database design, database programming, and capacity planning. This section of the application stores the user's home city, favorite cities, and other user specific preferences. I used C#, ASP.Net, Oracle, PL/SQL, and JavaScript with Ajax.
-   As part of a team, I collaborated closely with our information architects and other developers to create solutions that address the challenges of television applications. The key difficulties we mitigated were:
    -   Entering text and navigating a UI with a hand-held remote.
    -   Visual display elements that looked acceptable on a wide variety of display technologies and qualities.
    -   The user's implicit expectation of the same level of reliability from integrated apps as their television service, much higher than expected from Internet service, or SmartTV apps.

# [Agile Tech]
## Challenges overcome for this project include:
-   A retrograde and unsupported hardware environment. Due to external limitations, the platform was restricted to IE6 on Windows 98 on older computers, with older UARTs. Active-X was the only feasible client side technology available.
-   A retrograde and unsupported development environment. Due to additional limitations, the control could not be pre-installed and had to be configured to auto-install on demand over-the-web with limited user interaction. I developed the control as a single, signed, self-registering, Active-X DLL. The HTML host wrapper declared it via CLSID/GUID with a codebase URL for auto-installation. A signature from a trusted authority allowed for minimally intrusive self installation.
-   The luggage scale's parallel port protocol was asynchronous and extemporaneous. The scale had a non-negligible bounce during which time it continued reporting weight values over the parallel port. I had to make my own determination of the stable weight. The weight displayed on the page was updated but not reported to the backend until it had stabilized. Of course the user could meanwhile be interacting with the page in any way.
-   IE6 hosts Active-X controls strictly in a single-threaded-apartment (STA) where the context and lifetime are tied to the webpage. The control needed to create and manage separate multi-threaded-apartments to create the multiple threads needed to maintain semi-persistent asynchronous communications with the parallel port. The control had to manage its own serialization and synchronization with the main STA, which was tricky because Windows/IE6 has its own separate mechanism for serializing the control's STA.
-   Communicating with the PIN pad was synchronous and more reliable, but navigating the handshaking and security protocols was more complex and time consuming. Testing was limited to a fixed set of predetermined interactions supported by the pad in test mode. I developed the documentation describing the control's properties, methods and events in HTML using JavaScript to implement a collapsible outline.


# [Ipswitch]
## Highlights:
-   My goal for version 7 was to make my FTP engine the fastest in the world. I achieved that goal against all known products available for comparison.
-   To implement a rich modern FTP client, I had to understand and implement many Internet RFCs, and overcome many challenges endemic to the protocol in a modern environment, such as firewalls, encryption, NAT, non-routable addresses, and Port and Passive callbacks.
-   I delved deeply into the Windows SDK, GDI; GUI; shell integration; resource management; internationalization; threading; thunking; algorithms; memory usage; performance; persistence; COM; ATL; SSL; SSH; PKI; digital signatures; key exchange; encryption, and secure sessions.
-   I helped to maintain and administer test environments of FTP and SSH servers on Windows and Linux.
-   As a principal developer, I travelled to and participated in company design and architecture meetings, as well as product feature and strategy meetings.

# [Asymetrix]
## Highlights:
-   I created an Active-X control and a corresponding Netscape plugin that simulated a Sabre® terminal in the web page. It emulated all the usually mapped keys of the terminal along with on-screen status indicators. It allowed the ticket agent the same control of the cursor and tabbing between fields, and allowed interaction with fields other than the correct intended field for the question. It simulated server round-trip updates for both correct and incorrect answers. I also created a version of the plugin as a Java applet.
-   I created an Active-X control and a corresponding Netscape plugin that simulated an airline ticket. The plugin displayed a picture of a ticket, with configurable data in the fields. The user could navigate between and choose fields, and edit the contents of fields.
-   I created pixel-perfect sample quizzes for Microsoft Word and Excel using ToolBook. The test requested the candidate to accomplish a task using menus and shortcut keys. The tester wanted the candidate to have access to the full menu and all shortcut keys so they would not be prompted to the correct answers by limited choices. I took screenshots of all the menus and submenus in Word and Excel, and simulated the menu system in ToolBook complete with mouse tracking, highlighting, sub-menu popups and keyboard accelerators. I wrote most of the painting code in a C DLL which I called from ToolBook scripts. I was also able to simulate limited functionality of some other features such as cut and paste (of specific text - not arbitrary text) but including full emulation of modifier keys for copy vs move with caret and cursor indication.

# [Fed]
## Highlights:
-   I designed and implemented an efficient program to solve a challenging accounting problem that equitably allocated funds orthogonally and hierarchically between various departments, accounts, and projects without losing or gaining pennies. I was able to do this rapidly and correctly despite previous failed attempts by others because of my strong understanding of data structures and algorithms.
-   I developed a check-printing program that communicated with a secure magnetic ink (MICR) printer via its secure protocol. The program converted and spelled out the dollar amount in words on the check.
-   I developed a code strategy for generating dynamic SQL in situations where the equivalent stored procedures contained too many code paths to be maintainable.
-   I developed a query technique to load and display large result sets achieving apparent sub-second latency for queries that had often taken more than a minute.
-   I developed custom data controls for viewing and quickly scrolling through large result sets. My controls were noticeably much more responsive and efficient than the Windows 3.1 controls available at the time. Using simple animation principles, I based the number of fields in dynamic queries based on how fast the scroll position was changing.
-   I created several custom controls and Window classes that emulated the Windows 95 look and feel in the Windows 3.1 environment, including, buttons, checkboxes, property pages, scrollbars and sliders. This required implementing several features at the Windows SDK level in C, including window message loops, tabs, arrow keys, accelerator key, navigating between sibling, parent and child windows, mouse handling and capture, hit tests, client area and child window management, and of course painting.

# [Nova]
## Highlights:
-   I generated custom formatted reports in C++ using the GDI directly. My reports supported typical modern formatting features such as font styles, pagination, repeated headers, column alignments, row grouping etc.
    -   Such reporting functionality is now typically implemented using controls or libraries such as SSRS or Crystal Reports which I have used in subsequent jobs.
-   I used efficient data structures and algorithms to analyze large volumes of transaction data to find suspicious events using criteria designed by the fraud monitoring team.
    -   My data analysis identified which criteria were most effective, and discovered new parameters for monitoring.
    -   I was able to provide this feedback to the fraud team, and incorporate changes as necessary.

# [HVL]
## Highlights:
-   I was a principal software developer on a 2-screen multimedia kiosk for the Army Research Lab DoD Supercomputing Resource Center which allowed the user to navigate a map of the premises on a computer monitor with a joystick, while viewing a synchronized video walkthrough of the route on an attached video monitor.
-   I was a principal software developer on a hypermedia training system for the City of Atlanta's water treatment plant. The HVL published a paper about this project here: [<http://www.sciencedirect.com/science/article/pii/009784939390072H>]
-   I wrote an application to control a single-frame video recorder to record ray-traced animations that were too detailed to be rendered in real time.
-   I wrote a program to create a video animation from experimental data in a paper published by a department professor about using fractals to visualize convergent series. The professor presented the paper and the video at ACM SIGGRAPH '92 in Anaheim which I also attended courtesy of the math department. I was publicly credited for animating the visualization. The paper is available here: [<http://dl.acm.org/citation.cfm?id=100451&CFID=843706001&CFTOKEN=51286743>]
-   I wrote an experimental HyperMedia viewer that navigated between scenes very quickly relative to current technology by saving and reusing the unpacked raster data stored in the device dependent bitmap (DDB) structure that Windows creates when it unpacks a bitmap file.
 