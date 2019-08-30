---
title: "Configure cloud hybrid search - roadmap"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/9/2018
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- Ent_O365_Hybrid
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- M365-collaboration
ms.custom: 
ms.assetid: 0bba350d-ec33-43db-a873-930559c78dee
description: "Learn how to configure cloud hybrid search for SharePoint Server by setting up a cloud Search service application in your SharePoint Server environment and connecting it to your search index in Office 365."
---

# Configure cloud hybrid search - roadmap

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]

Learn how to configure [cloud hybrid search](/SharePoint/hybrid/learn-about-cloud-hybrid-search-for-sharepoint) for SharePoint Server by setting up a cloud Search service application in your SharePoint Server environment and connecting it to your search index in Office 365. 
  
This article describes how you set up cloud hybrid search in an environment with SharePoint Server and SharePoint Online for Office 365 for enterprises. With the cloud hybrid search solution, you add crawled metadata from all your content, including on-premises content, to your search index in Office 365. When users search in Office 365, they get search results from both on-premises and from Office 365 content.
  
> [!NOTE]
> If you are an Office 365 Dedicated customer, setting up cloud hybrid search requires engagement of SharePoint Service Engineering staff. Contact your Microsoft Service Delivery Manager for assistance. If you aren't sure what type of customer you are, you can safely disregard this note. 
  
## Before you start

To complete the configuration steps you'll need these items:
  
- The [hardware and software](/SharePoint/hybrid/hardware-and-software-requirements-for-sharepoint-hybrid) that's needed in a SharePoint Server hybrid environment. 
    
- An on-premises server or virtual machine for cloud hybrid search that has:
    
  - Minimum 100 GB storage, 16 GB RAM, and four 1.8 GHz CPUs.
    
  - SharePoint Server installed.
    
  - Is a member of a Windows Server Active Directory domain.
    
- (SharePoint Server 2013 only) You must have at least [Service Pack 1 and the January 2016 public update installed](/officeupdates/sharepoint-updates).
    
- The [accounts](/SharePoint/hybrid/accounts-needed-for-hybrid-configuration-and-testing) that are needed in a SharePoint Server hybrid environment, a search account for cloud hybrid search in SharePoint Server, and a managed account for default content access in SharePoint Server. Ensure that the account for default content access has at least read access to the content to crawl. 
    
- Your company's or organization's SharePoint Online portal URL, such as https://\<yourtenantname\>.sharepoint.com
    
- The search architecture plan you made for cloud hybrid search.
    
- If you'll use the [Hybrid picker in the SharePoint Online admin center](hybrid-picker-in-the-sharepoint-online-admin-center.md) wizard to help you configure, ensure that the application farm that hosts the SharePoint Server Central Administration website has [.NET 4.6.3](https://www.microsoft.com/en-us/download/details.aspx?id=53321) installed. 
    
