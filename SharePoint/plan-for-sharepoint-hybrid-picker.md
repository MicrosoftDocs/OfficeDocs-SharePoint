---
title: Plan for SharePoint Hybrid Picker
ms.prod: SHAREPOINT
ms.assetid: 8fa6b865-c11a-4bc3-b3da-df492ffadf38
---


# Plan for SharePoint Hybrid Picker
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Office 365 Enterprise, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-20* **Summary:** Use Hybrid Picker to configure hybrid features between SharePoint Server and Office 365.
## What does Hybrid Picker do for you?

The Hybrid Picker simplifies configuring hybrid sites features by automating the configuration of the server-to-server trust between SharePoint Server and Office 365. It also configures hybrid OneDrive for Business and hybrid sites features for you. Before you can use Hybrid Picker, you must complete your  [Office 365 setup for hybrid](html/configure-office-365-for-sharepoint-hybrid.md) and configure the needed [SharePoint Server 2016 Beta 2 services](html/set-up-sharepoint-services-for-hybrid-environments.md).Note that different hybrid features require different public updates for your SharePoint Server farm. See  [Minimum public update levels for SharePoint hybrid features](https://support.office.com/article/eafa9e37-1433-42ff-a842-a72d6ebe2a07) for details.
## Where can I find Hybrid Picker tool?

Hybrid Picker is part of Office 365. You can find it in the SharePoint Tenant Admin console. You need to log on as a Global Administrator or a user assigned the SharePoint Administrator role. To use Hybrid Picker, you also need to be logged in to a SharePoint Server farm server as a Farm Administrator.
## What am I picking and choosing?

Hybrid Picker currently sets up either hybrid OneDrive for Business or hybrid sites features:
- ** [Hybrid OneDrive for Business](https://go.microsoft.com/fwlink/p/?LinkID=746869)** - This redirects your users' OneDrive for Business to OneDrive for Business in Office 365. It also installs a server-to-server (OAuth/S2S) connection between SharePoint Server on-premises and SharePoint Online in case further hybrid configurations are planned.
    
  
- **Hybrid site features** - This option configures a server-to-server (OAuth/S2S) trust between SharePoint Server and Office 365, and then configures hybrid sites features. Choosing the option configures hybrid OneDrive for Business as well.
    
  
To get started deploying a hybrid feature, choose a  [configuration roadmap](html/sharepoint-server-2016-hybrid-configuration-roadmaps.md).
# See also

#### 

 [Hybrid sites and search](https://go.microsoft.com/fwlink/p/?LinkID=746868)
  
    
    

  
    
    

