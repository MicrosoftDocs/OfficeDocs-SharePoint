---
title: "How to change the text that is displayed in the Search Box Web Part in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/24/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: de0a2fb6-4372-47fc-9871-584724b7e7c7
description: "Learn how to change the text that is displayed in the Search Box Web Part in SharePoint Server."
---

# How to change the text that is displayed in the Search Box Web Part in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article will be short and sweet, so let's get right to it.
  
## How to change the text that is displayed in the Search Box Web Part

The following screen shot shows the default text that is displayed in the Search Box Web Part.
  
![Default Text in Search Box](../media/OTCSP_DefaultText.png)
  
Here are the steps to change this text:
  
1. In your mapped network drive, go to **Display Templates** --> **Search**, and open the file  *Control_SearchBox*  . For details about mapping your network drive, see [Stage 6: Upload and apply a new master page to a publishing site in SharePoint Server](../administration/stage-6-upload-and-apply-a-new-master-page-to-a-publishing-site.md).
    
2. Replace the value for the  *promt*  variable with the text you want to display. Enclose the text in quotation marks. 
    
    The following screen shot shows how we changed this in our Search Center scenario.
    
     ![Replace the Prompt Text](../media/OTCSP_NewText.png)
  
3. Save the file.
    
    In the Search Center, you can now see the new text.
    
     ![New Text Displayed](../media/OTCSP_NewTextDisplayed.png)
  
So that's it for this series. If you plan to change how search results are displayed in your Search Center, we hope you'll find the information in this series helpful.
  

