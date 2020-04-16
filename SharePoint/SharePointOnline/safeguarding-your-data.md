---
title: "Cloud data security measures in SharePoint & OneDrive"
ms.reviewer: mswann
manager: 
ms.author: kaarins
author: kaarins
ms.date: 5/25/2018
audience: Admin
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom:
- seo-marvel-mar2020
search.appverid:
- SPO160
- ODB160
- MET150
ms.assetid: 5aa038e8-8ff0-4704-9e6a-fd72af0a2035
description: "Learn what Microsoft does to protect your data in SharePoint and OneDrive, and steps you can take to increase security"
---

# How SharePoint Online and OneDrive safeguard your data in the cloud
 
You control your data. When you put your data in SharePoint Online and OneDrive, you remain the owner of the data. For more info about the ownership of your data, see [Office 365 Privacy by Design](https://www.microsoft.com/trustcenter/privacy/privacy-overview).
  
## How we treat your data
 
Microsoft engineers administer SharePoint Online and OneDrive using a Windows PowerShell console that requires two-factor authentication. We perform day-to-day tasks by running workflows so we can rapidly respond to new situations. Check-ins to the service require code review and management approval.
  
No engineer has standing access to the service. When engineers need access, they must request it. Eligibility is checked, and if engineer access is approved, it's only for a limited time. In rare cases where Microsoft engineers need access to content (for example, if you submit a support ticket because a user can't access an important file that we believe is damaged), the engineers must check in a specific workflow that requires business justification and manager approval. An audit event is generated that you can view in the Microsoft 365 admin center. You can also turn on a feature called Customer Lockbox, so you need to approve the request. The engineer gets access only to the file in question. Learn how to turn on or off Customer Lockbox and approve and deny requests: [Office 365 Customer Lockbox Requests](/office365/admin/manage/customer-lockbox-requests).
  
## How you can safeguard your data
 
One of the most important things you can do to safeguard your data is to require two-factor authentication for your identities in Office 365. This prevents credentials from being used without a second factor and mitigates the impact of compromised passwords. The second factor can be made through a phone call, text message, or app. When you roll out two-factor authentication, start with your global admins, and then other admins and site collection admins. For information on how to do this, see [Set up multi-factor authentication for Office 365 users](/office365/admin/security-and-compliance/set-up-multi-factor-authentication).
  
Other things we recommend to increase security: 
  
- Use Azure Active Directory device-based conditional access to block or limit access on unmanaged devices like airport or hotel kiosks. See [Control access from unmanaged devices](control-access-from-unmanaged-devices.md).
    
- Create policies to sign users out of Office 365 web sessions after a period of inactivity. For information, see [Sign out inactive users](sign-out-inactive-users.md).
    
- Evaluate the need for IP-based sessions. These simulate the access model of an on-premises deployment. Read more at [Control access based on network location or app](/onedrive/control-access-based-on-network-location-or-app).
    
- Empower workers to share broadly but safely. You can require sign-in or use links that expire or grant limited privileges. See [Manage external sharing for your SharePoint Online environment](external-sharing-overview.md).
    
- Prevent accidental exposure of sensitive content. Create DLP policies to identify documents and prevent them from being shared. See [Overview of data loss prevention policies](/office365/securitycompliance/data-loss-prevention-policies).
    
## Protected in transit and at rest
 
### Protected in transit
 
When data transits into the service from clients, and between datacenters, it's protected using best-in-class encryption. For info, see [Data Encryption in OneDrive for Business and SharePoint Online](/office365/securitycompliance/data-encryption-in-odb-and-spo). We only permit secure access. We won't make authenticated connections over HTTP but, instead, redirect to HTTPS.
  
