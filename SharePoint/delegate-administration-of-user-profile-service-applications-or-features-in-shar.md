---
title: Delegate administration of User Profile service applications or features in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 9136a204-9877-4591-a7e5-0cdeda60114e
---


# Delegate administration of User Profile service applications or features in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-08-01* **Summary:** Learn how to delegate administration of a User Profile service application or selected features of a User Profile service application in SharePoint Server 2013 and SharePoint Server 2016.Farm administrators can delegate administration of either a User Profile service application or selected features of a User Profile service application to a service application administrator. A service application administrator can, in turn, delegate administration of a feature or features of a User Profile service application to another user, who is known as a feature administrator. A feature administrator can perform all administrative tasks that are related to the delegated feature or features. A feature administrator cannot manage other features, service applications, or settings that are contained in Central Administration.The following User Profile features can be configured for administration independently of each other:
- Profiles
    
  
- Audiences
    
  
- Permissions
    
  
- Retrieve people data for search crawlers
    
  
- Social data
    
  

## Delegate administration of a User Profile service application
<a name="section1"> </a>

Use the following procedure to configure delegate administration of a User Profile service application. **To delegate administration of a User Profile service application**
1. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  
2. In the list of service applications, click the row for the user profile service application (but don't click the link).
    
  
3. On the **Service Applications** tab, in the **Operations** section, click **Administrators**.
    
  
4. On the **Administrators for User Profile Service Application** page, type or select a user or group account and then click **Add**.
    
  
5. In the **Permissions for Administrator:** box, check the feature or features for which you want to delegate administration, or check **Full Control** to delegate administration for the entire service application.
    
  
6. Click **OK**
    
  

# See also

#### 

 [Administer the User Profile service in SharePoint Server](html/administer-the-user-profile-service-in-sharepoint-server.md)
  
    
    
 [Overview of the User Profile service architecture in SharePoint Server](html/overview-of-the-user-profile-service-architecture-in-sharepoint-server.md)
  
    
    

  
    
    

