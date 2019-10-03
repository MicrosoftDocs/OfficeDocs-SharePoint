---
title: "Overview of SharePoint 2013 installation and configuration"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/23/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 26de3fb0-c4d9-44b9-94ad-555d61ec0f92
description: "Learn about how to install and configure SharePoint Server 2013 in a farm."
---

# Overview of SharePoint 2013 installation and configuration

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
Although SharePoint products farms vary in complexity and size, a combination of careful planning and a phased deployment that includes ongoing testing and evaluation significantly reduces the risk of unexpected outcomes. This article provides an overview for all types of SharePoint Server 2013 farm deployment.
  
For a visual representation of the information in this article, see the SharePoint 2013 Products Deployment model in the [Technical diagrams for SharePoint Server](../technical-reference/technical-diagrams.md) topic. Related technical diagrams include " **Topologies for SharePoint 2013** and **Services in** SharePoint Server 2013". 
  
    
## Concepts
<a name="Concepts"> </a>

The logical result of SharePoint Server 2013's flexibility and richness can be a high degree of complexity around installing and configuring SharePoint Server 2013 correctly. A fundamental understanding of the following key structural elements in a SharePoint Server 2013 environment is required in order to correctly deploy and support SharePoint Server 2013:
  
- Server farm: The top-level element of a logical architecture design for SharePoint Server 2013.
    
- Web application: An IIS Web site that is created and used by SharePoint Server 2013.
    
- Content database: Provides storage Web application content. You can separate content into multiple content databases at the site collection level.
    
- Site collection: A set of Web sites that have the same owner and share administration settings.
    
- Site: One or more related Web pages and other items (such as lists, libraries, and documents) that are hosted inside a site collection.
    
In addition to understanding the elements of a SharePoint Server 2013 environment and how they have to be configured for your solution, you must consider the following additional factors: physical architecture, installation and configuration, and the various stages of deployment.
  
## Physical architecture
<a name="Physical"> </a>

The physical architecture, which consists of one or more servers and the network infrastructure, enables you to implement the logical architecture for a SharePoint Server 2013 solution. The physical architecture is typically described in two ways: by its size and by its topology. Size, which can be measured in several ways, such as the number of users or the number of documents, is used to categorize a farm as small, medium, or large. Topology uses the idea of tiers or server groups to define a logical arrangement of farm servers.
  
### Size

Size uses the number of users and number of content items as a fundamental measure to indicate whether a server farm is small, medium, and large, as follows:
  
- A small server farm typically consists of at least two Web servers and a database server. One of the Web servers hosts the Central Administration site and the other handles additional farm-related tasks, such as serving content to users.
    
    The small farm can be scaled out to three tiers using a dedicated application server in response to the number of users, the number of content items, and the number of services that are required. 
    
- A medium server farm typically consists of two or more Web servers, two application servers, and more than one database servers. We recommend that you start with the preceding configuration and then scale out to accommodate the workload placed on the servers.
    
    In scenarios where services are known to use a disproportionate amount of resources, you can scale out the application tier. Performance data will indicate which services you should consider off-loading to a dedicated server.
    
- A large server farm can be the logical result of scaling out a medium farm to meet capacity and performance requirements or by design before a SharePoint Server 2013 solution is implemented. A three-tier topology environment typically uses dedicated servers on all the tiers. Additionally, these servers are often grouped according to their role in the farm. For example, all client-related services can be grouped onto one or two servers and then scaled out by adding servers to this group as needed in response to user demand for these services.
    
    > [!NOTE]
    > The recommendation for scaling out a farm is to group services or databases with similar performance characteristics onto dedicated servers and then scale out the servers as a group. In large environments, the specific groups that evolve for a farm depend on the specific demands for each service in a farm. 
  
For specific numbers related to small, medium, and large farms, see [Performance planning in SharePoint Server 2013](../administration/performance-planning-in-sharepoint-server-2013.md).
  
### Topology

Topology uses tiers as a model for logically arranging farm servers according to the components that they host or their roles in a server farm. A SharePoint Server 2013 farm is deployed on one, two, or three tiers, as follows:
  
- In a single-tier deployment, SharePoint Server 2013 and the database server are installed on one computer.
    
- In a two-tier deployment, SharePoint Server 2013 components and the database are installed on separate servers. This kind of deployment maps to what is called a small farm. The front-end Web servers are on the first tier and the database server is located on the second tier. In the computer industry, the first tier is known as the Web tier. The database server is known as the database tier or database back-end.
    
- In a three-tier deployment, the front-end Web servers are on the first tier, the application servers are on the second tier, which is known as the application tier, and the database server is located on the third tier. A three-tier deployment is used for medium and large farms.
    
