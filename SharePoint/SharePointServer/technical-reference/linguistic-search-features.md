---
title: "Linguistic search features in SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 3/7/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 0ed3c559-86c1-40d0-8804-8adb7038492f
description: "Learn which linguistic features search by default uses, and for which languages."
---

# Linguistic search features in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)] 
  
SharePoint Server use several linguistic features to help improve search relevance. 
  
## Linguistic search features

The following table shows the languages that SharePoint Server by default supports for each linguistic feature search uses. The support of these languages doesn't depend on any installed language packs.
  
 **Note** the following:
  
- For dynamic spelling correction to work, you should have at least several thousand medium-sized documents.

- People search uses fuzzy name matching. Fuzzy name matching includes phonetic matching of names, and can't be disabled. 

- Stemming for Norwegian Nynorsk is done with the Norwegian Bokmål stemmer.

- Reductive stemming is used for some languages, and can't be disabled. These languages are Arabic, Estonian, Finnish, Hebrew, Hungarian, Korean, Latvian, Lithuanian, Slovak, and Turkish.

|Language|Code|Document language detection|Word breaking|Stemming|Spelling variants|Spelling correction, static|Spelling correction, dynamic|Decompounding|Fuzzy name matching|Company name extraction|
|---|---|---|---|---|---|---|---|---|---|---|
|Afrikaans|af|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Albanian|sq|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Arabic|ar|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|Yes|
|Armenian|hy|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Azerbaijani|az|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Bangla|bn|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Basque (Basque)|eu|Yes|No|No|No|Yes|Yes|Not applicable|No|No|
|Belarusian|be|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Bosnian|bs|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Breton|br|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Bulgarian|bg|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Catalan|ca|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Chinese Simplified|zh-cn|Yes|Yes|No|No|No|No|Not applicable|No|No|
|Chinese Traditional|zh-tw|Yes|Yes|No|No|No|No|Not applicable|No|No|
|Croatian|hr|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Czech|cs|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Danish|da|Yes|Yes|Yes|Yes|Yes|Yes|Yes|No|No|
|Dutch|nl|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|English|en|Yes|Yes|Yes|No|Yes|Yes|Not applicable|Yes|Yes|
|Estonian|et|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Faeroese|fo|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Farsi|fa|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Filipino|tl|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Finnish|fi|Yes|Yes|Yes|No|No|Yes|Yes|No|No|
|French|fr|Yes|Yes|Yes|Yes|Yes|Yes|Not applicable|Yes|Yes|
|Frisian|fy|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Galician|gl|Yes|No|No|No|Yes|Yes|Not applicable|No|No|
|Georgian|ka|Yes|No|No|No|No|Yes|Not applicable|No|No|
|German|de|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Greek|el|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Gujarati|gu|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Hausa|ha|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Hebrew|he|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Hindi|hi|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Hungarian|hu|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Icelandic|is|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Indonesian|id|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Irish Gaelic|ga|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Italian|it|Yes|Yes|Yes|No|Yes|Yes|Not applicable|Yes|Yes|
|Japanese|ja|Yes|Yes|No|No|No|No|Not applicable|Yes|Yes|
|Kannada|kn|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Kazakh|kk|Yes|No|No|No|Yes|Yes|Not applicable|No|No|
|Kirghiz|ky|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Korean|ko|Yes|Yes|Yes|No|No|No|Not applicable|No|No|
|Kurdish|ku|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Latin|la|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Latvian|lv|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Lithuanian|lt|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Luxembourgish|lb|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Macedonian|mk|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Malay|ms|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Malayalam|ml|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Maltese|mt|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Maori|mi|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Marathi|mr|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Mongolian|mn|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Norwegian Bokmål|nb|Yes|Yes|Yes|No|Yes|Yes|Yes|No|Yes|
|Norwegian Nynorsk|nn|Yes|No|Yes|No|Yes|Yes|Not applicable|No|Yes|
|Pashto|ps|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Polish|pl|Yes|Yes|Yes|No|Yes|Yes|Not applicable|Yes|No|
|Portuguese|pt|Yes|Yes|Yes|Yes|Yes|Yes|Not applicable|Yes|Yes|
|Punjabi|pa|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Romanian|ro|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Romansh|rm|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Russian|ru|Yes|Yes|Yes|No|Yes|Yes|Not applicable|Yes|Yes|
|Sami Nothern|se|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Serbian|sr|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Slovak|sk|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Slovenian|sl|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Sorbian|wen|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Spanish|es|Yes|Yes|Yes|Yes|Yes|Yes|Not applicable|Yes|Yes|
|Swahili|sw|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Swedish|sv|Yes|Yes|Yes|No|Yes|Yes|Yes|No|No|
|Tamil|ta|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Telugu|te|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Thai|th|Yes|Yes|No|No|No|Yes|Not applicable|No|No|
|Turkish|tr|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Ukrainian|uk|Yes|Yes|Yes|No|Yes|Yes|Not applicable|No|No|
|Urdu|ur|Yes|Yes|Yes|No|No|Yes|Not applicable|No|No|
|Uzbek|uz|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Vietnamese|vi|Yes|Yes|No|No|No|Yes|Not applicable|No|No|
|Welsh|cy|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Yiddish|yi|Yes|No|No|No|No|Yes|Not applicable|No|No|
|Zulu|zu|Yes|No|No|No|No|Yes|Not applicable|No|No|