### Protected at rest
 
 **Physical protection**: Only a limited number of essential personnel can gain access to datacenters. Their identities are verified with multiple factors of authentication, including smart cards and biometrics. There are on-premises security officers, motion sensors, and video surveillance. Intrusion detection alerts monitor anomalous activity. 
  
 **Network protection**: The networks and identities are isolated from the Microsoft corporate network. We administer the service with dedicated Active Directory domains, we have separate domains for test and production, and the production domain is divided into multiple isolated domains for reliability and security. For more information about the built-in physical and logical security from Office 365, see [Built in Security from Office 365](https://www.microsoft.com/security).
  
 **Application security**: Engineers who build features follow the security development lifecycle. Automated and manual analyses help identify possible vulnerabilities. The Microsoft security response center ([Microsoft Security Response Center](https://www.microsoft.com/msrc?rtc=1)) helps triage incoming vulnerability reports and evaluate mitigations. Through the Microsoft Cloud Bug Bounty, people across the world can earn money by reporting vulnerabilities. Read more about this at [Microsoft Cloud Bug Bounty Terms](https://www.microsoft.com/msrc/bounty-microsoft-cloud?rtc=1
).
  
 **Content protection**: Your data is encrypted at the disk level using BitLocker encryption and at the file level using keys. For info, see [Data Encryption in OneDrive for Business and SharePoint Online](/office365/securitycompliance/data-encryption-in-odb-and-spo). For information about using Customer Key to provide and control the keys that are used to encrypt your data at rest in Office 365, see [Service encryption with Customer Key for Office 365 FAQ](/office365/securitycompliance/service-encryption-with-customer-key-faq).
  
The Office 365 anti-malware engine scans documents at upload time for content matching an AV signature (updated hourly). For information, see [Virus detection in SharePoint Online](/office365/securitycompliance/virus-detection-in-spo). For more advanced protection, use Office 365 Advanced Threat Protection (ATP). ATP analyzes content that's shared and applies threat intelligence and analysis to identify sophisticated threats. For information, see [Office 365 Advanced Threat Protection](/office365/securitycompliance/office-365-atp).
  
To limit the risk of content being downloaded to untrusted devices: 
  
- Limit sync to devices on the domains you specify: [Allow syncing only on computers joined to specific domains](/onedrive/allow-syncing-only-on-specific-domains).
    
- Use Intune to limit access to content in the OneDrive and SharePoint mobile apps: [Control access to features in the OneDrive and SharePoint mobile apps](/onedrive/control-access-to-mobile-app-features).
    
To manage content at rest: 
  
- Configure IRM policies on SharePoint document libraries to limit download of content. See [Set up Information Rights Management (IRM) in SharePoint admin center](/office365/securitycompliance/set-up-irm-in-sp-admin-center).
    
- Evaluate the use of Azure Information Protection (AIP). Classification and labeling let you track and control how data is used. Visit [Azure Information Protection](https://azure.microsoft.com/services/information-protection/).
    
## Highly available, always recoverable
 
Our datacenters are geo-distributed within the region and fault tolerant. Data is mirrored in at least two datacenters to mitigate the impact of a natural disaster or service-impacting outage. For more information, see [Where's my data?](https://o365datacentermap.azurewebsites.net/).
  
Metadata backups are kept for 14 days and can be restored to any point in time within a 5-minute window. 
  
In the case of a ransomware attack, you can use Version history ([Enable and configure versioning for a list or library](https://support.office.com/article/1555d642-23ee-446a-990a-bcab618c7a37)) to roll back, and the recycle bin or site collection recycle bin to restore ([Restore deleted items from the site collection recycle bin](https://support.office.com/article/5fa924ee-16d7-487b-9a0a-021b9062d14b)). If an item is removed from the site collection recycle bin, you can call support within 14 days to access a backup. For information about the new Files Restore feature that lets users restore an entire OneDrive to any point within the past 30 days, see [Restore your OneDrive](https://support.office.com/article/fa231298-759d-41cf-bcd0-25ac53eb8a15.aspx).
  
## Continuously validated
 
We continuously monitor our datacenters to keep them healthy and secure. This starts with inventory. An inventory agent scans each subnet looking for neighbors. For each machine, we perform a state capture.
  
After we have an inventory, we can monitor and remediate the health of machines. The security patch train applies patches, updates anti-virus signatures, and makes sure we have a known good configuration saved. We have role-specific logic that ensures we only patch or rotate out a certain percentage of machines at a time.
  
We have an automated workflow to identify machines that don't meet policies and queue them for replacement.
  
The Office 365 "Red Team" within Microsoft is made up of intrusion specialists. They look for any opportunity to gain unauthorized access. The "Blue Team" is made up of defense engineers who focus on prevention, detection, and recovery. They build intrusion detection and response technologies. To keep up with the learnings of the security teams at Microsoft, see [Security, Privacy, and Compliance Blog](https://techcommunity.microsoft.com/t5/Security-Privacy-and-Compliance/bg-p/securityprivacycompliance).
  
To monitor and observe activity in your Office 365 subscription:
  
- If you have an on-premises security operations center or SIEM, you can monitor activity with the Management Activity API. For information, see [Office 365 Management APIs overview](/office/office-365-management-api/office-365-management-apis-overview). This will show you activity from across SharePoint, Exchange, Azure Active Directory, DLP, and more. If you don't have an on-premises security operations center or SIEM, you can use Cloud App Security. Cloud App Security uses the Management Activity API. For information, see [Overview of Office 365 Cloud App Security](/office365/securitycompliance/office-365-cas-overview). Through Cloud App Security, you can report, search, and alert on activity.
    
- Use Azure Active Directory identity protection. This applies machine learning to detect suspicious account behavior, for example, simultaneous sign-ins from the same user in different parts of the world. You can configure identity protection to take action to block these sign-ins. For more information, see [Azure Active Directory Identity Protection](/azure/active-directory/identity-protection/overview).
    
- Use Secure Score to evaluate the security profile of your subscription against a known good baseline and identify opportunities to increase protection: [Introducing the Office 365 Secure Score](/office365/securitycompliance/office-365-secure-score).
    
## Audited and compliant
 
Regulatory compliance is fundamental to Office 365. We make sure the service complies with regulatory and compliance standards. We also help you meet your audit and compliance obligations. The [Service Trust Portal](https://servicetrust.microsoft.com) is a one-stop-shop for compliance and trust information for Microsoft enterprise services. The portal contains reports, whitepapers, vulnerability assessments, and compliance guides. The portal also includes the Compliance Manager, which evaluates the configuration of your subscription against a set of compliance criteria. For more info about the Service Trust Portal, see [Get started with the Microsoft Service Trust Portal](/office365/securitycompliance/get-started-with-service-trust-portal).
  
To meet your regulatory requirements: 
  
- Audit Office 365 activity in the Security &amp; Compliance Center: [Search the audit log in the Office 365 Security &amp; Compliance Center](/office365/securitycompliance/search-the-audit-log-in-security-and-compliance).
    
- Create eDiscovery cases: [Manage eDiscovery cases in the Office 365 Security &amp; Compliance Center](/Office365/SecurityCompliance/ediscovery-cases)
    
- Apply retention policies: [Create and apply information management policies](https://support.office.com/article/eb501fe9-2ef6-4150-945a-65a6451ee9e9).
