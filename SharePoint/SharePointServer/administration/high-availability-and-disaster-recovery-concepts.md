---
title: "High availability and disaster recovery concepts in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/2/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 837761f9-0e18-4b42-8798-3776997a6c95
description: "Understand high availability and disaster recovery concepts in SharePoint Server so you can choose the best strategy for your farm."
---

# High availability and disaster recovery concepts in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
High availability and disaster recovery is the highest priority when you create a plan and system specifications for a SharePoint Server farm. Other aspects of the plan, such as high performance and capacity, are negated if farm servers are not highly available or a farm cannot be recovered.
  
To design and implement an effective strategy that maintains efficient and uninterrupted operations, you should understand the basic concepts of high availability and disaster recovery. These concepts are also important to evaluate and pick the best technical solutions for your SharePoint environment.
  
    
## Introduction to business continuity management
<a name="IntroBCM"> </a>

Business continuity management is a management process or program that defines, assesses, and helps manage the risks to the continued running of an organization. Business continuity management focuses on creating and maintaining a business continuity plan, which is a roadmap for continuing operations when normal business operations are interrupted by adverse conditions. These conditions can be natural, man-made, or a combination of both. A continuity plan is derived from the following analyses and inputs:
  
- A business impact analysis
    
- A threat and risk analysis
    
- A definition of the impact scenarios
    
- A set of documented recovery requirements
    
The result is a solution design or identified options, an implementation plan, a testing and organization acceptance plan, and a maintenance plan or schedule.
  
