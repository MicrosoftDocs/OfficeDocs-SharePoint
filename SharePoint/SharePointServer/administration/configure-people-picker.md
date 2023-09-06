---
title: "Configure People Picker in SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 08/29/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
description: "Learn how to configure the People Picker web control in SharePoint Server."
---

# Configure People Picker in SharePoint Server

[!INCLUDE[appliesto-2010-2013-2016-2019-xxx-md](../includes/appliesto-2010-2013-2016-2019-xxx.md)]

People Picker can be configured for a farm at the zone level by using the Stsadm **setproperty** operation. By configuring the settings for this control, you can filter and restrict the results that are displayed when a user searches for a user, group, or claim. Those settings will apply to every site within the site collection.

The information in this article applies only to Web applications that use Windows authentication in either classic mode or claims mode.

The People Picker control is used to find and select users, groups, and claims when a site, list, or library owner assigns permissions in Microsoft SharePoint Server. For more information about the People Picker properties, see [Peoplepicker: Stsadm properties](/previous-versions/office/sharepoint-2007-products-and-technologies/cc263318(v=office.12)).

> [!NOTE]
> There are no Windows PowerShell commands to configure People Picker in SharePoint Server 2010, SharePoint Server 2013, SharePoint Server 2016, or SharePoint Server 2019. However, you can use the PowerShell commands to configure People Picker in SharePoint Subscription Edition. For more information, see [Configure People Picker in SharePoint Subscription Edition](configure-people-picker-subscription-edition.md).

This article contains information on how to configure People Picker for specific scenarios. For more information about the People Picker control and how it works, its relationship to authentication and claim providers, and how to plan for People Picker, see [People Picker and claims providers overview](people-picker-and-claims-providers-overview.md).

## Prerequisites to configure People Picker

Ensure that the following requirements are met before configuring People Picker:

- Verify that the account you use to run `Stsadm` is a member of the local Administrators group on the server in which SharePoint Server is installed.
- Open the command prompt window as an administrator to perform the procedures in this article.
- In the command prompt on the driver where SharePoint Server is installed, change to the following directory: `%CommonProgramFiles%\Microsoft Shared\Web Server Extensions\x\Bin`.

   >[!NOTE]
   > Replace the number mapping value, that is "x" in the directory based on the version of SharePoint you have installed. The following are the SharePoint versions and their respective number mapping values:
   >
   > - SharePoint 2010: **14**
   > - SharePoint 2013: **15**
   > - SharePoint 2016 and SharePoint 2019: **16**

## People Picker settings configuration

Once the prerequisites are met, you can perform the following procedures:

