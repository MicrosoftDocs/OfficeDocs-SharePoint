---
title: Yammer networks, groups, and users overview
ms.prod: SHAREPOINT
ms.assetid: 85ba39ff-5dd3-4a88-98c2-5ec9d6928d2e
---


# Yammer networks, groups, and users overview
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, Yammer Enterprise*  * **Topic Last Modified:** 2016-09-16* **Summary:** Learn about the roles of networks, groups, and users in Yammer.This article describes Yammer networks, groups, and users, which together serve as a foundation for providing you with a rich Yammer experience within SharePoint.Yammer supports both internal and external networks. An internal network is restricted to users inside the organization, while an external network is open to users outside the organization’s domain. Users in external networks must be invited. External networks are considered extensions of, and are always associated with, a single internal network.An internal network is associated with one primary domain. Yammer creates a network for the primary email domain in your organization so that when users log on, they’re routed to the same Yammer network as their email domain. Only people with a valid organization email address can join the organization’s network. For example, in the following diagram, Jane is in the contoso.com network, and John is in the northwindtraders.com network. They can both log on as guests to sites in the external networks for both organizations. But they can only log on as users in their internal networks. **Yammer networks and users**
  
    
    
![Yammer networks, groups, and users diagram](images/)
  
    
    
For organizations with multiple email domains, the Yammer network is associated with only one domain. Users with email addresses from valid alternate domains within that organization can still log on by using their alternate domain email address. For example, Coho Vineyard and Winery might have one domain for the parent organization, cohovineyardandwinery.com, and separate domains for each division, cohovineyard.com and cohowinery.com. The Yammer network is associated with the domain cohovineyardandwinery.com, but users can log on with their separate cohovineyard.com or cohowinery.com email address.
## Yammer networks

Yammer offers two types of networks to help users communicate and collaborate in the most convenient and effective ways possible:
- **Internal network:** Also known as a *home network*  . This is a private collaboration space where organization employees can connect with their coworkers. Only employees with a valid corporate email address can join the internal network and access its content and users. Users from one internal network can't view the content or interact with users from another network unless they have a valid email address for that network. Messages posted within your internal network are owned by your organization and cannot be shared externally. Administrators can invite external users as guests to the internal network.
    
  
- **External network:** A separate extension of your internal network. It includes invited users from outside your organization. It’s a private collaboration space for your organization to engage with outside partners, like customers, suppliers, or investors. Although external networks can accommodate users who have different email domains, access is by invitation only.
    
  

## Yammer groups

By using Yammer groups, you can create a workspace dedicated to a certain topic, like a functional team within your organization, a project taskforce, or a group of people with a shared interest. By using Yammer groups, a team can collaborate and seamlessly share information, such as documents, notes, and links. Yammer has two types of groups:
- By using **public groups**, anyone in the network can view content and participate in the group activity. By default, Yammer groups are public.
    
  
- By using **private groups**, you can limit membership and participation to invitation or approval only from group administrators. You can hide private groups from the group’s directory.
    
  

> [!NOTE:]

  
    
    


## Yammer users

Users are the core of the enterprise social network, and there are multiple ways to add them to Yammer.
1. Add users individually or in bulk from the Yammer **Admin** page.
    
  
2. Use Yammer Active Directory Sync to automate the provisioning and de-provisioning of users by syncing data with the organization directory.
    
  
3. Integrate Yammer with your organization’s single sign-on (SSO) portal, which stores the different URLs, user names, and passwords for your enterprise apps for convenient and more secure access.
    
  
Yammer users exist in a limited number of states, as shown in the following diagram: **Yammer user states**
  
    
    
![Yammer user states diagram](images/)
  
    
    

### Table: Yammer user states

User stateDescriptionPending  <br/> Invited users who are not yet active. Pending users can be activated or deleted.  <br/> Active  <br/> Users that have joined the network and that can use Yammer features. Active users can be suspended or deleted.  <br/> Suspended  <br/> Users can be deactivated either through the **Admin** page or directory sync. Suspended users can be reactivated or deleted. <br/> Deleted  <br/> After some time, the state of the user account changes from Suspended to Deleted. If a user is deleted, you can invite or add the email address again, and the user is pending until activated.  <br/> 
# See also

#### 

 [Integrate Yammer with on-premises SharePoint 2013 environments](html/integrate-yammer-with-on-premises-sharepoint-2013-environments.md)
  
    
    
 [Social scenarios with Yammer and SharePoint Server 2013](html/social-scenarios-with-yammer-and-sharepoint-server-2013.md)
  
    
    

  
    
    

