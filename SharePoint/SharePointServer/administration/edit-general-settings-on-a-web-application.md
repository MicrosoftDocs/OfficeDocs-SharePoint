---
title: "Edit general settings on a web application in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/28/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 8b96e40d-8a2f-486e-aaea-a3567cca77ad
description: "Illustrates how to make changes to general settings for a SharePoint Server web application in Central Administration."
---

# Edit general settings on a web application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
## Edit a web application by using Central Administration
<a name="section1"> </a>

Use the procedure described in this section to edit a SharePoint Server web application using the Central Administration.
  
 **To edit a web application by using Central Administration**
  
1. Verify that you have the following administrative credentials:
    
  - To edit a web application, you must be a member of the Farm Administrators SharePoint group.
    
2. Start SharePoint 2016 Central Administration.
    
  - For Windows Server 2008 R2:
    
  - Click **Start**, click **SharePoint 2016**, and then click **SharePoint 2016 Central Administration**.
    
  - For Windows Server 2012:
    
  - On the **Start** screen, click **SharePoint 2016 Central Administration**.
    
    If **SharePoint 2016 Central Administration** is not on the **Start** screen: 
    
  - Right-click **Computer**, click **All apps**, and then click **SharePoint 2016 Central Administration**.
    
    For more information about how to interact with Windows Server 2012, see [Common Management Tasks and Navigation in Windows Server 2012](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831491(v=ws.11)).
    
3. On the Central Administration home page, click **Application Management**.
    
4. On the **Application Management** page, in the **Web Applications** section, click **Manage web applications**.
    
5. Click on the web application that you want to edit.
    
6. In the ribbon, from the **WEB APPLICATIONS** tab, click **General Settings**, and do the following:
    
  - To change the default time zone for sites that are created on the web application, in the **Default Time Zone** section, from the **Select time zone** drop-down list, select a time zone. 
    
  - To change the user settings provider for sites that are created on the web application, in the **User Settings Provider** section, from the **Select User Settings Provider** drop-down list, select a user settings provider. 
    
  - To change the default quota template for site collections created on the web application, in the **Default Quota Template** section, from the **Select quota template** drop-down list, select a quota template. 
    
  - To disable person name actions and online presence information from being shown on sites on the web application, in the **Person Name Actions and Presence Settings** section, from **Enable additional actions and Online Status for members**, select **No**. 
    
  - To disable alerts for sites in on the web application, in the **Alerts** section, from **Alerts on this server are**, select **No**. If you don't want to disable alerts completely, but want to limit the number of alerts a user can create, change the settings for **Maximum number of alerts that a user can create** accordingly. 
    
  - To disable RSS feeds for sites on the web application, in the **RSS Settings** section, from **Enable RSS feeds**, select **No**. 
    
  - To disable the MetaWeblog API for the web application, in the **Blog API Settings** section, from **Enable Blog API**, select **No**.
    
    The Metablog API allows SharePoint blog entries to be written, modified, or removed through web services. If **Accept user name and password from the API** is **Yes**, then the credentials to manage the blog post are sent in clear text, unless SSL to the web app is configured. If **Accept user name and password from the API** is set to **No**, SharePoint authorization for the web app is used.
    
  - To change the browser file handling so that the browser automatically executes web content, in the **Browser File Handling** section, select **Permissive**.
    
  - To disable security validation for sites on the web application, in the **Web Page Security Validation** section, from **Security validation is**, select **Off**. To change the expiration time for a security validation, change the settings for **Security validation expires** accordingly. 
    
  - To disable the ability to send users their user name and password by e-mail, in the **Send User Name and Password in E-Mail** section, from **Send user name and password**, select **No**.
    
  - To deny pages in the _Layouts folder to reference site master pages for sites on the web application, in the **Master Page Settings for Application _Layouts Page**, from **Application _Layout pages reference site master pages**, select **No**.
    
  - To turn off recycle bins on sites in the web application, in the **Recycle Bin** section, from **Recycle Bin Status**, select **Off**. Alternatively, you can change when items in recycle bins should be deleted by changing the settings for **Delete items in the Recycle Bin** and **Second stage Recycle Bin**. 
    
  - To change the maximum allowed size of content uploads to a site in the web application, in the **Maximum Upload Size** section, change the number in **Maximum upload size** accordingly. 
    
  - To disable the collection of web site analytics for sites in the web application, in the **Customer Experience Improvement Program** section, from **Enable Customer Experience Improvement Program**, select **No**.
    
  - To enable usage cookies to be used for anonymous users on sites in the web application, in the **Usage Cookie** section, from **Usage Cookie Status**, select **On**.
    
    > [!IMPORTANT]
    > Local legal restrictions might apply when you enable usage cookies on sites that have anonymous users. 
  
7. To save your changes to this web application, click **OK**.
    
## See also
<a name="section1"> </a>


[Extend claims-based web applications in SharePoint](/SharePoint/administration/extend-a-claims-based-web-application)

