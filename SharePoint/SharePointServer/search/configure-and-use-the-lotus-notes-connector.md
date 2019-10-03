---
title: "Configure and use the Lotus Notes connector for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: a7960bf4-d5be-4ad7-a430-724ef194ad39
description: "Learn about the administrative roles, required software, user accounts, and processes that are required to install and operate the Lotus Notes Client and the Lotus Notes Connector to work with SharePoint Server search."
---

# Configure and use the Lotus Notes connector for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information about prerequisites:
  
- [Required administrative roles](configure-and-use-the-lotus-notes-connector.md#LN_AdminRoles)
    
- [Required software](configure-and-use-the-lotus-notes-connector.md#LN_SWReq)
    
- [User accounts required to crawl Lotus Domino databases](configure-and-use-the-lotus-notes-connector.md#LN_UserAcc)
    
The procedures in this article must be repeated on all the servers in the SharePoint Server farm that host a crawl component. 
  
## Prerequisites
<a name="LN_Prereqs"> </a>

The following sections list the required administrative roles, software and user accounts. 
  
### Required administrative roles
<a name="LN_AdminRoles"> </a>

The following administrative roles are required to prepare any server that hosts a crawl component to crawl Lotus Notes content that is hosted by one or more Lotus Domino databases: 
  
- Administrator of the Lotus Domino server that you want to crawl.
    
- Server administrator of the server that hosts a crawl component that you want to use to crawl Lotus Notes content.
    
- Service application administrator for the Search service application.
    
### Required software
<a name="LN_SWReq"> </a>

The following software is required:
  
- Lotus C++ API Toolkit for Notes.
    
- Lotus Notes client application, available for purchase from IBM.
    
- Lotus Notes Domino Server, available for purchase from IBM.
    
The following table shows combinations of versions of the Lotus Notes Domino server and Lotus Notes client that the Lotus Notes Connector works with.
  
|                     |                 |                 |                 |
| :------------------ | :-------------- | :-------------- | :-------------- |
| This server version | With client 6.x | With client 7.x | With client 8.x |
| Server 6.x          | YES             | NO              | NO              |
| Server 7.x          | NO              | YES             | YES             |
| Server 8.x          | NO              | NO              | YES             |
   
### User accounts required to crawl Lotus Domino databases
<a name="LN_UserAcc"> </a>

A Domino administrator must grant a Lotus Notes user ID (which represents a Domino user) at least the Reader permission to the Lotus Domino databases and individual documents that you want to crawl. The Domino administrator must also add this Lotus Notes user ID and the Windows domain user account that is assigned to the SharePoint Server Search 15 service (OSearch15) to a mappings database on the Lotus Domino server that you want to crawl.
  
> [!NOTE]
> Only the user account that is assigned to the OSearch15 service can be used to crawl Lotus Domino databases. You cannot use the default content access account or a crawl rule to specify a different user account to crawl Lotus Domino databases. 
  
The following table summarizes the user accounts that are required to crawl Lotus Domino databases. 
  
|    **Required account**     |                                                                                                     **Comment**                                                                                                     |                                                         **Example**                                                         |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------- |
| Windows domain user account | The user account that is assigned to the OSearch15 service must also be a member of the Administrators group on the server that hosts the crawl component.                                                          | Contoso\User1, where Contoso is the domain name and User1 is the name of the Windows domain user account.                   |
| Lotus Notes user ID         | The Lotus Notes user ID must be granted at least Reader access on the Lotus Domino databases and on the individual documents that you want to crawl. The Domino certificate also contains this Lotus Notes user ID. | User2  <br/><br/> **NOTE:** The name of this account and its password do not have to match the Windows domain user account. |
   
More information about this mappings table is provided later in this article, see [Configure security mappings](configure-and-use-the-lotus-notes-connector.md#LN_ConfigSecMap).
  
## Install the Lotus Notes client application
<a name="LN_Install_LN_Client"> </a>

Follow this procedure to install the Lotus Notes client application on the server that hosts the crawl component in the server farm that you want to use to crawl a Lotus Domino database. This client application serves as a protocol handler and is used to configure the Notes.ini file. Both are used by the crawler when crawling Lotus Domino databases.
  
 **To install Lotus Notes**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that hosts the crawl component and has at least Manager permissions on the Domino server. 
    
2. Copy the Lotus Notes client application to the server that hosts the crawl component that you want to use to crawl Lotus Notes documents.
    
3. Start the Lotus Notes Installation Wizard.
    
4. In the **Welcome to the Installation Wizard for Lotus Notes** dialog box, click **Next**.
    
5. On the License Agreement page, click **I accept the terms in the license agreement**, and then click **Next** to continue. 
    
6. On the Customer Information page, type a user name in the **User Name** box and the name of the organization in the **Organization** box, or accept the default settings, and then click **Next**.
    
7. On the Installation Path Selection page, specify the path for the program and data files, or accept the default installation paths, and then click **Next**.
    
    > [!NOTE]
    > By default, program files are stored in the  _\<SystemDrive\>_:\Program Files (x86)\lotus\notes\ folder and data files are stored in the  _\<SystemDrive\>_:\Program Files (x86)\lotus\notes\data\ folder, where  _\<SystemDrive\>_ is the drive on which Lotus Notes is installed. 
  
8. On the Custom Setup page, select the program features that you want to install on the local hard disk drive, and then click **Next**.
    
    The table below shows the features and sub-features that are required by the Lotus Notes connector.
    
9. On the Ready to Install the Program page, if you do not want Lotus Notes to be the default email program, clear the selection **Make Notes my default email program**.
    
10. Click **Install**.
    
    The Installing Lotus Notes page shows the status of the installation.
    
11. On the Install Wizard Completed page, click **Finish**.
    
### Features and sub-features required by the Lotus Notes connector

|   **Feature**   |                **Subfeature**                |
| :-------------- | :------------------------------------------- |
| Notes Client    | Client Help Files                            |
|                 | Domino Enterprise Connection Services (DECS) |
| Domino Designer | Designer Help                                |
   
## Grant permissions on the data folder
<a name="LN_GrantPerm"> </a>

Follow this procedure to grant Full Control permissions for the WSS_WPG group on the  _\<SystemDrive\>_:\Program Files (x86)\Lotus\Notes\Data folder on the server that hosts the crawl component.
  
 **To grant permissions on the data folder**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that hosts the crawl component and has at least Manager permissions on the Domino server. 
    
2. On the server that hosts the crawl component, click **Start**, point to **All Programs**, click **Accessories**, and then click **Windows Explorer**.
    
3. In Windows Explorer, go to the  _\<SystemDrive\>_:\Program Files (x86)\Lotus\Notes\Data folder, where  _\<SystemDrive\>_ is the drive on which Lotus Notes is installed. 
    
4. Right-click the **Data** folder, and then click **Sharing and Security**.
    
5. In the **Properties** dialog box, on the **Security** tab, click **Add**.
    
6. In the **Select the object names to select** box, do one of the following, and then click **OK**:
    
  - If search is installed on an Active Directory domain controller, type  _domain_\WSS_WPG, where  _domain_ is the name of the domain that is associated with the domain controller. 
    
  - If search is installed on a server that is not an Active Directory domain controller, type  _server_\WSS_WPG, where  _server_ is the NetBIOS name of the server that hosts the crawl component. 
    
7. In the **Properties** dialog box, in the **Permissions for WSS_WPG** section, select the **Allow** box in the **Full control** row, and then click **OK**.
    
## Configure the Lotus Notes client application
<a name="LN_ConfigClient"> </a>

Follow this procedure to configure the Lotus Notes client application. The configuration settings selected in this procedure are written to the Notes.ini file, which the crawler uses to discover how to connect to the Lotus Domino server.
  
 **To configure Lotus Notes**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that hosts the crawl component and has at least Manager permissions on the Domino server. 
    
2. On the server that hosts the crawl component, click **Start**, point to **All Programs**, point to **Lotus Applications**, and then click **Lotus Notes**.
    
3. On the Welcome page, click **Next**.
    
4. On the User Information page, in the **Your name** box, type the user name associated with the Domino certificate. 
    
5. Type the hierarchical name of the Domino server that you want to crawl in the **Domino server** box. For example, Contoso/marketing/west. 
    
6. Ensure that **I want to connect to a Domino server** is selected, and then click **Next**.
    
7. On the Notes ID File page, click **Browse**, and then locate where the certificate is stored. Select the certificate, click **Open**, and then click **Next**. 
    
8. Click **Yes** to copy the certificate to the specified location. 
    
    > [!NOTE]
    > If you are not prompted for a Domino certificate, click **Previous**, and ensure that you have entered the correct information. 
  
9. If a dialog box appears that informs you that you are not authorized to access the specified directory, click **OK** to close the dialog box. This error is expected if the account that you are logged on with does not have access to the email folder on the Domino server. 
    
10. On the Instant Messaging Setup page, cancel the selection **Setup instant messaging**.
    
11. Click **Next**.
    
12. On the Additional Services page, click **Next**.
    
13. In the **Lotus Notes message** box, click **OK**.
    
    The Lotus Notes Welcome screen appears.
    
    Leave the Lotus Notes client application open. You will need it for the next procedure.
    
## Verify access to the Lotus Domino database that you want to crawl
<a name="LN_VerifyAccess"> </a>

Follow this procedure to verify that the certificate that you installed has access to the database that you want to crawl.
  
 **To verify access**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that hosts the crawl component and has at least Manager permissions on the Domino server. 
    
2. In Lotus Notes, click **File**, point to **Database**, and then click **Open**.
    
3. In the **Open Database** dialog box, select the Lotus Domino server that you want to connect to from the **Server** list. 
    
4. In the **Database** list, select the database that you want to connect to, and then click **Open**. 
    
    The documents that are contained by the database that you selected are displayed in the **Document Name** section. This means that the server that hosts the crawl component as the necessary permissions to crawl these documents. 
    
5. Repeat steps 1 to 3 for each additional database that you want to verify access to.
    
6. On the **File** menu, click **Exit Notes**.
    
## Configure security mappings
<a name="LN_ConfigSecMap"> </a>

Use the information in the following table to help you create the mappings database. 
  
|        **Item**         |                                                                   **Description**                                                                    |
| :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mappings database name  | Name of the Lotus Domino database that maps Lotus Notes user IDs to Windows domain user accounts.                                                    |
| Lotus Notes field name  | Name of the field in the Lotus Domino database file that stores Lotus Notes user IDs.                                                                |
| Windows user field name | Name of the field in the Lotus Domino database file that stores Windows user names.                                                                  |
| Form name               | Name of the form that stores the **Lotus Notes field name** and **Windows user field name** fields.                                                  |
| View name               | Name of the view for the form that stores the Lotus Notes user IDs to Windows user name mappings.  <br/><br/> **NOTE:** This name is case-sensitive. |
   
### Create the mappings database

Follow this procedure to create a mappings database by using Domino Designer. You only require one mappings database for each forest of Domino servers that contain databases that you want to crawl. 
  
 **To create a mappings database**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that hosts the crawl component and has at least Manager permissions on the Domino server that you want to crawl. 
    
2. On the server that hosts the crawl component, open Domino Designer.
    
3. Click **File**, point to **Database**, and then click **New**.
    
4. In the **New Database** dialog box, do the following: 
    
  - Select the Domino server from the **Server name** list. 
    
  - In the **Title** box, type a title for the new database. 
    
    This content automatically populates the **File Name** box, and it is appended with the .nsf file name extension. 
    
    If the title that you chose is more than eight characters long, the file name will be truncated.
    
  - Click **OK** to close the **New Database** dialog box. 
    
5. Click **Create**, point to **Design**, and then click **Form**.
    
6. Click **Create**, and then click **Field**. 
    
7. In the **Field** dialog box, in the **Name** box, type the name that you want to use for this field. This field will be used to store the Lotus Notes user IDs. 
    
8. Close the dialog box to save the field.
    
9. Click **Create**, and then click **Field**. 
    
10. In the **Field** dialog box, in the **Name** box, type the name that you want to use for this field. This field will be used to store the Windows domain user accounts. 
    
11. Close the dialog box to save the field.
    
12. Click **File**, click **Save**, and then do the following:
    
  - Type a name in the **Save Form as** box. 
    
  - Click **OK** to close the dialog box. 
    
13. On the **Create** menu, point to **Design**, and then click **View**.
    
14. In the **Create View** dialog box, do the following: 
    
  - In the **View name** box, type a name for this view. 
    
  - Select **Shared** from the **View type** list. 
    
  - Click **OK** to save the view. 
    
15. Open the view that you created in step 14.
    
16. On the **Objects** tab, select the column that you created in step 7. In the lower right pane, select **Field** and then select the field that has the same name. 
    
17. On the **Objects** tab, select the column that you created in step 10. In the lower right pane, select **Field** and then select the field of the same name. 
    
18. Click **File** and then click **Save** to save the view, and then close Domino Designer. 
    
### Add user accounts to the mappings database

Follow this procedure to add user accounts to the mappings database using the Lotus Notes client. You should add all accounts which require access to the mappings database and the Domino server. 
  
 **To add user accounts to the mappings database**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that hosts the crawl component and has at least Manager permissions on the Domino server. 
    
2. On the server that hosts the crawl component, open the Lotus Notes client application.
    
3. Click **File**, point to **Database**, and then click **Open**.
    
4. In the **Open Database** dialog box, do the following: 
    
  - Select the Domino server from the **Server name** list. 
    
  - Select the mappings database that you created earlier. 
    
  - Click **Open**. 
    
5. In the left pane, select the view that you created for this database. 
    
6. Click **Create**, and then click the name of the form that you created earlier. 
    
7. In the form, in the field that you created to store the Lotus Notes user IDs, type a Lotus Notes user ID that you want to map to a Windows domain user account. For example, ContosoUser. This field is case-sensitive.
    
8. In the field that you created to map to the Lotus Notes user IDs, type the Windows domain user account that you want to map to the Lotus Notes user ID that you entered in step 7. This must be in the form of domain\user, for example, Contoso\user1.
    
9. Click **File**, and then click **Save** to save the document. 
    
10. Repeat steps 6to 8 if you want to add more mappings. Otherwise, go to step 11.
    
11. When finished, save the form and then close the Lotus Notes client application.
    
## Restart the server that hosts the crawl component
<a name="LN_RestartCrawl"> </a>

You must restart the server that hosts the crawl component before continuing to the next procedure.
  
> [!IMPORTANT]
> After the server that hosts the crawl component restarts, do not open the Lotus Notes client application again. This is because the Lotus Notes client application might lock files that could cause the following procedures and crawling Lotus Domino databases to fail. 
  
## Register Lotus Notes with the server that hosts the crawl component
<a name="LN_RegisterLN"> </a>

Following this procedure to register Lotus Notes with the operating system of the server that hosts the crawl component.
  
 **To register Lotus Notes**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that hosts the crawl component. 
    
2. Run Notessetup.exe on the server that hosts the crawl component by using the same credentials that are used to provision the Lotus Notes Connector.
    
3. On the server that hosts the crawl component, in Windows Explorer, go to the  _\<SystemDrive\>_:\Program Files\Microsoft Office Servers\15\Bin\1033 folder, where  _\<SystemDrive\>_ is the drive on which Microsoft SharePoint Server is installed. 
    
4. Double-click **NotesSetup.exe**.
    
5. On the Welcome to the Lotus Notes Index Setup Wizard page, click **Next**.
    
6. In the **Register Lotus Notes for use with SharePoint Server** dialog box, do the following: 
    
  - In the **Location of the notes.ini file** box, ensure that the correct path of the Notes.ini file is specified. The default path of this file is  _\<SystemDrive\>_:\Program Files (x86)\lotus\notes\notes.ini, where  _\<SystemDrive\>_ is the drive on which Lotus Notes is installed. 
    
  - In the **Location of the Lotus Notes install directory** box, ensure that the correct path of the Lotus Notes installation directory is specified. By default, the path of this directory is  _\<SystemDrive\>_:\Program Files (x86)\lotus\notes.
    
  - In the **Password** box, type the password for the user name that is associated with the Domino certificate. 
    
  - In the **Confirm Password** box, retype the password for the user name that is associated with the Domino certificate. 
    
7. We recommend that you leave the **Ignore Lotus Notes security while building the index** box cleared. This allows the crawl to include all Lotus Notes documents in the search index without restriction. Security for these documents and objects is determined by the mappings table and provides security data without excluding documents from the index. 
    
8. Click **Next**.
    
9. On the Specify Lotus Notes Owner Field to Windows User Name Mapping page, do the following:
    
  - In the **Lotus Notes server name** box, type the NetBIOS name or IP address of the Domino server. 
    
  - In the **Lotus Notes database file name** box, type the file name of the Lotus Domino database that maps the Lotus Notes user IDs to Windows domain user accounts. Ensure that you include the .nsf file name extension with this name, for example, Mappings.nsf. 
    
  - In the **View name** box, type the view name of the Lotus Domino database that stores the Lotus Notes user IDs to Windows user name mappings. 
    
  - In the **Lotus Notes field name column title** box, type the name of the column in the Lotus Notes database file that is used to store Lotus Notes user IDs. 
    
  - In the **Windows user name column title** box, type the name of the column in the Lotus Notes database file that is used to store the Windows user accounts. 
    
10. Click **Next**.
    
11. On the Completing the Lotus Notes Index Setup Wizard page, click **Finish**.
    
## Provision the Lotus Notes Connector
<a name="LN_ProvisionLN"> </a>

Follow this procedure to provision the Lotus Notes Connector with the operating system of the server that hosts the crawl component.
  
 **To provision Lotus Notes**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that hosts the crawl component. 
    
2. Open SharePoint Central Administration. In the System Settings section, click **Manage services on Server**.
    
3. On the Services on Server page, in the Service column, find the Lotus Notes Connector service.
    
4. In the Action column, click **Start**.
    
5. On the Lotus Notes connector settings page, in the application pool section, select **Create new application pool**, and then enter a name for the new application pool.
    
6. In the Configurable drop-down, select or register the same security account used for installation of the NotesSetup.exe. 
    
7. Click **Provision**.
    
The Lotus Notes connector is now provisioned and started.
  
## Restart the OSearch15 service
<a name="LN_RestartSearch"> </a>

The server administrator of the server that hosts the crawl component must restart the OSearch15 service before a content source can be created for Lotus Domino databases.
  
> [!IMPORTANT]
> Do not use the Services on Server page on the SharePoint Central Administration website to restart this service. Doing so resets the search index, which requires you to do a full crawl of all content to rebuild the index. 
  
 **To restart the OSearch15 service**
  
1. Verify that the user account that is performing this procedure is an administrator for the server that hosts the crawl component. 
    
2. Open a command prompt window.
    
3. To stop the OSearch15 service, type this command: net stop osearch15
    
4. To start the OSearch15 service, type this command: net start osearch15
    

