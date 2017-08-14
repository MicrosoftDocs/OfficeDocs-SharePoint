---
title: The unattended Service Account Application ID is not specified or has an invalid value (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: ec3a8cb2-141f-4c4b-a3c3-068ea89121cf
---


# The unattended Service Account Application ID is not specified or has an invalid value (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The Unattended Service Account Application ID is not specified or has an invalid value" for SharePoint Server 2016. **Rule name:**    The Unattended Service Account Application ID is not specified or has an invalid value. **Summary:**    The Unattended Service Account Application ID setting stores an application identifier (ID) in the registered Secure Store Service. The application ID is used to reference the Unattended Service Account credentials. The Unattended Service Account is a single, low-privileged account that Visio Graphics Service impersonates when it connects to data sources external to SharePoint Server 2016, such as SQL Server. This account is required to connect to these external data sources. For more information about Visio Graphics Service, see [Plan for Visio Services in SharePoint Server](html/plan-for-visio-services-in-sharepoint-server.md) and [Plan Visio Services security in SharePoint Server](html/plan-visio-services-security-in-sharepoint-server.md). **Resolution:   Specify a valid application ID value**
1. Verify that the user account that is performing this procedure is an administrator of the Visio Graphics Service service application and the Secure Store Service service application.
    
  
2. In Central Administration, on the Home page, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Service Applications page, click the Secure Store Service service application.
    
  
4. On the Secure Store Service page, record the application ID from the **Target Application ID** column.
    
    For more information about the Secure Store Service service application, see  [Plan the Secure Store Service in SharePoint Server](html/plan-the-secure-store-service-in-sharepoint-server.md).
    
  
5. On the Service Applications page, click the Visio Graphics service application.
    
  
6. On the Manage the Visio Graphics Service page, click **Global Settings**.
    
  
7. On the Visio Graphics Service Settings page, in the **External Data** section, in the **Unattended Service Account** text box, type the application ID that you recorded in step 4 of this procedure.
    
  
8. Click **OK**.
    
  

