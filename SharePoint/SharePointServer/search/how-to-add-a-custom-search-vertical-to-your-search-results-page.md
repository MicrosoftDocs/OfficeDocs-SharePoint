---
title: "How to add a custom search vertical to your search results page in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 8f5ab43a-d45c-4143-8229-34ed0c20584d
description: "Learn how to add a custom search vertical to your results page in SharePoint Server."
---

# How to add a custom search vertical to your search results page in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
In the previous article in this series, [How to add refiners to your search results page in SharePoint Server](how-to-add-refiners-to-your-search-results-page.md), we showed you how to add and configure refiners for your classic search results page. In this article you'll learn:
  
- [Using a search vertical in an everyday situation](how-to-add-a-custom-search-vertical-to-your-search-results-page.md#BKMK_UsingaSearchVerticalinanEverydaySituation)
    
- [About search verticals in SharePoint Server](how-to-add-a-custom-search-vertical-to-your-search-results-page.md#BKMK_AboutSearchVerticalsinSharePoint2013)
    
- [Result sources - why setting limits is a good thing](how-to-add-a-custom-search-vertical-to-your-search-results-page.md#BKMK_ResultSourcesWhySettingLimitsisaGoodThing)
    
- [How to create a custom search vertical](how-to-add-a-custom-search-vertical-to-your-search-results-page.md#BKMK_HowtoCreateaCustomSearchVertical)
    
- [What you can do after you have successfully set up a Search Center](how-to-add-a-custom-search-vertical-to-your-search-results-page.md#BKMK_WhatYouCanDoAfterYouHaveSuccessfullySetUpaSearchCenter)
    
## Using a search vertical in an everyday situation
<a name="BKMK_UsingaSearchVerticalinanEverydaySituation"> </a>

You may not have heard the term "search vertical" before, but it's likely you have used them several times. Let's take a closer look at what we mean by the term "search vertical."
  
Suppose you enjoy skiing, so you often search for ski-related content. When you enter the word "ski" in a search engine, you get many search results.
  
![Search Vertical Web](../media/OTCSP_WebSki.png)
  
You are delighted to see there is much information out there about skiing, but in this case, you are just looking for great ski pictures. This is where search verticals can be used.
  
On the same search results page, you click **IMAGES**, and in an instant your screen is filled with images of people in colorful clothing, racing down white slopes while bathing in sunshine from a clear blue sky. Wow! 
  
![Search Vertical Images](../media/OTCSP_ImagesSki.png)
  
When you click **IMAGES**, you are using a search vertical. Bing has five search verticals: **WEB**, **Images**, **VIDEOS** **Maps**, and **NEWS**. 
  
![Five Search Verticals](../media/OTCSP_BingVerticals.png)
  
A search vertical filters search results so only a certain type of search results are displayed. When we clicked the **IMAGES** search vertical, the search results were filtered so only images were displayed. 
  
## About search verticals in SharePoint Server
<a name="BKMK_AboutSearchVerticalsinSharePoint2013"> </a>

In SharePoint Server, search verticals are displayed in the **Search Navigation Web Part**. There are four default search verticals: **Everything**, **People**, **Conversations**, and **Videos**. 
  
![Four Default Search Verticals](../media/OTCSP_DefaultSPSearchVerticals.png)
  
When users click one of these search verticals, it will in fact move to a new page. For example, the default search results page, the **Everything** search vertical, uses the **results.aspx** page. 
  
![Everything Page](../media/OTCSP_EverythingPage.png)
  
When a user clicks on the **People** search vertical, they navigate to the **peopleresults.aspx** page. 
  
![People Page](../media/OTCSP_PeoplePage.png)
  
The following are the default pages that are used for the four search verticals:
  
|**Search vertical**|**Use this page**|
|:-----|:-----|
|Everything  <br/> |results  <br/> |
|People  <br/> |peopleresults  <br/> |
|Conversations  <br/> |conversationresults  <br/> |
|Videos  <br/> |videoresults  <br/> |
   
To view these pages, from the **Site settings** menu, select **Site contents** --> **Pages**. 
  
![Default Pages](../media/OTCSP_DefaultPages.png)
  
The default vertical pages all use these Web Parts:
  
![Web Parts On Search Vertical Page](../media/OTCSP_WepPartsOnSearchVerticalPage.png)
  
1. Refinement Web Part
    
2. Search Box Web Part
    
3. Search Navigation Web Part
    
4. Search Results Web Part
    
The difference between these pages is how the **Search Results Web Part** is configured. To be specific: the Web Parts are configured to use different  *result sources*  . 
  
## Result sources - why setting limits is a good thing
<a name="BKMK_ResultSourcesWhySettingLimitsisaGoodThing"> </a>

As explained in an earlier article, a  *result source*  specifies the source from which your search results can come. For example, suppose that your search index is the cube as shown in the following diagram, where you have four result sources: 
  
- Result source 1: search results can come from the complete cube.
    
- Result source 2: search results can come only from the Bs.
    
- Result source 3: search results can come only from the Cs.
    
- Result source 4: search results can come only from the Ds.
    
![Search Vertical Cube](../media/OTCSP_SearchVerticalCube.png)
  
So, by limiting from where search results can come from, you can make it easier for your users to find what they're looking for.
  
In our internal search center scenario, all search results are list items that represent a type of media file, for example an article, an image or a video. We wanted to create three custom search verticals for three specific types of media files:
  
- Art: list items that represent images
    
- Video: list items that represent videos
    
- Interop: list items that represent interoperable articles (interoperable articles are a specific type of article we produce)
    
But, before we could begin to create these search verticals, we had to create one result source for each custom search vertical. We showed you how to create a result source in [How to create a result source](how-to-configure-the-search-results-web-part-to-use-a-new-result-source.md#BKMK_HowtoCreateaResultSource).
  
This is how we defined the  *Art result source*  . 
  
![Art Result Type Query](../media/OTCSP_ArtResultTypeQuery.png)
  
Remember,  `{searchTerms?}(contentclass:sts_listitem) path:http://<path>` was the query text of the Article result source that we created earlier. To this, we added  `AND ContentType:Art`
  
In our lists, we use the site column  *Content Type*  to specify the different media files. For example, all images have the value  *Art*  for  *Content Type*  . 
  
![Content Type:Art](../media/OTCSP_ContentTypeArt2.png)
  
So, by adding  `AND ContentType:Art` to the query text, only list items that have the value  *Art*  for  *Content Type*  will be returned in search results. 
  
Here are the three new result sources we created.
  
![New Result Sources](../media/OTCSP_ThreeNewResultSources.png)
  
Now that we had three new result sources, we could move on to creating the custom search verticals.
  
## How to create a custom search vertical
<a name="BKMK_HowtoCreateaCustomSearchVertical"> </a>

When you create a custom search vertical, the first thing that you must do is to create a page the search vertical will use. Here are the steps to create a new page:
  
1. From the **Site Settings** menu, select **Site contents**. 
    
     ![Create Search Vertical: Site Contents](../media/OTCSP_SiteContents.png)
  
2. Select **Pages**. 
    
3. In the **Pages** library, select the **FILES** tab --> **New Document** --> **Page**. 
    
     ![New Page](../media/OTCSP_NewPage.png)
  
4. On the **Create Page** page, enter a **Title** and a **URL Name**. 
    
    In our scenario, we entered  *Art*  and  *art*  . 
    
     ![Create Page](../media/OTCSP_NewArtPage.png)
  
5. Click **Create**. 
    
    Your new page is displayed in your **Pages** library. 
    
     ![Pages Library](../media/OTCSP_NewPageInLibrary.png)
  
    Now that you have a page for your custom search vertical, you can begin to create the actual search vertical. Here's what you should do:
    
6. On the **Site Settings** page, click **Search Settings**. 
    
     ![Search Settings](../media/OTCSP_SearchSettings.png)
  
7. On the **Search Settings** page, in the **Configure Search Navigation** section, click **Add Link**. 
    
     ![Configure Search Navigation](../media/OTCSP_AddLink.png)
  
8. In the **Navigation Link** dialog box, in the **Title** field, enter the search vertical title. This text will appear as the "tab" name on your search results page. 
    
    In our scenario, we entered  *Art*  . 
    
     ![Navigation Title](../media/OTCSP_NavigationTitle.png)
  
9. In the **URL** field, select **Browse** and select a page for your search vertical. 
    
    In our scenario, we selected the  *art*  page we just created. 
    
     ![URL Art](../media/OTCSP_URLArt.png)
  
10. Click **OK** to close the **Navigation Link** dialog Box. 
    
11. On the **Search Settings** page, in the **Configure Search Navigation** section, select the search verticals that you don't want to display, and then click **Delete**. 
    
    In our scenario, we deleted the **People**, **Conversations**, and **Videos** verticals so that we were only left with the **Everything** and the **Art** search vertical. 
    
     ![Two Verticals](../media/OTCSP_TwoVerticals.png)
  
12. Click **OK** to save all changes. 
    
13. In your Search Center, enter a query. On your search results page, your newly created search vertical is displayed.
    
    On our search results page, the  *Art*  vertical was displayed. 
    
     ![New Art Vertical](../media/OTCSP_NewArtVertical.png)
  
14. On your search results page, click on your newly created search vertical, and verify that the URL is the same as you specified in step 4.
    
    In our scenario, we clicked  *Art*  , and verified that the URL was  *\<site\>/articles/Pages/art.aspx*  . We also noticed that 13 search results were displayed. 
    
     ![Query Art Vertical](../media/OTCSP_QueryArtVertical.png)
  
15. On your new search vertical page, select to edit the page, and then to edit the **Search Results Web Part**. 
    
16. In the Web Part tool page, click **Change query**. This opens a dialog box. 
    
     ![Change Query](../media/OTCSP_ChangeQuery.png)
  
17. In the **Build Your Query** dialog box, from the **Select a query** menu, select the result source that you created for this search vertical (what we did in the previous section). 
    
    In our scenario, we selected  *Art result source (Site Collection)*  . 
    
     ![Select a Query](../media/OTCSP_SelectAQuery.png)
  
18. Click **OK** and save the page. 
    
    On your new search vertical page, enter a query to verify that the correct search results are displayed.
    
    In our scenario, we entered  *united airlines*  again, and noticed that only 11 search results were displayed. Remember, before we changed the result source in the **Search Result Web Part**, 13 results were displayed. So our new vertical was working. Nice! 
    
     ![Final Art Vertical Result](../media/OTCSP_FinalArtVerticalResult.png)
  
    In our scenario, we added two more search verticals,  *Video*  and  *Interop*  . And with that, we had completed the Search Center set up. 
    
     ![All Search Verticals](../media/OTCSP_AllSearchVerticals.png)
  
## What you can do after you have successfully set up a Search Center
<a name="BKMK_WhatYouCanDoAfterYouHaveSuccessfullySetUpaSearchCenter"> </a>

When you have successfully set up a Search Center, the first thing that you should do is congratulate yourself on a job well done! Nice job!
  
But, the job usually doesn't end here. To make the Search Center even more user-friendly, you can change the way search results are displayed, for example to display information that is specific to your company or business. You can read about how to do that in series [How to change the way search results are displayed in SharePoint Server](how-to-change-the-way-search-results-are-displayed.md).
  