## Installation and configuration
<a name="Installation"> </a>

After you finish planning your solution you can create a SharePoint Server 2013 farm to host the solution. The first step is to install SharePoint Server 2013 and create the farm that is required for the solution. The process of preparing your environment consists of the following phases:
  
1. Prepare the servers
    
2. Create the farm
    
3. Configure settings, services, solutions, and sites
    
> [!NOTE]
> The farm that you create and deploy will undergo significant changes in size, topology, and complexity as you move through the different deployment stages illustrated in the SharePoint Server 2013 Products Deployment model. This is typical and the expected result of a phased deployment. This is why we recommend that you follow all of the stages described in the "Deployment stages" section of this article. 
  
### Prepare the servers

In this phase, you get your servers ready to host the product. This includes the supporting servers and the servers that will have SharePoint Server 2013 installed. The following servers must be configured to support and host a farm:
  
- Database server: The required version of SQL Server, including service packs and cumulative updates must be installed on the database server. The installation must include any additional features, such as SQL Analysis Services, and the appropriate SharePoint Server 2013 logins have to be added and configured. The database server must be hardened and, if it is required, databases must be created by the DBA. For more information, see:
    
  - [Hardware and software requirements for SharePoint 2013](hardware-and-software-requirements-0.md)
    
  - [Configure SQL Server security for SharePoint Server](../security-for-sharepoint-server/configure-sql-server-security-for-sharepoint-environments.md)
    
- Application servers and front-end Web servers: The farm servers that will have SharePoint Server 2013 installed must be prepared as follows: verify that they meet the hardware requirements, have the operating system hardened, have the required networking and security protocols configured, have the SharePoint Server 2013 software prerequisites installed and hardened, and have the required authentication configured. For more information, see:
    
  - [System requirements for SharePoint 2013](system-requirements-for-sharepoint-2013.md)
    
  - "Installing software prerequisites" in [Hardware and software requirements for SharePoint 2013](hardware-and-software-requirements-0.md)
    
  - [Plan security hardening for SharePoint Server](../security-for-sharepoint-server/security-hardening.md)
    
  
