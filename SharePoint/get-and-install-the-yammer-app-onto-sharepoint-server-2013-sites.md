---
title: Get and install the Yammer app onto SharePoint Server 2013 sites
ms.prod: SHAREPOINT
ms.assetid: 7bc6999f-c4f4-476f-ba0b-28b74166e9c2
---


# Get and install the Yammer app onto SharePoint Server 2013 sites
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Office 365, SharePoint Server 2013, Yammer Enterprise*  * **Topic Last Modified:** 2017-07-31* **Summary:** Learn how to add the Yammer app to the app catalog and make it available on My Sites and team sites.
> [!WARNING:]

  
    
    

The Yammerapp for SharePoint lets you embed Yammer feeds into on-premises SharePoint Server 2013 sites to make them more social and engaging. Before you can do that, you have to both remove the Newsfeed Web Parts from My Sites and team sites and hide the user interface controls that provide the social features you’ll replace with Yammer. Next, you add the Yammer app to the App Catalog and install and set up the Yammer feed on your sites. This article takes you through the steps that are required to do the second part: add the Yammer app to the App Catalog and install and set up the Yammer feed on your team sites. For information about how to remove the Newsfeed Web Parts from My Sites and team sites and hide the user interface controls, see  [Hide SharePoint Server 2013 social features](html/hide-sharepoint-server-2013-social-features.md).Before you get started, make sure you have configured one of the  [Yammer social scenarios](html/social-scenarios-with-yammer-and-sharepoint-server-2013.md) in SharePoint Server 2013.
> [!NOTE:]

  
    
    


## Get the Yammer app from the SharePoint Store
<a name="proc1"> </a>

First, you have to get the Yammerapp for SharePoint from the SharePoint Store. If you have already installed the Yammerapp for SharePoint, make sure that you have the most current version. For more information, see  [Update to the latest Yammer App for SharePoint](https://go.microsoft.com/fwlink/?LinkId=395077). Use an account that is a member of the farm admins group to follow these steps:
> [!IMPORTANT:]

  
    
    


1. On the SharePoint Central Administration website, choose **Apps**.
    
     ![The Apps page in Central Administration](images/)
  

  
2. Choose **Purchase Apps**. The SharePoint Store opens.
    
     ![The SharePoint Apps Store](images/)
  

  
3. In the **Find an app** box, enter **Yammer**, and then press Enter.
    
  
4. On the Search results page, choose **Yammer App for SharePoint**.
    
  
5. On the **Yammer App for SharePoint** page, choose **Add It**.
    
    > [!NOTE:]
      

     ![Add It button for free apps in SharePoint Store](images/)
  

  
6. When the following confirmation message is shown, choose **Return to site**. The Yammerapp for SharePoint is now available in the App Catalog. You can use the app on a site where a Yammer feed is needed.
    
     ![Confirmation screen for Yammer App](images/)
  

  

## Install the Yammer app on your site
<a name="proc2"> </a>

Use a farm admin account to follow these steps:
1. Choose **Newsfeed** to go to the farm admin's My Site.
    
  
2. Choose **Settings**, and then choose **Manage shared apps**.
    
  
3. On the **Site Contents** page, choose **add an app** > **From Your Organization** > **Yammer app for SharePoint** > **Trust It**. The Yammer app is now installed for your site.
    
  

## Add the Yammer home feed to the My Site Newsfeed page
<a name="proc3"> </a>

Any user who has Contribute permissions can follow these steps:
1. Choose **Newsfeed** to view your My Site.
    
  
2. Choose **Settings**, and then choose **Edit page**.
    
  
3. Choose **Add a Web Part**.
    
  
4. In the **Categories** section, choose **Apps**.
    
  
5. Choose **Yammer Feed**.
    
  
6. In the **About the part** section, choose a zone in which to add the Web Part, and then choose **Add**. The Yammerapp for SharePoint Web Part is now added to the page.
    
  
7. Choose **Login** to sign in to the app by using your Yammer account.
    
  
8. Select the Yammer home feed as the feed type on the configuration page.
    
  
9. Select your network on the drop-down menu, and then save the configuration. Refresh the page to check that the Yammer home feed is successfully embedded on your My Site.
    
     ![Yammer home feed on a My Site page](images/)
  

  

## Add the Yammer group feed to a team site
<a name="proc4"> </a>

The following steps have to be done on every team site to which you want to add a Yammer group feed. Any user who has Contribute permissions can follow these steps:
1. Browse to the team site's home page.
    
  
2. On the ribbon, choose **Page**, and then choose **Edit**.
    
  
3. Choose **Insert**, and then choose **App Part**.
    
  
4. Choose **Yammer app for SharePoint**.
    
  
5. Choose **Add**. The Yammerapp for SharePoint Web Part is now added to the team site.
    
  
6. Choose **Save**.
    
  
7. Choose **Login** to sign in to the app by using your Yammer account.
    
  
8. Choose the Yammer group feed as the feed type on the configuration page.
    
  
9. Enter the Group Feed ID, and then save the configuration. Refresh the page to verify that the Yammer group feed is now added to your team site.
    
     ![Yammer group feed on a team site page](images/)
  

  

## Acknowledgements
<a name="proc4"> </a>

The SharePoint Server 2013 Content Publishing team thanks Vidya Srinivasan, Microsoft SharePoint Server Product Team, for her contribution to this article.
# See also

#### 

 [Integrate Yammer with on-premises SharePoint 2013 environments](html/integrate-yammer-with-on-premises-sharepoint-2013-environments.md)
  
    
    
 [Hide SharePoint Server 2013 social features](html/hide-sharepoint-server-2013-social-features.md)
  
    
    

  
    
    

