---
title: Add apps for SharePoint to a SharePoint site
ms.prod: SHAREPOINT
ms.assetid: 57d52c9e-5069-4bcf-87e3-24482198a462
---


# Add apps for SharePoint to a SharePoint site
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Site owners can add apps for SharePoint to SharePoint sites so that they and other users of the site can use the app.Site owners can add apps for SharePoint from the SharePoint Store or an App Catalog to their sites. Adding an app installs an instance of that app to the site. This article covers how to add apps to your sites.Be sure you've  [configured your environment for SharePoint apps](html/configure-an-environment-for-apps-for-sharepoint-server.md) before you get started.
## Add apps for SharePoint to SharePoint sites

Site owners can add apps for SharePoint from the following sources to their sites:
- from the list of apps already available for a site (default apps, such as standard lists and libraries, and apps that have been purchased already).
    
  
- from the App Catalog.
    
  
- from the SharePoint Store.
    
  
Note that a user logged in as teh system account cannot install a app.When you add an app for SharePoint, the app requests permissions that it needs to function (for example, access to Search, or to create a list). If you don't have those permissions, the app won't install. Contact your administrator to get the needed permissions or have someone with those permissions add the app.The following procedures provide steps for adding apps from these sources. **To add an app from the list of available apps in a site**
1. Verify that the user account that is performing this procedure is a member of the site Owners group.
    
  
2. On the home page, under **Get started with your site**, click **Add lists, libraries, and other apps.**
    
    If the Get started with your site control does not appear on the home page, click the **Settings** icon, and click **View Site Contents**, and then on the **Site Contents** page, click **Add an App**.
    
  
3. In the Your Apps list, click the app you want to add.
    
  
4. Follow the instructions to Trust the app (if it is a custom component) or Name the app (if it is a SharePoint component).
    
    The app for SharePoint is added and appears in the **Apps** section of your Site Contents list.
    
  
 **To add an app from an App Catalog**
1. Verify that the user account that is performing this procedure is a member of the site Owners group.
    
  
2. On the home page, under **Get started with your site**, click **Add lists, libraries, and other apps.**
    
    If the Get started with your site control does not appear on the home page, click the Settings icon, and click **View Site Contents**, and then on the Site Contents page, click **Add an App**.
    
  
3. Click **From** *Name*  .
    
    Where  *Name*  is the name of your organization's App Catalog. For example, "From Contoso".
    
    > [!TIP:]
      
4. Click the app you want to add.
    
  
5. In the Grant Permission to an App dialog box, if you trust the app, click **Allow Access**.
    
    The app for SharePoint is added and appears in Apps section of your Site Contents list.
    
  
 **To add an app from the SharePoint Store**
1. Verify that the user account that is performing this procedure is a member of the site Owners group.
    
  
2. On the home page, under **Get started with your site**, click **Add lists, libraries, and other apps.**
    
    If the Get started with your site control does not appear on the home page, click the Settings icon, and click **View Site Contents**, and then on the Site Contents page, click **Add an App**.
    
  
3. Click **SharePoint Store**.
    
  
4. Browse the SharePoint Store to find an app that you want.
    
  
5. Click the app you want to add.
    
  
6. Click Details, and then click **Buy It**.
    
  
7. Follow the steps to log in and purchase the app, if required.
    
  
8. In the **Grant Permission to an App** dialog box, if you trust the app, click **Allow Access**.
    
    The app for SharePoint is added and appears in the Apps section of your Site Contents list.
    
  

# See also

#### 

 [Install and manage apps for SharePoint Server](html/install-and-manage-apps-for-sharepoint-server.md)
  
    
    

#### 

 **Import-SPAppPackage**
  
    
    
 **Install-SPApp**
  
    
    

  
    
    

