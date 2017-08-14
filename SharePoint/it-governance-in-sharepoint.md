---
title: IT governance in SharePoint
ms.prod: SHAREPOINT
ms.assetid: 7c75dc80-6910-4c10-a9a0-d821bedd602d
---


# IT governance in SharePoint
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013*  * **Topic Last Modified:** 2017-07-19* **Summary:** Learn about key factors in governing a SharePoint 2013 service and what to include in a service-level agreement.How will you control the services that you offer? What will you provide with each service? What will you include in service-level agreements for each service? And how do you prevent proliferation of unmanaged servers? These questions should be answered as part of your IT governance plan. We recommend that you develop a good governance plan when you create an IT service to support SharePoint. A good governance plan ensures that the service meets the business needs of your organization securely and cost-effectively. When you add to the service, a good governance plan helps you do so seamlessly. A good governance plan to run a successful IT service should include the following elements:
### 

IconElement![Users icon](images/) <br/> A  [governance team](what-is-governance-in-sharepoint.md#GovernanceTeam) defines the initial offerings of the service and its ongoing policies, and meets regularly to evaluate success. <br/> ![Policy icon](images/) <br/> The policies you develop are communicated to your organization and are enforced.  <br/> ![Install icon](images/) <br/> Users are encouraged to use the service and not create their own solutions. Installations are tracked and rogue installations are blocked.  <br/> 
### 

![Foundation icon](images/) This article is part of a set of articles about governance. The following articles describe other aspects of governance: <br/>  [What is governance in SharePoint?](html/what-is-governance-in-sharepoint.md) <br/> **Information management and governance in SharePoint** <br/>  [Application management and governance in SharePoint](html/application-management-and-governance-in-sharepoint.md) <br/>  The What is governance? poster gives a summary of this content. Download the [PDF version](https://go.microsoft.com/fwlink/?LinkId=331051) or [Visio version](https://go.microsoft.com/fwlink/?LinkId=331050), or  [Zoom into the model in full detail with Zoom.it from Microsoft](https://go.microsoft.com/fwlink/?LinkId=331052).  <br/> 
## What is a SharePoint service?
<a name="Section1"> </a>

A SharePoint service is an IT service that offers hosted sites based on SharePoint. The benefits of a SharePoint service include backup and recovery, content storage, support for customizations, security, and service levels based on speed and availability as show in the following illustration.
  
    
    
![Elements of a SharePoint service](images/)
  
    
    

  
    
    

  
    
    

## Elements of a successful service
<a name="Section2"> </a>

As you plan and implement your SharePoint service, consider the following elements that can contribute to the success of the governing effort:
- **Form and use a governing group.**    Your IT service for SharePoint should be governed by a group that includes executive stakeholders, business division leaders, influential information workers, IT managers, and IT technical specialists, among others. The goal of the governing group should be to oversee the service. In this capacity, the governing group defines the initial offerings of the service, defines the service's ongoing policies, and meets regularly to evaluate success.
    
  
- **Communicate the policies.**    The governance policies that you develop must be publicized to your organization. Maintain a website that describes the service.
    
  
- **Encourage use of the service.**    Discourage or block users from deploying their own servers. Instead, encourage them to use the service. Isolated servers may not be configured according to IT security policy and the organization’s regulatory requirements. Furthermore, users who deploy their own servers may not properly back up their servers or keep servers up-to date with software patches and updates. Finally, content on servers that are not governed by the service may not be detected by the organization’s indexing service, which may create isolated pockets of content.
    
  

## What to govern in a SharePoint service
<a name="Section3"> </a>

Determine limits and policies for the areas shown in the following table.
### Areas that should have limits or policies in a governance plan

AreaRecommendationSecurity, infrastructure, and  [web application policies](html/manage-permission-policies-for-a-web-application-in-sharepoint-server.md) <br/> How is the system and infrastructure maintained and who has access at what levels? What’s the maximum upload size you want to allow? Are you controlling the use of **fine-grained permissions** ? <br/> Data protection ( [backup and recovery](html/overview-of-backup-and-recovery-in-sharepoint-server.md))  <br/> Vary the level of data protection that you offer based on service levels. Plan how often you back up the farms and how quickly you can guarantee the data is restored.  <br/> Site policies  <br/> Use  [site policies](html/overview-of-site-policies-in-sharepoint-server.md) to help control site proliferation. A site policy defines the life cycle of a site by specifying when the site will be closed and when it will be deleted. When you close or delete a site, any subsites are also closed or deleted. If an Exchange mailbox is associated with a site, the mailbox is deleted from Exchange Server 2013 when the site is deleted. <br/> Quotas  <br/>  [Quota templates](html/create-edit-and-delete-quota-templates-in-sharepoint-server.md) define how much data can be stored in a site collection and the maximum size of uploaded files. Associate different quota templates with site collections at different service levels. <br/> Asset classification  <br/>  Classify sites and content by value and impact of the content to the organization (such as high, medium, or low business value/impact). That classification then controls other requirements, such as encryption for high business impact information. <br/>  Impact = Exposure <br/>  If this leaks, will it hurt my business? <br/>  Value = Availability <br/>  If this isn’t available, can my business run? <br/> 
## Service-level agreements
<a name="SLA"> </a>

Your organization should create appropriate service-level agreements for each service you provide. A good service-level agreement should include:
- The approval process, including the length of time and approvals necessary to create a site.
    
  
- Costs for users or departments.
    
  
- Operations-level agreement, which specifies which teams perform which operations and how frequently.
    
  
- Policies around problem resolution through a support team.
    
  
- Negotiated performance targets for first load of a site, subsequent loads, and performance at remote locations.
    
  
- Recovery, load balancing, and failover strategies.
    
  
- Customization policies.
    
  
- Storage limits for content and sites.
    
  
- How to handle inactive or stale sites.
    
  
- Multilingual support.
    
  

## Deployment governance
<a name="SLA"> </a>

In addition to governing services that you offer, you also need to govern installations of SharePoint in your environment.
- **Track installations**    An Active Directory Domain Services (AD DS) marker named Service Connection Point identifies the SharePoint servers in an organization. Set this marker for each domain in your organization if you want to track installations in all domains. See [Track or block SharePoint Server 2010 installations](https://go.microsoft.com/fwlink/?LinkId=403888).
    
  
- **Block installations**    You can block installations of SharePoint Server 2016 to prevent users from installing it to unauthorized servers that you don’t want to support. Use a Group Policy in Active Directory Domain Services (AD DS) to set a registry key on all servers to block installations. This registry key existed by default in SharePoint Server 2010, but is not included in SharePoint Server 2016. You can create it yourself in the registry if you want to block installations. See **Track or block SharePoint Server 2010 installations**.
    
  
- **Keep current with software updates**    Keep your servers current. Test and install recommended software updates. See the [Updates Resource Center](https://go.microsoft.com/fwlink/?LinkId=330874) for SharePoint Server 2016.
    
    
    
  
- **Site collection upgrades**    Site collections can now be upgraded independently from the content databases. Determine who, when, and how to upgrade site collections when a new version or an update is available. See **Plan for site collection upgrades in SharePoint 2013**.
    
  

# See also

#### 

 [What is governance in SharePoint?](html/what-is-governance-in-sharepoint.md)
  
    
    
 [Application management and governance in SharePoint](html/application-management-and-governance-in-sharepoint.md)
  
    
    

#### 

 **Governance planning in SharePoint**
  
    
    
 **Information management and governance in SharePoint**
  
    
    
 [SharePoint - Sample Service Level Agreement (SLA) - "From the Field" blog (https://go.microsoft.com/fwlink/p/?LinkId=203973)](https://go.microsoft.com/fwlink/p/?LinkId=203973)
  
    
    
 [Sample template: SharePoint products and technologies governance plan (http://go.microsoft.com/fwlink/p/?LinkID=162169)](http://go.microsoft.com/fwlink/p/?LinkID=162169&amp;clcid=0x409)
  
    
    
 [What is governance poster (Visio format)](https://go.microsoft.com/fwlink/?LinkId=331050)
  
    
    
 [What is governance poster (PDF format)](https://go.microsoft.com/fwlink/?LinkId=331051)
  
    
    

  
    
    

