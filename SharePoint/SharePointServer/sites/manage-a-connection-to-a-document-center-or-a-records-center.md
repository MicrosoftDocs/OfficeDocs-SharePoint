---
title: "Manage a connection to a document center or a records center in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SharePoint_Online
ms.assetid: 5f0402ca-90c6-4528-b1de-04d4f28fb2a6
description: "How to connect a web application to a SharePoint Server document center or records center and how to modify and delete connections."
---

# Manage a connection to a document center or a records center in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
A connection is a path used for sending documents to a document center or a records center. The connection specifies the web application that documents will be sent from, the document center or records center that they will be sent to, and certain aspects of how the documents are sent. A records center is a site that is designed for records management.
  
Connections are created by a farm administrator in SharePoint Server. The farm administrator configures the connection to copy content, to move content, or to move the content and leave a link in the source site collection. 
  
    
> [!NOTE]
> The destination document or record center must already exist before you perform the procedures for this task. You also need the URL of the destination document or record center for the procedures in this article. 
  
## Create a connection
<a name="section1"> </a>

Use this procedure to create a connection to a document repository or a records center.
  
### To create a connection

1. To create a connection, you must be a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **General Application Settings** and in the **External Service Connections** section, select **Configure Send To Connections**.
    
3. On the **Configure Send To Connections** page, in the **Web Application** field, select the web application that hosts the site collections from which documents will be sent. 
    
4. In the **Tenant Settings** section, select **Allow sites to send to connections outside their tenancy** if you want tenants on this farm to able to send content to other tenants on this farm. 
    
5. In the **Send To Connections** list, select **New Connection**.
    
6. In the **Display name** field, type a name for this connection. This is the name that users will see as one of the options to which to send a document. 
    
7. In the **Send to URL** field, enter the URL to the Content Organizer for the destination site. (To find the correct URL go to the **Site Settings** page, in the **Site Administration** section, click **Content Organizer Settings**, and then look in the **Submission Points** section of the **Content Organizer : Settings** page of the destination repository.) Use **Click here to test** if you want to confirm that you have entered a URL to a Content Organizer. 
    
8. To display this connection in the list that appears when a user clicks **Send To**, select **Allow manual submission from the Send To menu**.
    
9. In the **Send To action** list, select one of the following values: 
    
   - **Copy** Select this option to create a copy of the document and send the copy to the destination repository. 
    
   - **Move** Select this option to delete the document from its current location and move the document to the destination repository. Users will no longer be able to access the document from its original location. 
    
   - **Move and Leave a Link** Select this option to delete the document from its current location, move it to the destination repository, and leave a link at the current location indicating that the document has been moved. When a user clicks this link, a page will appear that displays the URL of the document and the document's metadata. 
    
10. In the **Explanation** dialog box, type the information to be added to the audit log when the user sends a document by using this connection. If you selected **Move and Leave a Link** in the previous step, the page that appears when the user clicks the link will also display the explanation. 
    
11. Click **Add Connection** to create the connection, and then click **OK** when you are finished configuring connections. 
    
> [!NOTE]
> The **Allow sites to send to connections outside their tenancy** option applies to all site subscription connections in a web application, and is not used when you add, modify, or delete a single connection. 
  
## Modify a connection
<a name="section2"> </a>

Use this procedure to modify an existing connection to a document repository or a records center.
  
### To modify a connection

1. To modify a connection, you must be a member of the Farm Administrators group.
    
2. On the Central Administration website, click **General Application Settings**, and select **Configure Send To Connections**.
    
3. On the **Configure Send To Connections** page, in the **Web Application** field, select the web application that contains the site collections that use this connection. 
    
4. In the **Send To Connections** list, select the connection that you want to modify. 
    
5. Modify any of the connection settings as described in the previous procedure.
    
6. Click **Update Connection** to modify the connection, and then click **OK** when you are finished configuring connections. 
    
## Delete a connection
<a name="section3"> </a>

Use this procedure to delete an existing connection to a document repository or a records center.
  
### To delete a connection

1. To delete a connection, you must be a member of the Farm Administrators group.
    
2. On the Central Administration website, click **General Application Settings**, and select **Configure Send To Connections**.
    
3. On the **Configure Send To Connections** page, in the **Web Application** field, select the web application that contains the site collections that use this connection. 
    
4. In the **Send To Connections** list, select the connection that you want to delete. 
    
5. Click **Remove Connection** to delete the connection, and then click **OK** when you are finished configuring connections. 
    
## See also
<a name="section3"> </a>

#### Concepts

[Manage site collections in SharePoint Server](manage-site-collections.md)
#### Other Resources

[Manage site collections and global settings in the SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=845346)

