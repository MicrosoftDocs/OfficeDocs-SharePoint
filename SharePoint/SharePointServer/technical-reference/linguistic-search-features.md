---
title: "Linguistic search features in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 0ed3c559-86c1-40d0-8804-8adb7038492f
description: "Learn which linguistic features search by default uses, and for which languages."
---

# Linguistic search features in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
SharePoint Server use several linguistic features to help improve search relevance. 
  
## Linguistic search features

The following table shows the languages that SharePoint Server by default supports for each linguistic feature search uses. The support of these languages doesn't depend on any installed language packs.
  
 **Note** the following: 
  
- For dynamic spelling correction to work, you should have at least several thousand medium-sized documents.
    
- People search uses fuzzy name matching. Fuzzy name matching includes phonetic matching of names, and can't be disabled. 
    
- Stemming for Norwegian Nynorsk is done with the Norwegian Bokmål stemmer.
    
- Reductive stemming is used for some languages, and can't be disabled. These languages are Arabic, Estonian, Finnish, Hebrew, Hungarian, Korean, Latvian, Lithuanian, Slovak, and Turkish.
    
||||||||||||
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|**Language** <br/> |**Code** <br/> |**Document language detection** <br/> |**Word breaking** <br/> |**Stemming** <br/> |**Spelling variants** <br/> |**Spelling correction, static** <br/> |**Spelling correction, dynamic** <br/> |**Decompounding** <br/> |**Fuzzy name matching** <br/> |**Company name extraction** <br/> |
|Afrikaans  <br/> |af  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Albanian  <br/> |sq  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Arabic  <br/> |ar  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |Yes  <br/> |
|Armenian  <br/> |hy  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Azerbaijani  <br/> |az  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Bangla  <br/> |bn  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Basque (Basque)  <br/> |eu  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Belarusian  <br/> |be  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Bosnian  <br/> |bs  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Breton  <br/> |br  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Bulgarian  <br/> |bg  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Catalan  <br/> |ca  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Chinese Simplified  <br/> |zh-cn  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Chinese Traditional  <br/> |zh-tw  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Croatian  <br/> |hr  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Czech  <br/> |cs  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Danish  <br/> |da  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |
|Dutch  <br/> |nl  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |
|English  <br/> |en  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |Yes  <br/> |Yes  <br/> |
|Estonian  <br/> |et  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Faeroese  <br/> |fo  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Farsi  <br/> |fa  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Filipino  <br/> |tl  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Finnish  <br/> |fi  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |
|French  <br/> |fr  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |Yes  <br/> |Yes  <br/> |
|Frisian  <br/> |fy  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Galician  <br/> |gl  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Georgian  <br/> |ka  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|German  <br/> |de  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |
|Greek  <br/> |el  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Gujarati  <br/> |gu  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Hausa  <br/> |ha  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Hebrew  <br/> |he  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Hindi  <br/> |hi  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Hungarian  <br/> |hu  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Icelandic  <br/> |is  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Indonesian  <br/> |id  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Irish Gaelic  <br/> |ga  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Italian  <br/> |it  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |Yes  <br/> |Yes  <br/> |
|Japanese  <br/> |ja  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Not applicable  <br/> |Yes  <br/> |Yes  <br/> |
|Kannada  <br/> |kn  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Kazakh  <br/> |kk  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Kirghiz  <br/> |ky  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Korean  <br/> |ko  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Kurdish  <br/> |ku  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Latin  <br/> |la  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Latvian  <br/> |lv  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Lithuanian  <br/> |lt  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Luxembourgish  <br/> |lb  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Macedonian  <br/> |mk  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Malay  <br/> |ms  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Malayalam  <br/> |ml  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Maltese  <br/> |mt  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Maori  <br/> |mi  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Marathi  <br/> |mr  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Mongolian  <br/> |mn  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Norwegian Bokmål  <br/> |nb  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |
|Norwegian Nynorsk  <br/> |nn  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |Yes  <br/> |
|Pashto  <br/> |ps  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Polish  <br/> |pl  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |Yes  <br/> |No  <br/> |
|Portuguese  <br/> |pt  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |Yes  <br/> |Yes  <br/> |
|Punjabi  <br/> |pa  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Romanian  <br/> |ro  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Romansh  <br/> |rm  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Russian  <br/> |ru  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |Yes  <br/> |Yes  <br/> |
|Sami Nothern  <br/> |se  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Serbian  <br/> |sr  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Slovak  <br/> |sk  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Slovenian  <br/> |sl  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Sorbian  <br/> |wen  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Spanish  <br/> |es  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |Yes  <br/> |Yes  <br/> |
|Swahili  <br/> |sw  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Swedish  <br/> |sv  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |
|Tamil  <br/> |ta  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Telugu  <br/> |te  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Thai  <br/> |th  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Turkish  <br/> |tr  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Ukrainian  <br/> |uk  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Urdu  <br/> |ur  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Uzbek  <br/> |uz  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Vietnamese  <br/> |vi  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Welsh  <br/> |cy  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Yiddish  <br/> |yi  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
|Zulu  <br/> |zu  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Not applicable  <br/> |No  <br/> |No  <br/> |
   

