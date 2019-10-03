---
title: "Configure and use the Exchange connector for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/6/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: ffec2e36-9142-45ae-866e-308d6efbc114
description: "Learn how to create a crawl rule and add a content source to crawl Exchange Server public folders."
---

# Configure and use the Exchange connector for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information about prerequisites:
  
- Create a Search service application
    
- Ensure that the crawler has at least Read permission to the Exchange Server public folder.
    
## Create a crawl rule
<a name="proc1"> </a>

This following procedure describes how to create a crawl rule. You must create a crawl rule if the default content access account does not have Read permission to the Exchange Server public folders that you want to crawl.
  
 **To create a crawl rule**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the Application Management section, click **Manage Service Applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click the Search service application.
    
4. On the Search Administration page, in the Crawling section, click **Crawl Rules**. 
    
5. On the Manage Crawl Rules page, click **New Crawl Rule**. 
    
6. On the Add Crawl Rule page, in the **Path** section, in the **Path** box, type the path to which the crawl rule will apply. You can use standard wildcard characters in the path. 
    
    > [!NOTE]
    > When creating a crawl rule, the URL that you type inside the **Path** box should be in the following form:  _\<protocol\>://hostname/\*_where  _\<protocol\>_ is the protocol that you want to use (typically http or https), and  _hostname_ is the NetBIOS or fully qualified domain name of the server that is running Exchange Server. 
  
7. In the **Crawl Configuration** section, select **Include all items in this path**.
    
8. In the **Specify Authentication** section, select the type of crawl authentication to use. This section is available only if **Include all items in this path** is selected. 
    
9. Click **OK**.
    
## Add a content source for Exchange Server public folders
<a name="proc2"> </a>

Use one of the following procedures to create a content source for Exchange Server public folders. Which procedure you should follow depends on the Exchange Server version. You can choose to add a content source to crawl public folders in: 
  
- Exchange Server 2007 and Exchange Server 2007 with Service Pack 1 (SP1)
    
- Exchange Server 2007 with Service Pack 2 (SP2) and Exchange 2010
    
### To add a content source for Exchange Server 2007 and Exchange Server 2007 SP1 public folders

1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. On the SharePoint Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, click the Search service application.
    
4. On the Search Administration page, in the **Crawling** section, click **Content Sources**.
    
5. On the Manage Content Sources page, click **New Content Source**.
    
6. On the Add Content Source page, in the **Name** box, type a name for the new content source. 
    
7. In the **Content Source Type** section, select **Exchange Public Folders**.
    
8. In the **Start Addresses** section, in the **Type start addresses below (one per line)** box, type the URLs for the Exchange Server public folders that you want to crawl. These URLs are typically in one of the following forms: 
    
  -  _\<protocol\>_:// _host name_/public
    
    Where  _\<protocol\>_ can be http or https, and  _host name_ is the NetBIOS or fully qualified domain name (FQDN) of the server that is running Exchange Server. 
    
  -  _\<protocol\>_:// _host name_/public/ _subfolder_
    
    Where  _\<protocol\>_ can be http or https,  _host name_ is the NetBIOS or FQDN of the server that is running Exchange Server, and  _subfolder_ is the name of the specific subfolder that you want to crawl. 
    
  For example, if you want to crawl all subfolders in the public folder on a server that is named exch-01 and that is in the Contoso domain, and that server does not use SSL, you could type either http://exch-01/public or http://exch-01.contoso.com. To crawl only a specific subfolder named Bob in the same public folder, type http://exch-01/public/bob or http://exch-01.contoso.com/bob.
    
  > [!NOTE]
  > For performance reasons, you cannot add the same start addresses to multiple content sources. 
  
9. In the **Crawl Settings** section, select the crawling behavior that you want. 
    
10. In the **Crawl Schedules** section, you can choose to specify when to start full and incremental crawls: 
    
  - To create a full crawl schedule, click the **Create Schedule** link below the **Full Crawl** list. 
    
  - To create an incremental crawl schedule, click the **Create schedule** link below the **Incremental Crawl** list. 
    
11. Click **OK**.
    
### To add content sources for Exchange Server 2007 SP2 and Exchange 2010 public folders

1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. Open a web browser and go to the Outlook Web Access webpage for the Exchange Server that contains the public folders that you want to crawl.
    
3. Log on to Outlook Web Access using any user account that has Read permissions on the public folders that you want to crawl.
    
4. Go to the public folder that you want to crawl, right-click the folder, and then select **Open in New Window**.
    
5. When the new window opens, go to the address bar and copy the complete URL. This is the Outlook Web Access public folder address.
    
6. On the SharePoint Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
7. On the Manage Service Applications page, click the Search service application.
    
8. On the Search Administration page, in the **Crawling** section, click **Content Sources**.
    
9. Click **New Content Source**. 
    
10. On the Add Content Source page, in the **Name** box, type a name for the new content source. 
    
11. In the **Content Source Type** section, select **Exchange Public Folders**.
    
12. In the **Start Addresses** section, paste the Outlook Web Access public folder address that you copied in step 5. 
    
13. In the **Crawl Settings** section, select the crawling behavior that you want. 
    
14. In the **Crawl Schedules** section, you can choose to specify when to start full and incremental crawls: 
    
  - To create a full crawl schedule, click the **Create Schedule** link below the **Full Crawl** list. 
    
  - To create an incremental crawl schedule, click the **Create schedule** link below the **Incremental Crawl** list. 
    
15. Click **OK**.
    

