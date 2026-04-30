# Dashboard in a Day - Online Workshop (DEVCOM AvMC Edition)

*Source: https://learn.microsoft.com/en-us/training/paths/dashboard-in-a-day/ — Customized for DEVCOM Aviation & Missile Center (AvMC) R&D engineering workload scenario*


# Module 1: Introduction and Prerequisites for Power BI

*Source: [https://learn.microsoft.com/en-us/training/modules/intro-power-bi](https://learn.microsoft.com/en-us/training/modules/intro-power-bi)*


---

## Introduction to Power BI

Microsoft's Power BI is a business analytics tool designed to provide users with comprehensive data analysis and visualization capabilities. It empowers organizations to connect to a wide array of data sources, ranging from simple Excel sheets to complex databases, and transform this data into interactive, insightful dashboards and reports.

With Power BI, users can create and share reports that highlight key performance indicators (KPIs) and trends, facilitating informed decision-making across all levels of an organization.

Its features include real-time analytics, the ability to perform ad-hoc analysis, and the seamless integration with other Microsoft products such as Azure and Office 365, enhancing productivity and collaboration. Power BI's interface and robust data modeling options make it accessible to data professionals and business users alike, ensuring that valuable data insights are always at your fingertips.

Throughout this course, you'll learn how to use these tools made available by Power BI, and acquire the skills to start building your own reports and start analyzing data like a pro.

The course focuses on the main components of Power BI Desktop. These sections highlight the features available in Power BI Desktop and walk the user through the process of exploring dashboards, building visualizations, modeling data relationships, and then understanding how data is loaded and shaped from raw sources.

This course includes steps for the user to follow along, with associated screenshots that provide a visual aid. In the screenshots, sections are highlighted with red boxes to indicate the area the user needs to focus on.

---

## Install the Power BI Desktop application

Note

Power BI Desktop is only available on Windows operating systems. For Mac users consider Boot Camp to setup a Windows partition on your Mac computer. https://support.apple.com/guide/mac-help/use-windows-on-your-mac-mh11850/mac

You must first verify if you have a 32-bit or a 64-bit Windows operating system. To check your operating system type:

From your Windows operating system, open **Control Panel,** select **System and Security**, and then choose **System**.

You'll be able to identify if your operating system is 32-bit or 64-bit based on the **System type** field as shown in the screenshot below.

You must download and install **Power BI Desktop** using any one of the options listed below:

Download and install the **Microsoft Power BI Desktop** from https://aka.ms/pbiSingleInstaller.

If you have a 64-bit Operating System, select the **PBIDesktopSetup_x64.exe** box or if you have a 32-bit Operating System select the **PBIDesktopSetup.exe** box and select **Download**.

After the download is finished, open the file appropriately named either PBIDesktopSetup_x64.exe or PBIDesktopSetup.exe.

In the pop-up window for the Power BI Setup Wizard, select your preferred **Language** and select **Next**.

After the Setup Wizard computes the space requirements, select **Next**.

**Accept** the terms in the License Agreement and select **Next**.

Choose where Power BI should be installed and **select** Next. It's best practice to keep Power BI in the Program Files of your C: drive, and should automatically install to the **C:\Program Files\Microsoft Power BI Desktop\** directory.

Select **Next** after configuring the destination folder, then **Install**.

Finally select **Finish** to complete the installation.

Or if you have Windows 10 or later, you can use the Microsoft App Store to download and install the Power BI Desktop app.

If you already have Power BI Desktop installed, ensure you have the latest version downloaded and installed.

---

## Tour of Power BI Desktop

In this section, we'll learn about the key parts of the Power BI desktop, where we'll ingest data, design data models and build visuals to explore our data.

At the top of the window within the ribbon, you'll see the **Home** tab where the most common operations you perform are available.

![Screenshot of the Home ribbon on Power BI Desktop.](images/home-ribbon.png)

The **Insert** tab in the ribbon allows you to insert shapes, a textbox, or new visuals.

![Screenshot of the Insert tab on Power BI Desktop.](images/insert-ribbon.png)

The **Modeling** tab in the ribbon enables additional data modeling capabilities like adding custom columns and calculating measures.

![Screenshot of the Modeling tab on Power BI Desktop.](images/modeling-ribbon.png)

The **View** tab has options to format the page layout.

![Screenshot of the View tab on Power BI Desktop.](images/view-ribbon.png)

The **Help** tab provides self-help options like guided learning, training videos and links to online communities, partner showcases and consulting services.

![Screenshot of the Help ribbon on Power BI Desktop.](images/help-ribbon.png)

On the left side of the window, you have four icons within the **Navigation** menu: **Report View, Table View**, **Model View**, and **DAX Query View**. If you hover over the icons, you can see the **tooltips**. Switching between these allows you to see the visualizations, tables, relationships, and DAX query editor.

![Screenshot of the report view.](images/views.png)

When in the **Report view**, the center **white space** is the canvas where you'll be creating visuals.

![Screenshot of the canvas for building visuals in Power BI Desktop.](images/canvas.png)

The **Visualizations** pane on the right-side of the window allows you to select visualizations, add values to the visuals, and add columns to the axis or filters.

![Screenshot of the Visualizations pane in Power BI Desktop.](images/visualizations.png)

The **Data** pane is where you see the list of tables, which are generated from queries. By selecting the arrow next to a table name, you can expand the list of fields for that table.

![Screenshot of the data pane.](images/data-pane.png)

---

## Unzip the course files

You must download and unzip the Dashboard in a Day (DIAD) class content.

Download the DIAD starter files (.zip).

Create a folder called DIAD on the C: drive of your local computer.

Copy all contents from the student files to the DIAD folder you created (C:\DIAD).

If you're unfamiliar with how to unzip files, you right-click on the Attendee.zip file and select Extract All.

![Screenshot of the zip file being extracted.](images/extract-zip.png)

Your `C:\DIAD\` directory should now have the folders **Data** and **Reports** in its root.

The .zip includes a pre-built Power BI file called **DIAD-AvMC-Starter.pbix** in the **Reports** folder. This file contains:

- **All data already loaded and transformed** — the R&D Workload, Lab, Program, and Directorate tables are ready to use.
- **A "Completed" page** — a finished report showing what your final dashboard will look like.
- **A "Blank" page** — an empty canvas where you'll build your own visuals step by step.

You'll start by exploring the completed dashboard, then rebuild it yourself. Later in the course, you'll learn how to load and transform data from scratch in a new Power BI instance.

The dataset you'll use for the Dashboard in a Day class is an R&D engineering workload and effort-share analysis. This type of analysis is common for a Technology Director. A Technology Director is focused not only on the organization's internal performance (how effectively our programs execute) but also externally (how our engineering effort compares with partner organizations and allied nations).

DEVCOM AvMC (Aviation & Missile Center) manages aviation and missile technology development across multiple R&D programs, tracking engineering labor hours and research tasks at labs nationwide and with allied partner nations through Foreign Military Sales (FMS) agreements.

Note

There is a problem with the South Korea International Programs data; this is by design so that users can learn how to shape data in a later module.

By the end of the class, you'll build a report, which will look like the screenshot below.

![Final Report Screenshot](images/final-report.png)



# Module 2: Dashboard Overview

---

## Introduction

In this module, you explore a completed Power BI report to understand what you'll be building throughout the course. You'll open the pre-built .pbix file, tour the finished dashboard, and gain familiarity with the data model that powers it.

By the end of this Module, you will:

- Understand the structure of the completed report
- Identify the key visuals and how they interact
- Explore the data model (tables, relationships, and measures)
- Be ready to start building your own version on the Blank page

## Example scenario

You act as the Technology Director for DEVCOM AvMC (Aviation & Missile Center). Your leadership has asked for a dashboard that shows R&D engineering effort across programs, directorates, labs, and allied partner nations. A colleague has already prepared the data and built a reference dashboard — your job is to understand it, then recreate it yourself.

---

## Exercise - Open and explore the completed dashboard

## Section 1: Open the starter file

Open **Power BI Desktop**.

**Sign in** using your Power BI credentials.

![Screenshot of the Power BI Desktop home page.](images/sign-in.png)

From the **File** menu, select **Open report** > **Browse reports**.

Navigate to the **DIAD** folder, then the **Reports** folder (C:\DIAD\Reports).

Select the **DIAD-AvMC-Starter.pbix** file and choose **Open**.

Once the file opens, you'll see two tabs at the bottom of the canvas: **Completed** and **Blank**.

Select the **Completed** tab to view the finished dashboard.

## Section 2: Tour the completed report

Take a moment to explore the completed report page. Notice the following elements:

- **Report title** — "Directorate Analysis" in the header area
- **Directorate slicer** — Logo-based buttons allowing you to filter by directorate
- **Stacked column chart** — Sum of LaborHours by Country, broken down by Directorate groups
- **Treemap** — Sum of LaborHours by Directorate, showing relative effort
- **Line and clustered column chart** — LaborHours and % Growth over time (by Year)
- **Gauge visual** — Current LaborHours vs. prior year target
- **Matrix visual** — Detailed breakdown by Program hierarchy with % Growth and conditional formatting
- **Background image and logo** — Custom branding elements

Select **DEVCOM AvMC** in the directorate slicer and observe how all visuals filter together. This interaction between visuals is called **cross-filtering** — it's one of Power BI's most powerful features.

Try selecting different columns in the charts and notice how other visuals highlight related data. This is **cross-highlighting**.

![Final Report Screenshot](images/final-report.png)

## Section 3: Explore the data model

Now let's look at how the data is organized behind the scenes.

Select the **Model view** icon in the left navigation menu.

You'll see the tables that power this report:

- **R&D Workload** — The main fact table containing labor hours, research tasks, dates, and foreign keys
- **Lab** — Lab location dimension with Country, State, District, and LabCode
- **Program** — Program dimension with Category, Segment, Program name, and TRL Level
- **Directorate** — Directorate dimension with names, logos, and groupings
- **Date** — A calculated date table for time intelligence

Notice the relationships between tables:

- **R&D Workload** connects to **Program** via ProgramID (many-to-one)
- **R&D Workload** connects to **Lab** via LabCode (many-to-one)
- **R&D Workload** connects to **Date** via Date (many-to-one)
- **Program** connects to **Directorate** via DirectorateID (many-to-one)

![Screen that shows the RDWorkload, Lab, Program, and Directorate tables resized, moved with 1 to many relationships.](images/02-move-tables.png)

These relationships allow Power BI to filter across tables — when you select a country in a chart, it filters the workload data to show only labor hours from labs in that country.

## Section 4: Review existing measures

In the **Data** pane, expand the **R&D Workload** table. Notice two DAX measures:

- **PY Labor Hours** — Calculates the prior year's labor hours using time intelligence
- **% Growth** — Calculates the year-over-year growth percentage

These measures enable the time-comparison visuals you saw in the completed report. You'll learn how to write these formulas yourself in Module 4.

---

Now that you understand the completed dashboard and its underlying model, you're ready to start building your own version. In the next module, you'll navigate to the **Blank** tab and begin creating visuals from scratch.

---


# Module 3: Build Your First Data Model

*Source: [https://learn.microsoft.com/en-us/training/modules/build-your-first-data-model](https://learn.microsoft.com/en-us/training/modules/build-your-first-data-model)*


---

## Introduction

In this Module, you learn how to:

Understand how to create relationships to link data property

Learn how to add and use visualizations

Learn how to create groups to organize data

## Example scenario

You continue to act as the Technology Director for DEVCOM AvMC. In this scenario, you need to build a data model for DEVCOM AvMC. Then after you build the model, you need to use visualizations to help show your findings from exploring the data.

Continue to use the **DIAD-AvMC-Starter.pbix** file you opened in Module 2. Navigate to the **Blank** tab at the bottom of the canvas — this is where you'll build your own visuals.

## Tasks to complete

In the first unit, you'll:

Create the model

Explore data

In the second unit, you'll:

Create relationships between the data

Visualize the data

In the third unit, you'll:

Group and bin the data

Use slicers

In the final unit of this module, you'll:

- Create and use a data table

## What is the main goal?

By the end of this session, you're able to:

Create a range of different charts

Highlight and cross-filter

Organize data into bins and groups

Use slicer visuals

Hide data fields from tables

---

## Create model and explore the data

In this section, you learn about the key parts of the Power BI desktop. You also learn how to model and explore the data and build visuals.

Continue to use the **DIAD-AvMC-Starter.pbix** file. Make sure you're on the **Blank** tab.

## Section 1: Data modeling

Go to the main **Power BI Desktop** window.

Select the **Table view** icon in the left navigation menu.

Select and expand the **RDWorkload** table in the **Data** pane.

![Screen that shows the RDWorkload table selected and expanded inside the Data pane.](images/02-RD-table.png)

Scroll up and down to see how fast you can go through millions of rows.

Select the **Model view** icon in the left navigation menu.

You see the tables along with relationships. Power BI supports multiple types of relationships:

1 to many

1 to 1

Many to many

For this exercise, use the 1 to many type of relationship, which is the most common type of relationship.

This means one of the tables involved in the relationship should have a unique set of values. You create other relationships later in the Module.

Drag, resize, and move the tables to appear like those shown in the following screenshot.

![Screen that shows the RDWorkload, Lab, Program, and Directorate tables resized, moved with 1 to many relationships.](images/02-move-tables.png)

Note

Tables might not look the same as shown in this screenshot. You can zoom in and out of the relationship models by dragging the zoom slider in the bottom right corner of the window. Also, if you want to make sure you can see all the tables, use the **Fit to Screen icon**. You can resize the tables by selecting the borders of the tables and dragging them.

Notice that Power BI may have automatically created a relationship between the **Lab** and **RDWorkload** tables. This relationship is incorrect because it doesn't account for duplicate lab codes across countries. You need to delete it before creating the correct relationship in the next unit.

Right-click the **relationship line** between the **Lab** and **RDWorkload** tables to open the **Edit relationship** dialog box. Select **Delete** to remove the relationship. Confirm the deletion when prompted.

![Screenshot that shows deleting the incorrect relationship between the Lab and RDWorkload tables in the Model view.](images/delete-relationship.png)

## Section 2: Data exploration

Now that you've reviewed the model, let's start building visuals. Navigate to the **Blank** tab to begin analyzing the engineering workload by country.

Select the **Report view** icon from the left navigation menu.

Make sure you're on the **Blank** tab at the bottom of the canvas.

Select the **Clustered column chart** visual from the **Visualizations** pane.

![Screen that shows the Clustered column chart visual selected in the Visualizations pane.](images/02-clustered-column-chart.png)

From the **Data** pane to the right of the screen, expand the **Lab** field.

Then, select the **checkbox** next to the **Country** field. The Country field is placed in the **X-axis** box in the **Visualizations** pane.

Still in the **Data** pane, expand the **RDWorkload** table.

Select the **checkbox** next to the **LaborHours** field. The LaborHours field is placed in the **Y-axis** box in the **Visualizations** pane.

**Resize** the visual as needed by dragging the anchor points around the edges of the visual.

![Screen that shows the Country and LaborHours fields selected in the data pane and the Clustered column chart visual resized.](images/02-resize-clustered-column-chart.png)

Note

The Sum of LaborHours for each country is the same. This is because there is currently no relationship between the tables used in the visual. We deleted it! In the next unit, you'll learn more about visualization and how to create missing relationships.

---

## Create missing relationships and use data visualizations

Make sure that you're viewing the **DIAD-AvMC-Starter.pbix** file on the **Blank** tab from the previous unit. Now you can create new relationships that are missing in your report.

## Section 1: Create missing relationships

Currently, there's no relationship between the **RDWorkload** and **Lab** tables, so you need to make one:

Select the **Model** icon in the left navigation menu to go to the **Model view**.

The engineering data is by lab code, so you need to connect the **LabCode** column from the **RDWorkload** table with **LabCode column** in the **Lab** table. Select, drag, and drop the **LabCode** field in the **RDWorkload** table and place on top of the **LabCode** field in the Lab table.

You see the **Create relationship** dialog box opens because there are multiple cardinality options to choose from. The default option of On to Many is automatically selected and the codes are shown for each table as examples.

Select the **Save** button at the bottom of the **Create relationship** dialog box.

![Screenshot that shows the many to many cardinality warning and the cancel button selected inside the create relationship dialog box.](images/03-create-relationship.png)

Go back to the **Report view**.

When you look at the clustered column chart you created earlier, it shows different labor hours for each country or region. The USA has the most labor hours, followed by Australia, then Japan.

Note

If your clustered column chart is missing countries then you might have made an error in the previous module.

By default, the chart is sorted by **LaborHours**. Next, you begin to use data visualization for the data model you designed.

## Section 2: Data visualization

Select the **Clustered column chart** visual.

Select the **ellipses (...)** located near the top right corner of the visual (or, the ellipses might be at the bottom of the chart). You can Sort axis by Country. **Don't make any changes for now**.

![Screenshot that shows the ellipsis selected to reveal the Sort axis option expanded to reveal the Country option.](images/03-sort-by-country.png)

Select the **Clustered column chart** again to close out the options menu.

Then, from the **Data** pane, expand the **Directorate** table.

Drag and drop the **Directorate** column to the **Legend** section of the **Visualizations** pane.

![Screenshot that shows the Directorate column selected and Directorate added to the Legend dropdown.](images/03-directorate-legend.png)

**Resize** the visual as needed in the canvas. Now you can see the top directorates by country.

Now you can try different visuals to see which chart represents the data the best.

With the **Clustered column chart** visual selected in the design space, select and change the chart to a **Stacked column chart** by choosing that visual type in the **Visualizations** pane.

![Screenshot that shows the Clustered column chart selected and changed to a Stacked column chart.](images/03-stacked-column-chart.png)

Select the **ellipses (...)** in the corner of the visual to sort the **legend** in **descending** order.

![Screenshot that shows the ellipses selected to show the Sort Legend option with Sort descending selected.](images/03-sort-descending.png)

If the Filters pane isn't yet expanded, select the **two greater than symbols (>>)** at the top right corner of the collapsed pane to expand it.

In the **Filters** pane, expand **Directorate** under the **Filters on this visual** section. A drop-down arrow will appear for you to expand when you hover your mouse over Directorate.

Using the **Filter type** dropdown menu, select **Top N**.

Enter **5** in the text box next to **Top**.

From the **RDWorkload** table, drag and drop the **LaborHours** field into the **By value** section.

Select **Apply filter** at the bottom of the **Directorate** section in the **Filters** pane to turn on the filter.

![Screenshot that shows a Top N filter applied to show the top five directorates by the Sum of LaborHours.](images/03-top-n-hours.png)

Notice the visual is filtered to display the top five directorates by Sum of LaborHours. The directorate DEVCOM AvMC has a higher share of engineering effort in Australia compared to other countries or regions.

If you want, you can now collapse the **Filters** pane until it's needed again. Now add total labels to the stacked visuals. You start with font formatting options.

Select the **Format visual** (the paintbrush icon) tab at the top of the **Visualizations** pane, and then expand the **X-axis** section.

Select the **Bold** and **Italic** options.

![Screenshot that shows the Format visual icon selected and the Bold and Italic values selected for the X-axis in the Visualizations pane.](images/03-format-visual-bold-italic.png)

Go to the **Total labels** section in the **Visualizations** pane.

Switch the **Total labels** setting to **On**.  Note you may need to scroll down.

![Screenshot that shows the total labels toggle on.](images/03-total-labels-on.png)

Notice the total labels now appear above each of the columns in the Stacked column chart. Any of these properties can easily be changed or turned on/off whenever you like.

Now let's remove the total labels. Select the **On/Off** toggle setting next to **Total labels** to switch the setting to **Off** again.

Switch the setting to **Off**.

Now that you learned various visualization techniques, in the next unit you'll learn how to group elements so that you don't need to add filters to each visual.

---

## Group and bin data

In this unit, you learn the process of grouping data to ensure filters can be applied to multiple elements.

As you continue working as the Technology Director for DEVCOM AvMC, you want to know who are the top five partner organizations by labor hours. For this task, you can group them you don't have to add a filter to every visual. Before you do that, you must remove the Top 5 visual level filter you added earlier.

## Section 1: Create Groups

Select the **Stacked column chart** in the canvas area.

Hover over and select the  **Clear filter** (eraser) icon next to the Directorate field in the **Filters** pane. You might need to expand the Filters pane if you previously collapsed it.

![Screen that shows the clear filter icon on the Directorate field in the Filters pane.](images/04-clear-filter.png)

Note

You'll only see the eraser icon if you hover your mouse over the Directorate filter section.

From the **Data** pane, expand the **Directorate** table.

Right-click on the **Directorate** field.

Note

Do not select the checkbox.

Select **New Group** from the options menu.

![Screen that shows the new group option selected on the Directorate field in the Data pane.](images/04-new-group-manufacturer.png)

Go to the **Ungrouped values** section of the **Groups** dialog.

Use the CTRL key to multi-select: **PEO Missiles & Space**, **DEVCOM ARL**, **SMDC**, and **Industry Partners**.

Select the **Group** button. This adds a new group in the Groups and members section.

![Screen that shows the group dialog box open with directorates selected and the Group button highlighted.](images/04-group-ungrouped.png)

Double-click the newly created group and rename it **Partner Organizations**.

![Screen that shows the new group name of Partner Organizations.](images/04-group-name.png)

Select **DEVCOM AvMC** from the **Ungrouped values** section and select the **Group** button to create the **DEVCOM AvMC** group.

Select the checkbox **Include Other group**. This action creates an **Other** group that includes all the other directorates.

Note

You may need to use the scroll bar along the bottom of the Groups box to move to the right to see the Include Other Group button.

Select **OK** to close the **Groups** dialog box.

![Screen that shows the group dialog box open with the OK button selected.](images/04-groups-dialog-window.png)

Go back to the **Build visual** tab of the **Visualizations** pane.

With the **Stacked column chart** selected in the canvas, select the **X** next to **Directorate** in the **Legend** section of the **Visualizations** pane. This action removes the Directorate field from the Legend.

From the **Data** pane, drag and drop the newly created **Directorate (groups)** to the **Legend** section of the **Visualizations** pane. Now you can see that DEVCOM AvMC has almost all of the effort share in Australia.

![Screen that shows the entry of the Directorate Groups field from the Directorate table to the Legend section in the Visualizations pane.](images/04-manufacturer-groups-legend.png)

Note

It's ok if the colors used in your column chart are in a different order than what appears in the screenshot. You can change the Legend sort order if you want.

Hover over one of the columns in the **Stacked column chart** and right-click.

Select **Show as a table** from the menu. This action starts the **Focus** mode with the chart displayed on top and the data displayed below. You can see DEVCOM AvMC has a large percent of the Australian market.

![Screen that shows the Show as table selected.](images/04-show-as-table.png)

Use the **Orientation** icon in the top right corner of the chart to switch to the **vertical layout**. In this layout, you see the chart in the left panel and the data in the right panel.

Go back to the **horizontal layout**, then select **Back to Report** to go back to the **Report** canvas.

![Screen that shows the horizontal layout of the table screen view.](images/04-show-as-table-view.png)

Note

You can also right-click on a column in the chart and select **Show data point as a table** to see records for a specific data point.

Next, create a **Sum of LaborHours by Directorate** visual. Select the white space in the canvas to deselect the Stacked column chart visual.

From the **Data** pane, select the checkbox next to the **LaborHours** field in the **RDWorkload** table.

From the **Data** pane, select the checkbox next to the **Directorate** field in the **Directorate** table.

From the **Visualizations** pane, select the **Treemap** visual. This action creates a **Sum of LaborHours by Directorate Treemap** visual.

Next, you see how the Stacked column chart and Treemap visual interact with each other.

In the **Treemap** visual, select **DEVCOM AvMC**. You'll see the **Stacked column chart** highlights only the values related to DEVCOM AvMC. This confirms that DEVCOM AvMC has a large share of the Australian workload.

![Screen that shows the selection of the Directorate field and LaborHours field checkboxes, and the selection of the Treemap visual.](images/04-avmc-labor.png)

To remove the highlight, select **DEVCOM AvMC** again. This interaction between visuals is called **cross-highlighting**.

## Section 2: Visual level filters

Earlier in the module, you added a Top 5 Visual level filter. Now you need to add a filter to the Page level, so you can work with the partner organizations and DEVCOM AvMC, and filter out all the other directorates. Make sure the **Filters** pane is expanded and open.

Note

Page-level filters apply to all visuals on the page. Visual-level filters apply only to the visual.

Keep the **Treemap** visual selected.

From the **Data** pane, drag and drop **Directorate (groups)** from the **Directorate** table to the **Filters on this page** box in the **Filters** pane.

Select both **Partner Organizations** and **DEVCOM AvMC**.

![Screen that shows the Directorate (groups) highlighted and Partner Organizations and DEVCOM AvMC both selected on the filters page.](images/04-filters-on-this-page.png)

Now, add a visual that provides labor hours information over time. First, select the white space in the **canvas** to make sure nothing is selected.

Select the checkbox next to the **Date** field in the **RDWorkload** table.

Note

A date hierarchy is created if you have Auto date/time turned on. If you don't see the date hierarchy go to **File** -> **Options and settings** -> **Options** -> **Current file** -> **Data load** -> **Auto date/time** to turn it on.

Select the checkbox next to the **LaborHours** field in the **RDWorkload** table. This action creates a visual.

Change the visual to a **Clustered column chart**. In the X-axis section, a date hierarchy is used. There are arrows on the visual header you can use to go through the hierarchy.

![Screen that shows a Clustered column chart for the Sum of LaborHours by Year and shows a date hierarchy for the X-axis.](images/04-revenue-by-year-chart.png)

You already know from the data that DEVCOM AvMC has a large share of the effort in Australia, but now you want to know how DEVCOM AvMC performed over time in Australia.

Select the **Sum of LaborHours by Country and Directorate (groups)** chart.

Select the **X** in the **Visualizations** pane to remove **Directorate (groups)** from the legend.

![Screen that shows the removal of the Directorate (groups) from the legend.](images/04-delete-group.png)


Select **DEVCOM AvMC** in the **Sum of LaborHours by Directorate** visual (Treemap).

Then, hold the CTRL key and select **Australia** in the **Sum of LaborHours by Country** visual. This action multi-selects and highlights both values.

![Screen that shows the Sum of LaborHours by Directorate treemap visual with DEVCOM AvMC and Australia multi-selected.](images/04-avmc-australia-selected.png)

With both DEVCOM AvMC and Australia selected, you can see consistent growth in labor hours for DEVCOM AvMC in Australia. You decide to investigate this further.

Hover over the **Sum of LaborHours by Year** visual.

Select the **down arrow** at the top of the **Sum of LaborHours by Year** visual to turn on the **Drill Mode**.

![Screen that shows the Sum of LaborHours by Year visual with the drill mode turned on.](images/04-drill-down.png)

Select the **2024** column in the **Sum of LaborHours by Year** visual.

Now that you drilled down to the quarter level of 2024, you Q2 is somewhat low. You decide to investigate more.

Select the **double down-arrow** icon at the top of the **Sum of LaborHours by Year and Quarter** visual. This action drills down to the next level of the hierarchy, which is the **month** level.

![Screen that shows the double down arrow selected to show a Clustered column chart visual for the Sum of LaborHours by month.](images/04-by-month.png)

Select the **up-arrow** icon at the top of the **Sum of LaborHours by Month** visual to drill back up to the **Quarter** level again.

Select the **drill up** icon a second time to go all the way back up to the **Year** level.

Select the **split arrow** icon at the top of the **Sum of LaborHours by Year** visual. This action expands down to the next level of the hierarchy, which is quarters for all the years; not just 2024.

![Screen that shows the split arrow icon selected on the Clustered column chart for the Sum of LaborHours by Year and quarter visual, to see quarters for all years.](images/04-all-months-all-years.png)

Resize the visual as needed. You notice the first-quarter effort is always high.

Expand down one more time to the month level to investigate. Select the **split arrow** icon for the **Sum of LaborHours by Year and Quarter** visual again. This action drills down to the next level of the hierarchy and shows labor hours for months for all the years.

![Screen that highlights the selection of the split arrow button for the visual that isn't drilled down to the month level for every year.](images/04-quarters-for-all-years.png)

## Section 3: Use slicers

Now you want to add a slicer to filter the data by the directorates.

Make sure there are no filtered or highlighted values.

**Be sure to reset all visuals to stop highlighting selected values.** If you have values selected, select the blank space of the Sum of LaborHours by Country visual. This action clears any selected values.

Select the white space in the canvas to deselect any currently selected visuals.

From the **Data** pane, select the checkbox next to the **Directorate** field in the **Directorate** table.

From the **Visualizations** pane, select the **Button Slicer** visual.

![Screen that highlights the selection of the checkbox for the Directorate field, and the Slicer visual from the Visualizations pane.](images/04-slicer-visual.png)

Select **DEVCOM AvMC** from the list of Directorates. You see all the visuals are filtered based on your selection. Also, select **Australia** in the **Sum of LaborHours by Country** visual.

With the **Slicer** visual still selected, go to the **Format visual** tab of the **Visualizations** pane.

Expand the **Slicer settings** menu. Then, deselect the **Single Select** option.


![Screen that shows the selection of the drop-down style option for the Slicer settings, and the selection of DEVCOM AvMC from the drop-down within the slicer visual.](images/04-slicer-format-dropdown.png)

Make sure you still have **Partner Organizations** and **DEVCOM AvMC** selected in the **Directorate (groups)** filter in the **Filters** pane.

Note

There is a box for **Filters on all pages** in the **Filters** pane. If you have more than one report page, this is how you sync a filter for the whole file.

Now you can use the **Directorate** slicer to analyze one directorate at a time. First, deselect the **Australia** column in the **Sum of LaborHours by Country** visual to remove the filter by country.

Next, select the **Sum of LaborHours by Directorate** (Treemap) visual.

From the **Visualizations** pane, navigate to the **Build visual** tab and select the **Card** visual. The card visual gives us the **Sum of LaborHours** as we filter and cross-filter the visuals.

![Screen that shows the selection of the Card visual type for the Sum of LaborHours visual.](images/04-card-visual.png)


You see all key dimensions are in tables with related attributes, except for the date. For example, **Program** attributes are in the **Program** table. **Directorate** attributes are in the **Directorate** table. In the next unit, you'll create a **Date** table.

---

## Create a date table

Make sure you still have the **DIAD-AvMC-Starter.pbix** file open from the previous units. You use it to create a Date table.

## Create a date table

Go to the **Table** view by selecting the **Table** icon in the navigation menu to the left of Power BI Desktop.

From the ribbon at the top of the screen, select the **Table Tools** tab.

Then, choose **New Table** from the menu at the top of the screen.

![Screenshot that shows the selection of the Table view icon button, and the location of the New Table button under the Table Tools tab.](images/05-new-table.png)

You see a new table called "Table" is created in the **Data** pane to the right of the Power BI Desktop and the formula bar opens at the top of your screen.

Enter the following formula in the formula bar, then hit **Enter** on your keyboard:

`Date = CALENDAR(DATE(2020,1,1), DATE(2026,12,31))`

You're using two DAX functions: the **CALENDAR** function, which accepts the start and end data, and the **DATE** function, which takes the year, month, and day fields.

For this scenario, you need to create dates from 2020 to 2025 (since we have data for those years). We can also add more fields, like **Year**, **Month**, **Week**, etc., to the table by using other DAX functions.

In the **Data** pane, select the **Date** field in the **Date** table.

![Screenshot that shows the Date field selected in the Date table, inside the Data pane.](images/05-date-field.png)

The Date field is in the **Date/Time** data type, but you need it to be the **Date** data type. To change it, select the **Column Tools**  tab from the ribbon.

Then, choose the **Data type** drop-down and select **Date**.

![Screenshot that shows the Date/Time data type get changed to the Date data type on the Column Tools tab.](images/05-data-type-date.png)

Now, you need to create a relationship between the **Date** and **RDWorkload** tables. From the ribbon, select the **Column Tools** tab, and then choose **Manage Relationships**.

The **Manage Relationships** dialog box opens. Select the **+ New relationship** button.

![Screenshot that shows the Manage Relationships dialog box with the new button selected.](images/05-new-relationship.png)

Then, the **New Relationship** dialog box opens. Select **Date** from the top dropdown menu.

Select **RDWorkload** from the second dropdown menu.

Highlight the **Date** field in both tables by multi-selecting.

Then, select **Save** to close the **New relationship** dialog box.

![Screenshot that shows a Date relationship created between the Date and RDWorkload tables, and the Save button selected.](images/05-create-date-relationship.png)

Select the **Close** button to close the **Manage relationships** dialog box.

Now, select the **Report view** icon in the left navigation menu to go to the **Report view**.

![Screenshot that shows the report icon selected to show the report view.](images/05-report-view.png)

The Sum of LaborHours by Date chart looks different now. Let's fix that.

Select the **Sum of LaborHours by Date** visual.

From the **X-axis** section in the **Visualizations** pane, select the **X** to remove the **Date** field.

From the **Data** pane, expand the **Date** table.

Now, drag and drop the **Date** field from the **Date** table to the **X-axis** section in the **Visualizations** pane.

Select the **Drill up** button above the visual until the visual is on the **Year** level.

![Screenshot that shows the Drill up button selected until the visual shows the labor hours data on the Year level.](images/05-add-date-axis.png)

Now, the new **Date** field behavior is like it was previously.

Since there are now two **Date** fields, you might be confused which one to use. To remove confusion, hide the **Date** field in the **RDWorkload** table.

From the **Data** pane, hover over and select the **ellipses (...)** to the right of the **Date** field in the **RDWorkload** table.

Then, select **Hide** from the options menu.

![Screenshot that shows the Date field hidden in the RDWorkload table, inside the Data pane.](images/05-hide-date.png)

Use the preceding steps to hide **Country**, **ProgramID**,  **LabCode**, and **Source.Name** in the RDWorkload table as well. The only fields that should now be in the **RDWorkload** table are **LaborHours** and **ResearchTasks**.

Then, hide **DirectorateID** from the **Directorate** table.

Hide **ProgramID** and **DirectorateID** from the **Program** table.

Tip

It's best practice to hide fields that are not used in your report visuals. These fields are the basis of our relationships between each table so we should not delete them.


# Module 4: Use Hierarchies and DAX in Your First Data Model

*Source: [https://learn.microsoft.com/en-us/training/modules/use-hierarchies-dax-first-data-model](https://learn.microsoft.com/en-us/training/modules/use-hierarchies-dax-first-data-model)*


---

## Introduction

In this module, you learn how to:

Create hierarchies for organizing data

Add and use matrix visualizations

Add DAX measures to models for further analysis

## Example scenario

You continue to act as the Technology Director for DEVCOM AvMC. In this scenario, you need to add a hierarchy to the data model you created for DEVCOM AvMC in Module 3. Then after you add hierarchies to the model, you need to use a matrix visualization and DAX measures for further analysis.

## Tasks to complete

In the first exercise, you'll:

- Use a hierarchy in your data model

In the second exercise, you'll:

- Build a matrix visual

In the final exercise of this module, you'll:

- Add DAX measures to your data model

## What is the main goal?

By the end of this session, you're able to:

Use and create matrix visuals

Add hierarchies to data models

Drill up and drill down

Write DAX expressions

Add DAX measures to models

Use calculated columns

---

## Use hierarchies in your data model

Make sure you're currently viewing the **DIAD-AvMC-Starter.pbix** file on the **Blank** tab from the previous units. 

In this exercise, you explore the use of hierarchies in your first data model and how to create them.

You're still the Technology Director for DEVCOM AvMC in this exercise and you need to model the data for the US, DEVCOM AvMC and 2024. You want to analyze the labor hours by country, then by state, and then by district. To do that, you can create a hierarchy with the fields Country, State, and District.

Select the **Sum of LaborHours by Country** visual.

From the **Data** pane, drag and drop the **State** field from the **Lab** table below the **Country** field in the **X-axis** section of the **Visualizations** pane.

![Screenshot that shows the State field from the Lab table, placed below the Country field, within the X-axis field of the Sum of LaborHours by Country visual.](images/state-x-axis.png)

Drag and drop the **District** field from the **Lab** table below the **State** field in the **X-axis** section of the **Visualizations** pane. You just created a hierarchy.

Select the **up arrow** in the **header** area of the visual twice to **Drill up** to the top level of the hierarchy again.

Make sure that **DEVCOM AvMC** is still selected in the **Directorate** slicer.

Turn on the **Drill down mode** by selecting the **down arrow** of the **Sum of LaborHours by Country** visual once.

Select **Australia** to drill down to the **State** level.

From the **Sum of LaborHours by Year** visual, select 2024 and notice what happens to the **Sum of LaborHours by Country**.

Tip

If you notice this step performs a drilldown into a table of data, select **Back to report**, then **Data / Drill**, and disable *Data point table* in the ribbon.

Now, **Drill up** to the **Country** level again.

**Turn off** drill mode by selecting the down arrow again on the **Sum of LaborHours by Country** visual. Now analyze the data by program. To start, create a program hierarchy.

Make sure that no visuals are selected in the design canvas.

From the **Data** pane, **right-click** the **Category** field in the **Program** table

Select **Create Hierarchy**.

![Screenshot that shows the Create Hierarchy option after right-clicking on the Category field within the Program table.](images/create-hierarchy.png)

You see a new object called **Category Hierarchy** is created inside the **Program** table.

Double-click **Category Hierarchy** and rename it to **Program Hierarchy**.

**Right-click** the **Segment** field in the **Program** table, select **Add to Hierarchy**, then choose **Program Hierarchy**.

Use steps 11-16 to add the **Program** field from the Program table to the Program Hierarchy. You created a Program Hierarchy with the fields **Category**, **Segment**, and **Program**.

![Screenshot that shows the newly created Program Hierarchy within the Data pane.](images/product-hierarchy.png)

Select the white space in the canvas to deselect any visual that might be selected.

From the **Visualizations** pane, select **Clustered bar chart**.

![Screenshot that shows the selection of a Clustered Bar Chart visual from the Visualizations pane.](images/clustered-bar-chart.png)

With the **Clustered bar chart** still selected, from the **Data** pane, expand the **Program** table.

Select the **checkbox** to the left of the **Program Hierarchy**. Notice the complete hierarchy is selected.

From the **Data** pane, expand the **RDWorkload** table.

Select the **checkbox** to the left of the **LaborHours** field.

Note

The **Program Hierarchy** is added to the **Y-axis** field and **Sum of LaborHours** is added to the **X-axis** field in the **Visualizations** pane. You see the visual in the canvas change and update as you select different fields.

![Screenshot that shows the selection of the Program Hierarchy and LaborHours field for the Clustered Bar Chart visual.](images/product-hierarchy-bar-chart.png)

---

## Build a matrix visual

Now, add a Matrix visual so you can view the data in rows and columns. You can apply conditional formatting to the Matrix visual to highlight the outliers.

Select the **Sum of LaborHours by Category** Clustered bar chart and change it to a **Matrix** visual.
Select the **+ (plus sign)** to the left of the **Future Vertical Lift** row to drill down.

![Screenshot shows the location of the plus sign for the Future Vertical Lift row used to drill down within the Matrix visual.](images/plus-sign-drill-down.png)

Next we'll add a *percent of total* field to the visual, enabling a better perspective of the data. With the **Matrix** selected, go to the **Data** pane.

From the **Data** pane, drag and drop the **LaborHours** field from the **RDWorkload** table to below the existing **Sum of LaborHours** field in the **Values** section of the **Visualizations** pane. It will look like **Sum of LaborHours** is in the **Values** section twice.

Select the **down arrow** to the right of the newly added **Sum of LaborHours** field in the **Values** section.

From the visual field menu, hover over **Show value as**.

Then, select **Percent of grand total**.

![Screenshot shows the location of the Percent Grand Total from the Show value as option for the newly added Sum of LaborHours field.](images/percent-of-grand-total.png)

Right-click on the newly created field in the Visualization - Values section and select **Rename for this visual**.

Name the field **%GT LaborHours**.

Drill back up to **Category** level if you aren't already there in the **Matrix** visual.

Then, select **Enable drill down mode** in the header of the Matrix visual.

Now, select the word **Future Vertical Lift**.

![Screenshot shows the selection of the drill-down arrow for the Matrix visual and the selection of the Future Vertical Lift category.](images/future-vertical-lift-drill-down.png)

Make sure that the **Matrix** visual is still selected. Then, hold down the **Ctrl** key to multi-select the **2024** column in the **Sum of LaborHours by Year** visual and the **Australia** column in the **Sum of LaborHours by Country** visual.

Now, look at the **Systems Integration** category for Australia over time. Notice the **SI** segment has around **60%** of the grand total.

Resize the visual as needed.

---

## Build DAX measures

Now, we need to  create a **Percent Growth** calculated measure so you can compare engineering effort over time.

Before you start, learn the difference between a measure and a calculated column:

- A *Calculated Column* is evaluated row-by-row. You extend a table by adding calculated columns.

- A *Measure* is used to aggregate values from many rows in a table.

Tip

Calculated columns are often better suited to be created in the Power Query Editor or as part of the data importing process because of the row-by-row evaluation mentioned above.

In the **Data** pane, select the **RDWorkload** table.

From the ribbon at the top of the screen, select the **Table Tools** tab, then select **New Measure**. A formula bar appears.

Enter the formula:

`PY Labor Hours = CALCULATE(SUM('R&D Workload'[LaborHours]), SAMEPERIODLASTYEAR('Date'[Date]))`

![Screenshot that shows the formula typed into the formula bar.](images/py-sales-dax.png)

Select the **checkmark** to the left of the formula bar or hit **Enter** on your keyboard. You'll see the **PY Labor Hours** measure created in the **RDWorkload** table.

![Screenshot that shows the addition of the PY Labor Hours measure within the RDWorkload table.](images/py-sales-measure.png)

Now, create another measure using a different method. In the **Data** pane, **right-click** the **RDWorkload** table.

Select **New Measure** from the options menu. A formula bar opens.

In the formula bar, enter the following formula:

`% Growth = DIVIDE(SUM('R&D Workload'[LaborHours])-[PY Labor Hours],[PY Labor Hours])`

Select the **checkmark** next to the formula bar or hit **Enter** on your keyboard. You'll see the **% Growth** measure is added to the **RDWorkload** table.

Make sure the **Matrix** visual is still selected. If not, select the **Matrix** visual and check that you still have the **Australia** and **2024** columns selected in the other visuals.

In the **Data** pane, select the **checkbox** next to the newly created **PY Labor Hours** and **% Growth** measures in the **RDWorkload** table. This action adds the measures to the **Values** section of the **Matrix**.

Resize the **Matrix** to see the newly added fields (you might also have to adjust the size of the other visuals where needed).

![Screenshot that shows the selection of the % Growth and PY Labor Hours measure checkboxes, as well as the changes made to the matrix visual.](images/add-matrix-measures.png)


To format the fields, start from the **Data** pane, select the **% Growth** field (the name, not the checkbox) in the **RDWorkload** table.

From the ribbon at the top of the screen, select the **Measure Tools** tab, choose the **Format** drop-down.

Then, select **Percentage**.

Tip

If your **% Growth** calculated measures show as 0.00% at any point, check that you still have **2024** and **Australia** selected as filters from the other visuals.

From the **Data** pane, select the **PY Labor Hours** field (the name, not the checkbox) in the **RDWorkload** table.

From the ribbon at the top of the screen, select the **Measure Tools** tab, choose the **Format** drop-down.

Then, select **Fixed decimal number** and change the number of decimal places from **Auto** to **2**.

From the Data pane, select the **LaborHours** field in the **RDWorkload** table.

Now, choose the **Format** drop-down under the **Column tools** tab, select **Whole number**.

Make sure you still have **Australia** selected in the **Sum of LaborHours by Country** visual, and you still have the **2024** column selected in the **Sum of LaborHours by Year visual**. Notice the programs show significant growth compared to last year.



# Module 5: Data Visualization and Reports in Power BI

*Source: [https://learn.microsoft.com/en-us/training/modules/data-visualization-reports-power-bi](https://learn.microsoft.com/en-us/training/modules/data-visualization-reports-power-bi)*


---

## Introduction

Continue to use the **DIAD-AvMC-Starter.pbix** file from the previous module.

In this Module, you still are the Technology Director of DEVCOM AvMC, and you need to create a full report that you publish to the Power BI Service in a later module. You learn how to do conditional formatting, add a logo to the directorate filter, and apply a custom theme to the report.

The flow of this Module includes screenshots to provide a visual aid for the users and a text description of the steps the user needs to follow. In the screenshots, sections are highlighted with red boxes to indicate the action or area on which you need to focus.

---

## Apply conditional formatting

## Conditional formatting

Now that we made a data model and added visuals, you now create a full report.

Let's get started. We begin where we left off at the end of **Module 4** within the **DIAD-AvMC-Starter.pbix** file.

With the **Matrix** visual selected, navigate to the **Values** section in the **Visualizations** pane.

Select the arrow to the right of **% Growth**.

Select **Conditional Formatting** and then choose **Background color**. The **Background color** dialog box opens. This dialog provides options to format the report background color using either rules or diverging colors.

![Screenshot highlights the location of the Background color option from the Conditional formatting option extension for the % Growth value.](images/background-color.png)

In the **Background color - % Growth** dialog box, select the **Add a middle color** checkbox.

Then, select **OK.**

![Screenshot highlights the selection of the Add a middle color button within the dialog, and the location of the OK button.](images/add-middle-color.png)

Note

Conditional formatting can also be based on another column using the **Color based on** option from the drop-down menu.

Note

As a reminder if you see 0.00% for every value in the **% of Growth** column in the Matrix then you likely need to multi-select **Australia** and **2024**, and drill-down to the **Extreme** catageory in the **Matrix** visual, like you did in **Module 4**.

Make sure the report is filtered by **DEVCOM AvMC** using the **Directorate** slicer.

Select the **down arrow** in the header of the **Sum of LaborHours by Country** visual to turn on the **drill down** mode *(this could also be located at the bottom of the visual based on how you placed the visual within the canvas)*.

Within the visual, select the **Australia** column to drill down to the **State** level.

**Disable** drill down mode on the **LaborHours** **by** **Country and State** visual.

Make sure you still have the year **2024** selected in the **Sum of LaborHours by Year** visual. If you don't, hold down the **Ctrl** key on your keyboard and select the **2024** column.

At this point, your canvas and visuals should look like the figure here. You can resize and move visuals as you need.

![Screenshot displays the current canvas and visuals.](images/example.png)

---

## Exercise - Add a logo to the directorate filter

In this unit, we continue adding more functionality and visual elements to help wrap up our report. Ensure that you're working on the **DIAD-AvMC-Starter.pbix** file that you have been using in the previous units.

## Section 1: Add a logo

Now it would be nice to add logos of the directorate to the Slicer instead of just text. Let's do it.

Check that the **Directorate** slicer visual is still selected. From the **Data** pane, select the **Logo** field from the **Directorate** table. (*Do not* select the checkbox; only select the *name* of the field.)

From the ribbon, select the **Column tools** tab and choose the **Data Category** drop down.

Then, select **Image URL.** Setting the data category property to **Image URL** helps Power BI understand that the data in this field is a URL so it can render the image in the report.

![Screenshot highlights the selection of the Logo field from the Directorate table, and the selection of the Image URL option for the Data category.](images/image-url.png)

With the **Slicer** visual selected, drag and drop the **Logo** field from the **Directorate** table to below the **Directorate** column in the **Value** box in the **Visualizations** pane.

Select the **X** to the right of the **Directorate** field in the box so that the **Logo** field replaces it.

![Screenshot highlights the addition of the Logo field from the Directorate table to the Value box for the slicer visual.](images/slicer-logo-field.png)

The logo images may appear too large for the buttons. To fix this, with the **Slicer** visual still selected, go to the **Format visual** tab (paint brush icon) in the **Visualizations** pane. Expand **Slicer settings**, then expand the **Image** section. Change the **Image fit** to **Fit**. 

![Screenshot highlights the Image section under Slicer settings in the Format visual pane, showing Image size and Inner padding options.](images/format-button-images.png)

Next, arrange the slicer buttons into a grid layout. Still in the **Format visual** tab, expand the **Grid** section under **Multi-Button Layout**. Set **Rows** to **2** and **Columns** to **4**. This arranges the directorate logos in a compact 2×4 grid so they fit neatly within the slicer visual.

**Resize** and **move** the visuals as needed.

Select the **DEVCOM AvMC** logo in the **Directorate** slicer visual to filter all the other visuals.

Select the **Sum of LaborHours by Year** visual.

From the **Visualizations** pane, select the **Line and clustered column** chart to change the visual type.

From the **Data** pane, drag and drop the **% Growth** field from the **RDWorkload** table to the **Line y-axis** box.

This provides a representation of the labor hours and growth over time.

![Screenshot highlights the selection of the line and clustered column chart visual type, and the addition of the % Growth field within the Line Y-axis field.](images/line-clustered-column-chart.png)

## Section 2: Gauge visual

Now, let's select the **Sum of** **LaborHours** card visual so we can change it to a **Gauge** visual.

Select the **Sum of LaborHours** card visual, and from the **Visualizations** pane, select the **Gauge** visual.

From the **Data** pane, drag and drop the **PY Labor Hours** field from the **RDWorkload** table to the **Target value** in the **Visualizations** pane.

![Screenshot highlights the selection of the Gauge visual type and the addition of the PY Labor Hours field within the Target Value field.](images/gauge-visual.png)

**Resize** and **move** the visuals as needed. Now we can compare **LaborHours** with the target.

Next we'll select the colors for this visual.

Select the **Gauge** visual.

From the **Visualizations** pane, select the **Format Visual** tab (*the paint brush icon*).

Expand the **Colors** section.

Select the drop-down for **Fill** color.

Notice you can pick a color from the default color palette or pick **More colors**. No need to make a change here because the next steps will standardize all the report colors used.

![Screenshot highlights the location of the Fill color drop down for the Gauge visual under the Format visual tab of the Visualizations pane.](images/fill-color.png)

Let's check out some of the **themes** available.

Ensure that the **Gauge** visual is still selected.

From the ribbon, select the **View** tab and choose the drop-down arrow within the **Themes** menu.

Then, select the **Temperature** theme.

![Screenshot displays the various available themes.](images/themes-menu.png)

Notice that the colors on all the visuals are updated. Feel free to try the other out-of-the-box themes.

Now that we covered adding logos to the directorate slicer, changed the clustered column chart, adapted the card visual to a gauge, and looked through report themes, in the next unit we'll cover the application of custom report themes.

---

## Exercise - Apply a custom report theme

In our scenario, Leadership is unhappy with the current report colors. They have instructed the S6 to use standard color themes to be used across reports. We can use the **Report Theme** feature in Power BI by uploading a theme. The **Report Theme** requires a **JSON file** where the data colors, background, foreground, and a table of accent colors are defined. The JSON file can be used across all the reports.

Make sure you're using the **DIAD-AvMC-Starter.pbix** file you've been working on in the previous units.

## Section 1: Apply a custom report theme

From the ribbon, select the **View** tab and choose the drop-down within the **Themes** menu.

Then, select **Browse for themes**.

![Screenshot highlights the location of the Browse for themes button within the Themes drop-down under the View tab.](images/browse-themes.png)

A file browser dialog box opens. Navigate to the **Data** folder, then the **Theme** folder (DIAD/Data/Theme).

Select the **DIADTheme2** file and then choose **Open**.

![Screenshot highlights the selection of the theme file within the file browser dialog.](images/theme-file-select.png)

Note

Here you can save and add your custom themes.

Once the theme is imported, a success dialog box opens. Select **Got it**.

![Screenshot highlights the location of the Got it button within the success dialog.](images/file-successfully-added.png)

Notice colors on all the visuals are updated. Your report should look like the figure below. This theme looks good. Now, most of the visuals are blue, so let's add some contrast.

![Screenshot highlights the new theme applied to the report visuals.](images/example-canvas.png)

## Section 2: Other formatting options

Now that we have our own custom theme applied, let's make more formatting changes for the theme to stand out.

Select the **Gauge** visual.

From the **Visualizations** pane, select the **Format visual** tab (*the paint brush icon*).

Expand the **Colors** section.

Select the drop-down menu below **Target color**. Notice the color palette is different now.

Select the color **black.** Notice the subtle change to the target line in the visual.

Collapse the **Colors** section.

In the **Visualizations** pane, under the **Format visual** tab, expand the **Data labels** section.

Then, expand the **Values** section and change the **Font** **size** to **10**.

While still in the **Visualizations** pane, expand the **Target label** section under the **Format visual** tab.

In the **Values** section, change the **Font size** to **10**.

Select the **Matrix** visual.

Using the arrows within the visual header, **Drill up** to the **Segment** level.

Select the **Sum of LaborHours by Country and State** visual.

Using the arrows within the visual header, **Drill up** to the **Country** level.

While the **Sum of LaborHours by Country** visual is still selected, in the **Visualizations** pane, select the **Format visual** tab (*the paint brush icon*).

Expand the **Columns** section, then the **Color** section.

Using the drop-down menu, select a *light shade* of **gray** as the **Default color.**

Check that the **Sum of LaborHours by Country** visual is still selected.

In the **Visualizations** pane under the **Format visual** tab, turn **On** the **Data labels**, and expand this section.

Expand the **Value** sub-section in the **Data labels** section.

Change the **Display units** to **Millions**.

Notice there are many formatting options. For example, a visual title can be changed and formatted, or you can add a border and background to the visual. Feel free to explore other options.

Let's move to another visual.

Select the **Sum of LaborHours and % Growth by Year** visual.

Note

You may need to move or resize the visuals to see all the information that will be needed in the next steps.

Since there's no **LaborHours** value in the year **2026**, right-click on the line above **2026** and select **Exclude**.

![Screenshot highlights the Exclude option after right-clicking on the line above the year 2026 within the visual.](images/exclude.png)

Next, from the **Visualizations** pane, select the **Format visual** tab (*the paint brush icon*).

Expand the **Columns** section.

Expand the **Color** section.

Select a *light shade* of **gray** as the **Default color**.

Check that the **Sum of LaborHours and % Growth by Year** visual is still selected. You can collapse the **Columns** section.

In the **Visualizations** pane under the **Format visual** tab, expand the **Lines** section.

Then, expand the **Color** section.

Set the % **Growth** color to **black**.

---

Now let's add a **report title**.

From the ribbon, select the **Home** tab and then choose **Text box** under *Insert*. Notice a text box visual is added.

Resize and move the visuals as needed.

Enter `Directorate Analysis` in the text box.

Highlight **Directorate Analysis** to format the text.

Select **Segoe (Bold)** as the **font**.

Select **32** as the **font size**.

Resize the text box as needed.

![Screenshot highlights the addition of a text box displaying Directorate Analysis in the font Segoe Bold, size 32.](images/text-box-options.png)

From the ribbon, select the **View** tab.

In the **Page options** section, select the **checkboxes** next to **Visual_Gridline_Show** and **Snap to grid**. This helps with aligning the visuals.

![Screenshot highlights the selection of the Gridlines and Snap to Grid tools located under the View tab.](images/gridlines-snap.png)

Now, use the **Gridlines** and **Snap to grid** features to **position** and **resize** your visuals like the figure below.

Uncheck the **Gridlines** and **Snap to grid** options to disable these features once you finish moving the visuals into the correct places.

![Screenshot displays the rearranged visuals within the report, and highlights the deselected Gridlines and Snap to Grid tools under the View tab.](images/placement-example.png)

**Right-click** the page name in the lower-left corner.

Then, select **Rename Page** from the options menu.

**Rename** the page to **Directorate**.

![Screenshot displays the page renamed to Directorate.](images/rename-page.png)

Now that we have a basis for the report, in the next Unit we'll cover how to import and implement custom visual elements.




# Module 6: Import Custom Visuals and Add Bookmarks

*Source: [https://learn.microsoft.com/en-us/training/modules/import-custom-visuals](https://learn.microsoft.com/en-us/training/modules/import-custom-visuals)*


---

## Introduction

Continue to use your **DIAD-AvMC-Starter.pbix** file from the previous module.

In this Module, you still are the Technology Director of DEVCOM AvMC, and you need to complete your report. You learn to import custom visuals and add bookmarks to your report to prepare your report to publish to the Power BI Service.

---

## Exercise - Import custom visuals

Power BI comes with many stylization options out of the box, but users are also given the opportunity to import their own visuals. Let's go over this process.

Make sure you're using the **DIAD-AvMC-Starter.pbix** file you have been working on in the previous units.

## Section 1: Add background images

We can use a background image to format the report. Let's try it.

Select the white space in the canvas to deselect any selected visuals.

From the **Visualizations** pane, select the **Format page** tab (*the paint brush icon*).

Expand the **Canvas Background** section.

Select the **Browse Image** button.

![Screenshot highlights the location of the Browse button within the Canvas Background section.](images/canvas-background.png)

A **File** browser dialog box opens. Browse to the **DIAD** folder, then the **Data** folder (DIAD/Data).

Select the **Background.jpg** file.

Select the **Open** button.

![Screenshot highlights the selection of the Background file within the File browser dialog.](images/background-file-explorer.png)

Within the **Canvas background** section of the **Visualizations** pane, change and set the **Transparency** slider to **0%**.

![Screenshot displaying the Canvas background sub-section of the Visualizations tab highlighting the transparency value.](images/canvas-background-transparency.png)

Notice our template has space for a **header** and **slots** for images.

Resize and position the visuals as shown in the figure below:

![Screenshot displays how the visuals should look after rearranging within the report canvas.](images/background-position-example.png)

## Section 2: Add a logo

Now let's add a logo.

From the ribbon, select the **Insert** tab and then choose **Image**.

Select **Style** from the **Format Image** section of the **Visualization Pane**. Then select **Browse**.

![Screenshot displaying the visualization pane to upload the image.](images/image-select.png)

The **File** browser dialog opens. Browse to the **DIAD** folder then the **Data** folder (DIAD/Data).

Select the **AvMC_Logo.png** file.

Then, select **Open**.

Resize and drag the image to the bottom left corner of the report.



# Module 7: Access and Prepare Data from Scratch

*Source: [https://learn.microsoft.com/en-us/training/modules/access-prepare-power-bi](https://learn.microsoft.com/en-us/training/modules/access-prepare-power-bi)*


---

## Introduction

Now that you've built a complete report using a pre-loaded data model, it's time to understand how that data got there in the first place. In this module, you'll open a **new instance** of Power BI Desktop and load, clean, and shape the raw data files from scratch — the same files included in your DIAD folder.

By the end of this Module, you will learn:

How to load data from Microsoft Excel and Comma-Separated Values (CSV) sources

How to clean the data to prepare it for reporting

How to prepare tables in Power Query and load them into the model

Understanding these steps gives you the foundation to work with any data source in Power BI, not just pre-built files.

In this module, you will:

Import DEVCOM AvMC US engineering workload data

Import partner organizations' US engineering data

Import and append engineering data from allied nations

Clean up all the data

---

## Exercise - Load data from various sources into Power BI

Open a **new instance** of Power BI Desktop (File > New, or launch a fresh window). You'll build an entirely new .pbix file to understand the data loading process.

The dataset for this course contains R&D engineering workload data from DEVCOM AvMC and other partner organizations. We have five years of workload data by day, program, and lab code for each directorate. We're going to analyze data from six allied nations.

To find the US engineering data, go to **Data** > **USEngineering** > **RDWorkload.csv**.

To find engineering data from all other countries, **Data** > **InternationalPrograms**.

Program, Lab, and Directorate information is in a Microsoft Excel file called bi_dimensions.xlsx in the **USEngineering** subfolder in the **Data** folder (**/Data/USEngineering/**).

## Task 1: Get US engineering data

**Sign in** using your Power BI credentials.

![Screenshot of the Power BI Desktop home page.](images/sign-in.png)

Select **Blank report** to open a new Power BI report.

![Screenshot of Blank Report Button.](images/blank-report.png)

The next step is to load data into **Power BI Desktop**.

Note

Power BI Desktop has the capability to connect to 300+ data sources. The newest sources are part of Microsoft Fabric's OneLake catalog. Fabric will be coming to IL5 Environments in the future, but for this class, we'll be using CSV and Excel files stored locally on your machine.

![Screenshot of the OneLake catalog drop-down.](images/onelake-data-hub.png)

We're using CSV and Excel data files in this lab for simplicity. If you would like a full list of data sources, see: Data sources in Power BI Desktop.

Start by loading **US engineering data**, which is in a CSV file.

From the ribbon at the top of the screen, select the **Home** tab. Then, choose the **Get Data** drop-down (*not the icon*).

Select **Text/CSV** from the **Common data sources** list.

![Screenshot of the Get data dropdown with Text/CSV highlighted.](images/text-csv.png)

Browse to the **DIAD** folder, double-click **Data**, double-click the **USEngineering** folder, and then select the **RDWorkload.csv** file.

Then, select the **Open** button.

Note

If your folder appears empty then this likely means you forgot to unzip your class files. Navigate to your location **in your file explorer** where you saved the class files and unzip the files by right-clicking on the .zip file, then select **Extract All**.

Power BI detects the data type in each column. There are three options for Data Type Detection: based on the first 200 rows, based on the entire dataset, or not detecting the data type. Since our dataset is large and it takes time and resources to scan the complete dataset, we leave the default option of selecting the dataset based on the first 200 rows.

After completing your selection, you have three options: Load, Transform Data, or Cancel.

**Load** adds the data from the source into Power BI Desktop for you to start creating reports.

**Transform Data** allows you to perform data shaping operations such as merging columns, adding extra columns, changing data types of columns, and bringing in other data.

**Cancel** returns you back to the main canvas.

In the **RDWorkload.csv** dialog window, select the **Transform Data** button.

![Screenshot of the RDWorkload.csv dialog window highlighting the Transform Data button.](images/transform-data.png)

You will be taken to the **Query Editor** window as shown in the following screenshot. The **Query Editor** is used to perform data shaping operations. Notice that the workload file you connected shows as a query in the pane to the left of the screen. You can see a preview of the data in the center pane. Power BI predicts the data type of each field (based on the first 200 rows) as indicated by the icons to the left of each column header. In the pane to the right of the screen, steps that the Query Editor performs are recorded in the **APPLIED STEPS** section on the right side of the screen.

![Screenshot of the Power Query Editor with the query and Applied Steps section highlighted.](images/applied-steps.png)

Notice that Power BI set the **LabCode** column to the data type **Whole Number**. To make sure that the leading zero isn't dropped from lab codes that start with zero, we format them as **Text**.

To do this, select the **LabCode** column.

Then, from the ribbon, select the **Transform** tab.

From the menu at the top of the screen, select the **Data Type** drop-down.

Then choose the **Text** option.

![Screenshot of the Data Type drop-down with the Text option highlighted.](images/transform-whole-number.png)

A **Change Column Type** notification box will open. Select the **Replace current** button, which overwrites Power BI's predicted data type.

Important

Missing these last two steps will introduce null values when the LabCode field contains both characters and numbers.

![Screenshot of the Change Column Type dialog with Replace current highlighted.](images/replace-current.png)

Now that we covered importing data into Power BI Desktop using Power Query, in the next section, we'll begin the process of loading data from various sources into Power BI.

## Task 2: Load various sources

Now, let's get the data that's in the Excel source file called **bi-dimensions.xlsx**.

From the ribbon at the top of the Power Query Editor, select the **Home** tab.

Choose the **New Source** drop-down (*not the icon*), and then select **Excel Workbook**.

![Screenshot of the New Source drop-down with Excel Workbook highlighted.](images/new-source.png)

Browse to the **DIAD** folder:

Select **Data**, then the **USEngineering** folder

Next, select the **bi_dimensions.xlsx** file

Then select **Open** and the **Navigator** dialog box appears.

![Screenshot of the Open dialog with the file selected.](images/bi-dimensions-open.png)

The **Navigator** dialog opens. In the list to the left of the dialog, you see three sheets listed that are in the Excel workbook. It also lists **Product_Table**, which is a pre-defined Excel table.

Note

Excel Tables are differentiated from worksheets by using different icons.

![Screenshot of the Navigator window with the Excel Table icons highlighted.](images/navigator-table-icons.png)

From the list to the left of the dialog, select the checkbox for **geo**. In the preview pane, notice that the first few rows are headers and aren't part of the data. We remove them shortly.

Select the checkbox for **directorate**. In the preview pane, notice that the last couple of rows are footers and aren't part of the data. We will remove them shortly.

Select the checkbox for **Product_Table**. Notice that the different icon indicates this data is stored in an Excel table.

Make sure that **Product_Table**, **geo** and **directorate** are selected in the pane to the left, and then select **OK**.

![Screenshot of the Navigator window with the selections highlighted.](images/navigator-selections.png)

Notice that three sheets are added as queries in the Query Editor: *Product_Table*, *geo*, and *directorate*.

![Screenshot of the Power Query Editor with the added queries highlighted.](images/added-queries.png)

Note

As you click on each query, you will notice some of the queries are not in a format optimized for reporting. You will transform this data in future steps within this module.

## Task 3: Add other data

In this scenario, the allied partner nations agree to provide their engineering workload data so that the organization's R&D effort can be analyzed together. You created a folder where they each put their data.

To analyze all the data together, you need to import the new data from each of the partner nations and combine it with the US engineering data you loaded earlier.

When you loaded the US engineering data earlier in this unit, you did so with a single file. However, Power BI gives you the option to load all the files in a folder together at once. This helps save you some time when you load data.

From the **Home** tab of the Query Editor, select the **New Source** drop-down (*not the icon*).

Select **More..** from the options list. The **Get Data** dialog opens.

![Screenshot of the New Source drop-down with More... highlighted.](images/more-sources.png)

In the **Get Data** dialog box, select **Folder** from the **All** list.

Then, select the **Connect** button and the **Folder** dialog box opens.

![Screenshot of the Get Data window with Folder and Connect highlighted.](images/connect-folder.png)

In the Folder dialog box, select the **Browse..** button.

In the **Browse For Folder** dialog, navigate to the location where you unzipped the class files.

Open the **DIAD** folder, then open the **Data** folder.

Select the **InternationalPrograms** folder.

Select **OK** to close the **Browse for Folder** dialog box.

![Screenshot of the InternationalPrograms folder selected in the Browse For Folder dialog.](images/browse-folder.png)

Then, select **OK** to close the **Folder** dialog box. The selected folder dialog box displays the list of files in the folder.

![Screenshot of the Folder dialog with the folder path and OK button.](images/folder-path-ok.png)

Note

This approach will load all the files located in the folder. This is useful when you have a group that puts files on an FTP (File Transfer Protocol) site each month and you are not always sure of the names of the files or the number of files. All the files must be of the same file type with columns in the same order.

Select the **Combine & Transform Data** button at the bottom of the dialog box.

![Screenshot of the file list with Combine & Transform Data button highlighted.](images/combine-transform.png)

The **Combine Files** dialog box opens. By default, Power BI again detects the data type based on the first 200 rows. Notice there's an option to select various file delimiters. The file we're working with is comma-delimited, so let's leave the default **Delimiter** option as **Comma**.

There's also an option to select each individual file in the folder (using the **Sample File** drop-down) to validate the format of the files.

Select the **OK** button located at the bottom of the **Combine Files** window.

![Screenshot of the Combine Files window with the OK button highlighted.](images/combine-files.png)

You'll be taken back to the **Power Query Editor** window with a new query named **InternationalPrograms**.

Tip

If you don't see the **Queries** pane to the left of the screen, select the **>** (greater than) icon to expand the pane.

Tip

If you don't see the **Query Settings** pane on the right of the screen, select the **View** tab in the ribbon and choose **Query Settings** to view the pane.

Select **InternationalPrograms** from the query pane on the left.

![Screenshot of the Power Query Editor with Query settings and InternationalPrograms highlighted.](images/query-settings.png)

Notice that the **LabCode** column is of the **Whole Number** type. Based on the first 200 rows, Power BI thinks the LabCode column consists of whole numbers. But lab codes can be alphanumeric in some regions or contain leading zeros. If we don't change the data type, we receive an error when we load the data. So, let's change the LabCode column to data type **Text**.

Select the **LabCode** column in the **InternationalPrograms** query, and then change the **Data Type** to **Text** using the drop-down under the **Home** tab.

![Screenshot of the Data Type drop-down with Text option highlighted.](images/data-type-text.png)

The **Change Column Type** dialog box opens. Select the **Replace Current** button when prompted.

In the **Queries** pane, notice that a **Transform File from the InternationalPrograms** folder is created. This contains the function used to load each of the files from the folder.

If you compare the **InternationalPrograms** and the **RDWorkload** table, you see the **InternationalPrograms** table contains two new columns: **Source.Name** and **Country**.

![Screenshot of the two new columns.](images/two-new-columns.png)

We don't need the **Source.Name** column in the **InternationalPrograms** query. To remove the column from the query:

Select the **Source.Name** column.

select the **Home** tab from the ribbon.

Choose the **Remove Columns** drop-down.

Now, select **Remove Columns** again.

![Screenshot of the Remove Columns option in the ribbon.](images/remove-column.png)

Note

You may find that Australia is the only country displayed. This is due to the **Power Query Editor** displaying only the first 1000 rows of any data source. To validate you have the data from all country files you can optionally select the drop-down menu next to the **Country** column, then select **Load more**.

![Screenshot of the Country column with Load more option highlighted.](images/load-more.png)

You will now see that **Australia**, **Canada**, **Germany**, **Japan**, **Mexico**, and **South Korea** are all selected.

![Screenshot of the Country column with all countries loaded.](images/more-countries.png)

If you did this optional step, select **Cancel**.

Now that you loaded all the necessary data for the upcoming report, you're ready to start preparing the data. In the next section, we'll explore methods to transform and clean our data using Power BI Desktop.

---

## Exercise - Perform common data cleaning practices

## Data preparation

In this section, we explore methods to transform data. Transforming the data by renaming tables, updating data types, and appending tables together ensures that the data is ready to be used for reporting. In some instances, this means cleaning the data up so that similar sets of data can be combined. In other instances, groups of data are renamed so that end users more easily recognize them and report writing is simplified.

## Section 1: Rename tables

In the **Queries** pane, minimize the folder called **Transform Files from InternationalPrograms**.

Next, **rename** the queries listed in the **Queries** pane. Using the text field in the **Properties** section of the **Query Settings** pane, use the new names listed here to change the name of each of the queries listed. After entering the new name in the text field, hit **Enter** on your keyboard to save the new name of the query.

Initial Name -> Final Name

RDWorkload -> R&D Workload

geo -> Lab

directorate -> Directorate

Product_Table -> Program

InternationalPrograms -> International Programs

The Query Editor window should appear as shown here:

![Screenshot of the Power Query Editor with updated table names.](images/name-changes.png)

Note

It is a best practice to provide descriptive query and column names. These names are used in visuals and in the Q&A section of Power BI, which is covered in a later module.

## Section 2: Fill empty values

In our scenario, some of the data isn't in the right format. Power BI provides extensive transformation capabilities to clean and prepare data to meet your needs. Let's start by selecting the **Program** query from the **Queries** pane.

Notice that the **Category** column has numerous **null** values. Hover over the green/gray bar (known as the quality bar) below the column header. This allows you to easily identify errors and empty values in your data previews. It looks like there are values in the Category column only when the value changes. We need to provide data in this column so there are values in each row.

![Screenshot of the Category column of the Program table.](images/category-null.png)

With the **Program** query selected from the **Queries** pane, select the **Category** column.

From the ribbon, select the **Transform** tab.

Choose the **Fill** drop-down, then select the **Down** option.

![Screenshot of the Fill-cell dropdown for the Program Category column.](images/fill-down.png)

Notice how all the null values are filled with the appropriate **Category** values.

Note

The fill down operation takes a column and traverses through the values in it to fill any null values in the next rows until it finds a new value. This process continues on a row-by-row basis until there are no more values in that column.

## Section 3: Split columns

In the **Program** query, notice the **Product** column. It looks like the program name and program segment are concatenated into one field with a pipe (|) separator. Let's **split** them into **two** columns. This is useful when we build visuals so we can analyze based on both fields.

From the **Queries** pane to the left, make sure that the **Program** query is selected.

Select the **Product** column from the query table.

From the ribbon, select the **Transform** tab.

Expand the **Split Column** drop-down.

Then, select **By Delimiter**. The **Split Column by Delimiter** dialog box opens.

![Screenshot of the Split Column drop-down with By Delimiter highlighted.](images/split-product-column.png)

In the dialog box, ensure that **Custom** is selected in the **Select or enter delimiter** drop-down menu.

Note

The **Select or enter delimiter** drop-down menu has some of the standard delimiters like comma, colon, and so on.

Notice that in the text box, there's a **hyphen** (-). Power BI assumes we want to split by hyphen. **Remove** the hyphen symbol and enter the **pipe** symbol (|). Then, choose **Left-most delimiter** under **Split at**, and select **OK**.

![Screenshot of the Split Column by Delimiter window with pipe symbol.](images/split-column-delimiter.png)

Note

If the delimiter occurs multiple times, the Split at section provides the option to split only once (either left most or right most) or the option to split the column on each occurrence of the delimiter. In this scenario, the delimiter occurs only once, therefore the Program column is split into two columns.

## Section 4: Rename columns

Let's rename the columns now to something more user friendly.

Select the **Program.1** column, and then right-click next to the column name.

Choose **Rename..** from the options menu.

**Rename** the field to **Program**.

Use the same steps to rename **Program.2** to **Segment**.

![Screenshot of renaming the columns in Power Query Editor.](images/rename-product-columns.png)

## Section 5: Use Column From Examples to split columns

In the **Program** query, notice that the **TechnologyReadinessLevel** column has a text prefix and a numeric level concatenated (combined) into one field (for example, **TRL 3**). To do any calculations, we only need the numeric value. Therefore, we need to extract the level number into its own column. We can use the split feature like earlier or we can use **Column From Examples**. **Column From Examples** is handy in scenarios where the pattern is more complex than simply a delimiter.

From the **Queries** pane to the left of the screen, make sure that the **Program** query is selected.

From the ribbon at the top of the screen, select the **Add Column** tab.

Choose the **Column From Examples** drop-down, and then select **From All Columns**.

![Screenshot of the From All Columns option under Column From Examples.](images/column-examples.png)

In the first row of the newly added **Column1**, enter the numeric portion of the first **TechnologyReadinessLevel** value, **7**.

Hit **Enter** on your keyboard.

Notice after you hit Enter, Power BI knows that you want to extract the numeric level from the **TechnologyReadinessLevel** column. The formula Power BI uses is displayed as well.

Note

A common mistake that can occur here is the **Column From Example** feature may attempt to auto-type **TRL 3** with the Intellisense feature. **DO NOT** accept this auto-typed value — you only want the numeric portion.

You may also need to enter the second value in the column to help Power BI recognize the pattern. If needed, enter **6** in the second row of the **Column1**.  Make sure the autofilled pattern is correct for your use case before proceeding to the next step.

Double-click the column header of the newly added column in the query table.

**Rename** the column to **TRLLevel** and select **OK** to apply the changes.

![Screenshot of the TRLLevel column entry and OK button.](images/trl-column.png)

Notice that the **TRLLevel** field has a Data Type of **Text**. The Data Type that it needs to be is **Whole Number**. Let's change it.

Select the **ABC** icon to the left of the **TRLLevel** column header.

From the menu, select **Whole Number**. Notice that all the steps we performed on the Program query are being recorded under **APPLIED STEPS** in the right panel.

![Screenshot of the TRLLevel data type selection and Applied Steps.](images/trl-data-type.png)

Now that we extracted the numeric level into the **TRLLevel** column, the original **TechnologyReadinessLevel** column is no longer useful. Let's remove it.

Make sure that you're still viewing the **Program** query. Right-click on the **TechnologyReadinessLevel** column.

Select **Remove** from the options menu.

![Screenshot of the Remove option for the TechnologyReadinessLevel column.](images/remove-technologyreadinesslevel.png)

## Section 6: Remove unwanted rows

In the **Lab** query, notice that the first two rows are informational. They aren't part of the data. Similarly, in the Directorate query, the last couple of rows aren't part of the data. Let's remove them so we have a clean dataset to work with.

In the **Queries pane** to the left of the screen, select the **Lab** query.

From the ribbon, select the **Home** tab.

Choose the **Remove Rows** drop-down.

Then, select **Remove Top Rows**.

![Screenshot of the Remove Top Rows option from Remove Rows drop-down.](images/remove-top-rows.png)

The **Remove Top Rows** dialog box opens. Enter **3** in the text box since we want to remove 3 rows, the top informational data row and the blank second row.

Then, select **OK**.

Notice the first row in the Lab query contains the column headers. Let's move them into the column header position.

Make sure that the **Lab** query is still selected in the Queries pane. From the ribbon at the top of the screen, select the **Home** tab.

Then choose **Use First Row as Headers**.

![Screenshot of the Use First Row as Headers button.](images/first-row-headers.png)

Power BI then predicts the data type of each field again. Notice that the column **LabCode** was changed to the **Whole Number** Data Type. Let's change it to **Text** again as we did earlier. If we don't, we'll see errors when loading the data.

Select the **data type** icon to the left of the **LabCode** column header.

From the options menu, select **Text**.

Select **Replace Current** in the **Change Column Type** dialog box.

From the **Queries** pane, select the **Directorate** query. Notice the bottom three rows aren't part of the data. Let's remove them.

From the ribbon, select the **Home** tab.

Choose the **Remove Rows** drop-down.

Then, select **Remove Bottom Rows**.

The **Remove Bottom Rows** dialog box opens. Enter **3** in the **Number of rows** text box.

Then, select **OK**.

## Section 7: Transpose data

From the **Queries pane** to the left of the screen, select the **Directorate** query. Notice that the **DirectorateID**, **Directorate**, and **Logo** data are laid across in rows. Also notice that the header isn't useful. We need to transpose the table to meet our needs. Transposing a table treats the rows as columns and columns as rows, effectively inverting the layout of a table.

From the ribbon at the top of the screen, select the **Transform** tab, then choose **Transpose**.

![Screenshot of the Transpose button under the Transform tab.](images/transpose-table.png)

Notice that this transposes the data into columns. Now we need the first row to be the header.

From the ribbon at the top of the screen, select the **Home** tab, and then choose the **Use First Row as Headers** button.

Notice that now the **Directorate** table is laid out the way we need it with a header and values along columns.

Also, notice that with the **Query Settings** pane, under **APPLIED STEPS**, you see the list of transformations and steps that were applied. You can navigate through each change made to the data by selecting the step. Steps can also be deleted by choosing the **X** that appears to the left of the step. The properties of each step can be reviewed by selecting the **gear** to the right of the step.

![Screenshot of the Applied Steps section tools.](images/applied-steps-properties.png)

## Section 8: Append queries

To analyze the engineering workload across all countries, it's convenient to have a single RDWorkload table. To do this, you need to use the **Append Queries** feature. With Append Queries, we can add all the rows from the **International Programs** query to the **RDWorkload** query.

In the **Queries** pane to the left of the screen, select the **RDWorkload** query.

From the ribbon at the top of the screen, select the **Home** tab, and then choose **Append Queries** button.

The **Append** dialog box opens. You can append Two tables or Three or more tables. Leave **Two tables** selected since we're appending just two tables.

From the **Table to append** drop-down, select **International Programs**.

Then, select **OK**.

![Screenshot of the Append dialog with Two Tables and International Programs selected.](images/append-two-tables.png)

You now see a new column in the **RDWorkload** table called **Country**. Since the **International Programs** query had the extra column for **Country**, the Power Query Editor added the **Country** column to the newly updated **RDWorkload** table when it loaded the values from the **International Programs** query.

You might also notice that there are **null** values in the **Country** column by default for the **RDWorkload** table rows. This is because that column didn't exist for the table with US data. We now add the value **USA** as a data shaping operation.

From the ribbon at the top of the screen, select the **Add Column** tab, and then choose the **Conditional Column** button.

![Screenshot of the Add Conditional Column dialog.](images/conditional-column.png)

In the **Add Conditional Column** dialog box, enter the name of the column as **CountryName**.

Select **Country** from the **Column Name** drop-down menu.

Choose **equals** from the **Operator** drop-down menu.

Enter **null** in the **Value** text box.

Enter **USA** in the **Output** text box.

Select the value drop-down menu under **Else**, and then choose the **Select a column** option.

Choose **Country** from the column drop-down menu.

Then select **OK**.

![Screenshot of the Add Conditional Column dialog filled in.](images/add-conditional-column.png)

This reads: *If the current Country value is equal to null, then the value should return USA; otherwise, if the value isn't null, then use the current Country value.*

Note

A common mistake on the previous step is that the **Else** may not be set correctly. Please double check that your **Else** part of the conditional column matches the screenshot above.

You see the **CountryName** column in the Query editor window. Notice that in the **APPLIED STEPS** list, it's added to the list the action you completed.

The original **Country** column containing the null values is no longer needed and can be removed from the final table for analysis.

In the **RDWorkload** query, right-click on the **Country** column.

Select **Remove** from the options menu.

With this column now removed, we can now **rename** the **CountryName** column to **Country**.

Right-click on the **CountryName** column and **rename** it to **Country**.

Select the **Data Type** icon to the left of the **Country** column header and change the **Data Type** to **Text**.

Next, select the **Data Type** **icon** to the left of the **LaborHours** column header.

Change the **Data Type** to **Fixed decimal number**. We do this because, well, does anyone really think they know what .0003 hours is? This also makes the data easier to read in reports and dashboards.

Note

The difference between a Fixed decimal number and a Decimal number is related to the length and precision of the decimal places. For more information, see Number types.

When the data is refreshed, it processes through all the **APPLIED STEPS** that you created.

The newly named **Country** column has names for **all countries**, including the USA. You can validate this by selecting the drop-down menu next to the **Country** column to see the unique values.

At first, you only see USA data. Select the **drop-down arrow** to the right of the **Country** column header. Select **Load more** to validate your data from all six countries.

Select **Cancel** to close this filter. You *don't* need to apply this filter to the data.

Now that the **International Programs** data is appended to the **RDWorkload** query, in order to avoid duplicating data we should suppress the **International Programs** table from loading into the data model.

From the **Queries** pane to the left of the screen, select the **International Programs** query.

Right-click on the **International Programs** query, and then choose **Enable Load** to **deselect** this setting. This disables loading of the International Programs query into the data model.

You should see the name of this query become italicized in the Queries pane after deselecting the Enable load option.

![Screenshot of the Enable Load option for the International Programs query.](images/enable-load.png)

Note

The appropriate data from the International Programs table will load onto the RDWorkload table each time the model is refreshed. By removing the International Programs table, we are preventing duplicate data from loading into the model and increasing its file size. In some instances, storing very large amounts of data affects the data model performance.

You might receive a message about Possible Data Loss Warning. If so, select **Continue** when this warning appears.

Next, while the **International Programs** query is still selected, choose the **View** tab from the ribbon.

Select the **Query Dependencies** button.

![Screenshot of the Query Dependencies button under the View tab.](images/query-dependencies.png)

This opens the **Query Dependencies** dialog box. The dialog box shows the source of each query and its dependencies. For example, we see that the **RDWorkload** query has a **CSV file source** and a dependency on the **International Programs** query. This is useful information to share knowledge with your team members.

Select **Close** at the bottom of the dialog box.

![Screenshot of the Query Dependencies dialog.](images/query-dependencies-window.png)

Note

You can zoom in and out of the **Query Dependencies** view as needed.

You successfully completed import and data shaping operations and are ready to load the data into the Power BI Desktop data model to visualize the data.

From the ribbon at the top of the screen, select the **File** tab, then choose **Close & Apply**. This closes out the Power Query window and applies all changes.

![Screenshot of Close and Apply option from the File tab.](images/close-apply.png)

All the data is loaded in memory in the Power BI Desktop. You see the progress dialog box with the number of rows being loaded in each table as shown in the Figure.

![Screenshot of the Load dialog box.](images/load-data.png)

Note

It may take several minutes to load all the tables.

Once the data finishes loading, select the **File** tab from the ribbon at the top of the screen.

Then, from the options menu to the left, select **Save as** to save the file.

Name the file **MyFirstPowerBIModel**. Save the file in the **DIAD Reports** folder.

![Screenshot of the Save option from the File tab.](images/save.png)

In the navigation pane to the left of the screen, select the Data icon to view the data that was loaded. If you need to return to the Power Query editor again, navigate to **Home** > **Transform data** > **Transform data**

![Screenshot of the Data icon and Transform Data option.](images/home-transform-data.png)

Congratulations! You now understand how the data in the starter .pbix was prepared. The techniques you learned in this module — loading CSV and Excel files, combining folder sources, cleaning and shaping data in Power Query — are the foundation for building any Power BI report from raw data sources.