An example of business continuity management is [Disaster recovery and protection for data and applications](http://go.microsoft.com/fwlink/?LinkID=787533&amp;clcid=0x409), which provides a snapshot of the business continuity program at Microsoft.
  
Obviously Information Technology (IT) is a significant aspect of business continuity planning for many organizations. However, business continuity is more encompassing - it includes all the operations that are needed to make sure that an organization can continue to do business during and immediately after a major disruptive event. A business continuity plan includes, but is not limited to, the following elements:
  
- policies, processes and procedures
    
- possible options and decision-making responsibility
    
- human resources and facilities
    
- information technology
    
Although high availability and disaster recovery are often equated to business continuity management; they are in fact, subsets of business continuity management.
  
## Describing high availability
<a name="DescHA"> </a>

For a given software application or service, high availability is ultimately measured in terms of the end user's experience and expectations. The tangible and perceived business impact of downtime may be expressed in terms of information loss, property damage, decreased productivity, opportunity costs, contractual damages, or the loss of goodwill.
  
 *The principal goal of a high availability solution is to minimize or mitigate the impact of downtime.*  A sound strategy for this optimally balances business processes and Service Level Agreements (SLAs) with technical capabilities and infrastructure costs. 
  
A platform is considered highly available per the agreement and expectations of customers and stakeholders. The availability of a system can be expressed as this calculation:
  
Actual uptime/Expected uptime X 100%
  
The resulting value is often expressed by industry in terms of the number of 9's that the solution provides; meant to convey an annual number of minutes of possible uptime, or conversely, minutes of downtime.
  
|**Number of 9's**|**Availability Percentage**|**Total Annual Downtime**|
|:-----|:-----|:-----|
|2  <br/> |99%  <br/> |3 days, 15 hours  <br/> |
|3  <br/> |99.9%  <br/> |8 hours, 45 minutes  <br/> |
|4  <br/> |99.99%  <br/> |52 minutes, 34 seconds  <br/> |
|5  <br/> |99.999%  <br/> |5 minutes, 15 seconds  <br/> |
   
### Planned versus unplanned downtime

System outages are either anticipated or planned for, or they are the result of an unplanned failure. Downtime need not be considered negatively if it is appropriately managed. There are two key types of foreseeable downtime:
  
- **Planned maintenance.** A time window is preannounced and coordinated for planned maintenance tasks such as software patching, hardware upgrades, password updates, offline re-indexing, data loading, or the rehearsal of disaster recovery procedures. Deliberate, well-managed operational procedures should minimize downtime and prevent any data loss. Planned maintenance activities can be seen as investments needed to prevent or mitigate other potentially more severe unplanned outage scenarios. 
    
- **Unplanned outage.** System-level, infrastructure, or process failures may occur that are unplanned or uncontrollable, or that are foreseeable, but considered either too unlikely to occur, or are considered to have an acceptable impact. A robust high availability solution detects these types of failures, automatically recovers from the outage, and then reestablishes fault tolerance. 
    
When establishing SLAs for high availability, you should calculate separate key performance indicators (KPIs) for planned maintenance activities and unplanned downtime. This approach allows you to contrast your investment in planned maintenance activities against the benefit of avoiding unplanned downtime.
  
### Degraded availability

High availability should not be considered as an all-or-nothing proposition. As an alternative to a complete outage, it is often acceptable to the end user for a system to be partially available, or to have limited functionality or degraded performance. These varying degrees of availability include:
  
- **Read-only and deferred operations.** During a maintenance window, or during a phased disaster recovery, data retrieval is still possible, but new workflows and background processing may be temporarily halted or queued. 
    
- **Data latency and application responsiveness.** Due to a heavy workload, a processing backlog, or a partial platform failure, limited hardware resources may be over-committed or under-sized. User experience may suffer, but work may still get done in a less productive manner. 
    
- **Partial, transient, or impending failures.** Robustness in the application logic or hardware stack that retries or self-corrects upon encountering an error. These types of issues may appear to the end user as data latency or poor application responsiveness. 
    
- **Partial end-to-end failure.** Planned or unplanned outages may occur gracefully within vertical layers of the solution stack (infrastructure, platform, and application), or horizontally between different functional components. Users may experience partial success or degradation, depending upon the features or components that are affected. 
    
The acceptability of these suboptimal scenarios should be considered as part of a spectrum of degraded availability leading up to a complete outage, and as intermediate steps in a phased disaster recovery.
  
## Quantifying downtime
<a name="QuantDT"> </a>

When downtime does occur, either planned, or unplanned, the primary business goal is to bring the system back online and minimize data loss. Every minute of downtime has direct and indirect costs. With unplanned downtime, you must balance the time and effort needed to determine why the outage occurred, what the current system state is, and what steps are needed to recover from the outage.
  
At a predetermined point in any outage, you should make or seek the business decision to stop investigating the outage or performing maintenance tasks, recover from the outage by bringing the system back online, and if needed, reestablish fault tolerance.
  
### Recovery objectives

Data redundancy is a key component of a high availability database solution. Transactional activity on your primary SQL Server instance is synchronously or asynchronously applied to one or more secondary instances. When an outage occurs, transactions that were in flight may be rolled back, or they may be lost on the secondary instances due to delays in data propagation.
  
You can both measure the impact, and set recovery goals in terms of how long it takes to get back in business, and how much time latency there is in the last transaction recovered:
  
- **Recovery Time Objective (RTO).** This is the duration of the outage. The initial goal is to get the system back online in at least a read-only capacity to facilitate investigation of the failure. However, the primary goal is to restore full service to the point that new transactions can take place. 
    
- **Recovery Point Objective (RPO).** This is often referred to as a measure of acceptable data loss. It is the time gap or latency between the last committed data transaction before the failure and the most recent data recovered after the failure. The actual data loss can vary depending upon the workload on the system at the time of the failure, the type of failure, and the type of high availability solution used. 
    
    > [!NOTE]
    > A related objective is **Recovery level objective (RLO)**. This objective defines the granularity with which you must be able to recover data — whether you must be able to recover the whole farm, Web application, site collection, site, list or library, or item. For more information, see [Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md). 
  
You should use RTO and RPO values as goals that indicate business tolerance for downtime and acceptable data loss, and as metrics for monitoring availability health.
  
### Justifying ROI or opportunity cost

The business costs of downtime may be either financial or in the form of customer goodwill. These costs may accrue with time, or they may be incurred at a certain point in the outage window. In addition to projecting the cost of incurring an outage with a given recovery time and data recovery point, you can also calculate the business process and infrastructure investments needed to attain your RTO and RPO goals or to avoid the outage all together. These investment themes should include:
  
- **Avoiding downtime.** Outage recovery costs are avoided all together if an outage doesn't occur in the first place. Investments include the cost of fault-tolerant and redundant hardware or infrastructure, distributing workloads across isolated points of failure, and planned downtime for preventive maintenance. 
    
- **Automating recovery.** If a system failure occurs, you can greatly mitigate the impact of downtime on the customer experience through automatic and transparent recovery. 
    
- **Resource utilization.** Secondary or standby infrastructure can sit idle, awaiting an outage. It also can be leveraged for read-only workloads, or to improve overall system performance by distributing workloads across all available hardware. 
    
For given RTO and RPO goals, the needed availability and recovery investments, combined with the projected costs of downtime, can be expressed and justified as a function of time. During an actual outage, this allows you to make cost-based decisions based on the elapsed downtime.
  
### Monitoring availability health

From an operational point of view, during an actual outage, you should not attempt to consider all relevant variables and calculate ROI or opportunity costs in real time. Instead, you should monitor data latency on your standby instances as a proxy for expected RPO.
  
In the event of an outage, you should also limit the initial time spent investigating the root cause during the outage, and instead focus on validating the health of your recovery environment, and then rely upon detailed system logs and secondary copies of data for subsequent forensic analysis.
  
### Planning for disaster recovery

While high availability efforts entail what you do to prevent an outage, disaster recovery efforts address what is done to re-establish high availability after the outage.
  
As much as possible, disaster recovery procedures and responsibilities should be formulated before an actual outage occurs. Based upon active monitoring and alerts, the decision to initiate an automated or manual failover and recovery plan should be tied to pre-established RTO and RPO thresholds. The scope of a sound disaster recovery plan should include:
  
- **Granularity of failure and recovery.** Depending upon the location and type of failure, you can take corrective action at different levels; that is, data center, infrastructure, platform, application, or workload. 
    
- **Investigative source material.** Baseline and recent monitoring history, system alerts, event logs, and diagnostic queries should all be readily accessible by appropriate parties. 
    
- **Coordination of dependencies.** Within the application stack, and across stakeholders, what are the system and business dependencies? 
    
- **Decision tree.** A predetermined, repeatable, validated decision tree that includes role responsibilities, fault triage, failover criteria in terms of RPO and RTO goals, and prescribed recovery steps. 
    
- **Validation.** After taking steps to recover from the outage, what must be done to verify that the system has returned to normal operations? 
    
- **Documentation.** Capture all of the above items in a set of documentation, with sufficient detail and clarity so that a third party team can execute the recovery plan with minimal assistance. This type of documentation is commonly called a 'run book' or a 'cook book'. 
    
- **Recovery rehearsals.** Regularly exercise the disaster recovery plan to establish baseline expectations for RTO goals, and consider regular rotation of hosting the primary production site on the primary and each of the disaster recovery sites. 
    
## See also
<a name="QuantDT"> </a>

#### Concepts

[Choose a disaster recovery strategy for SharePoint Server](plan-for-disaster-recovery.md)

#### Other Resources

[What workloads can you protect with Azure Site Recovery?](/azure/site-recovery/site-recovery-workload)

[Replicate a multi-tier SharePoint application for disaster recovery using Azure Site Recovery](/azure/site-recovery/site-recovery-sharepoint)