- [Check the setting value for any property](#check-the-setting-value-for-any-property)
- [Clear a property value from People Picker](#clear-a-property-value-from-people-picker)
- [Set an encryption key for use with a one-way trust](#set-an-encryption-key-for-use-with-a-one-way-trust)
- [Enable cross-forest or cross-domain queries with a one-way trust](#enable-cross-forest-or-cross-domain-queries-when-using-a-one-way-trust)
- [Restrict People Picker to a certain group in Active Directory](#restrict-people-picker-to-a-certain-group-in-active-directory)
- [Define the location of administrator accounts](#define-the-location-of-administrator-accounts)
- [Force People Picker to pick only from users in the site collection](#force-people-picker-to-pick-only-from-users-in-the-site-collection)
- [Filter Active Directory accounts by using LDAP queries](#filter-active-directory-accounts-by-using-ldap-queries)
- [Return only non-Active Directory user accounts](#return-only-non-active-directory-user-accounts)

### Check the setting value for any property

To check the setting for any People Picker property, type the following command:

```console
stsadm.exe -o getproperty -pn <Property Name> -url <Web application URL>
```

For more information, see [Peoplepicker: Stsadm properties](/previous-versions/office/sharepoint-2007-products-and-technologies/cc263318(v=office.12)).

### Clear a property value from People Picker

You can remove the setting for a People Picker property by specifying the property name you want to clear and using empty quotation marks for the property value.

To remove a property setting from People Picker, type the following command:

```console
stsadm.exe -o setproperty -pn <Property Name> -pv "" -url <Web application URL>
```

For more information, see [Peoplepicker-searchadforests: Stsadm property](/previous-versions/office/sharepoint-2007-products-and-technologies/cc263460(v=office.12)).

### Set an encryption key for use with a one-way trust

If the forest or domain on which SharePoint Server is installed has a one-way trust with another forest or domain, you must first set the credentials for the account that is allowed to authenticate with the forest or domain to be queried before you can use the Stsadm **peoplepicker-searchadforests** property.

> [!NOTE]
> The encryption key must be set on every front-end Web server in the farm on which SharePoint Server is installed.

To set an encryption key, type the following command:

```console
stsadm.exe -o setapppassword -password <key>
```

### Enable cross-forest or cross-domain queries when using a one-way trust

If the forest or domain on which SharePoint Server is installed has a one-way trust with another forest or domain, you must specify the credentials to be used to query the forest or domain, in addition to the names of the forests or domains to be queried. People Picker will only query the forests or domains that you specify in the **peoplepicker-searchadforests** property setting.

To specify the forests or domains to be queried along with the credentials, type the following command:

```console
stsadm.exe -o setproperty -pn peoplepicker-searchadforests -pv <Valid list of forests or domains, Login name, Password> -url <Web application URL>
```

> [!NOTE]
> You do not need to include the encryption key password that you assigned to the account when using the **peoplepicker-searchadforests** property. However, if you have not already set an encryption key for the account, en error message will be displayed.

The following example configures People Picker for use with a forest named Contoso.com and a domain named Fabrikam.com, and includes the credentials for each:

```console
sTSADM.exe -o setproperty -pn peoplepicker-searchadforests -pv "forest:Contoso.com,Contoso\User1,Password1; domain:Fabrikam.com,Fabrikam\User2,Password2" -url https://ServerName
```

For more information, see [Peoplepicker-searchadforests: Stsadm property](/previous-versions/office/sharepoint-2007-products-and-technologies/cc263460(v=office.12)).

### Restrict People Picker to a certain group in Active Directory

If a Web application is using Windows authentication and the site user directory path isn't set, the People Picker control searches the entire Active Directory to resolve users' names or find users, instead of searching only users within a particular organizational unit (OU). The Stsadm **setsiteuseraccountdirectorypath** operation allows the user's directory path to be set to a specific OU in the same domain. After the directory path is set to a site collection, the People Picker control will only search under that particular OU.

To restrict People Picker to a certain OU in Active Directory, type the following command:

```console
stsadm -o setsiteuseraccountdirectorypath -path <Valid OU name> –url <Web application URL>
```

The following example configures People Picker to only return users and groups in the OU named "Sales":

```console
stsadm -o setsiteuseraccountdirectorypath -path "OU=Sales,DC=ContosoCorp,DC=local" -url https://ServerName
```

> [!NOTE]
> Only a single site user directory path can be set at a time for a site collection. Hence this property specifies only one OU at a time, and you should run the Stsadm **setsiteuseraccountdirectorypath** operation only once per site collection.

For more information, see [Setsiteuseraccountdirectorypath: Stsadm operation](/previous-versions/office/sharepoint-2007-products-and-technologies/cc263328(v=office.12)).

### Define the location of administrator accounts

Administrative user accounts are often located in a different OU from regular site users. If you have used the Stsadm **setsiteuseraccountdirectorypath** operation to force People Picker to only return query resulting from a specific OU, you must also set the Stsadm **peoplepicker-serviceaccountdirectorypaths** property so the administrator can manage the site collection.

> [!NOTE]
> Before the **peoplepicker-serviceaccountdirectorypaths** property works, the **Setsiteuseraccountdirectorypath** operation must be set to contain a value.

To define the location of administrator accounts, type the following command:

```console
stsadm -o setproperty -pn peoplepicker-serviceaccountdirectorypaths -pv <A list of OU names> -url <Web application URL>
```

The following example configures People Picker to allow users that are in the OU "FarmAdmin":

```console
stsadm -o setproperty -pn peoplepicker-serviceaccountdirectorypaths -pv "OU=FarmAdmin,DC=Contoso,DC=local" -url https://ServerName
```

For more information, see [Peoplepicker-serviceaccountdirectorypaths: Stsadm property](/previous-versions/office/sharepoint-2007-products-and-technologies/cc263012(v=office.12))).

## Force People Picker to pick only from users in the site collection

The People Picker control consists of a text box, and two buttons, such as the **Check Names** button and the **Browse** button. 

- The **Check Names** button is used to resolve a user name, group name or e-mail address exactly as it was typed into the text box. 
- The **Browse** button opens the **Select People and Groups** dialog box, which can be used to submit a query for a full or partial string. 

The main difference between the two is that the **Check Names** button only resolves exactly what is in the text box, whereas the **Select People and Groups** dialog box searches for the query string. You can force People Picker to only return users who have permissions in the site collection by using either the **PeoplePicker-Peopleeditoronlyresolvewithinsitecollection** property or the **PeoplePicker-Onlysearchwithinsitecollection** property. However, the property you use to configure this restriction will depend on whether you want to set the restriction for the text box (People editor) and **Check Names** button, or for the **Select People and Groups** dialog box.

To force People Picker to only return users who have permissions in the site collection when the **Check Names** button is clicked, type the following command:

```console
stsadm -o setproperty –pn peoplepicker-Peopleeditoronlyresolvewithinsitecollection –pv yes –url <Web application URL>
```

To force People Picker to only return users who have permissions in the site collection when the **Select People and Groups** dialog box is used, type the following command:

```console
stsadm -o setproperty –pn peoplepicker-onlysearchwithinsitecollection –pv yes –url <Web application URL>
```

For more information, see [Peoplepicker-onlysearchwithinsitecollection: Stsadm property](/previous-versions/office/sharepoint-2007-products-and-technologies/cc261988(v=office.12)) and [Peoplepicker-peopleeditoronlyresolvewithinsitecollection: Stsadm property](/previous-versions/office/sharepoint-foundation-2010/gg602064(v=office.14)).

### Filter Active Directory accounts by using LDAP queries

You can use a Lightweight Directory Access Protocol (LDAP) query to create a custom filter for displaying query results. For more information about LDAP queries, see [LDAP Query Basics](https://go.microsoft.com/fwlink/p/?linkid=207670).

To use a custom LDAP query, type the following command:

```console
Stsadm –o setproperty –pn peoplepicker-searchadcustomfilter -pv <LDAP query filter> -url <Web application URL>
```

The following example filters out user accounts that don't have e-mail addresses, or that are disabled. Because security groups don't always have e-mail addresses associated with them, an *OR* statement is used to ensure that security groups are still included in the query results:

```console
stsadm -o setproperty -pn peoplepicker-searchadcustomfilter -pv "(|(&(mail=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))(objectcategory=group))" -url https://ServerName
```

The following example only returns active users, and not groups:

```console
stsadm -o setproperty -pn peoplepicker-searchadcustomfilter -pv "(&(objectCategory=person)(objectClass=user)(!userAccountControl:1.2.840.113556.1.4.803:=2))" -url https://ServerName
```

For an explanation of the user account control string used in this query, see [Search Filter Syntax](https://go.microsoft.com/fwlink/p/?linkid=210020).

The following example returns a list of Active Directory users with the title "Manager":

```console
stsadm -o setproperty -pn peoplepicker-searchadcustomfilter -pv "((Title=Manager))" -url https://ServerName
```

> [!IMPORTANT]
> Remember that every time you run the `setproperty` command for a specific property, that property's current values will be overwritten by the new values you specify. If you need to filter query results based on multiple criteria, you will need to build a compound LDAP query that includes all the values for which you want to filter.

For more information, see [Peoplepicker-searchadcustomfilter: Stsadm property](/previous-versions/office/sharepoint-2007-products-and-technologies/cc263452(v=office.12)).

### Return only non-Active Directory user accounts

If your Web application uses forms-based authentication, you can prevent People Picker from returning Active Directory accounts in the query results.

To return only non-Active Directory user accounts, type the following command:

```console
stsadm -o setproperty -pn peoplepicker-nowindowsaccountsfornonwindowsauthenticationmode -pv yes -url <Web application URL>
```

For more information, see [Peoplepicker-nowindowsaccountsfornonwindowsauthenticationmode: Stsadm property](/previous-versions/office/sharepoint-2007-products-and-technologies/cc263264(v=office.12)).

## See Also

- [Configure People Picker in SharePoint Subscription Edition](configure-people-picker-subscription-edition.md)
- [Enhanced People Picker for modern authentication](enhanced-people-picker-for-trusted-authentication-method.md)
