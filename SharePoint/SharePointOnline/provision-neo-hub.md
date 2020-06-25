---
title: Add and customize the New employee onboarding hub
ms.reviewer: 
ms.author: hokavian
author: hokavian
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:  
- Strat_SP_modern
- M365-collaboration
search.appverid:
- SPO160
- MET150
description: "Learn how to add and customize the NEO hub to your tenant"
---

##Overview of the Microsoft Open Source New Employee Onboarding Hub 
Microsoft has created an open source New Employee Onboarding (NEO) Hub to help organizations improve their onboarding process and help realize the benefits of a well-thought out and supported new employee onboarding experience. The NEO Hub helps organizations: 

•	Provide new employee experiences and information
•	Connect new employees to people & culture
•	Help stakeholders easily contribute to new employee onboarding
•	Measure effectiveness of new employee onboarding

###Why invest in a new employee onboarding site?
New employee onboarding (NEO) should be a strategic process that integrates new employees into an organization and its culture while providing the knowledge and tools needed to become fully contributing team members. 
NEO processes often fall short for both the new hires and the organization. Only 12% of employees strongly agree their organization does a great job of onboarding new employees.   An engaging and well organized NEO process can make all the difference in helping a new hire navigate through an exciting – but stressful -  career journey, and it can have major organizational benefits. 

Strategically planned NEO experience can:

**Improve new hire performance and time to productivity**
Organizations with a standard onboarding process report 50% greater new-hire productivity.   

**Improve new employee retention**
69% of employees are more likely to stay with a company for three years if they had a great onboarding experience. Employees who have a negative onboarding experience are twice as likely to look for new opportunities in the near future.    

![Image of the neo experience overview](media/neoexperienceoverview.png)


###NEO Hub contents:

•	A fully configured and customizable set of new hire related sites built on SharePoint Online communication sites: The NEO Hub includes the sites, information architecture, design, user interface and features to help provide new hires with a great onboarding experience. The NEO Hub can be customized to add your organization’s new hire content and to align with its look and feel. The NEO Hub sites are responsive and work as they should on mobile. 
•	Onboarding journey: Onboarding can be an overwhelming experience for new hires with everything the new hire is typically expected to do and learn in a short period of time. Avoid overwhelming your new employees by providing them a curated onboarding journey that paces the new hire through a configurable activity list of administrative, technology, culture, training, and connection related to-do’s. The onboarding journey comes with a pre-configured list of new employee onboarding activities for you to customize for your processes. 
•	Sample new hire site pages: To inspire and provide design templates for arranging your content, the NEO Hub includes sample inner site pages. Use these site pages as templates for your content. 
•	Easy provisioning: Provision the NEO Hub from the SharePoint look book with just a few easy steps

###New hire sites 
New employee onboarding involves multiple levels within an organization, including corporate onboarding, and departmental onboarding. Sometimes teams within a department also need a unique onboarding experience. Each onboarding level provides its own unique value, contributing to a comprehensive onboarding experience each new employee should experience. 
Research has shown pre-onboarding new hires, after they sign their acceptance letter but before they officially join the company, can lead to higher performance and better retention rates. 
To deliver a consistent and integrated new hire onboarding experience the Microsoft open source New Employee Onboarding Hub consists of three types of SharePoint site templates, designed to work as one cohesive and familiar experience for new hires. 

![Image of the neo hub content](media/neotimeline.png)

1.	Pre-Onboarding site: A site for new hires, who have yet to officially join the company, to learn more about the company they have joined and to get ready for their official start date. External guest access can be used for providing pre-start hires, with no corporate credentials, access to the pre-onboarding site only. 
2.	Corporate onboarding site: A place for new hires to visit to get the information they need and make the connections they want to successfully onboard to the organization. 
3.	Departmental onboarding sites: A place for new hires to visit to learn more about the department they are joining, its people, culture, and priorities. The new employee onboarding hub includes two departmental template sites, one for an engineering department and one for a sale department


##Step 1: Provision NEO Hub
The New Employee Onboarding (NEO) Hub can be provisioned from the [SharePoint look book](https://lookbook.microsoft.com/). With the SharePoint look book, an Office 365 Tenant Administrator can start the provisioning process with a few simple clicks. It is fast, easy, and takes only a few minutes to start the process. Before starting the provisioning process, make sure you have met the prerequisites for provisioning.
Prerequisites
To successfully set up the NEO Hub via the SharePoint look book, the person doing the provisioning must meet the following pre-requisites:
•	The person provisioning the NEO Hub must be a Tenant Administrator of the tenant where the NEO Hub will be provisioned.


###Provision the NEO Hub
1.	Go to the [NEO Hub solution page](https://provisioning.sharepointpnp.com/details/3df8bd55-b872-4c9d-88e3-6b2f05344239).
2.	Select **Add to your tenant**. If you are not signed into to your tenant, the SharePoint look book will ask for your Tenant Admin credentials.
3.	From the permissions requested dialog box, select **Consent on behalf of your organization** and then select **Accept**.
The provisioning service requires these permissions to create the tenant app catalog, install the application into the tenant app catalog and provision the site template. There is no overall impact on your tenant and these permissions are explicitly used for the purpose of the solution installation. You must accept these permissions to proceed with the installation.
4.	Complete the fields on the provisioning information page as appropriate for your installation. At a minimum enter the email address where you wish to get notifications about the provisioning process and the destination URL for your site to be provisioned to.

> [!NOTE]
> Make the destination URL for your site something intuitive to your team members such as "/sites/MyTraining" or "/teams/LearnMicrosoft365".


6.	Select Provision when ready to install the NEO Hub into your tenant environment. The provisioning process will take up to 15 minutes. You will be notified via email (to the notification email address you entered on the Provisioning page) when the site is ready for access.


###Add Owners to the Site
As the Tenant Admin, it's unlikely you'll be the person customizing the sites, so you'll need to assign a few site owners to the sites. Owners have administrative privileges on the site so they can modify site pages, content, and rebrand the site. 
1.	From the SharePoint Settings menu, select Site Permissions.
2.	Select **Advanced Permission Settings**.
3.	Select **Microsoft 365 learning pathways Owners**.
4.	Select **New > Add Users to this group**, and then add the people you want to be site owners.
5.	Include the site URL in the Share message, and then select **Share**.
