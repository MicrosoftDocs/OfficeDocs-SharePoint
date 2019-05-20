---
title: "Manage the App Catalog in SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/27/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: a19bb905-2984-4512-8e8a-3c17ec3680c0
description: "Learn how to configure and manage an App Catalog for SharePoint Server environments to control access to available apps."
---

# Manage the App Catalog in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can store apps for SharePoint and Office apps for your organization's internal use in an App Catalog site. This article contains an overview of the App Catalog site and shows how to configure the App Catalog for a web application.
  
Be sure you've [configured your SharePoint environment to support apps](configure-an-environment-for-apps-for-sharepoint.md) before getting started. 
  
## Configure the App Catalog site for a web application
<a name="ConfigureAppGallery"> </a>

The App Catalog site is a special site collection. Because an App Catalog is scoped to a web application, all apps that you want to make available for a web application have to be in the App Catalog site collection for that web application.
  
When you create an App Catalog site, you get two libraries for apps:
  
- Apps for SharePoint
    
- Apps for Office
    
You create the App Catalog site collection from SharePoint Central Administration.
  
 **To create an App Catalog site collection for a web application**
  
1. Verify that the user account that is performing this procedure is a member of the Farm administrators group.
    
2. In Central Administration, on the Apps page, in the **App Management** section, click **Manage App Catalog**.
    
    If no App Catalog exists for the farm, the **Web Application** page opens, so you can select a web application. 
    
3. On the **Web Application** page, select the web application for which you want to create a catalog. 
    
4. In the App Catalog Site section, select **Create a new app catalog site**, and then click **OK**. 
    
5. On the Create App Catalog page, in the **Title** box, type a title for the App Catalog site. 
    
6. In the **Description** box, type the description for the site. 
    
7. In the **URL** box, fill in the URL to use for the site. 
    
8. In the Primary Site Collection Administrator section, in the **User Name** box, type the user who will manage the catalog. 
    
    Only one user name can be entered. Security groups are not allowed.
    
9. In the End Users section, in the **Users/Groups**box, type the names of the users or groups that you want to be able to browse the catalog. 
    
    Added users or groups have read access to the App Catalog site. You can add multiple user names and security groups. Users must be added as End Users to be able to browse the App Catalog from their site collections.
    
10. In the **Select a quota template** list box, select the quota template to use for the site. 
    
11. Click **OK**.
    
Once the site has been created, a link to it is available on the Manage App Catalog page in Central Administration.
  
## Configure app requests
<a name="AppRequests"> </a>

By default, site owners can purchace and download apps from the SharePoint Store. If you don't want site owners to be able to purchase apps directly, you can configure the SharePoint Store settings in Central Administration to only allow site owners to request apps. Apps can then be approved or denied by the App Catalog administrator.
  
 **To configure app requests in the SharePoint Store settings**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. In Central Administration, on the Apps page, in the **SharePoint and Office Store** section, click **Configure Store Settings**.
    
3. On the SharePoint Store Settings page, verify that the selected web application is the web application that you want to configure.
    
    If you want to switch to a different web application, click the down arrow next to the web application URL to change to a different web application.
    
4. To allow or prevent purchases, select an option for **Should end users be able to get apps from the SharePoint Store?**
    
  - Select **Yes** to allow site owners to purchase apps. 
    
  - Select **No** to prevent purchases but allow users to request apps. 
    
5. To allow or prevent apps for Office from the Office Store to be started when a user opens a document in the browser, select an option for **Should apps for Office from the store be able to start when documents are opened in the browser?**
    
  - Select **Yes** to allow apps for Office from the Office Store to start. 
    
  - Select **No** to prevent apps for Office from the Office Store from starting. 
    
6. Click **OK**.
    
## Manage app requests
<a name="AppRequests"> </a>

When site owners request an app for SharePoint from the SharePoint Store, they can request a specific number of licenses and provide a justification for the purchase of the app for SharePoint. Submitted requests are added to the **App Requests** list in the App Catalog of the web application that contains a user's site collection. The app request includes the following fields: 
  
- **Requested by** The user name of the person requesting the app for SharePoint. 
    
- **Title** The title of the app for SharePoint. 
    
- **Seats** and **Site License** The number of licenses the user requested for that app for SharePoint. 
    
- **Justification** The reason why the app for SharePoint would be useful for the organization. 
    
- **Status** By default, the status is set to New for new requests. The person who reviews the request can change the status to Pending, Approved, Declined, Withdrawn, Closed as Approved, or Closed as Declined. 
    
- **View App Details** A link to the app details page in the SharePoint Store. 
    
- **Approver Comments** The person who reviews the request can add comments for the requestor. 
    
 **To view and manage app requests**
  
1. Verify that the user account that is performing this procedure is a member of the site Owners or Designers group for the App Catalog.
    
2. On the App Catalog site, click the **App Requests** list. 
    
3. Select a request in the list, and then click the **Edit** button. 
    
4. Review the details of the request.
    
5. Change the Status to the appropriate value - **Approved** if you want to user to be able to purchase the app, or **Declined** if you do not want to allow the app to be purchased. 
    
6. Add any comments in the **Approver Comments** box, and then click **Save**.
    
    To view a request, requestors can go to the Add an App page in their site collection, and then click **Your Requests**.
    
## Add apps to the App Catalog
<a name="AddApps"> </a>

After you have configured the App Catalog, you can add apps that users can then install to their SharePoint sites or use in their Office documents.
  
 **To add an app to the App Catalog**
  
1. Verify that the user account that is performing this procedure is a member of the site Owners or Designers group for the App Catalog.
    
2. On the App Catalog site, click the **Apps for SharePoint** list. 
    
    On the **Apps for SharePoint** page, click **new item**.
    
3. In the **Choose a file** box, click **Browse**, and then locate the folder that contains the app that you want to upload.
    
    > [!TIP]
    > You can also click **Upload files using Windows Explorer instead** to drag and drop an app for SharePoint into the App Catalog. 
  
4. Select the app, and then click **Open**.
    
5. Click **OK** to upload the app. 
    
6. In the Item details box, verify the Name, Title, Short Description, Icon URL, and other settings for the app.
    
    Be sure that the **Enabled** check box is selected so that users can see the app in their sites. 
    
    You can select the **Featured** check box to list the app in the Featured content view of the App Catalog. 
    
7. Click **Save**.
    
You can also categorize apps in the App Catalog. To add categories, edit the Category field for the App Catalog list and add the category names you want to use.
  
## Remove apps from the App Catalog
<a name="RemoveApp"> </a>

If you no longer want to offer a particular app to your users, you can remove it from the App Catalog. Removal does not uninstall or remove the app from sites to which it has been added. It merely removes the app from the App Catalog, and users cannot add the app to other sites.
  
 **To remove an app from the App Catalog**
  
1. Verify that the user account that is performing this procedure is a member of the site Owners or Designers group for the App Catalog.
    
2. On the App Catalog site, click the **Apps for SharePoint** list. 
    
3. On the **Apps for SharePoint** page, select the app that you want to remove. 
    
4. In the ribbon, on the **Files** tab, click **Delete Document** to remove the app. 
    
5. In the dialog box, click **OK** to confirm that you want to send the item to the site Recycle Bin. 
    
    The app is removed.
    
## See also
<a name="RemoveApp"> </a>

#### Concepts

[Install and manage apps for SharePoint Server](install-and-manage-apps-for-sharepoint-server.md)
  
[Plan for apps for SharePoint Server](plan-for-apps-for-sharepoint.md)

