---
title: "How SharePoint Online and OneDrive safeguard your data in the cloud"
ms.author: kaarins
author: kaarins
ms.date: 5/25/2018
ms.audience: Admin
ms.topic: conceptual
ms.prod: office-online-server
localization_priority: Normal
ms.collection: Strat_SP_admin
search.appverid:
- SPO160
- ODB160
ms.assetid: 5aa038e8-8ff0-4704-9e6a-fd72af0a2035
description: "Learn what Microsoft does to protect your data in SharePoint Online and OneDrive, and steps you can take to increase security"
---

# How SharePoint Online and OneDrive safeguard your data in the cloud

You control your data. When you put your data in SharePoint Online and OneDrive, you remain the owner of the data. For more info about the ownership of your data, see [Office 365 Privacy by Design](https://products.office.com/en-us/business/office-365-trust-center-privacy).
  
## How we treat your data

Microsoft engineers administer SharePoint Online and OneDrive using a Windows PowerShell console that requires two-factor authentication. We perform day-to-day tasks by running workflows so we can rapidly respond to new situations. Check-ins to the service require code review and management approval.
  
No engineer has standing access to the service. When engineers need access, they must request it. Eligibility is checked, and if engineer access is approved, it's only for a limited time. In the rare cases where Microsoft engineers need access to content, (for example if you submit a support ticket because a user can't access an important file that we believe is damaged), the engineers must check in a special workflow that requires business justification and manager approval. An audit event is generated that you can view in the Office 365 admin center. You can also turn on a feature called Customer Lockbox so you need to grant approval. The engineer gets access only to the file in question. Learn how to turn on or off Customer Lockbox and approve and deny requests: [Office 365 Customer Lockbox Requests](https://support.office.com/en-us/article/Office-365-Customer-Lockbox-Requests-36f9cdd1-e64c-421b-a7e4-4a54d16440a2).
  
## How you can safeguard your data

One of the most important things you can do to safeguard your data is to require two-factor authentication for your identities in Office 365. This prevents credentials from being used without a second factor and mitigates the impact of compromised passwords. The second factor can be made through a phone call, text message, or app. When you roll out two-factor authentication, start with your global admins, and then other admins and site collection admins. For information on how to do this, see [Set up multi-factor authentication for Office 365 users](https://support.office.com/article/8f0454b2-f51a-4d9c-bcde-2c48e41621c6).
  
Other things we recommend to increase security: 
  
- Use Azure Active Directory device-based conditional access to block or limit access on unmanaged devices like airport or hotel kiosks. See [Control access from unmanaged devices](control-access-from-unmanaged-devices.md).
    
- Create policies to sign users out of Office 365 web sessions after a period of inactivity. For information, see [Idle Session Timeout (currently in preview).](https://go.microsoft.com/fwlink/?linkid=867121)
    
- Evaluate the need for IP-based sessions. These simulate the access model of an on-premises deployment. Read more at [Control access based on network location or app](https://support.office.com/article/59b83701-cefd-4bf8-b4d1-d4659b60da08).
    
- Empower workers to share broadly but safely. You can require sign-in or use links that expire or grant limited privileges. See [Manage external sharing for your SharePoint Online environment](external-sharing-overview.md).
    
- Prevent accidental exposure of sensitive content. Create DLP policies to identify documents and prevent them from being shared. See [Overview of data loss prevention policies](https://support.office.com/article/1966b2a7-d1e2-4d92-ab61-42efbb137f5e#office).
    
## Protected in transit and at rest

### Protected in transit

When data transits into the service from clients, and between datacenters, it's protected using best-in-class encryption. For info, see [Data Encryption in OneDrive for Business and SharePoint Online](https://support.office.com/article/6501b5ef-6bf7-43df-b60d-f65781847d6c). We only permit secure access. We won't make authenticated connections over HTTP, but instead redirect to HTTPS.
  
### Protected at rest

 **Physical protection**: Only a limited number of essential personnel can gain access to datacenters. Their identities are verified with multiple factors of authentication including smart cards and biometrics. There are on-premises security officers, motion sensors, and video surveillance. Intrusion detection alerts monitor anomalous activity. 
  
 **Network protection**: The networks and identities are isolated from the Microsoft corporate network. We administer the service with dedicated Active Directory domains, we have separate domains for test and production, and the production domain is divided into multiple isolated domains for reliability and security. For more information about the built-in physical and logical security from Office 365, see [Built in Security from Office 365](https://products.office.com/en-us/business/office-365-trust-center-security).
  
 **Application security**: Engineers who build features follow the security development lifecycle. Automated and manual analyses help identify possible vulnerabilities. The Microsoft security response center ( [Microsoft Security Response Center](https://technet.microsoft.com/en-us/security/dn440717.aspx)) helps triage incoming vulnerability reports and evaluate mitigations. Through the Microsoft Cloud Bug Bounty, people across the world can earn money by reporting vulnerabilities. Read more about this at [Microsoft Cloud Bug Bounty Terms](https://technet.microsoft.com/en-us/dn800983).
  
 **Content protection**: You data is encrypted at the disk level using BitLocker encryption and at the file level using keys. For info, see [Data Encryption in OneDrive for Business and SharePoint Online](https://support.office.com/article/6501b5ef-6bf7-43df-b60d-f65781847d6c). For information about using Customer Key to provide and control the keys that are used to encrypt your data at rest in Office 365, see [Service encryption with Customer Key for Office 365 FAQ](https://support.office.com/article/41ae293a-bd5c-4083-acd8-e1a2b4329da6).
  
The Office 365 anti-malware engine scans documents at upload time for content matching an AV signature (updated hourly). For information, see [Virus detection in SharePoint Online](https://support.office.com/article/e3c6df61-8513-499d-ad8e-8a91770bff63). For more advanced protection, use Office 365 Advanced Threat Protection (ATP). ATP analyzes content that's shared and applies threat intelligence and analysis to identify sophisticated threats. For information, see [Office 365 Advanced Threat Protection](https://support.office.com/article/e100fe7c-f2a1-4b7d-9e08-622330b83653).
  
To limit the risk of content being downloaded to untrusted devices: 
  
- Limit sync to devices on the domains you specify: [Allow syncing only on computers joined to specific domains](https://support.office.com/article/a3b03efd-ccd0-4d3c-b9ae-7f8f3f9485bc).
    
- Use Intune to limit access to content in the OneDrive and SharePoint mobile apps: [Control access to features in the OneDrive and SharePoint mobile apps](https://support.office.com/article/d25713bb-5cf8-4874-9b5b-e8bee3b94f13).
    
To manage content at rest: 
  
- Configure IRM policies on SharePoint document libraries to limit download of content. See [Set up Information Rights Management (IRM) in SharePoint admin center](https://support.office.com/article/239ce6eb-4e81-42db-bf86-a01362fed65c).
    
- Evaluate the use of Azure Information Protection (AIP). Classification and labeling lets you track and control how data is used. Visit [Azure Information Protection](https://www.microsoft.com/en-us/cloud-platform/azure-information-protection).
    
## Highly available, always recoverable

Our datacenters are geo-distributed within the region and fault tolerant. Data is mirrored in at least two datacenters to mitigate the impact of a natural disaster or service-impacting outage. See the [Where's my data?](https://o365datacentermap.azurewebsites.net/).
  
Metadata backups are kept for 14 days and can be restored to any point in time within a 5-minute window. 
  
In the case of a ransomware attack, you can use Version history ([Enable and configure versioning for a list or library](https://support.office.com/article/1555d642-23ee-446a-990a-bcab618c7a37)) to roll back, and the recycle bin or site collection recycle bin to restore ([Restore deleted items from the site collection recycle bin ](https://support.office.com/article/5fa924ee-16d7-487b-9a0a-021b9062d14b)). If an item is deleted from the site collection recycle bin, you can call support within 14 days to access a backup. For info about the new Files Restore feature that lets users restore an entire OneDrive to any point within the past 30 days, see [Restore your OneDrive](https://support.office.com/article/fa231298-759d-41cf-bcd0-25ac53eb8a15.aspx).
  
## Continuously validated

We constantly monitor our datacenters to keep them healthy and secure. This starts with inventory. An inventory agent scans each subnet looking for neighbors. For each machine, we perform a state capture.
  
After we have an inventory, we can monitor and remediate the health of machines. The security patch train applies patches, updates anti-virus signatures, and makes sure we have a known good configuration saved. We have role-specific logic that ensures we only patch or rotate out a certain percentage of machines at a time.
  
We have an automated workflow to identify machines that don't meet policies and queue them for replacement.
  
The Office 365 "Red Team" within Microsoft is made up of intrusion specialists. They look for any opportunity to gain unauthorized access. The "Blue Team" is made up of defense engineers who focus on prevention, detection, and recovery. They build intrusion detection and response technologies. To keep up with the learnings of the security teams at Microsoft, see [Security Office 365 (blog)](https://blogs.technet.microsoft.com/office365security/).
  
To monitor and observe activity in your Office 365 subscription:
  
- If you have an on-premises security operations center or SIEM, you can monitor activity with the Management Activity API. For information, see [Office 365 Management APIs overview](https://msdn.microsoft.com/en-us/office-365/office-365-managment-apis-overview). This will show you activity from across SharePoint, Exchange, Azure Active Directory, DLP and more. If you don't have an on-premises security operations center or SIEM, you can use Cloud App Security. Cloud App Security uses the Management Activity API. For information, see [Overview of Office 365 Cloud App Security](https://support.office.com/en-us/article/Overview-of-Office-365-Cloud-App-Security-81f0ee9a-9645-45ab-ba56-de9cbccab475?ui=en-US&amp;rs=en-US&amp;ad=US). Through Cloud App Security, you can report, search, and alert on activity.
    
- Use Azure Active Directory identity protection. This applies machine learning to detect suspicious account behavior, for example, simultaneous sign-ins from the same user in different parts of the world. You can configure identity protection to take action to block these sign-ins. For more information, see [Azure Active Directory Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/active-directory-identityprotection).
    
- Use Secure Score to evaluate the security profile of your subscription against a known good baseline and identify opportunities to increase protection: [Introducing the Office 365 Secure Score](https://support.office.com/en-us/article/Introducing-the-Office-365-Secure-Score-c9e7160f-2c34-4bd0-a548-5ddcc862eaef).
    
## Audited and compliant

Regulatory compliance is fundamental to Office 365. We make sure the service complies with regulatory and compliance standards. We also help you meet your audit and compliance obligations. The [Service Trust Portal](https://servicetrust.microsoft.com) is a one-stop shop for compliance and trust information for Microsoft enterprise services. The portal contains reports, whitepapers, vulnerability assessments, and compliance guides. The portal also includes the Compliance Manager which evaluates the configuration of your subscription against a set of compliance criteria. For more info about the Service Trust Portal, see [Get started with the Microsoft Service Trust Portal](https://support.office.com/article/f30e2353-0bd6-41ed-8347-eea1fb8d2662).
  
To meet your regulatory requirements: 
  
- Audit Office 365 activity in the Security &amp; Compliance Center: [Search the audit log in the Office 365 Security and Compliance Center](https://support.office.com/article/0d4d0f35-390b-4518-800e-0c7ec95e946c).
    
- Create eDiscovery cases: [Manage eDiscovery cases in the Office 365 Security and Compliance Center](https://support.office.com/article/9a00b9ea-33fd-4772-8ea6-9d3c65e829e6)
    
- Apply retention policies: [Create and apply information management policies](https://support.office.com/article/eb501fe9-2ef6-4150-945a-65a6451ee9e9).
    

