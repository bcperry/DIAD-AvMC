# Dashboard in a Day - Online Workshop

*Source: https://learn.microsoft.com/en-us/training/paths/dashboard-in-a-day/*


# Module 1: Introduction and Prerequisites for Power BI

*Source: [https://learn.microsoft.com/en-us/training/modules/intro-power-bi](https://learn.microsoft.com/en-us/training/modules/intro-power-bi)*


---

## Introduction to Power BI

Microsoft's Power BI is a business analytics tool designed to provide users with comprehensive data analysis and visualization capabilities. It empowers organizations to connect to a wide array of data sources, ranging from simple Excel sheets to complex databases, and transform this data into interactive, insightful dashboards and reports.

With Power BI, users can create and share reports that highlight key performance indicators (KPIs) and trends, facilitating informed decision-making across all levels of an organization.

Its features include real-time analytics, the ability to perform ad-hoc analysis, and the seamless integration with other Microsoft products such as Azure and Office 365, enhancing productivity and collaboration. Power BI's interface and robust data modeling options make it accessible to data professionals and business users alike, ensuring that valuable data insights are always at your fingertips.

Throughout this course, you'll learn how to use these tools made available by Power BI, and acquire the skills to start building your own reports and start analyzing data like a pro.

The course focuses on the main components of Power BI Desktop. These sections highlight the features available in Power BI Desktop and walk the user through the process of bringing in data from data sources, organizing data in a model, and creating visualizations.

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

The **Insert** tab in the ribbon allows you to insert shapes, a textbox, or new visuals.

The **Modeling** tab in the ribbon enables additional data modeling capabilities like adding custom columns and calculating measures.

The **View** tab has options to format the page layout.

The **Help** tab provides self-help options like guided learning, training videos and links to online communities, partner showcases and consulting services.

On the left side of the window, you have four icons within the **Navigation** menu: **Report View, Table View**, **Model View**, and **DAX Query View**. If you hover over the icons, you can see the **tooltips**. Switching between these allows you to see the visualizations, tables, relationships, and DAX query editor.

When in the **Report view**, the center **white space** is the canvas where you'll be creating visuals.

The **Visualizations** pane on the right-side of the window allows you to select visualizations, add values to the visuals, and add columns to the axis or filters.

The **Data** pane is where you see the list of tables, which are generated from queries. By selecting the arrow next to a table name, you can expand the list of fields for that table.

---

## Unzip the course files

You must download and unzip the Dashboard in a Day (DIAD) class content.

Download the DIAD starter files.

Create a folder called DIAD on the C: drive of your local computer.

Copy all contents from the student files to the DIAD folder you created (C:\DIAD).

If you're unfamiliar with how to unzip files, you right-click on the Attendee.zip file and select Extract All.

Note

Users should use their own files for each lab. The solutions provided for each lab are a final product to reference. The solutions are not meant to be the starting point for each lab.

Your `C:\DIAD\` directory should now have the folders **Data** and **Reports** in its root.

The dataset you'll use for the Dashboard in a Day class is a sales and market share analysis. This type of analysis is common for a Chief Marketing Officer (CMO). Unlike the Chief Financial Officer (CFO), a CMO is focused not only on the company's performance internally (how well our products sell) but also externally (how well we do against competing products).

The company VanArsdel, Ltd. manufactures expensive retail products that can be used for fun and work. This company sells their products directly to consumers nationwide and in several other countries.

Note

There is a problem with the Nigeria International Sales data; this is by design so that users can learn how to shape data.

By the end of the class, you'll build a report, which will look like the screenshot below.




# Module 2: Access and Prepare Data for Power BI Desktop

*Source: [https://learn.microsoft.com/en-us/training/modules/access-prepare-power-bi](https://learn.microsoft.com/en-us/training/modules/access-prepare-power-bi)*


---

## Introduction

In this module, you learn about various key features of the Power BI service. This is an introductory course intended to teach you how to build reports on the Power BI Desktop, create operational dashboards, and share content via the Power BI Service.

By the end of this Module, you will learn:

How to load data from Microsoft Excel and Comma-Separated Values (CSV) sources

How to clean the data to prepare it for reporting

How to prepare tables in Power Query and load them into the model

Learning these steps prepares you for the modeling exercises in Module 1. Additionally, the results from this Module are the starting point for Module 3.

In this module, you will:

Import VanArsdel, Ltd. USA sales data

Import their competitors' USA sales data

Import and append sales data from other countries

Clean up all the data

---

## Exercise - Load data from various sources into Power BI

The dataset for this course contains sales data from VanArsdel, Ltd. and other competitors. We have seven years of transaction data by day, product, and zip code for each manufacturer. We're going to analyze data from seven countries.

To find the USA sales data, go to **Data** > **USSales** > **Sales.csv**.

To find sales of all other countries, **Data** > **InternationalSales**.

Product, Geography, and Manufacturer information is in a Microsoft Excel file called bi_dimensions.xlsx in the **USSales** subfolder in the **Data** folder (**/Data/USSales/**).

## Task 1: Get USA sales data

If you don't already have the **Power BI Desktop** open, launch it now.

Upon opening for the first time, you may see a pop-up presenting **Dark mode** options. This course will be using the **Default** mode, but you may choose otherwise. Select **Next** after making your choice and **Close** on the next screen.

**Sign in** using your Power BI credentials.

Select **Blank report** to open a new Power BI report.

Next, let's set the **Locale** to US English to make it convenient for the rest of this lab.

From the ribbon, select **File**, then choose **Options and settings**. Then, select **Options**.

Under **CURRENT FILE** in the left *Options* pane, select **Regional Settings**.

From the **Locale** drop-down, select **English (United States)**.

Then, select **OK** to close the dialog box.

The next step is to load data into **Power BI Desktop**.

Note

Power BI Desktop has the capability to connect to 300+ data sources. The newest sources are part of Microsoft Fabric's OneLake catalog. You will not be using OneLake in today's class but to learn more read here: Tutorial: Fabric for Power BI users.

We're using CSV and Excel data files in this lab for simplicity. If you would like a full list of data sources, see: Data sources in Power BI Desktop.

Start by loading **USA Sales data**, which is in a CSV file.

From the ribbon at the top of the screen, select the **Home** tab. Then, choose the **Get Data** drop-down (*not the icon*).

Select **Text/CSV** from the **Common data sources** list.

Browse to the **DIAD** folder (this folder might be called **Attendee** if you didn't rename it in Module 1), double-click **Data**, double-click the **USSales** folder, and then select the **Sales.csv** file.

Then, select the **Open** button.

Note

If your folder appears empty then this likely means you forgot to unzip your class files. Navigate to your location **in your file explorer** where you saved the class files and unzip the files by right-clicking on the .zip file, then select **Extract All**.

Power BI detects the data type in each column. There are three options for Data Type Detection: based on the first 200 rows, based on the entire dataset, or not detecting the data type. Since our dataset is large and it takes time and resources to scan the complete dataset, we leave the default option of selecting the dataset based on the first 200 rows.

After completing your selection, you have three options: Load, Transform Data, or Cancel.

**Load** adds the data from the source into Power BI Desktop for you to start creating reports.

**Transform Data** allows you to perform data shaping operations such as merging columns, adding extra columns, changing data types of columns, and bringing in other data.

**Cancel** returns you back to the main canvas.

In the **Sales.csv** dialog window, select the **Transform Data** button.

You will be taken to the **Query Editor** window as shown in the following screenshot. The **Query Editor** is used to perform data shaping operations. Notice that the sales file you connected shows as a query in the pane to the left of the screen. You can see a preview of the data in the center pane. Power BI predicts the data type of each field (based on the first 200 rows) as indicated by the icons to the left of each column header. In the pane to the right of the screen, steps that the Query Editor performs are recorded in the **APPLIED STEPS** section.

Notice that Power BI set the **Zip** column to the data type **Whole Number**. To make sure that the leading zero isn't dropped from Zip codes that start with zero, we format them as **Text**.

To do this, select the **Zip** column.

Then, from the ribbon, select the **Transform** tab.

From the menu at the top of the screen, select the **Data Type** drop-down.

Then choose the **Text** option.

A **Change Column Type** notification box will open. Select the **Replace current** button, which overwrites Power BI's predicted data type.

Important

Missing these last two steps will introduce null values when the Zip field contains both characters and numbers.

Now that we covered importing data into Power BI Desktop using Power Query, in the next section, we'll begin the process of loading data from various sources into Power BI.

In the previous unit, you were introduced to importing data into Power BI Desktop using Power Query. Now we begin working with various sources, walking through the steps needed to combine these sources into one model. After you learn how to deal with multiple sources, unit 3 will cover how to clean up all this pulled data.

## Task 2: Load various sources

Now, let's get the data that's in the Excel source file called **bi-dimensions.xlsx**.

From the ribbon at the top of the Power Query Editor, select the **Home** tab.

Choose the **New Source** drop-down (*not the icon*), and then select **Excel Workbook**.

Browse to the **DIAD** folder:

Select **Data**, then the **USSales** folder

Next, select the **bi_dimensions.xlsx** file

Then select **Open** and the **Navigator** dialog box appears.

The **Navigator** dialog opens. In the list to the left of the dialog, you see three sheets listed that are in the Excel workbook. It also lists **Product_Table**, which is a pre-defined Excel table.

Note

Excel Tables are differentiated from worksheets by using different icons.

From the list to the left of the dialog, select the checkbox for **geo**. In the preview pane, notice that the first few rows are headers and aren't part of the data. We remove them shortly.

Select the checkbox for **manufacturer**. In the preview pane, notice that the last couple of rows are footers and aren't part of the data. We will remove them shortly.

Select the checkbox for **Product_Table**. Notice that the different icon indicates this data is stored in an Excel table.

Make sure that **Product_Table**, **geo** and **manufacturer** are selected in the pane to the left, and then select **OK**.

Notice that three sheets are added as queries in the Query Editor: *Product_Table*, *geo*, and *manufacturer*.

Note

As you click on each query, you will notice some of the queries are not in a format optimized for reporting. You will transform this data in future units within this module.

## Task 3: Add other data

In this scenario, the international subsidiaries agree to provide their sales data so that the company's sales can be analyzed together. You created a folder where they each put their data.

To analyze all the data together, you need to import the new data from each of the subsidiaries and combine it with the US Sales you loaded earlier.

When you loaded the US sales data earlier in this unit, you did so with a single file. However, Power BI Gives you the option to load all the files in a folder together at once. This helps save you some time when you load data.

From the **Home** tab of the Query Editor, select the **New Source** drop-down (*not the icon*).

Select **More..** from the options list. The **Get Data** dialog opens.

In the **Get Data** dialog box, select **Folder** from the **All** list.

Then, select the **Connect** button and the **Folder** dialog box opens.

In the Folder dialog box, select the **Browse..** button.

In the **Browse For Folder** dialog, navigate to the location where you unzipped the class files.

Open the **DIAD** folder, then open the **Data** folder.

Select the **InternationalSales** folder.

Select **OK** to close the **Browse for Folder** dialog box.

Then, select **OK** to close the **Folder** dialog box. The selected folder dialog box displays the list of files in the folder.

Note

This approach will load all the files located in the folder. This is useful when you have a group that puts files on an FTP (File Transfer Protocol) site each month and you are not always sure of the names of the files or the number of files. All the files must be of the same file type with columns in the same order.

Select the **Combine & Transform Data** button at the bottom of the dialog box.

The **Combine Files** dialog box opens. By default, Power BI again detects the data type based on the first 200 rows. Notice there's an option to select various file delimiters. The file we're working with is comma-delimited, so let's leave the default **Delimiter** option as **Comma**.

There's also an option to select each individual file in the folder (using the **Sample File** drop-down) to validate the format of the files.

Select the **OK** button located at the bottom of the **Combine Files** window.

You'll be taken back to the **Power Query Editor** window with a new query named **InternationalSales**.

Tip

If you don't see the **Queries** pane to the left of the screen, select the **>** (greater than) icon to expand the pane.

Tip

If you don't see the **Query Settings** pane on the right of the screen, select the **View** tab in the ribbon and choose **Query Settings** to view the pane.

Select **InternationalSales** from the query pane on the left.

Notice that the **Zip** column is of the **Whole Number** type. Based on the first 200 rows, Power BI thinks the Zip column consists of whole numbers. But zip codes can be alphanumeric in some regions or contain leading zeros. If we don't change the data type, we receive an error when we load the data. So, let's change the Zip column to data type **Text**.

Select the **Zip** column in the **InternationalSales** query, and then change the **Data Type** to **Text** using the drop-down under the **Home** tab.

The **Change Column Type** dialog box opens. Select the **Replace Current** button when prompted.

In the **Queries** pane, notice that a **Transform File from the InternationalSales** folder is created. This contains the function used to load each of the files from the folder.

If you compare the **InternationalSales** and the **Sales** table, you see the **InternationalSales** table contains two new columns: **Source.Name** and **Country**.

We don't need the **Source.Name** column in the **InternationalSales** query. To remove the column from the query:

Select the **Source.Name** column.

select the **Home** tab from the ribbon.

Choose the **Remove Columns** drop-down.

Now, select **Remove Columns** again.

Note

You may find that Australia is the only country displayed. This is due to the **Power Query Editor** displaying only the first 1000 rows of any data source. To validate you have the data from all country files you can optionally select the drop-down menu next to the **Country** column, then select **Load more**.

You will now see that **Australia**, **Canada**, **Germany**, **Japan**, **Mexico**, and **Nigeria** are all selected.

If you did this optional step, select **Cancel**.

Now that you loaded all the necessary data for the upcoming report, you're ready to start preparing the data. In the next unit, we'll explore methods to transform and clean our data using Power BI Desktop.

---

## Exercise - Perform common data cleaning practices

## Data preparation

In this section, we explore methods to transform data. Transforming the data by renaming tables, updating data types, and appending tables together ensures that the data is ready to be used for reporting. In some instances, this means cleaning the data up so that similar sets of data can be combined. In other instances, groups of data are renamed so that end users more easily recognize them and report writing is simplified.

## Section 1: Rename tables

In the **Queries** pane, minimize the folder called **Transform Files from InternationalSales**.

Next, **rename** the queries listed in the **Queries** pane. Using the text field in the **Properties** section of the **Query Settings** pane, use the new names listed here to change the name of each of the queries listed. After entering the new name in the text field, hit **Enter** on your keyboard to save the new name of the query.

Initial Name
Final Name

Sales
Sales

geo
Geography

manufacturer
Manufacturer

Product_Table
Product

InternationalSales
International Sales

The Query Editor window should appear as shown here:

Note

It is a best practice to provide descriptive query and column names. These names are used in visuals and in the Q&A section of Power BI, which is covered in a later module.

## Section 2: Fill empty values

In our scenario, some of the data isn't in the right format. Power BI provides extensive transformation capabilities to clean and prepare data to meet your needs. Let's start by selecting the **Product** query from the **Queries** pane.

Notice that the **Category** column has numerous **null** values. Hover over the green/gray bar (known as the quality bar) below the column header. This allows you to easily identify errors and empty values in your data previews. It looks like there are values in the Category column only when the value changes. We need to provide data in this column so there are values in each row.

With the **Product** query selected from the **Queries** pane, select the **Category** column.

From the ribbon, select the **Transform** tab.

Choose the **Fill** drop-down, then select the **Down** option.

Notice how all the null values are filled with the appropriate **Category** values.

Note

The fill down operation takes a column and traverses through the values in it to fill any null values in the next rows until it finds a new value. This process continues on a row-by-row basis until there are no more values in that column.

## Section 3: Split columns

In the **Product** query, notice the **Product** column. It looks like the product name and product segment are concatenated into one field with a pipe (|) separator. Let's **split** them into **two** columns. This is useful when we build visuals so we can analyze based on both fields.

From the **Queries** pane to the left, make sure that the **Product** query is selected.

Select the **Product** column from the query table.

From the ribbon, select the **Transform** tab.

Expand the **Split Column** drop-down.

Then, select **By Delimiter**. The **Split Column by Delimiter** dialog box opens.

In the dialog box, ensure that **Custom** is selected in the **Select or enter delimiter** drop-down menu.

Note

The **Select or enter delimiter** drop-down menu has some of the standard delimiters like comma, colon, and so on.

Notice that in the text box, there's a **hyphen** (-). Power BI assumes we want to split by hyphen. **Remove** the hyphen symbol and enter the **pipe** symbol (|). Then, choose **Left-most delimiter** under **Split at**, and select **OK**.

Note

If the delimiter occurs multiple times, the Split at section provides the option to split only once (either left most or right most) or the option to split the column on each occurrence of the delimiter. In this scenario, the delimiter occurs only once, therefore the Product column is split into two columns.

## Section 4: Rename columns

Let's rename the columns now to something more user friendly.

Select the **Product.1** column, and then right-click next to the column name.

Choose **Rename..** from the options menu.

**Rename** the field to **Product**.

Use the same steps to rename **Product.2** to **Segment**.

## Section 5: Use Column From Examples to split columns

In the **Product** query, notice that the **Price** column has price and currency concatenated (combined) into one field. To do any calculations, we only need the numeric value. Therefore, we need to split this field into two columns. We can use the split feature like earlier or we can use **Column From Examples**. **Column From Examples** is handy in scenarios where the pattern is more complex than simply a delimiter.

From the **Queries** pane to the left of the screen, make sure that the **Product** query is selected.

From the ribbon at the top of the screen, select the **Add Column** tab.

Choose the **Column From Examples** drop-down, and then select **From All Columns**.

In the first row of the newly added **Column1**, enter the first **Price** value, **412.13**.

Hit **Enter** on your keyboard.

Notice after you hit Enter, Power BI knows that you want to split the **Price** column. The formula Power BI uses is displayed as well.

Note

A common mistake that can occur here is the **Column From Example** feature may attempt to auto-type **USD 412.13** with the Intellisense feature. **DO NOT** accept this auto-typed value.

Double-click the column header of the newly added column in the query table.

**Rename** the column to **MSRP** and select **OK** to apply the changes.

Notice that the **MSRP** field has a Data Type of **Text**. The Data Type that it needs to be is **fixed decimal**. Let's change it.

Select the **ABC** icon to the left of the **MSRP** column header.

From the menu, select **Fixed Decimal Number**. Notice that all the steps we performed on the Product query are being recorded under **APPLIED STEPS** in the right panel.

Now let's create a **Currency** column in the same way.

With the **Product** query selected, from the ribbon, select the **Add Column** tab,

Choose the **Column From Examples** drop-down.

Then select **From All Columns**.

In the first row of the newly added Column1, enter the first Currency value as `USD` and then hit Enter on your keyboard.

**Rename** the column header from **Column1** to **Currency**.

Select **OK** to apply the changes.

Notice that after you hit **Enter**, Power BI knows you want to split the **Price** column. The formula it uses is displayed above as well.

Now that we split the **Price** column into the **MSRP** and **Currency** columns, we no longer need the original Price column. Let's remove it.

Make sure that you're still viewing the Product query. Right-click on the **Price** column.

Select **Remove** from the options menu.

## Section 6: Remove unwanted rows

In the **Geography** query, notice that the first two rows are informational. They aren't part of the data. Similarly, in the Manufacturer query, the last couple of rows aren't part of the data. Let's remove them so we have a clean dataset to work with.

In the **Queries pane** to the left of the screen, select the **Geography** query.

From the ribbon, select the **Home** tab.

Choose the **Remove Rows** drop-down.

Then, select **Remove Top Rows**.

The **Remove Top Rows** dialog box opens. Enter **2** in the text box since we want to remove 2 rows, the top informational data row and the blank second row.

Then, select **OK**.

Notice the first row in the Geography query contains the column headers. Let's move them into the column header position.

Make sure that the **Geography** query is still selected in the Queries pane. From the ribbon at the top of the screen, select the **Home** tab.

Then choose **Use First Row as Headers**.

Power BI then predicts the data type of each field again. Notice that the column **Zip** was changed to the **Whole Number** Data Type. Let's change it to **Text** again as we did earlier. If we don't, we'll see errors when loading the data.

Select the **data type** icon to the left of the **Zip** column header.

From the options menu, select **Text**.

Select **Replace Current** in the **Change Column Type** dialog box.

From the **Queries** pane, select the **Manufacturer** query. Notice the bottom three rows aren't part of the data. Let's remove them.

From the ribbon, select the **Home** tab.

Choose the **Remove Rows** drop-down.

Then, select **Remove Bottom Rows**.

The **Remove Bottom Rows** dialog box opens. Enter **3** in the **Number of rows** text box.

Then, select **OK**.

## Section 7: Transpose data

From the **Queries pane** to the left of the screen, select the **Manufacturer** query. Notice that the **ManufacturerID**, **Manufacturer**, and **Logo** data are laid across in rows. Also notice that the header isn't useful. We need to transpose the table to meet our needs. Transposing a table treats the rows as columns and columns as rows, effectively inverting the layout of a table.

From the ribbon at the top of the screen, select the **Transform** tab, then choose **Transpose**.

Notice that this transposes the data into columns. Now we need the first row to be the header.

From the ribbon at the top of the screen, select the **Home** tab, and then choose the **Use First Row as Headers** button.

Notice that now the **Manufacturer** table is laid out the way we need it with a header and values along columns.

Also, notice that with the **Query Settings** pane, under **APPLIED STEPS**, you see the list of transformations and steps that were applied. You can navigate through each change made to the data by selecting the step. Steps can also be deleted by choosing the **X** that appears to the left of the step. The properties of each step can be reviewed by selecting the **gear** to the right of the step.

## Section 8: Append queries

To analyze the sales of all countries, it's convenient to have a single Sales table. To do this, you need to use the **Append Queries** feature. With Append Queries, we can add all the rows from the **International Sales** query to the **Sales** query.

In the **Queries** pane to the left of the screen, select the **Sales** query.

From the ribbon at the top of the screen, select the **Home** tab, and then choose **Append Queries** button.

The **Append** dialog box opens. You can append Two tables or Three or more tables. Leave **Two tables** selected since we're appending just two tables.

From the **Table to append** drop-down, select **International Sales**.

Then, select **OK**.

You now see a new column in the **Sales** table called **Country**. Since the **International Sales** query had the extra column for **Country**, the Power Query Editor added the **Country** column to the newly updated **Sales** table when it loaded the values from the **International Sales** query.

You might also notice that there are **null** values in the **Country** column by default for the **Sales** table rows. This is because that column didn't exist for the table with USA data. We now add the value **USA** as a data shaping operation.

From the ribbon at the top of the screen, select the **Add Column** tab, and then choose the **Conditional Column** button.

In the **Add Conditional Column** dialog box, enter the name of the column as **CountryName**.

Select **Country** from the **Column Name** drop-down menu.

Choose **equals** from the **Operator** drop-down menu.

Enter **null** in the **Value** text box.

Enter **USA** in the **Output** text box.

Select the value drop-down menu under **Else**, and then choose the **Select a column** option.

Choose **Country** from the column drop-down menu.

Then select **OK**.

This reads: *If the current Country value is equal to null, then the value should return USA; otherwise, if the value isn't null, then use the current Country value.*

Note

A common mistake on the previous step is that the **Else** may not be set correctly. Please double check that your **Else** part of the conditional column matches the screenshot above.

You see the **CountryName** column in the Query editor window. Notice that in the **APPLIED STEPS** list, it's added to the list the action you completed.

The original **Country** column containing the null values is no longer needed and can be removed from the final table for analysis.

In the **Sales** query, right-click on the **Country** column.

Select **Remove** from the options menu.

With this column now removed, we can now **rename** the **CountryName** column to **Country**.

Right-click on the **CountryName** column and **rename** it to **Country**.

Select the **Data Type** icon to the left of the **Country** column header and change the **Data Type** to **Text**.

Next, select the **Data Type** **icon** to the left of the **Revenue** column header.

Change the **Data Type** to **Fixed decimal number**. We do this because it's a currency field.

Note

The difference between a Fixed decimal number and a Decimal number is related to the length and precision of the decimal places. For more information, see Number types.

When the data is refreshed, it processes through all the **APPLIED STEPS** that you created.

The newly named **Country** column has names for **all countries**, including the USA. You can validate this by selecting the drop-down menu next to the **Country** column to see the unique values.

At first, you only see USA data. Select the **drop-down arrow** to the right of the **Country** column header. Select **Load more** to validate your data from all seven countries.

Select **Cancel** to close this filter. You *don't* need to apply this filter to the data.

Now that the **International Sales** data is appended to the **Sales** query, in order to avoid duplicating data we should suppress the **International Sales** table from loading into the data model.

From the **Queries** pane to the left of the screen, select the **International Sales** query.

Right-click on the **International Sales** query, and then choose **Enable Load** to **deselect** this setting. This disables loading of the International Sales query into the data model.

You should see the name of this query become italicized in the Queries pane after deselecting the Enable load option.

Note

The appropriate data from the International Sales table will load onto the Sales table each time the model is refreshed. By removing the International Sales table, we are preventing duplicate data from loading into the model and increasing its file size. In some instances, storing very large amounts of data affects the data model performance.

You might receive a message about Possible Data Loss Warning. If so, select **Continue** when this warning appears.

Next, while the **International Sales** query is still selected, choose the **View** tab from the ribbon.

Select the **Query Dependencies** button.

This opens the **Query Dependencies** dialog box. The dialog box shows the source of each query and its dependencies. For example, we see that the **Sales** query has a **CSV file source** and a dependency on the **International Sales** query. This is useful information to share knowledge with your team members.

Select **Close** at the bottom of the dialog box.

Note

You can zoom in and out of the **Query Dependencies** view as needed.

You successfully completed import and data shaping operations and are ready to load the data into the Power BI Desktop data model to visualize the data.

From the ribbon at the top of the screen, select the **File** tab, then choose **Close & Apply**. This closes out the Power Query window and applies all changes.

All the data is loaded in memory in the Power BI Desktop. You see the progress dialog box with the number of rows being loaded in each table as shown in the Figure. Once the load completes, the results of this Power BI Desktop file are used in Module 3.

Note

It may take several minutes to load all the tables.

Once the data finishes loading, select the **File** tab from the ribbon at the top of the screen.

Then, from the options menu to the left, select **Save as** to save the file.

Name the file **MyFirstPowerBIModel**. Save the file in the **DIAD Reports (DIADReports)** folder.

In the navigation pane to the left of the screen, select the Data icon to view the data that was loaded. If you need to return to the Power Query editor again, navigate to **Home** > **Transform data** > **Transform data**




# Module 3: Build Your First Data Model

*Source: [https://learn.microsoft.com/en-us/training/modules/build-your-first-data-model](https://learn.microsoft.com/en-us/training/modules/build-your-first-data-model)*


---

## Introduction

In this Module, you learn how to:

Understand how to create relationships to link data property

Learn how to add and use visualizations

Learn how to create groups to organize data

## Example scenario

You continue to act as the Chief Marketing Officer (CMO) for VanArsdel, Ltd. In this scenario, you need to build a data model for VanArsdel, Ltd. Then after you build the model, you need to use visualizations to help show your findings from exploring the data.

Continue to use your **MyFirstPowerBIModel.pbix** file from Module 2. If you're joining at this point or unable to complete Module 2, start this Module using the *Lab 1 solution.pbix* file in the **Reports** folder.

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

Continue to use your **MyFirstPowerBIModel.pbix** file from Module 2. If you're joining at this point or unable to complete Module 2, start this Module using the *Lab 1 solution.pbix* file in the **Reports** folder.

## Section 1: Data modeling

Open the *MyFirstPowerBIModel* file (the file you saved at the end of Module 2) and go to the main **Power BI Desktop** window.

Select the **Table view** icon in the left navigation menu.

Select and expand the **Sales** table in the **Data** pane.

Scroll up and down to see how fast you can go through millions of rows.

Select the **Model view** icon in the left navigation menu.

You see the tables you imported along with relationships. The Power BI Desktop can often automatically infer relationships between the tables:

A relationship is created between the Sales and Product tables using the ProductID column.

A relationship is created between the Product and Manufacturer tables using the ManufacturerID column.

Power BI supports multiple types of relationships:

1 to many

1 to 1

Many to many

For this exercise, use the 1 to many type of relationship, which is the most common type of relationship.

This means one of the tables involved in the relationship should have a unique set of values. You create other relationships later in the Module.

Drag, resize, and move the tables to appear like those shown in the following screenshot.

Note

Tables might not look the same as shown in this screenshot. You can zoom in and out of the relationship models by dragging the zoom slider in the bottom right corner of the window. Also, if you want to make sure you can see all the tables, use the **Fit to Screen icon**. You can resize the tables by selecting the borders of the tables and dragging them.

## Section 2: Data exploration

Now that you loaded the data, analyze the sales by country. Make sure that you’re currently viewing the report you created and titled *MyFirstPowerBIModel* in the previous Module.

Select the **Report view** icon from the left navigation menu.

Select the **Clustered column chart** visual from the **Visualizations** pane.

From the **Data** pane to the right of the screen, expand the **Geography** field.

Then, select the **checkbox** next to the **Country** field. The Country field is placed in the **X-axis** box in the **Visualizations** pane.

Still in the **Data** pane, expand the **Sales** table.

Select the **checkbox** next to the **Revenue** field. The Revenue field is placed in the **Y-axis** box in the **Visualizations** pane.

**Resize** the visual as needed by dragging the anchor points around the edges of the visual.

Note

The Sum of Revenue of each country is the same. This is because there is currently no relationship between the tables used in the visual. In the next unit, you'll learn more about visualization and how to create missing relationships.

---

## Create missing relationships and use data visualizations

Make sure that you're viewing the report titled *MyFirstPowerBIModel* from the previous unit. Now you can create new relationships that are missing in your report.

## Section 1: Create missing relationships

Currently, there's no relationship between the **Sales** and **Geography** tables, so you need to make one:

Select the **Model** icon in the left navigation menu to go to the **Model view**.

The sales data is by Zip code, so you need to connect the **Zip** column from the **Sales** table with **Zip column** in the **Geography** table. Select, drag, and drop the **Zip** field in the **Sales** table and place on top of the **Zip** field in the Geography table.

You see the **Create relationship** dialog box opens with a warning message at the bottom stating the relationship has a many-to-many cardinality. In this type of relationship, more than one record in one table is related to more than one record in another table.

You see this warning because there aren't unique Zip values in the Geography table. Multiple countries could have the same Zip code, which triggers the warning. Let’s concatenate the Zip and Country columns to create a unique value field to fix the issue.

Select the **Cancel** button at the bottom of the **Create relationship** dialog box.

You need to create a new column in both the **Geography** table and the **Sales** table that combines the **Zip** and **Country** columns. Start by creating a new column in the **Sales** table.

Select the **Report** icon from the left navigation menu to go to the **Report view**.

In the **Data** pane, hover over the **Sales** table name, then select the ellipses (…) to the right of the table name.

Choose **New Column** from the options menu. Then, a formula bar appears to help create this new column.

Now you can combine the Zip and Country columns into a new column called **ZipCountry**. To create this column called ZipCountry, type the following calculation in the formula bar:

`ZipCountry = Sales[Zip] & "," & Sales[Country]`

Note

If you get an error creating a new column, make sure your Zip column is the **Text Data Type**. Also, make sure your creating your new column on the **Sales table**.

Once the formula is in the formula bar, press **Enter** on your keyboard or select the **checkmark** to the left side of the formula bar.

Important

You’ll see IntelliSense appears to guide you to choose the correct column. The language you used to create this new column is called **Data Analysis Expression (DAX)**. You're connecting columns (Zip and Country) in each row by using the “&” symbol. The icon with an (fx), near the new column ZipCountry, indicates that you have a column containing an expression, also referred to as a calculated column.

An alternative way to add a new column is to select the table from the **Data** pane, then select the **Table Tools** or **Modeling** tab, and then choose **New Column** from the menu.

Now create a **ZipCountry** column in the **Geography** table by selecting the **Geography** table in the **Data** pane, then from the **Table Tools** tab in the top navigation ribbon, select **New Column**.

A formula bar appears. Enter the following DAX expression in the formula bar:

`ZipCountry = Geography[Zip] & "," & Geography[Country]`

You see a new column, **ZipCountry**, in the **Geography** table. The final step is to set up the relationship between the two tables using the newly created **ZipCountry** columns in each of these tables.

Select the **Model** icon in the left navigation menu to go back to the **Model view**.

Drag and drop the **ZipCountry** field from the **Sales** table and place on top of the **ZipCountry** field in the **Geography** table, then select **Save** in the **Create relationship** window.

Note

If you don't see the ZipCountry column, select **Collapse** twice at the bottom of the **Geography** and **Sales** tables. You may need to scroll down on the list of columns in each table.

You've successfully created a relationship. The number **1** next to **Geography** indicates it’s on the one-side of the relationship and the ***** next to **Sales** means it's on the many-side of the relationship. In summary, one to many in this context means that **one** row of the **Geography** table could relate to **many** rows of the **Sales** table.

Select the **Report** icon in the left navigation menu.

Go back to the **Report view**.

When you look at the clustered column chart you created earlier, it shows different sales for each country or region. The USA has the most sales, followed by Australia, then Japan.

Note

If your clustered column chart is missing countries then you might have made an error in the previous module.

By default, the chart is sorted by **Revenue**. Next, you begin to use data visualization for the data model you designed.

## Section 2: Data visualization

Select the **Clustered column chart** visual.

Select the **ellipses (…)** located near the top right corner of the visual (or, the ellipses might be at the bottom of the chart). You can Sort axis by Country. **Don't make any changes for now**.

Select the **Clustered column chart** again to close out the options menu.

Then, from the **Data** pane, expand the **Manufacturer** table.

Drag and drop the **Manufacturer** column to the **Legend** section of the **Visualizations** pane.

**Resize** the visual as needed in the canvas. Now you can see the top manufacturers by country.

Now you can try different visuals to see which chart represents the data the best.

With the **Clustered column chart** visual selected in the design space, select and change the chart to a **Stacked column chart** by choosing that visual type in the **Visualizations** pane.

Select the **ellipses (...)** in the corner of the visual to sort the **legend** in **descending** order.

If the Filters pane isn't yet expanded, select the **two greater than symbols (>>)** at the top right corner of the collapsed pane to expand it.

In the **Filters** pane, expand **Manufacturer** under the **Filters on this visual** section. A drop-down arrow will appear for you to expand when you hover your mouse over Manufacturer.

Using the **Filter type** dropdown menu, select **Top N**.

Enter **5** in the text box next to **Top**.

From the **Sales** table, drag and drop the **Revenue** field into the **By value** section.

Select **Apply filter** at the bottom of the **Manufacturer** section in the **Filters** pane to turn on the filter.

Notice the visual is filtered to display the top five manufacturers by Sum of Revenue. The manufacturer VanArsdel, Ltd. has a higher percentage of sales in Australia compared to other countries or regions.

If you want, you can now collapse the **Filters** pane until it's needed again. Now add total labels to the stacked visuals. You start with font formatting options.

Select the **Format visual** (the paintbrush icon) tab at the top of the **Visualizations** pane, and then expand the **X-axis** section.

Select the **Bold** and **Italic** options.

Go to the **Total labels** section in the **Visualizations** pane.

Switch the **Total labels** setting to **On**.

Notice the total labels now appear above each of the columns in the Stacked column chart. Any of these properties can easily be changed or turned on/off whenever you like.

Now let’s remove the total labels. Select the **On/Off** toggle setting next to **Total labels** to switch the setting to **Off** again.

Switch the setting to **Off**.

Now that you learned various visualization techniques, in the next unit you'll learn how to group elements so that you don't need to add filters to each visual.

---

## Group and bin data

In this unit, you learn the process of grouping data to ensure filters can be applied to multiple elements.

As you continue working as the CMO for VanArsdel, Ltd., you want to know who are the top five competitors by revenue. For this task, you can group them you don’t have to add a filter to every visual. Before you do that, you must remove the Top 5 visual level filter you added earlier.

## Section 1: Create Groups

Select the **Stacked column chart** in the canvas area.

Hover over and select the  **Clear filter** (eraser) icon next to the Manufacturer field in the **Filters** pane. You might need to expand the Filters pane if you previously collapsed it.

Note

You'll only see the eraser icon if you hover your mouse over the Manufacturer filter section.

From the **Data** pane, expand the **Manufacturer** table.

Right-click on the **Manufacturer** field.

Note

Do not select the checkbox.

Select **New Group** from the options menu.

Go to the **Ungrouped values** section of the **Groups** dialog.

Use the CTRL key to multi-select: **Fabrikam, Inc.**, **Nod Publishers**, **Tailwind Traders**, and **Wide World Importers**.

Select the **Group** button. This adds a new group in the Groups and members section.

Double-click the newly created group and rename it **Top Competitors**.

Select **VanArsdel, Ltd.** from the **Ungrouped values** section and select the **Group** button to create the **VanArsdel, Ltd.** group.

Select the checkbox **Include Other group**. This action creates an **Other** group that includes all the other manufacturers.

Note

You may need to use the scroll bar along the bottom of the Groups box to move to the right to see the Include Other Group button.

Select **OK** to close the **Groups** dialog box.

Go back to the **Build visual** tab of the **Visualizations** pane.

With the **Stacked column chart** selected in the canvas, select the **X** next to **Manufacturer** in the **Legend** section of the **Visualizations** pane. This action removes the Manufacturer field from the Legend.

From the **Data** pane, drag and drop the newly created **Manufacturer (groups)** to the **Legend** section of the **Visualizations** pane. Now you can see that VanArsdel has nearly 50% share in Australia.

Note

It’s ok if the colors used in your column chart are in a different order than what appears in the screenshot. You can change the Legend sort order if you want.

Hover over one of the columns in the **Stacked column chart** and right-click.

Select **Show as a table** from the menu. This action starts the **Focus** mode with the chart displayed on top and the data displayed below. You can see VanArsdel has a large percent of the Australian market.

Use the **Orientation** icon in the top right corner of the chart to switch to the **vertical layout**. In this layout, you see the chart in the left panel and the data in the right panel.

Go back to the **horizontal layout**, then select **Back to Report** to go back to the **Report** canvas.

Note

You can also right-click on a column in the chart and select **Show data point as a table** to see records for a specific data point.

Next, create a **Sum of Revenue by Manufacturer** visual. Select the white space in the canvas to deselect the Stacked column chart visual.

From the **Data** pane, select the checkbox next to the **Revenue** field in the **Sales** table.

From the **Data** pane, select the checkbox next to the **Manufacturer** field in the **Manufacturer** table.

From the **Visualizations** pane, select the **Treemap** visual. This action creates a **Sum of Revenue by Manufacturer Treemap** visual.

Next, you see how the Stacked column chart and Treemap visual interact with each other.

In the **Treemap** visual, select **VanArsdel, Ltd.** You'll see the **Stacked column chart** highlights only the values related to VanArsdel, Ltd. This confirms that VanArsdel, Ltd. has a large percentage of the Australian market.

To remove the highlight, select **VanArsdel, Ltd.** again. This interaction between visuals is called **cross-highlighting**.

## Section 2: Visual level filters

Earlier in the module, you added a Top 5 Visual level filter. Now you need to add a filter to the Page level, so you can work with the top competitors and VanArsdel, and filter out all the other manufacturers. Make sure the **Filters** pane is expanded and open.

Note

Page-level filters apply to all visuals on the page. Visual-level filters apply only to the visual.

Keep the **Treemap** visual selected.

From the **Data** pane, drag and drop **Manufacturer (groups)** from the **Manufacturer** table to the **Filters on this page** box in the **Filters** pane.

Select both **Top Competitors** and **VanArsdel, Ltd.**

Now, add a visual that provides sales information over time. First, select the white space in the **canvas** to make sure nothing is selected.

Select the checkbox next to the **Date** field in the **Sales** table.

Note

A date hierarchy is created if you have Auto date/time turned on. If you don't see the date hierarchy go to **File** -> **Options and settings** -> **Options** -> **Current file** -> **Data load** -> **Auto date/time** to turn it on.

Select the checkbox next to the **Revenue** field in the **Sales** table. This action creates a visual.

Change the visual to a **Clustered column chart**. In the X-axis section, a date hierarchy is used. There are arrows on the visual header you can use to go through the hierarchy.

You already know from the data that VanArsdel, Ltd. has a large share of the market in Australia, but now you want to know how VanArsdel, Ltd. performed over time in Australia.

Select the **Sum of Revenue by Country and Manufacturer (groups)** chart.

Select the **X** in the **Visualizations** pane to remove **Manufacturer (groups)** from the legend.

Select **VanArsdel** in the **Sum of Revenue by Manufacturer** visual (Treemap).

Then, hold the CTRL key and select **Australia** in the **Sum of Revenue by Country** visual. This action multi-selects and highlights both values.

With both VanArsdel, Ltd. and Australia selected, you can see a spike in 2021 sales for VanArsdel, Ltd. in Australia. You decide to investigate this spike in sales further.

Hover over the **Sum of Revenue by Year** visual.

Select the **down arrow** at the top of the **Sum of Revenue by Year** visual to turn on the **Drill Mode**.

Select the **2021** column in the **Sum of Revenue by Year** visual.

Now that you drilled down to the quarter level of 2021, you see a large spike in the fourth quarter. You decide to investigate more.

Select the **double down-arrow** icon at the top of the **Sum of Revenue by Year and Quarter** visual. This action drills down to the next level of the hierarchy, which is the **month** level.

Select the **up-arrow** icon at the top of the **Sum of Revenue by Month** visual to drill back up to the **Quarter** level again.

Select the **drill up** icon a second time to go all the way back up to the **Year** level.

Select the **split arrow** icon at the top of the **Sum of Revenue by Year** visual. This action expands down to the next level of the hierarchy, which is quarters for all the years; not just 2021.

Resize the visual as needed. You notice the fourth-quarter sales are always high, but in 2021 there's a larger sales spike in the fourth quarter than usual.

Expand down one more time to the month level to investigate. Select the **split arrow** icon for the **Sum of Revenue by Year and Quarter** visual again. This action drills down to the next level of the hierarchy and shows revenue for months for all the years.

## Section 3: Use slicers

Now you want to add a slicer to filter the data by the manufacturers.

Make sure there are no filtered or highlighted values.

**Be sure to reset all visuals to stop highlighting selected values.** If you have values selected, select the blank space of the Sum of Revenue by Country visual. This action clears any selected values.

Select the white space in the canvas to deselect any currently selected visuals.

From the **Data** pane, select the checkbox next to the **Manufacturer** field in the **Manufacturer** table.

From the **Visualizations** pane, select the **Slicer** visual.

Select **VanArsdel, Ltd.** from the list of Manufacturers. You see all the visuals are filtered based on your selection. Also, select **Australia** in the **Sum of Revenue by Country** visual.

With the **Slicer** visual still selected, go to the **Format visual** tab of the **Visualizations** pane.

Expand the **Slicer settings** menu. Then, expand the **Options** menu in the **Slicer settings**.

From the **Options** drop-down under **Style**, select **Dropdown**.

Then, in the **Slicer** visual, select **VanArsdel, Ltd.** from the **Manufacturer** dropdown.

Make sure you still have **Top Competitors** and **VanArsdel, Ltd.** selected in the **Manufacturer (groups)** filter in the **Filters** pane.

Note

There is a box for **Filters on all pages** in the **Filters** pane. If you have more than one report page, this is how you sync a filter for the whole file.

Now you can use the **Manufacturer** slicer to analyze one manufacturer at a time. First, deselect the **Australia** column in the **Sum of Revenue by Country** visual to remove the filter by country.

Next, select the **Sum of Revenue by Manufacturer** (Treemap) visual.

From the **Visualizations** pane, navigate to the **Build visual** tab and select the **Card** visual. The card visual gives us the **Sum of Revenue** as we filter and cross-filter the visuals.

To edit the amount of units displayed after the decimal, go to the **Format your Visual** in the top of the Visualization Pane, expand **Callout**, apply settings to **Sum of Revenue**. In the **Value** section, adjust the **Value Decimal Places** to 2.

You see all key dimensions are in tables with related attributes, except for the date. For example, **Product** attributes are in the **Product** table. **Manufacturer** attributes are in the **Manufacturer** table. In the next unit, you’ll create a **Date** table.

---

## Create a date table

Make sure you still use the report you created titled **MyFirstPowerBIModel** from the previous units. You use it to create a Date table.

## Create a date table

Go to the **Table** view by selecting the **Table** icon in the navigation menu to the left of Power BI Desktop.

From the ribbon at the top of the screen, select the **Table Tools** tab.

Then, choose **New Table** from the menu at the top of the screen.

You see a new table called "Table" is created in the **Data** pane to the right of the Power BI Desktop and the formula bar opens at the top of your screen.

Enter the following formula in the formula bar, then hit **Enter** on your keyboard:

`Date = CALENDAR(DATE(2014,1,1), DATE(2022,12,31))`

You're using two DAX functions: the **CALENDAR** function, which accepts the start and end data, and the **DATE** function, which takes the year, month, and day fields.

For this scenario, you need to create dates from 2014 to 2021 (since we have data for those years). We can also add more fields, like **Year**, **Month**, **Week**, etc., to the table by using other DAX functions.

In the **Data** pane, select the **Date** field in the **Date** table.

The Date field is in the **Date/Time** data type, but you need it to be the **Date** data type. To change it, select the **Column Tools**  tab from the ribbon.

Then, choose the **Data type** drop-down and select **Date**.

Now, you need to create a relationship between the **Date** and **Sales** tables. From the ribbon, select the **Column Tools** tab, and then choose **Manage Relationships**.

The **Manage Relationships** dialog box opens. Select the **+ New relationship** button.

Then, the **New Relationship** dialog box opens. Select **Date** from the top dropdown menu.

Select **Sales** from the second dropdown menu.

Highlight the **Date** field in both tables by multi-selecting.

Then, select **Save** to close the **New relationship** dialog box.

Select the **Close** button to close the **Manage relationships** dialog box.

Now, select the **Report view** icon in the left navigation menu to go to the **Report view**.

The Sum of Revenue by Date chart looks different now. Let's fix that.

Select the **Sum of Revenue by Date** visual.

From the **X-axis** section in the **Visualizations** pane, select the **X** to remove the **Date** field.

From the **Data** pane, expand the **Date** table.

Now, drag and drop the **Date** field from the **Date** table to the **X-axis** section in the **Visualizations** pane.

Select the **Drill up** button above the visual until the visual is on the **Year** level.

Now, the new **Date** field behavior is like it was previously.

Since there are now two **Date** fields, you might be confused which one to use. To remove confusion, hide the **Date** field in the **Sales** table.

From the **Data** pane, hover over and select the **ellipses (…)** to the right of the **Date** field in the **Sales** table.

Then, select **Hide** from the options menu.

Use the preceding steps to hide **Country**, **ProductID**, **Zip**, and **ZipCountry** in the Sales table as well. The only fields that should now be in the **Sales** table are **Revenue** and **Units**.

Next, hide **ZipCountry** from the **Geography** table.

Then, hide **ManufacturerID** from the **Manufacturer** table.

Hide **ProductID** and **ManufacturerID** from the **Product** table.

Tip

It’s best practice to hide fields that are not used in your report visuals. These fields are the basis of our relationships between each table so we should not delete them.




# Module 4: Use Hierarchies and DAX in Your First Data Model

*Source: [https://learn.microsoft.com/en-us/training/modules/use-hierarchies-dax-first-data-model](https://learn.microsoft.com/en-us/training/modules/use-hierarchies-dax-first-data-model)*


---

## Introduction

In this module, you learn how to:

Create hierarchies for organizing data

Add and use matrix visualizations

Add DAX measures to models for further analysis

## Example scenario

You continue to act as the Chief Marketing Officer (CMO) for VanArsdel, Ltd. In this scenario, you need to add a hierarchy to the data model you created for VanArsdel, Ltd in Module 3. Then after you add hierarchies to the model, you need to use a matrix visualization and DAX measures for further analysis.

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

Make sure you're currently viewing the report you created titled **MyFirstPowerBIModel** from the previous units. If you're starting from this module, or missed the previous, start with the **Lab 2 solution.pbix** file located in the **Reports** folder in the student files.

In this exercise, you explore the use of hierarchies in your first data model and how to create them.

You're still the CMO for VanArsdel, Ltd. in this exercise and you model the data for Australia, VanArsdel, Ltd. and 2021. Check if the spike occurred in a specific region in Australia.

Select the **Sum of Revenue by Country** visual.

From the **Data** pane, drag and drop the **State** field from the **Geography** table below the **Country** field in the **X-axis** section of the **Visualizations** pane.

Drag and drop the **District** field from the **Geography** table below the **State** field in the **X-axis** section of the **Visualizations** pane. You just created a hierarchy.

Select the **up arrow** in the **header** area of the visual twice to **Drill up** to the top level of the hierarchy again.

Make sure that **VanArsdel, Ltd.** is still selected in the **Manufacturer** slicer.

Turn on the **Drill down mode** by selecting the **down arrow** of the **Sum of Revenue by Country** visual once.

Select **Australia** to drill down to the **State** level.

From the **Sum of Revenue by Year** visual, select 2021 and notice what happens to the **Sum of Revenue by Country**.

Tip

If you notice this step performs a drilldown into a table of data, select **Back to report**, then **Data / Drill**, and disable *Data point table* in the ribbon.

Now, **Drill up** to the **Country** level again.

**Turn off** drill mode by selecting the down arrow again on the **Sum of Revenue by Country** visual. Now analyze the data by product. To start, create a product hierarchy.

Make sure that no visuals are selected in the design canvas.

From the **Data** pane, **right-click** the **Category** field in the **Product** table

Select **Create Hierarchy**.

You see a new object called **Category Hierarchy** is created inside the **Product** table.

Double-click **Category Hierarchy** and rename it to **Product Hierarchy**.

**Right-click** the **Segment** field in the **Product** table, select **Add to Hierarchy**, then choose **Product Hierarchy**.

Use steps 11-16 to add the **Product** field from the Product table to the Product Hierarchy. You created a Product Hierarchy with the fields **Category**, **Segment**, and **Product**.

Select the white space in the canvas to deselect any visual that might be selected.

From the **Visualizations** pane, select **Clustered bar chart**.

With the **Clustered bar chart** still selected, from the **Data** pane, expand the **Product** table.

Select the **checkbox** to the left of the **Product Hierarchy**. Notice the complete hierarchy is selected.

From the **Data** pane, expand the **Sales** table.

Select the **checkbox** to the left of the **Revenue** field.

Note

The **Product Hierarchy** is added to the **Y-axis** field and **Sum of Revenue** is added to the **X-axis** field in the **Visualizations** pane. You see the visual in the canvas change and update as you select different fields.

---

## Build a matrix visual

Now, add a Matrix visual so you can view the data in rows and columns. You can apply conditional formatting to the Matrix visual to highlight the outliers.

Select the **Sum of Revenue by Category** Clustered bar chart and change it to a **Matrix** visual.

Select the **+ (plus sign)** to the left of the **Urban** row to drill down.

Next we'll add a *percent of total* field to the visual, enabling a better perspective of the data. With the **Matrix** selected, go to the **Data** pane.

From the **Data** pane, drag and drop the **Revenue** field from the **Sales** table to below the existing **Sum of Revenue** field in the **Values** section of the **Visualizations** pane. It will look like **Sum of Revenue** is in the **Values** section twice.

Select the **down arrow** to the right of the newly added **Sum of Revenue** field in the **Values** section.

From the visual field menu, hover over **Show value as**.

Then, select **Percent of grand total**.

Right-click on the newly created field and select **Rename for this visual**.

Name the field **%GT Revenue**.

Drill back up to **Category** level if you aren't already there in the **Matrix** visual.

Then, select **Enable drill down mode** in the header of the Matrix visual.

Now, select the word **Urban**.

Make sure that the **Matrix** visual is still selected. Then, hold down the **Ctrl** key to multi-select the **2021** column in the **Sum of Revenue by Year** visual and the **Australia** column in the **Sum of Revenue by Country** visual.

Now, look at the **Extreme** category for Australia over time. Notice the **Extreme** segment has around **40%** of the grand total.

Now, **drill down** into the **Extreme Segment** to determine if a **Product** stands out.

In the **Matrix** visual, select the word **Extreme** to drill down to the **Product** level.

Note

The revenue totals and % of Grand Total may differ from the images shown here if you used the +/- icons instead of the row name in **steps 12 & 15** to drill down. **Using +/- icons** expands or collapes rows while keeping totals at the highest level. **Clicking a row or label** drills down, recalculating the grand total based on the selected item.

Resize the visual as needed.

Select the **ellipses (…)** in the top or bottom right corner of the matrix visual header.

Select **Sort By > %GT Revenue** and **Sort Descending** (should be selected by default).

Now you can see the top **Products**. Make sure **2021** is selected in the **Sum of Revenue by Year** visual, and **Australia** in the **Sum of Revenue by Country** visual. Notice Maximus UE-04 and Maximus UE-21 are the top products and that Product **Maximus UE-04** has nearly **7%** of the grand total *for the Extreme Segment of the Urban Category*.

You can take the time to test these drilldown features by clicking on the row names, the +/- icons, and the arrows above the visuals to produce different totals.

---

## Build DAX measures

Earlier you created a calculated column named **ZipCountry** using Data Analysis Expression (DAX). Now, create a **Percent Growth** calculated measure so you can compare sales over time.

Before you start, learn the difference between a measure and a calculated column:

- A *Calculated Column* is evaluated row-by-row. You extend a table by adding calculated columns.

- A *Measure* is used to aggregate values from many rows in a table.

Tip

Calculated columns are often better suited to be created in the Power Query Editor or as part of the data importing process because of the row-by-row evaluation mentioned above.

In the **Data** pane, select the **Sales** table.

From the ribbon at the top of the screen, select the **Table Tools** tab, then select **New Measure**. A formula bar appears.

Enter the formula:

`PY Sales = CALCULATE(SUM(Sales[Revenue]), SAMEPERIODLASTYEAR('Date'[Date]))`

Select the **checkmark** to the left of the formula bar or hit **Enter** on your keyboard. You'll see the **PY Sales** measure created in the **Sales** table.

Now, create another measure using a different method. In the **Data** pane, **right-click** the **Sales** table.

Select **New Measure** from the options menu. A formula bar opens.

In the formula bar, enter the following formula:

`% Growth = DIVIDE(SUM(Sales[Revenue])-[PY Sales],[PY Sales])`

Select the **checkmark** next to the formula bar or hit **Enter** on your keyboard. You'll see the **% Growth** measure is added to the **Sales** table.

Make sure the **Matrix** visual is still selected. If not, select the **Matrix** visual and check that you still have the **Australia** and **2021** columns selected in the other visuals.

In the **Data** pane, select the **checkbox** next to the newly created **PY Sales** and **% Growth** measures in the **Sales** table. This action adds the measures to the **Values** section of the **Matrix**.

Resize the **Matrix** to see the newly added fields (you might also have to adjust the size of the other visuals where needed).

To format the fields, start from the **Data** pane, select the **% Growth** field (the name, not the checkbox) in the **Sales** table.

From the ribbon at the top of the screen, select the **Measure Tools** tab, choose the **Format** drop-down.

Then, select **Percentage**.

Tip

If your **% Growth** calculated measures show as 0.00% at any point, check that you still have **2021** and **Australia** selected as filters from the other visuals.

From the **Data** pane, select the **PY Sales** field (the name, not the checkbox) in the **Sales** table.

From the ribbon at the top of the screen, select the **Measure Tools** tab, choose the **Format** drop-down.

Then, select **Currency** (if it isn’t already formatted to Currency) and change the number of decimal places from **Auto** to **2**.

From the Data pane, select the **Revenue** field in the **Sales** table.

Now, choose the **Format** drop-down under the **Column tools** tab, select **Currency**, and change the number of decimal places from **Auto** to **2**.

Make sure you still have **Australia** selected in the **Sum of Revenue by Country** visual, and you still have the **2021** column selected in the **Sum of Revenue by Year visual**. Notice **Maximus UE-04** has nearly **158%** growth compared to last year.

Select the white space in the canvas to **deselect** any of the possible selected visuals.

Then, from the ribbon at the top of the screen, select **File**, and choose **Save** from the menu to the left of the screen.

Make sure to keep your *MyFirstPowerBIModel* file; you need it for the upcoming modules.




# Module 5: Data Visualization and Reports in Power BI

*Source: [https://learn.microsoft.com/en-us/training/modules/data-visualization-reports-power-bi](https://learn.microsoft.com/en-us/training/modules/data-visualization-reports-power-bi)*


---

## Introduction

Continue to use your **MyFirstPowerBIModel** file saved from the previous module. If you're joining the Dashboard in a Day at this point or were unable to complete previous modules, start this module with the provided **Lab 3 solution.pbix** file found in the Reports folder of the class files.

In this Module, you still are the Chief Marketing Officer of VanArsdel, Ltd., and you need to create a full report that you publish to the Power BI Service in a later module. You learn how to do conditional formatting, add a logo to the manufacturer filter, and apply a custom theme to the report.

The flow of this Module includes screenshots to provide a visual aid for the users and a text description of the steps the user needs to follow. In the screenshots, sections are highlighted with red boxes to indicate the action or area on which you need to focus.

---

## Apply conditional formatting

## Conditional formatting

Now that we made a data model and added visuals, you now create a full report.

Let's get started. We begin where we left off at the end of **Module 4** within the report you saved titled **MyFirstPowerBIModel**. If you're starting the lab from this module, or missed the last modules, start with the **Lab 3 solution.pbix** file located in the **Reports** folder of the student files.

With the **Matrix** visual selected, navigate to the **Values** section in the **Visualizations** pane.

Select the arrow to the right of **% Growth**.

Select **Conditional Formatting** and then choose **Background color**. The **Background color** dialog box opens. This dialog provides options to format the report background color using either rules or diverging colors.

In the **Background color - % Growth** dialog box, select the **Add a middle color** checkbox.

Then, select **OK.**

Note

Conditional formatting can also be based on another column using the **Color based on** option from the drop-down menu.

Note

As a reminder if you see 0.00% for every value in the **% of Growth** column in the Matrix then you likely need to multi-select **Australia** and **2021**, and drill-down to the **Extreme** catageory in the **Matrix** visual, like you did in **Module 4**.

Make sure the report is filtered by **VanArsdel, Ltd.** using the **Manufacturer** slicer.

Select the **down arrow** in the header of the **Sum of Revenue by Country** visual to turn on the **drill down** mode *(this could also be located at the bottom of the visual based on how you placed the visual within the canvas)*.

Within the visual, select the **Australia** column to drill down to the **State** level.

**Disable** drill down mode on the **Revenue** **by** **Country and State** visual.

Make sure you still have the year **2021** selected in the **Sum of Revenue by Year** visual. If you don't, hold down the **Ctrl** key on your keyboard and select the **2021** column.

At this point, your canvas and visuals should look like the figure here. You can resize and move visuals as you need.

Select the **Manufacturer slicer** visual in the canvas.

In the **Visualizations** pane, switch to the **Format** **visual** tab.

Expand the **Slicer** **settings** section, then expand the **Options** section.

From the **Style** drop-down, select **Tile**. Notice that the Manufacturer slicer visual changes to a tile style. You might need to resize your visual so that you can view all the Manufacturers at once within the list.

Note

There are other options that can optionally be changed here to modify the outline color, weight, and more. There is an option to enable the **Select All** option in the visual. There is also an option to make the slicer **multi-select**. Feel free to explore other formatting options.

Select **VanArsdel, Ltd.** in the **Slicer** visual.

Now that we applied some conditional formatting and extended the Slicer visual to have clickable tiles, we'll work towards refining the report further in the next unit.

---

## Exercise - Add a logo to the manufacturer filter

In this unit, we continue adding more functionality and visual elements to help wrap up our report. Ensure that you're working on the **MyFirstPowerBIModel** file that you have been using in the previous units.

## Section 1: Add a logo

Now it would be nice to add logos of the manufacturer to the Slicer instead of just text. Let's do it.

Check that the **Manufacturer** slicer visual is still selected. From the **Data** pane, select the **Logo** field from the **Manufacturer** table. (*Do not* select the checkbox; only select the *name* of the field.)

From the ribbon, select the **Column tools** tab and choose the **Data Category** drop down.

Then, select **Image URL.** Setting the data category property to **Image URL** helps Power BI understand that the data in this field is a URL so it can render the image in the report.

With the **Slicer** visual selected, drag and drop the **Logo** field from the **Manufacturer** table to below the **Manufacturer** column in the **Field** box in the **Visualizations** pane.

Select the **X** to the right of the **Manufacturer** field in the box so that the **Logo** field replaces it.

**Resize** and **move** the visuals as needed.

Select the **VanArsdel, Ltd.** logo in the **Manufacturer** slicer visual to filter all the other visuals.

Select the **Sum of Revenue by Year** visual.

From the **Visualizations** pane, select the **Line and clustered column** chart to change the visual type.

From the **Data** pane, drag and drop the **% Growth** field from the **Sales** table to the **Line y-axis** box.

This provides a representation of the revenue and growth over time.

## Section 2: Gauge visual

Now, let's select the **Sum of** **Revenue** card visual so we can change it to a **Gauge** visual.

Select the **Sum of Revenue** card visual, and from the **Visualizations** pane, select the **Gauge** visual.

From the **Data** pane, drag and drop the **PY Sales** field from the **Sales** table to the **Target value** in the **Visualizations** pane.

**Resize** and **move** the visuals as needed. Now we can compare **Revenue** with the target.

Next we'll select the colors for this visual.

Select the **Gauge** visual.

From the **Visualizations** pane, select the **Format Visual** tab (*the paint brush icon*).

Expand the **Colors** section.

Select the drop-down for **Fill** color.

Notice you can pick a color from the default color palette or pick **More colors**. No need to make a change here because the next steps will standardize all the report colors used.

Let's check out some of the **themes** available.

Ensure that the **Gauge** visual is still selected.

From the ribbon, select the **View** tab and choose the drop-down arrow within the **Themes** menu.

Then, select the **Temperature** theme.

Notice that the colors on all the visuals are updated. Feel free to try the other out-of-the-box themes.

Now that we covered adding logos to the manufacturer slicer, changed the clustered column chart, adapted the card visual to a gauge, and looked through report themes, in the next unit we'll cover the application of custom report themes.

---

## Exercise - Apply a custom report theme

In our scenario, the Marketing department provides standard color themes to be used across reports. We can use the **Report Theme** feature in Power BI by uploading a theme. The **Report Theme** requires a **JSON file** where the data colors, background, foreground, and a table of accent colors are defined. The JSON file can be used across all the reports.

Make sure you're using the file titled **MyFirstPowerBIModel** you've been working on in the previous units.

## Section 1: Apply a custom report theme

From the ribbon, select the **View** tab and choose the drop-down within the **Themes** menu.

Then, select **Browse for themes**.

A file browser dialog box opens. Navigate to the **Data** folder, then the **Theme** folder (DIAD/Data/Theme).

Select the **DIADTheme2** file and then choose **Open**.

Note

Here you can save and add your custom themes.

Once the theme is imported, a success dialog box opens. Select **Got it**.

Notice colors on all the visuals are updated. Your report should look like the figure below. This theme looks good. Now, most of the visuals are blue, so let's add some contrast.

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

Select the **Sum of** **Revenue by Country and State** visual.

Using the arrows within the visual header, **Drill up** to the **Country** level.

While the **Sum of Revenue by Country** visual is still selected, in the **Visualizations** pane, select the **Format visual** tab (*the paint brush icon*).

Expand the **Columns** section, then the **Color** section.

Using the drop-down menu, select a *light shade* of **gray** as the **Default color.**

Check that the **Sum of Revenue by Country** visual is still selected.

In the **Visualizations** pane under the **Format visual** tab, turn **On** the **Data labels**, and expand this section.

Expand the **Value** sub-section in the **Data labels** section.

Change the **Display units** to **Millions**.

Notice there are many formatting options. For example, a visual title can be changed and formatted, or you can add a border and background to the visual. Feel free to explore other options.

Let's move to another visual.

Select the **Sum of Revenue and % Growth by Year** visual.

Note

You may need to move or resize the visuals to see all the information that will be needed in the next steps.

Since there's no **Revenue** value in the year **2022**, right-click on the line above **2022** and select **Exclude**.

Next, from the **Visualizations** pane, select the **Format visual** tab (*the paint brush icon*).

Expand the **Columns** section.

Expand the **Color** section.

Select a *light shade* of **gray** as the **Default color**.

Check that the **Sum of Revenue and % Growth by Year** visual is still selected. You can collapse the **Columns** section.

In the **Visualizations** pane under the **Format visual** tab, expand the **Lines** section.

Then, expand the **Color** section.

Set the % **Growth** color to **black**.

Now let's add a **report title**.

From the ribbon, select the **Home** tab and then choose **Text box** under *Insert*. Notice a text box visual is added.

Resize and move the visuals as needed.

Enter `Manufacturer Analysis` in the text box.

Highlight **Manufacturer Analysis** to format the text.

Select **Segoe (Bold)** as the **font**.

Select **32** as the **font size**.

Resize the text box as needed.

From the ribbon, select the **View** tab.

In the **Page options** section, select the **checkboxes** next to **Visual_Gridline_Show** and **Snap to grid**. This helps with aligning the visuals.

Now, use the **Gridlines** and **Snap to grid** features to **position** and **resize** your visuals like the figure below.

Uncheck the **Gridlines** and **Snap to grid** options to disable these features once you finish moving the visuals into the correct places.

**Right-click** the page name in the lower-left corner.

Then, select **Rename Page** from the options menu.

**Rename** the page to **Manufacturer**.

Now that we have a basis for the report, in the next Unit we'll cover how to import and implement custom visual elements.




# Module 6: Import Custom Visuals and Add Bookmarks

*Source: [https://learn.microsoft.com/en-us/training/modules/import-custom-visuals](https://learn.microsoft.com/en-us/training/modules/import-custom-visuals)*


---

## Introduction

Continue to use your file from the previous module. If you're joining the Dashboard in a Day at this point you can open the completed files to catch up.

In this Module, you still are the CMO of VanArsdel, Ltd., and you need to complete your report. You learn to import custom visuals and add bookmarks to your report to prepare your report to publish to the Power BI Service.

---

## Exercise - Import custom visuals

Power BI comes with many stylization options out of the box, but users are also given the opportunity to import their own visuals. Let's go over this process.

Make sure you're using the **MyFirstPowerBIModel** file you have been working on in the previous units. If you missed the previous modules, or are starting from this one, open the **Lab 4 solution.pbix** file located in the **Reports** folder of your student files.

## Section 1: Add background images

We can use a background image to format the report. Let's try it.

Select the white space in the canvas to deselect any selected visuals.

From the **Visualizations** pane, select the **Format page** tab (*the paint brush icon*).

Expand the **Canvas Background** section.

Select the **Browse Image** button.

A **File** browser dialog box opens. Browse to the **DIAD** folder, then the **Data** folder (DIAD/Data).

Select the **Background.jpg** file.

Select the **Open** button.

Within the **Canvas background** section of the **Visualizations** pane, change and set the **Transparency** slider to **0%**.

Notice our template has space for a **header** and **slots** for images.

Resize and position the visuals as shown in the figure below:

## Section 2: Add a logo

Now let's add a logo.

From the ribbon, select the **Insert** tab and then choose **Image**.

Select **Style** from the **Format Image** section of the **Visualization Pane**. Then select **Browse**.

The **File** browser dialog opens. Browse to the **DIAD** folder then the **Data** folder (DIAD/Data).

Select the **VanArsdel_Logo.png** file.

Then, select **Open**.

Resize and drag the image to the top left corner of the report.

Note

The logo is white. You will need to place it over the blue background to see it.

Now let's change the font color of the report title.

Highlight **Manufacturer Analysis** within the text box.

Select the drop-down arrow next to the **A** to change the font color.

Select the color **white**.

Change the **font size** to **20**.

Within the **Effects** section of the **Format text box** pane, expand the **Background** sub-section.

Set the **Transparency** to **100%**.

Resize and move the visuals around if needed, making sure they're still in the same locations as before.

Now let's add a **smart narrative visual** to our report.

First, resize the **Sum of Revenue and % Growth by Year** visual to make space to the left of the visual at the bottom of the report.

Add a **Narrative visual** to the canvas. Remember, you need to deselect any current visuals by selecting blank space on the canvas.

Note

If your tenant has Copilot enabled, a window will open asking if you want to use **Copilot** to build the narrative. If so, select **Custom**.

The Narrative visualization helps you quickly summarize visuals and reports. It provides relevant innovative insights that you can customize.

## Section 3: Import custom visuals

Out of the box, Power BI has a large selection of visuals. However, there might be a use-case when you need a custom visual. To meet this requirement, the visualization engine is open-sourced. The Power BI community contributes visuals in the marketplace. You can add and use these visuals in your reports.

There's also an option to create your own visual or import visuals in Power BI Desktop.

Now, let's add a **custom visual**.

From the **Visualizations** pane, select the **ellipses** (**..**.) in the last row of visuals.

Select **Get more visuals**.

Note

You might be asked to sign into your Power BI account to access the custom visuals library. If you're unable to login, you can select **Import a visual from a file** and select the **Play Axis** visual that's found in the class files in the **Data** folder.

Type **play axis** in the **search box** in the top right-hand corner of the Power BI visuals dialog box.

Select the **Search** icon.

Select the **Play Axis (Dynamic Slicer)**.

Note

Notice the checkmark in the blue star. This image helps to identify certified custom visuals. Custom visuals that meet Power BI teams coding requirements are certified. Certified custom visuals support features like export to PowerPoint and the ability to display in subscription emails which aren't supported by non-certified custom visuals.

The **AppSource** dialog box appears.

Select the **Add** button below the **Play Axis (Dynamic Slicer)** cover image.

After a few moments, you should see a notification that the visual was successfully imported. Select **OK**.

Notice a new visual is added to the list of available visuals.

Select the white space in the canvas to deselect anything that might be currently selected.

From the **Visualizations** pane, select the newly imported **Play Axis** visual.

From the **Data** pane, select the **checkbox** next to the **Date** field in the **Date** table.

From the **Visualizations** pane, select the **Format visual** tab.

Expand the **Colors** section.

Turn on the **Show all** option.

**Resize** and **position** the visual as shown in the figure below.

---

## Exercise - Add bookmarks to a report

Now that we have a report ready, let's use **Bookmarks** to tell the story we discovered. Bookmarks capture the currently configured view of a report page, including filtering and the state of visuals, which helps to present the story.

## Section 1: Add bookmarks

Make sure you're using the **MyFirstPowerBIModel** file you've been working on in the previous units.

From the ribbon, select the **View** tab.

Select the **Bookmarks** button to turn on Bookmarks. The **Bookmarks** pane opens.

Select **Add** in the **Bookmarks** pane. This adds the current state of the visual to the bookmark.

Select the **ellipses** (**...**) to the right of the newly created **Bookmark 1**.

Choose **Rename** and change the name to **Initial State**.

In the **Sum of Revenue by Country** visual, select the **USA** column.

Hover over the **Sum of Revenue by Country** visual and select the **ellipses** (**...**) in the top right corner.

Select **Spotlight**.

In the **Bookmarks** pane, select **Add**. This adds a new bookmark with the current state of the report.

Change the bookmark name to **USA Revenue**.

Select the canvas to ensure that nothing is currently selected.

Select **Australia** within the **Sum of Revenue by Country** visual.

In the **Bookmarks** pane, select **Add**. This adds a new bookmark with the current state of the report.

Change the bookmark name to **Australia Revenue**.

From the **Bookmarks** pane, select **View**. You're now in Bookmarks slide show mode. You're in the first bookmark, which we named **Initial State**. Notice on the bottom of the report pane there's an option to navigate between bookmarks.

You can use the arrows to navigate between bookmarks and tell your story.

From the **Bookmarks** pane, select **Exit** to exit the Bookmarks slide show mode.

If time permits, feel free to explore other options available with Bookmarks, such as **Selected Visuals**, as you continue to build your story.

From the ribbon, select the **View** tab.

*Unselect* the **Bookmarks Pane** button.

Collapse the **Visualizations** and **Filters** panes by selecting the arrows to the top left corner of each pane.

Next we'll add a **Bookmark navigator** to move freely between bookmarks.

## Section 2: Add a bookmark navigator

Let's add bookmark navigator buttons to the canvas.

From the ribbon, select the **Insert** tab.

Select **Buttons** and choose **Navigator** > **Bookmark navigator**.

Arrange the Bookmark navigator to fit on the page as shown in the figure below:

With the buttons visual still selected, navigate to the **Format navigator** pane, expand the **Style** section, then expand the **Fill** section.

Change the **Fill color** to a **light blue** and set the **Transparency** to **40%**.

While still in the **Format navigator** pane, expand the **Shape** section.

From the **Shape** drop-down menu, select **Rounded Rectangle**.

Note

You may need to adjust the size of the buttons within the report after changing the shape.

Feel free to test out the new functionality.

Using the **Ctrl** key on your keyboard, select the **Australia Revenue** bookmark from the visual. Notice how the data changes within the visuals in the report.

Note

To use the new buttons, you must use CTRL + Select while inside the Power BI Desktop. After publishing the report your end users will simply select the buttons without needing to hold CTRL.

Your report should look like the figure shown below. Now let's finish up by saving the file.

Note

Interacting with the report can significantly change the report's appearance. For example, selecting a year from the **Sum of Revenue and % Growth by Year** will activate the conditional formatting in the matrix.

From the ribbon, select the **File** tab.

From the menu to the left, select **Save**.

You successfully created a report you can share with your team. The next Module covers creating a dashboard from this report to share with your team. You saw an overview of the functionality in Power BI Desktop. There are many more features for you to explore with your data in the next Modules.




# Module 7: Publish and Access Reports in Power BI Service

*Source: [https://learn.microsoft.com/en-us/training/modules/publish-access-reports](https://learn.microsoft.com/en-us/training/modules/publish-access-reports)*


---

## Introduction

Through the course of this module, you explore using Power BI Desktop to create a mobile view, publish a report, create a workspace in the Power BI Service, and build a dashboard.

The following concepts are covered:

Creating mobile views

Publishing a report to the Power BI Service

The Navigation pane in Power BI Service

Creating a workspace

Building and organizing a dashboard

Pinning visuals to a dashboard

Adding images from a URL

---

## Exercise - Create a mobile report view

Start this module with the provided **DIAD Final Report.pbix** file located in the **Reports** folder.

The flow of this Module includes screenshots to provide a visual aid for you and text descriptions of the steps you need to follow. In the screenshots, sections are highlighted with red boxes to indicate the action or area on which you need to focus.

## Creating a mobile view

Navigate to the **DIAD** folder and then to the **Reports** folder (DIAD/Reports).

Open the **DIAD Final Report.pbix** file.

This file uses the same model that you used for previous Modules. We have added more visuals and performed other formatting in the report. Feel free to explore the report.

Navigate to the **Market Share** page located in the bottom left corner of the report.

Make sure your report is pulling data from the **Last 15 Years**. You can change this by selecting the number drop-down in the Date slicer visual at the top of the report.

Select the **View** tab from the ribbon and then select **Mobile layout**.

Note

We will create our own, but the **Auto-create mobile layout** button will create a layout for your mobile device using all of the visuals and images available.

From the **Page visuals** pane, drag the **Market Analysis** title to the top of the phone layout.

Notice the text isn't visible on the white background of the mobile view, highlight the **Market Analysis** title and change the text color to **black**.

Resize and move the title to look like the one in the figure below. If there are any other visuals on the mobile layout remove them by hovering over the graphic and selecting the **x** in the upper right corner.

Select the **View** tab, then uncheck the checkboxes next to **Gridlines** and **Snap to grid** (if selected) to turn them off.

Also, make sure that the **Selection** pane is turned off.

Drag the **VanArsdel Market Share** card from the **Page** **visuals** pane to below the **Market Analysis** title on the mobile layout.

Then, resize the **Market Share** card to look like the one shown in the figure below.

Drag the **% Growth by Manufacturer** column chart from the **Page** **visuals** pane to be placed below the **VanArsdel Market Share** card on the mobile layout.

Resize the chart to look like the one shown in the figure below.

Drag the **Revenue** **by** **Year** **and** **Manufacturer** line chart from the **Page visuals** pane to below the **% Growth by Manufacturer** column chart on the mobile layout.

Resize the **Revenue by Year and Manufacturer** line chart to stretch across the phone layout to look like the one shown in the figure below. If you need more space below you can use the scroll bar on the right of the mobile screen.

Drag the **Revenue by Country** map from the **Page visuals** pane to below the **Revenue by Year and Manufacturer** line chart on the mobile layout.

Resize the **Revenue by Country** map to look like the one shown in the figure below.

Select the **File** tab from the ribbon.

From the option menu, select **Save**.

Now that we have a general layout for the Mobile view of our Power BI model, in the next unit we'll explore the Power BI Service and publish our report.

---

## Exercise - Publish a report to the Power BI service

You'll now use a report authored using Power BI Desktop to create a dashboard for the VanArsdel data analysis team and CMO (Chief Marketing Officer). A Power BI Desktop file with more reports and visuals titled **DIAD Final Report.pbix** is provided. Use this file for the next section of the Module.

## Publishing the report

If you haven't signed up for a Power BI account, go to https://aka.ms/pbidiadtraining and sign up for Power BI with a business email address.

If you haven't already opened the **app.powerbi.com** page, open a browser and navigate to https://app.powerbi.com.

Note

US Government customers should check here for the appropriate URL: https://learn.microsoft.com/en-us/power-bi/enterprise/service-govus-overview#sign-in-to-power-bi-for-us-government.

Sign-in to Power BI using your user account. Once logged in, you'll be taken to the **Home** screen.

Note

If you have previously signed into Power BI, then your **Home** screen will list your **Favorites**, as well as recent reports and dashboards.

Notice the navigation pane on the left. Let's review the items here:

The following options are listed in the navigation pane:

- **Copilot**: An AI-powered assistant that helps you create reports, generate visuals, and summarize insights using natural language.

Note

Availability to see this depends on your organization’s tenant settings and licensing.

**Home**: This is a one-stop-shop for all your content. It lists your favorite and recent content such as reports, dashboards, and apps. It also shows the most recent content that was shared with you.

**Create**: Allows you to add data manually or use an already existing semantic model.

**Browse**: Allows you to browse your recently viewed Power BI collateral.

**OneLake Catalog**: Allows you to easily navigate to all datasets that you have either created or that have been shared with you.

**Apps**: Lists all the Power BI apps you have installed.

**Metrics**: Allows you to curate metrics and track them against key business objectives, in a single pane.

**Monitor:** View and track the status of the activities across all the workspaces for which you have permissions with.

**Learn:** Allows the user to have access to started content, samples, and links to videos.

**Real-Time:** Use Real-Time hub to discover, ingest, transform, and manage your real-time data from both within Fabric and externally.

**Workspaces**: Lists all the workspaces you're assigned. By default, you're assigned to *My Workspace.*

**My workspace**: Your personal repository for Power BI collateral that can only be viewed by you.

Select **My Workspace**.

Notice the workspace is waiting for you to add content like Dashboards, Reports, Workbooks, and Semantic Models. Let's import a Power BI Desktop file and create a dashboard.

My Workspace is your personal workspace. We need to create a workspace where we can collaborate with team members and distribute content to end-users. To do this, we'll create a new workspace.

In the pane to the left, select **Workspaces** and then choose **+ New workspace**. The **Create a workspace** dialog box opens.

Note

Creating a workspace is a **Pro feature**. If you do not have a Pro license, please choose the trial option.

In the **Create a workspace** dialog box, select **Upload** to upload a Workspace image.

A file browser dialog box opens. Browse to the **DIAD** folder and then the **Data** folder (**DIAD/Data**).

Select the **VanArsdel_Logo.png** file and then select **Open.**

In the **Name your workspace** text box, type **DIAD_MyFirstPowerBIReport**.

In the **Description** text box, type **This workspace is for the DIAD class**.

Select **Apply** to create the workspace.

Note

Each workspace within a tenat needs a unique name.

Notice you're navigated to the workspace you created.

Let's publish our report to the Power BI Service using the **Publish** feature in Power BI Desktop, then we'll come back to the browser.

Navigate back to the **DIAD Final Report** file in Power BI Desktop that you saved earlier.

Check that the **Mobile View** is **off**.

From the **Home** tab, select **Publish**.

If you haven't already logged into Power BI, a **Sign in** dialog box opens. Please sign in.

Also, if you haven't already saved your changes to the document, a **Save Changes** dialogue box will open. Select **save** to save your changes.

Once you're signed in, the **Publish to Power BI** dialog box opens.

Select **DIAD_MyFirstPowerBIReport** in the dialog box.

Choose the **Select** button in the bottom right corner.

The **Publishing to Power BI** dialog box opens. Once the process is complete, a success message displays.

Select **Got it** to close the dialog box.

Now that we have published the report to the Power BI service, let's **navigate back to the browser** and start exploring.

Once you are in the browser, navigate to the **DIAD_MyFirstPowerBI** workspace, notice that the **DIAD Final Report** semantic model and report appear.

Now that we have our model and report published, we can start creating a dashboard through the Power BI Service.

---

## Exercise - Build a dashboard

In this Unit, we'll create a dashboard that combines data from the **Market Share** report.

By the end of this Unit, we'll have created a dashboard that looks like the figure below.

## Build a dashboard

From your newly created workspace, select the **Report** called **DIAD Final Report**. You'll then be taken to the **Market Share** page of the DIAD Final Report.

In the **map visual**, turn on the drill-down function by **hovering** over the visual and selecting the down-arrow from the visual header.

Once you have selected the arrows, choose **Australia** to drill down to the **State** level.

Now let's pin visuals to the dashboard.

Hover over the **VanArsdel Market Share** card visual.

Select the **pin** icon in the header of the visual. The **Pin to dashboard** dialog box opens.

To create a dashboard, select **New dashboard**.

Then, enter **VanArsdel, Ltd.** in the **Dashboard name** text box.

Now, select **Pin**.

Notice that alert messages are displayed stating the dashboard is ready to view.

Navigate back to your workspace and select the **VanArsdel, Ltd.** Dashboard.

Notice the **VanArsdel Market Share** tile is pinned to the dashboard.

Select the **VanArsdel Market Share** tile. Notice that you're sent to the **DIAD Final Report**.

Note

Dashboard Tiles are not interactive like report visuals we've learned about so far. You also cannot pin things like Slicers to a dashboard since the main purpose of the Slicer is to be interactive.

In the navigation pane to the left of the screen, select the **DIAD Final Report** again to find more items to pin to your dashboard.

Hover over the **% Growth by Manufacturer** column chart visual.

Select the **pin** icon within the header of the visual. The **Pin to dashboard** dialog box opens.

Make sure that **Existing dashboard** and **VanArsdel, Ltd.** are both selected, then select **Pin**.

Close out the alert notification boxes in the top right corner of the screen.

Hover over the **Revenue by Year and Manufacturer** visual.

Select the **pin** icon from the header of the visual.

Repeat the steps to pin it to the existing **VanArsdel, Ltd.** dashboard.

Close out the alert notification boxes in the top right corner of the screen.

Go to the **By Manufacturer** page using the **Pages** menu/pane to the left of the screen.

**Pin** the **Revenue and PY Sales** gauge visual to the existing **VanArsdel, Ltd.** dashboard.

**Pin** the **Revenue by Country** bar chart visual, from the **By Manufacturer** page, to the **VanArsdel, Ltd.** dashboard.

Close out the alert notification boxes in the top right.

Go back to the workspace titled **DIAD_MyFirstPowerBIReport**.

Then, choose the **VanArsdel, Ltd.** dashboard again. Notice that all the visuals are pinned as tiles to the dashboard.

You'll see the visuals on the dashboard like in the figure above. Each visual on the dashboard is called a **Tile**. The tiles represent selected data and update as the data model updates. Tiles aren't interactive.

Let's organize the dashboard.

Resize and move the **gauge** tile as shown in the figure below. To resize the visual, select the bottom right-hand corner and drag to the desired size. Tiles can be of various sizes (1x1 to 5x5).

As you're dragging, note the gray shadow, which indicates the size of the tile when you stop dragging.

Select the **Edit** dropdown from the ribbon at the top of the screen and choose **Add a tile**. The **Add tile** dialog box opens.

Select **Image** as the source.

Choose **Next**.

In the **URL** text box of the **Add image tile** dialog, type the following URL: `https://raw.githubusercontent.com/PragmaticWorksTraining/DIAD/main/Logos/VanArsdel.png`

Note

The URL is case-sensitive.

Then, select **Apply** at the bottom of the dialog.

Notice that a new tile with the **VanArsdel, Ltd.** logo is added to the dashboard.

Resize and rearrange the tiles as shown in the figure below.

The **Revenue by Country** tile shows data for Revenue by Country for VanArsdel, Ltd. Let's **rename** it.

Hover over the **Revenue by Country** tile.

Select the **ellipsis** in the top right corner of the tile.

Select **Edit Details**. The **Tile Details** dialog box opens.

Change the **Title** to **VanArsdel, Ltd. Revenue in Australia**.

Select **Apply**.

Now that we have a dashboard in Power BI Service, in the next unit we'll show you different interactions and personalization options you can use for your report.




# Module 8: Interact, Share, and Collaborate Power BI Dashboards

*Source: [https://learn.microsoft.com/en-us/training/modules/interact-share-power-bi](https://learn.microsoft.com/en-us/training/modules/interact-share-power-bi)*


---

## Introduction

In this module, you learn how to interact with your Power BI Dashboard. You also learn how to share and to collaborate with other team members, publish your first Power BI App through the Power BI Service, and view dashboards on the Power BI Mobile App.

Concepts covered:

Using Q&A

Generating insights and using Quick Insights

Setting alerts

Managing user access, and the four levels of permission:

Contributor

Member

Admin

Viewer

Building and Publishing a Power BI App

Editing the Audience of a Power BI App

Finding Apps in the Power BI Service

Viewing a report on the Power BI Mobile App

---

## Exercise - Power BI service interaction and personalization

Make sure you're in the VanArsdel, Ltd. dashboard for the Final Report in your DIAD workspace on Power BI Service.

Let's create a visual that represents **Market Share by country**.

## Section 1: Using Q&A

Notice on the top of the dashboard, there's an option to **Ask a question about your data**. This is like **Ask a question** in the desktop.

Select the **Ask a question about your data** text box at the top of the page. You'll then be taken to a **Q&A** page.

Type **VanArsdel market share** in the text box at the top of the page. Notice that a card visual is created.

Type **VanArsdel market share by country**. Notice that a bar chart is created.

Type **VanArsdel market share by country as treemap**. Notice that a treemap visual is created.

In the top right corner of the screen, select **Pin Visual**.

The **Pin to dashboard** dialog box opens. Make sure that **Existing dashboard** is selected, then select **Pin** to pin the visual to the **VanArsdel, Ltd.** dashboard.

Close the alert dialog boxes.

Select **Exit Q&A** in the top left corner of the page to go back to the dashboard.

Notice that the treemap visual is added as a tile to the dashboard. Selecting the treemap visual will take you back to the Q&A section.

Power BI quickly searches different subsets of your model while applying a set of sophisticated algorithms to discover potentially interesting insights. You can run insights against a model or a dashboard tile.

## Section 2: Generate insights

Let's generate **insights** on a dashboard tile. When we run insights on a dashboard tile, instead of searching for insights against an entire model, the search is narrowed to the data used to create a single dashboard tile. This is called scoped insights.

Hover over the **Revenue by Manufacturer** line chart on the dashboard.

Select the **ellipsis** on the top right corner of the line chart.

Choose **View Insights**.

You'll be taken to **Focus mode** for the line chart.

Scroll on the Insights pane to the right of the screen to review the various insights Power BI can generate. Notice that there's an option to pin insight visuals to the dashboard.

Select **Exit Focus mode** in the top left corner of the page to go back to the dashboard.

## Section 3: Setting alerts

We want to be notified when **VanArsdel's Market Share** goes above or below a threshold. We can set up **alerts** to do this.

Hover over the **VanArsdel Market Share** card tile.

Select the **ellipsis** in the top right corner of the tile.

Choose **Manage alerts**. The **Manage alerts** dialog box opens.

Select **Add alert rule.**

Notice that you can add **Above** or **Below** **threshold**. You can also set the notification frequency.

Select **Cancel** to close the dialog box.

From the **Unsaved changes** alert dialog box, select **Don't Save**.

Select the **VanArsdel Market Share** card visual tile to navigate to the report.

In the **Revenue by Country and State** map visual, drill up from the State level to the Country level.

Hover your mouse over the **Australia** bubble in the map and choose **Drill through**.

Then, select **By Manufacturer**.

You'll then go to the **By Manufacturer** page of the report with the **Australia** filter applied to the report page.

Hover over the **Matrix** visual and drill up to the highest level if it's not already there.

Select the **Focus mode** icon in the top right corner of the visual.

Select the **double-down arrow** to drill down.

Then, select the **Back to report** button in the top left-hand corner of the page.

Open the **Bookmark** panel on the right-side of the report by selecting the bookmark icon in the top-right corner and choosing **Show more bookmarks**, then select **View** to open the bookmark viewing interface.

Notice that you can view and move through the bookmarks using the **arrow** at the bottom of the screen. This behavior is like in Power BI Desktop. You can test this out on your own.

Select **Exit** under the **Report bookmarks** section of the pane to close it.

## Section 4: Quick insights

Power BI provides an option to get quick insights into the complete dataset or Semantic model.

Go back to the workspace you created earlier in the lab using the navigation pane to the left of the screen.

Once in the workspace, find the semantic model called **DIAD Final Report** and select the **ellipsis** (...).

From the menu, select **Get quick insights**.

It might take a few minutes for the insights to be created. Once the insights are ready, a message appears in the top right corner.

From the **Insights are ready** alert dialog box, select **View insights.**

A quick insights report is displayed based on the model. This provides insights into data you might have missed and helps to get a quick start on creating dashboards. Hovering over each report provides an option to **Pin it** to a dashboard.

Now that you've published your report and built your dashboard, the required portion of this Module is complete.

In the next optional unit, we'll show you the process of sharing your dashboard and collaborating with other team members and see how you can create storytelling presentations within PowerPoint using data from Power BI.

---

## Exercise - Share your work with Power BI apps

This is the final module of 8 total modules.

Continue to use your file after completing Module 7. If you're joining the DIAD at this point or were unable to complete previous modules, start this module with the provided **DIAD Final Report.pbix** file located in the Reports folder.

At the end of this Module, you'll have learned how to share your dashboard and collaborate with other users. You'll also have learned how to access your dashboard on your mobile device.

This module includes steps for the user to follow-along together with matching screenshots that provide a visual aid. In the screenshots, sections are highlighted with red boxes to indicate the area the user needs to focus on.

## Collaboration and distribution

You have built the dashboard and are now ready to get feedback and collaborate with your team members.

**Sign in** to https://app.powerbi.com to access your workspace.

From the navigation pane to the left of the screen, select **Workspaces**.

Select the workspace **DIAD_MyFirstPowerBI** that you created previously.

Select **Manage Access** at the top of the page.

After the **Manage Access** dialog opens, select the **+ Add people or groups** button. Enter the email addresses of colleagues you want to collaborate with. Each user can belong to one of four roles:

Contributor:

- Add/edit/delete content within a workspace.

Member:

Add/edit/delete content within a workspace.

Reshare, Publish, and update Apps.

Admin:

Everything a member can do.

Change/delete a workspace.

Add Admins.

Viewer:

View/interact

Read data stored in workplace Data Flows

Select the appropriate role and then select **Add**.

Once you have finished adding your colleagues, select **Close** at the top right.

Note

If you don't have a colleague's email, please close without submission. If you do have a colleague's email, enter it in the box, and after you have selected the **Add** button, you can ask your colleague to login and access the workspace.

Now let's **share** the content we have created with report viewers and consumers. To start, we need to **publish** an App. An App can include multiple dashboards and reports.

Navigate back to your workspace called **DIAD_`youremailaddress`**.

On the **Workspace** page, notice there's an option named **Included in app**, which can be selected to include the Dashboard in the App. Once the App is created, the **Included in app** toggle will turn on.

If you have reports and dashboards included in your workspace that you don't want to share with report viewers, an option will appear later to exclude these items.

In the top part of your screen, select the **Create app** button.

On the **Build your app** page, under the **Setup** tab, rename the App to `DIAD`.

Then, type **This is a DIAD app** in the **description** field.

Select the **Next: Add content** button located in the bottom right corner of the **Setup** page.

Select the green colored **Add content** button located in the middle of the screen.

In the **Add content** dialog box that appears, select **DIAD Final Report (report)** and **VanArsdel, Ltd. (dashboard)**.

Then, select the **Add** button located in the bottom right corner of the dialog box.

Notice that the newly added dashboard and report are added to the list in the **Content** pane to the left.

Next, select the **Next: Add audience** button located in the bottom right corner of the Content page.

Note

When continuing to the **Audience** tab by completing step 17, a dialog box may pop up giving information about what audiences are and how to utilize them within Power BI. Select **Next** and then **Got it** to close this pop up.

In the **Edit Audience** pane, enter the emails to whom you want to give access in **Specific users or groups** text box.

Then, select the **Publish app** button located in the bottom right corner of the pane.

Note

If you do not have an email to share the App with, continue by selecting the Publish app button.

With Audiences, the authors can decide which content can be shared with specific audience groups using a single workspace. This allows access control for the App users based on their group permissions and minimizes overhead for the App authors.

The **Ready to publish** dialog will appear, select **Publish**.

Once the App is published, a success dialog will appear.

In the **Successfully published** dialog box, you can copy the link to the App and share it with individuals.

Select the **Close** button.

A better way for report viewers to see the App is by logging on to Power BI Service and registering the App. Let's impersonate a report viewer.

From the navigation pane to the left, select **Apps**.

Then, select **Get apps**.

The **Power BI apps** dialog box opens. You'll notice the **DIAD** App is listed under the **All apps** tab.

Select the newly added **DIAD** App.

This is a one-time registration. Going forward, when you select **Apps** in the left pane, you'll see the **DIAD** App in the list of Apps you have registered.

Your newly created DIAD App should look similar to the figure below:

Now that we've published our App and sent it to our teammates, in the next unit, we'll cover the process of accessing the report from a mobile device.

---

## Exercise - Access the report from your mobile device

In this unit, we'll go through the Power BI Mobile App and cover the steps needed to access the DIAD Final Report we have been working on.

## Mobile app

Open the **Power BI Mobile App** on your mobile device.

Select **Sign in** and follow the steps for entering your credentials.

Once you have signed in, you'll be prompted through a **walk-through of the App**. Select **Next** to continue through the App walk-though.

On the last page of the walk-through, select **Let's go!** to navigate to the **Home** screen of the Mobile App.

A dialog box will appear asking if you want to allow notifications from Power BI on your mobile app. Select **Allow** or **No, thanks**.

Once you've made the choice to allow notifications or not, you'll see the main home screen of the Power BI Mobile App. Under the **Frequents** section, select the **DIAD Final Report** (report).

Once you have selected the DIAD Final Report, a **You are in control** dialog box will appear. Select **Got it**.

Lastly, you should see the Mobile view you published from Power BI Desktop



