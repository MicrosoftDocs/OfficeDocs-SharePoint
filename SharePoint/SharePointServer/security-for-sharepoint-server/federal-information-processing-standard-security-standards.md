---
title: "Federal Information Processing Standard security standards and SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/5/2018
audience: ITPro
ms.topic: reference
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 70ea3042-e4b6-4f20-a314-56d686ea65d1
description: "Learn about the Federal Information Processing Standard (FIPS) with SharePoint Server 2016 and SharePoint Server 2013."
---

# Federal Information Processing Standard security standards and SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
SharePoint Server uses several Windows encryption algorithms for computing hash values that do not comply with Federal Information Processing Standard (FIPS) 140-2,  *Security Requirements for Cryptographic Modules*  . These algorithms are not used for security purposes; they are used for internal processing. For example, SharePoint Server uses MD5 to create hash values that are used as unique identifiers. 
  
## 
<a name="intro"> </a>

Because SharePoint Server uses these algorithms, it does not support the Windows security policy setting that requires FIPS compliant algorithms for encryption and hashing. This Windows security policy is managed through the **FIPSAlgorithmPolicy** registry key in Windows, which is described in the "Configure FIPS policy for a mixed environment" section of the following topic: 
  
- [Additional System Countermeasures](https://go.microsoft.com/fwlink/p/?LinkId=209130)
    
FIPS 140-2 defines security standards that the United States and Canadian governments use to validate security levels for products that implement cryptography. For more information about FIPS 140-2, see the following references:
  
- [FIPS 140 Evaluation](/windows/security/threat-protection/security-policy-settings/system-cryptography-use-fips-compliant-algorithms-for-encryption-hashing-and-signing)
    
- [FIPS Publications](https://go.microsoft.com/fwlink/p/?LinkId=209157)
    
The goal of FIPS is to provide a standardized way to ensure the security and privacy of sensitive information in computer systems of the United States and Canadian governments. Using a FIPS compliant algorithm for encryption of data over an open network is a key requirement for FISMA certification. The Windows FIPSAlgorithmPolicy registry key is neither necessary nor sufficient for FISMA certification, it is a useful enforcement tool for many solutions, but not SharePoint Server.
  
The FIPS contribution to FISMA certification is the strength of encryption used for security purposes. Security-related encryption within SharePoint Server is performed by using FIPS-compliant cipher suites.
  
For additional information about FISMA see,[Federal Information Security Management Act (FISMA) Implementation Project](https://go.microsoft.com/fwlink/?LinkId=242329)
  

