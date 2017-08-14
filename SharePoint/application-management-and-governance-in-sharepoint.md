---
title: Application management and governance in SharePoint
ms.prod: SHAREPOINT
ms.assetid: f8efdfaf-8ef6-445c-9fb9-8845667e478b
---


# Application management and governance in SharePoint
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013*  * **Topic Last Modified:** 2017-07-20* **Summary:** Learn how to govern applications for SharePoint 2013 by creating a customization policy and understanding the app model, branding, and life-cycle management.How will you manage the applications that are developed for your environment? What customizations do you allow in your applications, and what are your processes for managing those applications?For effective and manageable applications, your organization should consider the following:
-  [Customization policy](#Customization)   SharePoint Server 2016 includes customizable features and capabilities that span multiple product areas, such as business intelligence, forms, workflow, and content management. Customization can introduce risks to the stability, maintenance, and security of the environment. To support customization while controlling its scope, you should develop a customization policy.
    
  
-  [Life-cycle management](#Lifecycle)   Follow best practices to manage applications and keep your environments in sync.
    
  
-  [Branding](#Branding)   If you are designing an information architecture and a set of sites to use across an organization, consider including branding in your governance plan. A formal set of branding policies helps ensure that sites consistently use enterprise imagery, fonts, themes, and other design elements.
    
  
-  [Solutions or apps for SharePoint?](#SolutionsApps)   Decide whether a solution or an app for SharePoint would be the best choice for specific customizations.
    
  

### 

![Foundation icon](images/) This article is part of a set of articles about governance. The following articles describe other aspects of governance: <br/>  [What is governance in SharePoint?](html/what-is-governance-in-sharepoint.md) <br/>  [IT governance in SharePoint](html/it-governance-in-sharepoint.md) <br/> **Information management and governance in SharePoint** <br/>  The What is governance? poster gives a summary of this content. Download the [PDF version](https://go.microsoft.com/fwlink/?LinkId=331051) or [Visio version](https://go.microsoft.com/fwlink/?LinkId=331050), or  [Zoom into the model in full detail with Zoom.it from Microsoft](https://go.microsoft.com/fwlink/?LinkId=331052).  <br/> 
## Customization policy
<a name="Customization"> </a>

Determine the types of customizations you want to allow and how to manage them. Your customization policy should include:
- **Service-level descriptions**    What are the parameters for supporting and managing customizations in your environments? See [Service-level agreements](it-governance-in-sharepoint.md#SLA).
    
  
- **Guidelines for updating customizations**    How do you manage changes to customizations, and how do you roll out those changes to your environments? Consider ways to manage source code, such as a source control system and standards for documenting the code.
    
  
- **Processes for analyzing**    How do you understand whether a particular customization is working well in your environment, or how do you decide which ones to create, change, or retire?
    
  
- **Approved tools for customization**    Consider development standards, such as coding best practices and the tools that you will to use across your organization. For example, you should decide whether to allow the use of SharePoint Designer 2013 and [Design Manager](https://go.microsoft.com/fwlink/?LinkId=330805), and specify which site elements can be customized and by whom.
    
  
- **Process for piloting and testing customizations**    How do you test and deploy customizations? How many people should be in a pilot testing group? What are your standards for testing and validating customizations?
    
  
- **Who is responsible for ongoing support**    Who will be responsible for supporting customizations in your environments—individual teams or a central group?
    
  
- **Guidelines for packaging and deploying customizations**    Do you have individual packages for each, or do you include several in a feature or solution? Which customizations should be apps for SharePoint instead of solutions? How do you ensure that customizations in one environment do not affect the rest of your SharePoint implementation?
    
  
- **Specific policies regarding each potential type of customization**    What types of customizations do you allow?
    
    For more information about kinds of customizations and their potential risks, see the Customizations table later in this article. For more information about processes for managing customizations, see the white paper  [SharePoint Products and Technologies customization policy](https://go.microsoft.com/fwlink/p/?linkid=92311). Most of this content still applies to SharePoint Server 2016.
    
  
- **Policies around using the App Catalog and SharePoint Store** Which apps for SharePoint do you want to make available to your organization? Can users purchase apps directly? See [Solutions or apps for SharePoint?](#SolutionsApps) later in this article for more information.
    
  
The highly customizable design of SharePoint products enables you to provide the look, behavior, or functionality that meets your business needs. Customizations can introduce risk to your environment, whether that risk is to the environment’s performance, availability, or supportability. Conversely, a "no customizations" policy severely restricts your organization’s ability to take advantage of the SharePoint platform.All customizations are not the same. You must decide carefully which kinds of customizations to allow in your environment. You must ensure the customizations support the performance, availability, and supportability you want for your environment. Your governance policy should balance a level of acceptable risk against the business needs for your organization.What is considered a customization? All of the following are considered kinds of customizations in SharePoint products:
- **Configuration**    Using the SharePoint user interface to configure SharePoint products.
    
  
- **Branding**    Changing logos, styles, colors, master pages and page layouts, and so on to create a custom look for your SharePoint sites. See more about [branding](#Branding).
    
  
- **Custom code**    Using developer tools to add or change functionality in SharePoint products or to interact with other applications. Risk can vary depending on kind of functionality and level of trust (full trust solutions should be rarely used; consider apps for SharePoint first).
    
    > [!TIP:]
      
Some customizations have very little risk or impact on your environment. Others have the potential for much higher risk and impact. The following table provides examples of different kinds of customizations, the risk level associated with that kind of customization, and potential issues that you might face if you allow that kind of customization.
### Customizations

Risk levelTypes of customizations and examplesConsiderations or impactUnsupported/High  <br/> Unsupported customizations such as direct changes to the database schema or modifying files on the file system.  <br/>  Will not be supported through Microsoft Customer Support. <br/>  Will be unable to upgrade. <br/>  Do not use. <br/> Moderate to high  <br/> Creating applications that interact with or redirect actions in key pipelines, such as events, claims, and so on.   <br/>  Potential for service outage or performance issues. <br/>  Might require rework at upgrade. <br/> Moderate to low  <br/> Using a custom Web Part outside a sandbox environment, creating custom actions such as adding a menu item, or creating a custom site provisioning process.  <br/>  Short or long-term performance issues or page errors. <br/>  Might require rework at upgrade. <br/> Low  <br/> Using solutions in a sandbox environment.  <br/> Short-term performance issues; you can avoid some performance issues by using resource throttling and quotas.  <br/> Very low to no risk  <br/> Using apps for SharePoint or using functionality within the product or configurations, such as associating a workflow with a list or using an instance of a built in Web Part.  <br/> Minor configuration or page errors that would have to be addressed. Apps can be uninstalled or updated.  <br/> 
> [!NOTE:]

  
    
    

Also, when you think through the customizations to allow in your environment, consider carefully whether a particular customization is necessary. If it recreates functionality that is already available in the product (such as creating a Web Part that does the same thing as the Content Editor Web Part or the Content by Query Web Part), then that might be unnecessary work. Consider first whether the standard functionality can do what you want, or check the SharePoint Store to see if there is an app for SharePoint available that does what you need.
## Life-cycle management
<a name="Lifecycle"> </a>

Follow these best practices to manage applications based on SharePoint Server 2016 throughout their life cycle:
- Use separate development, preproduction, and production environments, and keep these environments as synchronized as possible so that you can accurately test your customizations.
    
  
- Test all customizations before releasing the first time and after any updates have been made before you release them to your production environment.
    
  
- Use source code control and solution and feature versioning to track changes to code.
    
  

  
    
    
![Development, test, and production environments](images/)
  
    
    

  
    
    

  
    
    

## Branding
<a name="Branding"> </a>

Consistent branding with a corporate style guide makes for more cohesive-looking sites and easier development. Store approved themes in the theme gallery for consistency so that users will know when they visit the site that they are in the right place. SharePoint Server 2016 includes a new feature to use for branding, Design Manager. By using Design Manager, you can create a visual design for your website with whatever web design tool or HTML editor you prefer and then upload that design into SharePoint. Design Manager is the central hub and interface where you manage all aspects of a custom design. Creating the visual design of a site often fits into a larger process, in which multiple people or organizations are involved. For a roadmap of the tasks from a larger perspective, see  [Design and branding in SharePoint 2013](https://go.microsoft.com/fwlink/?LinkId=262838).
## Solutions or apps for SharePoint?
<a name="SolutionsApps"> </a>

SharePoint Server 2016 has a new development model based on apps for SharePoint. Apps for SharePoint are self-contained pieces of functionality that extend the capabilities of a SharePoint website. An app may include SharePoint features such as lists, workflows, and site pages, but it can also use a remote web application and remote data in SharePoint. An app has few or no dependencies on any other software on the device or platform where it is installed, other than what is built into the platform. Apps have no custom code that runs on the SharePoint servers.The guidance for whether to use apps for SharePoint or SharePoint solutions is to:
- **Design apps for end users**
    
    Apps for SharePoint:
    
  - Are easy for users (tenant administrators and site owners) to discover and install.
    
  
  - Use safe SharePoint extensions.
    
  
  - Provide the flexibility to develop future upgrades.
    
  
  - Can integrate with cloud-based resources.
    
  
  - Are available for both SharePoint Online and on-premises SharePoint sites.
    
  
- **Use farm solutions for administrators**
    
    SharePoint solutions:
    
  - Can access the server-side object-model APIs that are needed to extend SharePoint management, configuration, and security
    
  
  - Can extend Central Administration, Microsoft PowerShell cmdlets, timer jobs, custom backups, and so on.
    
  
  - Are installed by administrators.
    
  
  - Can have farm, web application, or site-collection scope.
    
  
Go to MSDN to get more information about the  [new development model](https://go.microsoft.com/fwlink/?LinkId=330807),  [Apps for SharePoint compared with SharePoint solutions](https://go.microsoft.com/fwlink/?LinkId=330806), and  [Deciding between apps for SharePoint and SharePoint solutions](https://go.microsoft.com/fwlink/?LinkID=330807). Set a policy for using apps for SharePoint in your organization. Can users purchase and download apps? How do you make your organization’s apps available? How do you tell if they’re being used?
- **SharePoint Store**    Determine whether users can purchase or download apps from the SharePoint Store.
    
  
- **App Catalog**    Make specific apps for SharePoint available to your users by adding them to the App Catalog.
    
  
- **App requests**    Configure app requests to control which apps are purchased and how many licenses are available.
    
  
- **Monitor apps**    Monitor specific apps in SharePoint Server 2016 to check for errors and to track usage.
    
  
Get more information about apps for SharePoint and  [governance for apps](plan-for-apps-for-sharepoint-server.md#AppPolicy) in the [Plan for apps for SharePoint Server](html/plan-for-apps-for-sharepoint-server.md) article.
# See also

#### 

 [What is governance in SharePoint?](html/what-is-governance-in-sharepoint.md)
  
    
    
 [IT governance in SharePoint](html/it-governance-in-sharepoint.md)
  
    
    

#### 

 **Governance planning in SharePoint**
  
    
    
 **Information management and governance in SharePoint**
  
    
    
 [Build sites for SharePoint 2013](https://go.microsoft.com/fwlink/?LinkID=330803)
  
    
    
 [What is governance poster (Visio format)](https://go.microsoft.com/fwlink/?LinkId=331050)
  
    
    
 [What is governance poster (PDF format)](https://go.microsoft.com/fwlink/?LinkId=331051)
  
    
    

  
    
    