- Domain controller: The required farm accounts have to be configured for the domain and directory synchronization must be configured. 
    
    > [!IMPORTANT]
    > SharePoint Server 2013 does not support installation on to a domain controller in a production environment. Additionally, SharePoint Server 2013 does not support installation on to a domain controller when using the sandbox service in developer, test, or demo environments. > A single label domain (SLD) names or single label forests is also not supported. Because the use of SLD names is not a recommended practice, SharePoint Server 2013 is not tested in this scenario. Therefore, there may be incompatibility issues when SharePoint Server 2013 are implemented in a single label domain environment. For more information, see [Information about configuring Windows for domains with single-label DNS names](https://go.microsoft.com/fwlink/p/?LinkID=193849) and the [DNS Namespace Planning Solution Center](https://go.microsoft.com/fwlink/p/?LinkId=198010). 
  
    For information about required accounts, see:
    
  - [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md)
    
### Create the farm

In this phase, you install the product and configure each server to support its role in the farm. You also create the configuration database and the SharePoint Central Administration Web site. The following servers are required for a SharePoint Server 2013 farm:
  
- Database server: Unless you plan to use DBA-created databases, the configuration database, content database, and other required databases are created when you run the SharePoint Products Configuration Wizard.
    
- Application server: After you prepare the application server, install any additional components that are required to support functions such as Information Rights Management (IRM) and decision support. Install SharePoint Server 2013 on the server that will host SharePoint Central Administration Web site and then run the SharePoint Products Configuration Wizard to create and configure the farm. 
    
- Front-end Web server: Install SharePoint Server 2013 on each Web server, install language packs, and then run the SharePoint Products Configuration Wizard to add the Web servers to the farm.
    
    > [!NOTE]
    > After you add and configure all the front-end Web servers, you can add any additional application servers that are part of your topology design to the farm. 
  
### Configure settings, services, solutions, and sites

In this phase, you prepare the farm to host your site content by completing the following tasks:
  
- Configure services.
    
- Configure global settings. For more information, see [Configure SharePoint Server](configure.md)
    
- Create and populate the sites. For more information, see [Create a web application in SharePoint Server](/previous-versions/office/sharepoint-server-2010/cc261875(v=office.14))
    
> [!NOTE]
> Farm configuration steps are not isolated to a specific tier in the server infrastructure. 
  
## Deployment stages
<a name="DeploymentStages"> </a>

By deploying a SharePoint Server 2013 solution in stages, you gain the benefits that are provided by a systematic approach, such as collecting performance and usage data that you can use to evaluate your solution. Additional benefits include verifying your capacity management assumptions and identifying issues before the farm is put into production. 
  
We recommend that you deploy your farm in the following stages:
  
- Planning
    
- Development
    
- Proof of concept
    
- Pilot
    
- User acceptance test
    
- Production
    
### Planning

Before you can deploy a farm, you must plan the solution that you want to deploy and determine the infrastructure requirements, such as server resources and farm topology. When you finish the planning stage, you should have documented the following:
  
- An infrastructure design to support your solution
    
- A detailed description of how you will implement the farm and the solution
    
- A plan for testing and validating the solution
    
- A site and solution architecture
    
- An understanding of the monitoring and sustained engineering requirements to support the solution
    
- A record of how the solution will be governed
    
- An understanding of how the solution will be messaged to the user to drive adoption of the solution
    
We recommend that you use the planning resources and articles described in [Plan for SharePoint Server](/previous-versions/office/sharepoint-server-2010/cc261834(v=office.14)).
  
> [!IMPORTANT]
> Resource and time issues may pressure you to be less rigorous during the planning stage. We recommend that you try to be as diligent as possible because missed or lightly touched planning elements can resurface as significant issues after you are in production. These issues can create much additional work, consume unbudgeted resources, and potentially take away from the success of your SharePoint Server 2013. 
  
After the planning stage, you move through the following deployment stages, updating and revising your plans, configurations, and topologies as you test.
  
### Development

During the development stage you will deploy SharePoint Server 2013 on a single server or on multiple servers to develop, test, evaluate, and refine the solution that you intend to implement. This environment is scaled according to your needs during solution development and can be retained as a scaled down environment for future development and testing. This is not a stable environment and there are no service-level agreements. 
  
### Proof of concept

During the proof of concept stage, the objective is two-fold: to understand SharePoint Server 2013 and to evaluate SharePoint Server 2013 in the context of how it can address your business needs. The first level of product evaluation can be done by installing all of the product components on a single server. You do a more extensive product evaluation by a proof-of-concept deployment.
  
A proof-of-concept deployment on a single server or on a small farm enables you to expand the scope of your evaluation. In this deployment, non-IT staff is added to the evaluation team, which provides a broader view of how SharePoint Server 2013 features might be actually be used in the organization. The benefit of a proof-of-concept deployment is that you can collect data that can be used to refine your original plan. This data—such as page views, user behavior patterns, and server resource consumption—also enables you to start to build a benchmark for sizing your farm. A proof of concept is also good when you evaluate service applications and determining what feature sets that you will offer your end users. 
  
It is important during the proof-of-concept stage that you understand the unique characteristics and functionality of these features because this understanding will help you define your overall topology. Be aware that a proof-of-concept deployment requires additional resources and extends the time required to put SharePoint Server 2013 into production.
  
> [!TIP]
> Virtualization provides a good platform for evaluating SharePoint Server 2013 because a virtual environment provides flexibility, rapid deployment capability, and the ability to roll back virtual machines to previous states. 
  
### Pilot

A pilot is used to test your solution on a small scale. There are two approaches to using a pilot deployment. In the first approach, the focus is on functional testing without using real data. By using the second approach you test for production characteristics by using real data and have your pilot users test different kinds of tasks. We recommend the second approach because of the broader scope and real-world data that you can collect and use to refine your solution design. 
  
A pilot deployment provides many benefits. It enables you to collect data that you can use to validate the following aspects of your farm design:
  
- Infrastructure design
    
- Capacity management assumptions
    
- Site and solution architecture
    
- Solution usage assumptions
    
The pilot stage also enables you to determine additional data that should be collected to increase the breadth and depth of your benchmarks. This is important if you want to assess the potential effect of additional features or services that you want to add to the farm before the user acceptance test.
  
At the conclusion of the pilot deployment, you can use the data that you collect to adjust the various components of the solution and its supporting infrastructure.
  
### User acceptance test (UAT)

A user acceptance test deployment—also known as a pre-production environment—is used by organizations as a transitional step from the pilot deployment to a production deployment. An organization's business processes determine the scope, scale, and duration of user accept testing. 
  
The topology of the pre-production environment should be the same as, or very similar to the planned production topology. During user acceptance testing, the SharePoint Server 2013 solution is tested against a subset or a complete copy of production data. This deployment stage provides a final opportunity for performance tuning and validating operational procedures such as backups and restores. 
  
### Production

The final stage is rolling your farm into a production environment. At this stage, you will have incorporated the necessary solution and infrastructure adjustments that were identified during the user acceptance test stage. 
  
Putting the farm into production requires you to complete the following tasks: 
  
- Deploy the farm.
    
- Deploy the solution.
    
- Implement the operations plan.
    
- If required, deploy additional environments such as authoring and staging farms, and services farms.
    