- If you'll use the **CreateCloudSSA.ps1** and **Onboard-CloudHybridSearch.ps1** Microsoft PowerShell scripts to help you configure, find them in the [Microsoft Download Center](https://go.microsoft.com/fwlink/?LinkId=717902). You'll also need the [Microsoft Online Services Sign-In Assistant for IT Professionals RTW](https://go.microsoft.com/fwlink/?LinkID=286152) and the [Azure Active Directory Module for Windows PowerShell](https://www.powershellgallery.com/packages/MSOnline/1.1.183.8).
    
## Follow these steps:

If you already completed step 1 when you configured a different hybrid solution, skip that step and go to the next.
  
|||
|:-----|:-----|
|Step  <br/> |Description  <br/> |
|**1. [Configure Office 365 for SharePoint hybrid](/SharePoint/hybrid/configure-office-365-for-sharepoint-hybrid)** <br/> |Configure your Office 365 tenant for a hybrid environment, including registering your domain, configuring UPN suffixes, and synchronizing your on-premises user accounts with Office 365.  <br/> |
|**2. [Create a cloud Search service application in SharePoint Server](configure-cloud-hybrid-searchroadmap.md#BKMK_CreateCloudSSA)** <br/> |Run the Hybrid Picker wizard on the application farm that hosts the SharePoint ServerCentral Administration website.  <br/> Alternatively, run the **CreateCloudSSA.ps1** PowerShellscript  <br/> |
|**3. [Connect your cloud Search service application to your Office 365 tenant](configure-cloud-hybrid-searchroadmap.md#BKMK_ConnectCloudSSAToO365)** <br/> |If you used the Hybrid Picker wizard to create a cloud Search service application, skip this step. The Hybrid Picker automatically connected your environments.  <br/> Otherwise, run the **Onboard-CloudHybridSearch.ps1** PowerShell script to onboard your cloud SSA and Office 365 tenant to cloud hybrid search. The script sets up the cloud SSA to interact with the Office 365 tenant and also sets up server-to-server authentication.  <br/> |
|**4. [Set up search architecture in SharePoint Server for cloud hybrid search](configure-cloud-hybrid-searchroadmap.md#BKMK_SetupSearchArch)** <br/> |This step is optional. If you planned a search architecture that's different from the default one, set up the planned search architecture.  <br/> |
|**5. [Create a content source for cloud hybrid search to crawl](configure-cloud-hybrid-searchroadmap.md#BKMK_CreateOnPremContentSource)** <br/> |We recommend adding a small file share first, you can add more on-premises content later.  <br/> |
|**6. [Set up a separate Search Center in Office 365 to validate hybrid search results](configure-cloud-hybrid-searchroadmap.md#BKMK_SetupValidationSearchCenter)** <br/> |Keep the existing search experience unchanged by setting up a separate Search Center in Office 365 so you can validate and tune the new search experience there.  <br/> |
|**7. [Start a full crawl of on-premises content for cloud hybrid search](configure-cloud-hybrid-searchroadmap.md#BKMK_StartFullCrawl)** <br/> |When the crawl completes, your on-premises content shows up in the search results in your validation Search Center in Office 365 and in Office Delve.  <br/> |
|**8. [Verify that cloud hybrid search works](configure-cloud-hybrid-searchroadmap.md#BKMK_VerifyCloudHybridSearch)** <br/> |Go to your Search Center in SharePoint Online in Office 365 and enter this query: "IsExternalContent:true". The results you get should show content from the on-premises content source that you've crawled.  <br/> |
|**9. [Tune cloud hybrid search](configure-cloud-hybrid-searchroadmap.md#BKMK_TuneCloudHybridSearch)** <br/> |Set up and tune the search experiences you've planned for your users.  <br/> |
|**10. Remove the validation Search Center and expose all users to hybrid search results.** <br/> |Set your Search Center and any site search in Office 365 to use the default result source and set up the default result source with the search experiences that you've tuned. Your on-premises content shows up in the search results in your Search Center in Office 365, site search in Office 365, and in Office Delve.  <br/> |
   
## Create a cloud Search service application in SharePoint Server
<a name="BKMK_CreateCloudSSA"> </a>

The cloud SSA lets you crawl and add metadata from on-premises content to the search index in Office 365. Each search farm can have only one cloud SSA, but can have multiple SSAs in combination with the cloud SSA. You can't convert an existing SSA to a cloud SSA. 
  
> [!NOTE]
> If your organization restricts computers from connecting to the internet, you need to allow access to the endpoints (FQDNs) that cloud hybrid search uses. Include the endpoints in your outbound allow lists. The endpoints are listed in the SharePoint Online section of the article [Office 365 URLs and IP address ranges](/office365/enterprise/urls-and-ip-address-ranges) and are marked for use with Hybrid Search. 
  
Use the Hybrid Picker to connect your SharePoint Server and Office 365 environments and create the cloud Search service application.
  
On the application server that hosts the SharePoint ServerCentral Administration website:
  
1. Log on to the console as a farm administrator.
    
2. Connect to Office 365 as a global administrator.
    
3. Navigate to [https://go.microsoft.com/fwlink/?linkid=867176](https://go.microsoft.com/fwlink/?linkid=867176) to download, install, and start the Hybrid Picker wizard. 
    
4. Follow the prompts in the Hybrid Picker and select the hybrid search feature.
  
The Hybrid Picker lets you choose between a cloud SSA with the default search architecture on the application server that hosts the SharePoint Server Central Administration website, or a cloud SSA with a search architecture on **two** application servers (supports [high availability](../search/plan-enterprise-search-architecture.md#BKMK_HiAvail))
    
The Hybrid Picker saves you time because it also connects the cloud SSA to your Office 365 tenant (step 3).
  
### Alternative methods for creating a cloud Search service application

You can also create the cloud SSA as follows:
  
- You can download the **CreateCloudSSA.ps1** Powershell script from the [Microsoft Download Center](https://go.microsoft.com/fwlink/?LinkId=717902) and run it. The script lets you choose between a cloud SSA with the default search architecture on the application server that hosts the SharePoint Server Central Administration website, or a cloud SSA with a search architecture on two application servers (supports [high availability](../search/plan-enterprise-search-architecture.md#BKMK_HiAvail)).
    
- You can [use the SharePoint Central Administration website](/SharePoint/search/create-and-configure-a-search-service-application), just like you would for an SSA. With this method you get a cloud SSA and the default search architecture installed on the application server that hosts the SharePoint Server Central Administration website.
    
To create a cloud SSA by running the **CreateCloudSSA.ps1** PowerShell script, follow the instructions below. 
  
> [!NOTE]
> When you installed SharePoint Server, the user account from which you ran the installation was granted the appropriate permissions to run Windows PowerShell cmdlets. 
  
On the application server that hosts the SharePoint ServerCentral Administration website , follow these steps:
  
1. Make sure you're using the same user account as when you installed SharePoint Server. This account is granted the appropriate permissions to run Window Powershell cmdlets.
    
2. Start the Windows Powershell console with administrator privileges: Click **Start**, type **PowerShell**, and then right-click **Windows PowerShell** and select **Run as administrator.**
    
3. Run the **CreateCloudSSA.ps1** PowerShell script. 
    
4. When prompted, type:
    
  - The host name of the search server in SharePoint Server.
    
  - If you've planned highly available search, the host name of the second search server.
    
  - The Search service account in this format: domain\username.
    
  - A name of your choice for the cloud SSA.
    
  - The name of the database server in SharePoint Server
    
5. Verify that you see the message that the cloud SSA was successfully created.
    
#### Can I make my own Windows PowerShell script for creating a cloud SSA?

If you want to make your own PowerShell script for creating a cloud SSA, first study the **CreateCloudSSA.ps1** PowerShell script we've provided. Notice that the difference between creating a cloud SSA and an SSA is the value of the property **CloudIndex**. You set **CloudIndex**: **true** when you create a cloud SSA (you can't change this value later). When **CloudIndex** is true, crawled metadata **is not** added to the on-premises search index. However, this doesn't mean that the metadata is added to the Office 365 search index, you have to onboard the cloud SSA to cloud hybrid search for that to happen (see [Connect your cloud Search service application to your Office 365 tenant](configure-cloud-hybrid-searchroadmap.md#BKMK_ConnectCloudSSAToO365)). Ensure that your PowerShell script:
  
- Tests that the Search service account is a managed account, and makes it a managed account if it isn't.
    
- Includes -CloudIndex $true as an argument when it uses the New-SPEnterpriseSearchServiceApplication PowerShell cmdlet.
    
## Connect your cloud Search service application to your Office 365 tenant
<a name="BKMK_ConnectCloudSSAToO365"> </a>

> [!NOTE]
> If you used the Hybrid Picker to create a cloud Search service application, then you can skip this step. 
  
This section guides you how to onboard your cloud SSA and Office 365 tenant to cloud hybrid search and covers:
  
- **Connecting your cloud SSA and your Office 365 tenant** - When your cloud SSA and your Office 365 tenant are correctly connected, the cloud hybrid search solution is ready to add crawled metadata from on-premises content to the search index in Office 365. When you've onboarded your cloud SSA, check to see that your cloud SSA has the value 1 for the property **IsHybrid**. You check by running this PowerShell command: $ssa.GetProperty("CloudIndex"). 
    
- **Configuring server-to-server authentication** - Server-to-server authentication allows servers to access and request resources from one another on behalf of users. 
    
On the application server that hosts the SharePoint ServerCentral Administration website, follow these steps:
  
1. Ensure that the date and time of the server is synchronized with the other servers in the SharePoint Server farm.
    
2. Download and install the [Microsoft Online Services Sign-In Assistant for IT Professionals RTW](https://go.microsoft.com/fwlink/?LinkID=286152) from the Microsoft Download Center. 
    
3. Download and install the latest version of the [Azure Active Directory Module for Windows PowerShell](https://www.powershellgallery.com/packages/MSOnline/1.1.183.8) from the PowerShell Gallery. 
    
4. Download the [OnBoard-CloudHybridSearch.ps1](https://go.microsoft.com/fwlink/?LinkId=717902) PowerShell script from the Microsoft Download Center.
    
5. If your environment is Office 365 Business, Office 365 Enterprise, Office 365 Education, Office 365 operated by 21Vianet, Office 365 Germany, or Office 365 US Government Defense, open an elevated PowerShell prompt, and run the **OnBoard-CloudHybridSearch.ps1** PowerShell script as follows: 
    
  ```
  Import-Module MSOnline
  ```

  ```
  .\OnBoard-CloudHybridSearch.ps1 -PortalUrl <SPOTenantPortalUrl> -CloudSsaId <CloudSSANameCreatd>
  ```

    **SPOTenantPortalUrl** is the URL of your company's or organization's SharePoint Online portal, and ** CloudSsaID ** is the name of the cloud SSA that you created earlier. 
    
6. If your environment is Office 365 US Government Communication, open an elevated PowerShell prompt, and run the **OnBoard-CloudHybridSearch.ps1** PowerShell script as follows: 
    
  ```
  Import-Module MSOnline
  ```

  ```
  .\OnBoard-CloudHybridSearch.ps1 -PortalUrl <SPOTenantPortalUrl> -CloudSsaId <CloudSSANameCreatd> -IsPortalForUSGovernment $true
  ```

    **SPOTenantPortalUrl** is the URL of your company's or organization's SharePoint Online portal, and ** CloudSsaID ** is the name of the cloud SSA that you created earlier. 
    
7. When prompted, type the global admin credentials for your Office 365 tenant.
    
## Set up search architecture in SharePoint Server for cloud hybrid search
<a name="BKMK_SetupSearchArch"> </a>

If you planned to use the default search architecture that you get when creating a cloud SSA, you can skip this step.
  
Otherwise, ensure that you have prepared the servers you need for your planned search architecture for cloud hybrid search, and follow the [guidance](/SharePoint/search/change-the-default-search-topology) for setting up your [planned search architecture](/SharePoint/hybrid/plan-cloud-hybrid-search-for-sharepoint). This guidance is applicable also for cloud hybrid search.
  
## Create a content source for cloud hybrid search to crawl
<a name="BKMK_CreateOnPremContentSource"> </a>

We recommend that you start with a small on-premises content source, for example a small file share, to test. You can add more on-premises content sources later.
  
1. Verify that the user account that is performing this procedure is an administrator for the cloud SSA.
    
2. On the home page of Central Administration, in the **Application Management** section, click **Manage service applications**. 
    
3. On the Manage Service Applications page, click the cloud SSA.
    
4. On the Search Administration Page, in the **Crawling** section, click ** Content Sources **. 
    
5. On the Manage Content Sources page, click **New Content Source**. 
    
6. On the Add Content Source page, in the **Name** section, in the **Name** box, type a name for the new content source. 
    
7. In the **Content Source Type** section, select the type of content that you want to crawl. 
    
8. In the **Start Addresses** section, in the **Type start addresses below (one per line)** box, type the URLs from which the crawler should begin crawling. 
    
9. In the **Crawl Settings** section, select the crawling behavior that you want. 
    
10. In the **Crawl Schedules** section, to specify a schedule for full crawls, select a defined schedule from the **Full Crawl** list. A full crawl crawls all content that is specified by the content source, regardless of whether the content has changed. To define a full crawl schedule, click **Create schedule**. 
    
11. To specify a schedule for incremental crawls, select a defined schedule from the **Incremental Crawl list**. An incremental crawl crawls content that is specified by the content source that has changed since the last crawl. To define a schedule, click **Create schedule**. You can change a defined schedule by clicking **Edit schedule**. 
    
12. To set the priority of this content source, in the **Content Source Priority** section, on the **Priority** list, select **Normal** or **High**. 
    
13. Click **OK**. 
    
## Set up a separate Search Center in Office 365 to validate hybrid search results
<a name="BKMK_SetupValidationSearchCenter"> </a>

After you've set up cloud hybrid search and completed a full crawl of your on-premises content, your existing Search Center in Office 365 as well as Office Delve will automatically show both on-premises and online search results. Before you start the full crawl, we recommend that you create a new, separate Search Center. Set it up to show the mixed on-premises and online search results. This way you can validate and tune the new search experience in the separate Search Center, while you keep the **existing** Search Center unchanged. 
  
Follow these steps to set up a separate Search Center in Office 365:
  
1. [Create a result source](/sharepoint/manage-result-sources) that retrieves search results from the search index of this tenant, but limits search results to Office 365 content by using a **Query Transform**. Change the default query transform to "{?{searchTerms} NOT IsExternalContent:true}". This works because content that has the managed property  *IsExternalContent*  set to true (see [About the IsExternalContent managed property](configure-cloud-hybrid-searchroadmap.md#BKMK_IsExternalContent)) in the SharePoint Online search schema, is on-premises content.
    
2. Modify the Search Results Web Part in your Office 365 Search Center to use the result source that you just created. Your users get the original search experience in this Search Center.
    
3. Create a second Office 365 Search Center that uses the default result source. This Search Center has hybrid search results when you've run a full crawl. Validate and tune your new search experience in this Search Center.
    
4. Set up access so only testers and administrators have access to the second Office 365 Search Center.
    
Here's an example of a validation environment:
![The illustration shows how content enters the Office 365 index from both a SharePoint Server content farm and from Office 365. The standard search center in Office 365 only retrieves Office 365 results from the search index, while the validation search ce](../media/9f9528f3-ee79-46b2-8113-d7b10be675ba.png)
  
1. On-premises content. During crawl, content is added to the Office 365 index.
    
2. Office 365 content. During crawl, content is added to the Office 365 index.
    
3. Default (or existing) Office 365 Search Center. This Search Center uses the custom result source that limits search results to only Office 365 content.
    
4. Second Office 365 Search Center, where you validate and tune how hybrid search results are shown. This Search Center uses the default result source and shows search results from both on-premises and Office 365 content.
    
### About the IsExternalContent managed property
<a name="BKMK_IsExternalContent"> </a>

An important part in this environment is the custom result source you use in the default or existing Office 365 Search Center. This result source keeps the search experience unchanged while you validate and tune how hybrid search results are displayed. An important piece in this custom result source is the  *IsExternalContent*  managed property in the SharePoint Online search schema. Before you set up cloud hybrid search, this managed property is empty. But, after you've set up cloud hybrid search and crawled your on-premises content, this property is set to true for all on-premises content. You can therefore limit search results to show only Office 365 content with  *NOT IsExternalContent:true*  . 
  
## Start a full crawl of on-premises content for cloud hybrid search
<a name="BKMK_StartFullCrawl"> </a>

Start a full crawl of the content source. See [Start, pause, resume, or stop a crawl in SharePoint Server 2013](/SharePoint/search/start-pause-resume-or-stop-a-crawl) or follow these steps: 
  
1. Verify that the user account that is performing this procedure is an administrator for the Cloud Search service application.
    
2. On the home page of the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**. 
    
3. On the Manage Service Applications page, click the cloud Search service application.
    
4. On the Search Administration page, in the **Crawling** section, click **Content Sources**. 
    
5. On the Manage Content Sources page, in the list of content sources, point to the name of the content source that you want to crawl, click the arrow and then click **Start Full Crawl**. The value in the **Status** column changes to **Crawling Full** for the selected content source. 
    
## Verify that cloud hybrid search works
<a name="BKMK_VerifyCloudHybridSearch"> </a>

After the full crawl completes, verify that your on-premises content shows up in the search results in your validation Search Center in Office 365.
  
1. Log in to Office 365 with your work or school account. Make sure that:
    
  - You have access to the validation Search Center.
    
  - You have access to the content in the content source that you have crawled. If you performed step 1 of this roadmap, you should have access.
    
  - Your organization hasn't assigned user access rights to the on-premises content by using one of the default security groups in Windows Server Active Directory (AD), for example the Domain Users security group, see [Plan cloud hybrid search for SharePoint](/SharePoint/hybrid/plan-cloud-hybrid-search-for-sharepoint).
    
2. Search for **IsExternalContent:1** in the validation Search Center. The results you get should show content from the on-premises content source that you've crawled. 
    
3. Verify that your on-premises content shows up in the search results.
    
## Tune cloud hybrid search
<a name="BKMK_TuneCloudHybridSearch"> </a>

After you've set up cloud hybrid search and verified that you get search results from on-premises content in your validation Search Center in Office 365, set up the search experiences that you planned.
  
You might find this guidance useful:
  
- With cloud hybrid search you manage the search schema in SharePoint Online in Office 365, just as you would in an Office 365 environment. Learn how in [Manage the Search Center in SharePoint Online](/sharepoint/manage-search-center).
    
- You manage how search results are displayed from the search schema in SharePoint Online, see [Manage the Search Center in SharePoint Online](/sharepoint/manage-search-center). If you've set up site search in SharePoint Server to get search results the Office 365, you also manage how these results are displayed from the search schema in SharePoint Online.
    
- [Enable previews of on-premises search results in cloud hybrid search](enable-previews-of-on-premises-search-results-in-cloud-hybrid-search.md) . 
    
- [Show results from Office 365 in on-premises SharePoint with cloud hybrid search](show-results-from-office-365-in-on-premises-sharepoint-with-cloud-hybrid-search.md) . 
    
- To publish your SharePoint Server site and make it accessible for your users, follow the best practices in Plan for Internet, intranet, and extranet publishing sites in SharePoint Server
    
- To open a link from a search result that comes from on-premises content, users have to either be connected to the on-premises intranet via a Virtual Private Network (VPN) connection or be logged on to where the content is stored. Alternatively, you enable users to open such links by [installing a reverse proxy device](/SharePoint/hybrid/configure-a-reverse-proxy-device-for-sharepoint-server-hybrid) for SharePoint Server. 
    
After setting up and validating the planned search experiences, you might want to clear your search index in Office 365 for metadata from the on-premises content you've used during this work. This works differently from what you might be familiar with from SharePoint Server.
  
In the SharePoint Central Administration website you can use the option "Index reset" for an SSA to remove all content from the search index. This option does not work for cloud hybrid search because there is no direct communication between the cloud SSA in SharePoint Server and the search index in Office 365. If you only want to remove some on-premises metadata, remove that on-premises content source, or create a crawl rule that doesn't crawl the URL of a file. If you need to remove all metadata from on-premises content from the search index in Office 365, open a ticket with [Microsoft Support](https://support.microsoft.com/en-us/assistedsupportproducts).

## Proxy Considerations
<a name="BKMK_SearchProxy"> </a>

If the SharePoint farm is behind a forward proxy (that is, traffic destined for the Internet must be sent through a proxy server), it may be necessary to configure additional proxy settings. Follow the steps outlined in [Configure proxy server settings for Search in SharePoint Server](../search/configure-proxy-server-settings-for-search.md).

In addition, it may be necessary to configure the `machine.config` to support the proxy. This file resides at `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\machine.config`. More information on configuring the appropriate element can be found at [Network Settings Schema](/dotnet/framework/configure-apps/file-schema/network/defaultproxy-element-network-settings).
  
## Related Topics
<a name="BKMK_TuneCloudHybridSearch"> </a>

[Learn about cloud hybrid search for SharePoint](/SharePoint/hybrid/learn-about-cloud-hybrid-search-for-sharepoint)
  
[Plan cloud hybrid search for SharePoint](/SharePoint/hybrid/plan-cloud-hybrid-search-for-sharepoint)
  

