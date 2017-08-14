---
title: Configure hybrid sites features - roadmap
ms.prod: SHAREPOINT
ms.assetid: 4bd426f4-105c-41cf-a4b8-815db62191ce
---


# Configure hybrid sites features - roadmap
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Office 365 Enterprise, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-21* **Summary:** Learn how to configure hybrid sites features for SharePoint hybrid with Office 365.This article provides a roadmap for configuring  [hybrid sites features](html/plan-for-hybrid-sites-features.md). Follow these steps in the order shown. If you already completed a step when you followed a different roadmap, skip that step, and go to the next one.
### 

StepDescription1.  [Configure Office 365 for SharePoint hybrid](html/configure-office-365-for-sharepoint-hybrid.md) <br/> Configure your Office 365 for enterprises tenant for a hybrid environment, including registering your domain, configuring UPN suffixes, and synchronizing your user accounts.  <br/> 2.  [Set up SharePoint services for hybrid environments](html/set-up-sharepoint-services-for-hybrid-environments.md) <br/> Configure the needed SharePoint services for hybrid search, including User Profiles, MySites, and the Application Management service.  <br/> **3. (SharePoint Server 2013 only)  [Install the September PU for SharePoint Server 2013](https://technet.microsoft.com/library/mt715807.aspx)** <br/> Install the September 2015 PU or higher for SharePoint Server 2013. (We recommend installing the latest PU.)  <br/> 3.  [Run Hybrid Picker](html/run-hybrid-picker.md) <br/> Configure hybrid sites features by running the Hybrid Picker in Office 365.  <br/> 4. Quick test  <br/>  Check to make sure hybrid sites features are working: <br/>  Log in to a SharePoint Server as a regular user. (Be sure you're a member of the correct audience if you used audiences.) <br/>  Click the Follow link at the top of the page. <br/>  You should see a small pop-up under **Follow** letting you know that you're following the site. Click this pop-up and notice that it navigates to your personal site, and the list of sites you're following in SharePoint Online. <br/> 
## The extensible hybrid app launcher

The app launcher is included as part of SharePoint Server 2016. If you want to add it to SharePoint Server 2013, open the SharePoint 2013 Management Shell and run the following cmdlet:.
```

install-SPFeature SuiteNav
```

For each site collection where you want to use the feature, run the following cmdlet:


```
Enable-SPFeature suitenav -url <SiteCollectionURL>
```


# See also

#### 

 [Hardware and software requirements for SharePoint hybrid](html/hardware-and-software-requirements-for-sharepoint-hybrid.md)
  
    
    
 [Accounts needed for hybrid configuration and testing](html/accounts-needed-for-hybrid-configuration-and-testing.md)
  
    
    

  
    
    

