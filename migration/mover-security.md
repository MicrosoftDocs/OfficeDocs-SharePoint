---
title: Mover services migration security
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Security measures that protect information when migrating and transmitting data via Microsoft Mover."
---
# Mover services migration security

Mover services consist of a highly available infrastructure with the primary purpose of moving files between cloud storage providers. We understand the importance of security and reliability to our customers, and provide a level of service tailored for each customer. We are dedicated to continually improving, and the practices presented here should be considered the minimum standard of our implementation.

## Secure storage & transfers

The files transmitted through Mover are encrypted using the AES-256 standard. Your files are encrypted as soon as we receive them. We manage the encryption keys.

Mover uses Microsoft Azure for our server infrastructure. You can find more information about Microsoft's security at the [Microsoft Azure website](https://azure.microsoft.com/en-us/).

If supported, your files are sent between the services you choose and our servers over a secure channel using 256-bit TLS (Transport Layer Security) encryption, the standard for secure Internet network connections.

## Access

We work hard to protect your information from unauthorized access.  Microsoft employees are prohibited from viewing the content of files you transmit through Mover. Only file metadata such as file names and paths are readable by Microsoft employees in order to support your migrations.

## Security in four primary areas

Security for us comes in four primary areas:

- [Authorization of the service for a user](#authorization-of-service)
- [Storage of user authorization information](#storage-of-user-authorization-information)
- [Protection of our infrastructure from external intrusion](#protection-of-our-infrastructure-from-external-intrusion)
- [Security of a user’s data as it flows through our system](#security-of-a-users-s-data-as-it-flows-through-our-system)

### Authorization of service

During the process of authentication with a cloud storage provider or other service, we require the collection of authentication data to be retrieved and stored for later use. There are two primary methods that are used to collect this data, OAuth and Direct password or key collection.

#### OAuth

OAuth (Open Authorization) is a web standard which provides a process for end-users to authorize third-party access to their server resources without sharing credentials. More information can be found at:

- [OAuth (Wikipedia)](http://en.wikipedia.org/wiki/OAuth)
- [OAuth.net](http://oauth.net/)

Although the exact encryption method varies browser by browser, Mover requires strong TLS encryption between Mover and the user for the initial authorization. All our OAuth token exchanges use TLS v1.2 to connect to the authorizing server. OAuth will allow the user to deny Mover access to the third-party service at any time by revoking our token.

#### Direct password or key collection

All password or key collection occurs through our web interface over a secure TLS connection utilizing strong ciphers, generally 256-bit AES or stronger.

### Storage of user authorization information

For us to have continual access to the user’s service, we need to store authorization credentials. In the case of OAuth or OAuth-like services such as Box, we store an authorization token which grants us access. 

In the case of a direct password or key, such as Amazon S3, we need to store direct authorization credentials.

These credentials are the key to accessing the customer’s files, and we take special care to secure these properly. All tokens and passwords are encrypted using AES 256 variant with both global and user specific encryption keys. This data is then stored in our internal database servers with no outside access.

### Security of infrastructure

It is important that our infrastructure is secured from external attacks. The following classes of servers have carefully implemented security policies.

#### Runners

*Runners* are our servers that move files. Because our services rely on outbound connections, our security policy is straightforward and secure. There is no outside access allowed to these servers. All outbound traffic is pushed through a point firewall, obfuscating the infrastructure behind.

For maintenance, SSH access is allowed through a two stage process. Access to the point firewall utilizing SSH keys only, then from there SSH access to the individual servers only via SSH keys. To further increase security, inbound SSH is only allowed from specific white-listed IP addresses.

#### API servers

Our API servers, both for our public API and internal API, have a public facing interface. Similar to the Runners, the API servers have SSH management access through a two stage process. The main difference is that our API servers require a public-facing web interface that is completely open. Only TLS web traffic is allowed into this interface. For our internal application API, only authenticated session based traffic is allowed. For our public API, all access is secured through our managed API keys.

#### Web interface

All applications by Mover that have a web interface are secured using TLS strong ciphers. User input, including username and passwords, are passed securely to the backend over this encrypted TLS connection, identified by our site-wide 2048-bit TLS certificate.

### User data as it flows through us

During the process of a transfer, all files are downloaded to our Runner servers, located in Microsoft Azure, then processed through to Microsoft 365 Migration APIs. Each step relies on TLS cryptographic protocols.

During mediation process, Mover temporarily maintains a copy of your file on an encrypted file system before it uploads it to Microsoft 365. As soon as the upload of the file has been verified, we immediately remove the file from our cache. We never keep a copy of your data. We simply facilitate the transfer of your data and we have no interest in, or benefit from, retaining your data.
