---
title: "Manage crawl rules in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 984e2448-e53a-4b4e-bd4a-4340213218a2
description: "Learn how to specify a content access account, create crawl rules to include or exclude directories, and prioritize crawl rules."
---

# Manage crawl rules in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can add a crawl rule to include or exclude specific paths when you crawl content. When you include a path, you can provide alternative account credentials to crawl it. In addition to creating or editing crawl rules, you can test, delete, or reorder existing crawl rules.
  
Use crawl rules to do the following:
  
- **Prevent content on a site from being crawled.** For example, if you created a content source to crawl **http://www.contoso.com**, but you do not want the search system to crawl content from the subdirectory **http://www.contoso.com/downloads**, create a crawl rule to exclude content from that subdirectory.
    
- **Crawl content on a site that would be excluded otherwise.** For example, if you excluded content from **http://www.contoso.com/downloads** from being crawled, but you want content in the subdirectory **http://www.contoso.com/downloads/content** to be crawled, create a crawl rule to include content from that subdirectory. 
    
- **Specify authentication credentials.** If a site to be crawled requires different credentials than those of the default content access account, create a crawl rule to specify the authentication credentials. 
    
You can use the asterisk (*) as a wildcard character in crawl rules. For example, to exclude JPEG files from crawls on **http://www.contoso.com**, create a crawl rule to exclude **http://www.contoso.com/\*.jpg**.
  
The order of crawl rules is important, because the first rule that matches a particular set of content is the one that is applied. 
  
    
## To create or edit a crawl rule
<a name="proc1"> </a>

1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click the Search service application.
    
4. On the Search Administration page, in the **Crawling** section, click **Crawl Rules**. The Manage Crawl Rules page appears.
    
5. To create a new crawl rule, click **New Crawl Rule**. To edit an existing crawl rule, in the list of crawl rules, point to the name of the crawl rule that you want to edit, click the arrow that appears, and then click **Edit**.
    
6. On the Add Crawl Rule page, in the **Path** section: 
    
  - In the **Path** box, type the path to which the crawl rule will apply. You can use standard wildcard characters in the path. 
    
  - To use regular expressions instead of wildcard characters, select **Use regular expression syntax for matching this rule**.
    
7. In the **Crawl Configuration** section, select one of the following options: 
    
  - **Exclude all items in this path**. Select this option if you want to exclude all items in the specified path from crawls. If you select this option, you can refine the exclusion by selecting **Exclude complex URLs (URLs that contain question marks (?))** to exclude URLs that contain parameters that use the question mark (?) notation. 
    
  - **Include all items in this path**. Select this option if you want all items in the path to be crawled. If you select this option, you can further refine the inclusion by selecting any combination of these options:
    
    **Follow links on the URL without crawling the URL itself**. Select this option if you want to crawl links contained within the URL, but not the starting URL itself.
    
    **Crawl complex URLs (URLs that contain a question mark (?))**. Select this option if you want to crawl URLs that contain parameters that use the question mark (?) notation.
    
    **Crawl SharePoint Server content as http pages**. Normally, SharePoint Server sites are crawled by using a special protocol. Select this option if you want SharePoint Server sites to be crawled as HTTP pages instead. When the content is crawled by using the HTTP protocol, item permissions are not stored.
    
8. In the **Specify Authentication** section, perform one of the following actions: 
    
    > [!NOTE]
    > This option is not available unless the **Include all items in this path** option is selected in the **Crawl Configuration** section. 
  
  - To use the default content access account, select **Use the default content access account**.
    
  - If you want to use a different account, select **Specify a different content access account** and then in the **Account** box, type the user account name that can access the paths that are defined in this crawl rule. Next, in the **Password** and **Confirm Password** boxes, type the password for this user account. To prevent basic authentication from being used, select the **Do not allow Basic Authentication** check box. The server attempts to use NTLM authentication. If NTLM authentication fails, the server attempts to use basic authentication unless the **Do not allow Basic Authentication** check box is selected. 
    
  - To use a client certificate for authentication, select **Specify client certificate**, expand the **Certificate** menu, and then select a certificate. 
    
  - To use form credentials for authentication, select **Specify form credentials**, type the form URL (the location of the page that accepts credentials information) in the **Form URL** box, and then click **Enter Credentials**. When the logon prompt from the remote server opens in a new window, type the form credentials with which you want to log on. You are prompted if the logon was successful. If the logon was successful, the credentials that are required for authentication are stored on the remote site.
    
  - To use cookies, select **Use cookie for crawling**, and then select **Obtain cookie from a URL** to obtain a cookie from a website or server. Or, select **Specify cookie for crawling**to import a cookie from your local file system or a file share. You can optionally specify error pages in the **Error pages (semi-colon delimited)** box. 
    
  - To allow anonymous access, select **Anonymous access**. 
    
9. Click **OK**.
    
## To test a crawl rule on a URL
<a name="proc2"> </a>

1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click the Search service application.
    
4. On the Search Administration page, in the **Crawling** section, click **Crawl Rules**.
    
5. On the Manage Crawl Rules page, in the **Type a URL and click test to find out if it matches a rule** box, type the URL that you want to test. 
    
6. Click **Test**. The result of the test appears below the **Type a URL and click test to find out if it matches a rule** box. 
    
## To delete a crawl rule
<a name="proc3"> </a>

1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click the Search service application.
    
4. On the Search Administration page, in the **Crawling** section, click **Crawl Rules**.
    
5. On the Manage Crawl Rules page, in the list of crawl rules, point to the name of the crawl rule that you want to delete, click the arrow that appears, and then click **Delete**.
    
6. Click **OK** to confirm that you want to delete this crawl rule. 
    
## To reorder crawl rules
<a name="proc4"> </a>

1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click the Search service application.
    
4. On the Search Administration page, in the **Crawling** section, click **Crawl Rules**.
    
5. On the Manage Crawl Rules page, in the list of crawl rules, in the **Order** column, specify the crawl rule position that you want the rule to occupy. Other values shift accordingly. 
    

